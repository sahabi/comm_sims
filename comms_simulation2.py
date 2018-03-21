#!/usr/bin/python
import itertools
import zmq, sys, re, time
sys.path.insert(0, 'lmcp/py')
from lmcp import LMCPFactory
from inspect import getmembers, isfunction
from libs.AvState import *
from ctrl_0 import Controller_0
from ctrl_1 import Controller_1
from time import sleep
from random import choice

class Location():
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

LOCATIONS = [0 for i in range(2)]
LOCATIONS[0] = Location(45.2871,-121.0122) # bottom left
LOCATIONS[1] = Location(45.2871,-120.9122) # bottom right

AVERROR = 'Error: AirVehicleState for ID ' 

def fire_outputs(cmds, states):
    goto(1,cmds[0])
    sleep(.1)
    goto(2,cmds[1])
    sleep(.1)
    return 1

def goto(uav, loc):
    factory = LMCPFactory.LMCPFactory()
    msg_obj = factory.createObjectByName("CMASI", "AutomationRequest")
    msg_obj.EntityList = [uav]
    msg_obj.TaskList = [loc]
    msg_obj.OperatingRegion = 100
    header = str(msg_obj.FULL_LMCP_TYPE_NAME) + "$lmcp|" +\
             str(msg_obj.FULL_LMCP_TYPE_NAME) + "||0|0$"
    smsg = LMCPFactory.packMessage(msg_obj, True)
    socket_send.send(header + smsg)

def update_avlocs(av_states, avlocs):
    for c,state in enumerate(av_states.values()):
        for i in range(len(LOCATIONS)):
            (t, d) = in_(i, state)
            if t:
                avlocs[c] = i+1
                break
    return avlocs

def update_inputs(avlocs):
    return [x,x] 

def in_(sp,state):
    width = 0.0192
    if state.Latitude > LOCATIONS[sp].lat - width and \
      state.Latitude < LOCATIONS[sp].lat + width and \
      state.Longitude > LOCATIONS[sp].lon - width and \
      state.Longitude < LOCATIONS[sp].lon + width:
          data = (str(state.ID) + " it is at " + str(state.Latitude) + ", " + str(state.Longitude),
                state.Latitude - (LOCATIONS[sp].lat - width),
                (LOCATIONS[sp].lat + width) - state.Latitude,
                (LOCATIONS[sp].lon + width) - state.Longitude,
                state.Longitude - (LOCATIONS[sp].lon - width))
          return (True,data)
    else:
        return (False,0)

def get_next_message(socket_sub, lmcp_factory):
        data = socket_sub.recv()
        address, attributes, msg = data.split('$', 2)
        msg_format, msg_type, msg_group, entityid, serviceid = attributes.split('|', 4)
        msg = msg
        obj = lmcp_factory.getObject(msg)
        if (int(entityid) == 0 and int(
                serviceid) == 0) or obj.FULL_LMCP_TYPE_NAME == "uxas.messages.uxnative.CreateNewService":
            return None
        else:
            return obj

def initialize_av_configurations(av_configurations, av_ids, lmcp_factory, socket_sub):
    while True:
        msg_obj = get_next_message(socket_sub, lmcp_factory)
        if msg_obj and msg_obj.FULL_LMCP_TYPE_NAME == 'afrl.cmasi.AirVehicleConfiguration':
            if msg_obj.get_ID() in av_ids:
                if not av_configurations.has_key(msg_obj.get_ID()):
                    print('Recording AirVehicleConfiguration with ID ' + str(msg_obj.get_ID()))
                else:
                    print('Warning: Recording duplicate AirVehicleConfiguration with ID ' + str(msg_obj.get_ID()))
                av_configurations[msg_obj.get_ID()] = msg_obj
            else:
                print('Warning: Ignoring AirVehicleConfiguration with ID ' + str(msg_obj.get_ID()) + \
                      ' not used in salt file')
        if msg_obj and msg_obj.FULL_LMCP_TYPE_NAME == 'afrl.cmasi.AirVehicleState':
            print('Saw first AirVehicleState with ID ' + str(msg_obj.get_ID()))
            if len(av_ids.difference(set(av_configurations.keys()))) > 0:
                print('Error: Missing AirVehicleConfigurations for ID(s): ' + ", ".join(str(e) for e in av_ids))
                sys.exit()
            break
    return msg_obj

def initialize_av_states(av_configurations, av_states, msg_obj, lmcp_factory, socket_sub):
    av_initializations = av_configurations.keys()
    while len(av_initializations) > 0:
        if msg_obj and msg_obj.FULL_LMCP_TYPE_NAME == 'afrl.cmasi.AirVehicleState':
            if not av_configurations.has_key(msg_obj.get_ID()):
                print('Warning: Ignoring unknown AirVehicleState ' + str(msg_obj.get_ID()))
            elif av_initializations.count(msg_obj.get_ID()) == 1:
                av_states[msg_obj.get_ID()] = AvState(av_configurations[msg_obj.get_ID()], 
                        msg_obj)
                av_initializations.remove(msg_obj.get_ID())
            else:
                print(av_error + str(msg_obj.get_ID()) + ' seen twice in one cycle.')
        msg_obj = get_next_message(socket_sub, lmcp_factory)
    return msg_obj

def update_av_states(av_states, msg_obj, lmcp_factory, socket_sub):
    av_initializations = av_states.keys()
    while len(av_initializations) > 0:
        if msg_obj and msg_obj.FULL_LMCP_TYPE_NAME == 'afrl.cmasi.AirVehicleState':
            if not av_states.has_key(msg_obj.get_ID()):
                print('Warning: Ignoring unknown AirVehicleState ' + str(msg_obj.get_ID()))
            elif av_initializations.count(msg_obj.get_ID()) == 1:
                av_states[msg_obj.get_ID()].update_state(msg_obj)
                av_initializations.remove(msg_obj.get_ID())
            else:
                print(AVERROR + str(msg_obj.get_ID()) + ' seen twice in one cycle.')
        msg_obj = get_next_message(socket_sub, lmcp_factory)
    return (msg_obj, av_states)

def main():
    print("Loading: Reactive Controllers")
    ctrl0 = Controller_0()
    ctrl1 = Controller_1()
    print("Initiated: Reactive Controllers")
    lmcp_factory = LMCPFactory.LMCPFactory()
    av_configurations = dict()
    av_states = dict()
    av_ids = set([1, 2])
    msg_obj = initialize_av_configurations(av_configurations, av_ids, 
            lmcp_factory, socket_sub)
    time.sleep(1.0)
    msg_obj = initialize_av_states(av_configurations, av_states, msg_obj, 
            lmcp_factory, socket_sub)
    avlocs = [0 for i in range(len(av_ids))]
    inp_1 = choice([0])
    prev_0 = 9
    prev_1 = 9
    while True:
        avlocs = update_avlocs(av_states, avlocs)
        comms_1 = ctrl0.comms(1)
        comms_0 = ctrl1.comms(0)
        inp_0 = 0  
        output_0 = ctrl0.move(inp_0,comms_0)+1
        output_1 = ctrl1.move(inp_1,comms_1)+1
        inp_1 = choice([0,1])
        if prev_0 != output_0 or prev_1 != output_1:
            fire_outputs([output_0,output_1], av_states)
        prev_0 = output_0
        prev_1 = output_1
        cc = 0
        while ( 
                output_0 != avlocs[0] or
                output_1 != avlocs[1]):
            if cc % 10 == 0:
                print(output_0, avlocs[0], output_1, avlocs[1])
            cc += 1
            avlocs = update_avlocs(av_states, avlocs)
            (msg_obj, av_states) = update_av_states(av_states, msg_obj, lmcp_factory, socket_sub)

if __name__ == '__main__':
    context = zmq.Context()
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect("tcp://127.0.0.1:5560")
    socket_sub.setsockopt(zmq.SUBSCRIBE, 'afrl.cmasi.AirVehicle')
    socket_send = context.socket(zmq.PUSH)
    socket_send.connect("tcp://127.0.0.1:5561")

    main()
