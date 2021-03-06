#! /usr/bin/python

import struct
import xml.dom.minidom
from lmcp import LMCPObject

## ===============================================================================
## Authors: AFRL/RQQA
## Organization: Air Force Research Laboratory, Aerospace Systems Directorate, Power and Control Division
## 
## Copyright (c) 2017 Government of the United State of America, as represented by
## the Secretary of the Air Force.  No copyright is claimed in the United States under
## Title 17, U.S. Code.  All Other Rights Reserved.
## ===============================================================================

## This file was auto-created by LmcpGen. Modifications will be overwritten.

from afrl.cmasi import Location3D


class TaskOption(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 20
        self.SERIES_NAME = "UXTASK"
        self.FULL_LMCP_TYPE_NAME = "uxas.messages.task.TaskOption"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.TaskID = 0   #int64
        self.OptionID = 0   #int64
        self.EligibleEntities = []   #int64
        self.Cost = 0   #int64
        self.StartLocation = Location3D.Location3D()   #Location3D
        self.StartHeading = 0   #real32
        self.EndLocation = Location3D.Location3D()   #Location3D
        self.EndHeading = 0   #real32


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.TaskID))
        buffer.append(struct.pack(">q", self.OptionID))
        buffer.append(struct.pack(">H", len(self.EligibleEntities) ))
        for x in self.EligibleEntities:
            buffer.append(struct.pack(">q", x ))
        buffer.append(struct.pack(">q", self.Cost))
        buffer.append(struct.pack("B", self.StartLocation != None ))
        if self.StartLocation != None:
            buffer.append(struct.pack(">q", self.StartLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.StartLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.StartLocation.SERIES_VERSION))
            buffer.append(self.StartLocation.pack())
        buffer.append(struct.pack(">f", self.StartHeading))
        buffer.append(struct.pack("B", self.EndLocation != None ))
        if self.EndLocation != None:
            buffer.append(struct.pack(">q", self.EndLocation.SERIES_NAME_ID))
            buffer.append(struct.pack(">I", self.EndLocation.LMCP_TYPE))
            buffer.append(struct.pack(">H", self.EndLocation.SERIES_VERSION))
            buffer.append(self.EndLocation.pack())
        buffer.append(struct.pack(">f", self.EndHeading))

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.TaskID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        self.OptionID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EligibleEntities = [None] * _arraylen
        _pos += 2
        if _arraylen > 0:
            self.EligibleEntities = struct.unpack_from(">" + `_arraylen` + "q", buffer, _pos )
            _pos += 8 * _arraylen
        self.Cost = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _valid = struct.unpack_from("B", buffer, _pos )[0]
        _pos += 1
        if _valid:
            _series = struct.unpack_from(">q", buffer, _pos)[0]
            _pos += 8
            _type = struct.unpack_from(">I", buffer, _pos)[0]
            _pos += 4
            _version = struct.unpack_from(">H", buffer, _pos)[0]
            _pos += 2
            from lmcp import LMCPFactory
            self.StartLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.StartLocation.unpack(buffer, _pos)
        else:
            self.StartLocation = None
        self.StartHeading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        _valid = struct.unpack_from("B", buffer, _pos )[0]
        _pos += 1
        if _valid:
            _series = struct.unpack_from(">q", buffer, _pos)[0]
            _pos += 8
            _type = struct.unpack_from(">I", buffer, _pos)[0]
            _pos += 4
            _version = struct.unpack_from(">H", buffer, _pos)[0]
            _pos += 2
            from lmcp import LMCPFactory
            self.EndLocation = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.EndLocation.unpack(buffer, _pos)
        else:
            self.EndLocation = None
        self.EndHeading = struct.unpack_from(">f", buffer, _pos)[0]
        _pos += 4
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        LMCPObject.LMCPObject.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "TaskID" and len(e.childNodes) > 0 :
                    self.TaskID = int(e.childNodes[0].nodeValue)
                elif e.localName == "OptionID" and len(e.childNodes) > 0 :
                    self.OptionID = int(e.childNodes[0].nodeValue)
                elif e.localName == "EligibleEntities" and len(e.childNodes) > 0 :
                    self.EligibleEntities = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.EligibleEntities.append( int(c.childNodes[0].nodeValue) )
                elif e.localName == "Cost" and len(e.childNodes) > 0 :
                    self.Cost = int(e.childNodes[0].nodeValue)
                elif e.localName == "StartLocation" and len(e.childNodes) > 0 :
                    for n in e.childNodes:
                        if n.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.StartLocation = seriesFactory.createObjectByName(n.getAttribute('Series'), n.localName)
                            if self.StartLocation != None:
                                self.StartLocation.unpackFromXMLNode(n, seriesFactory)
                elif e.localName == "StartHeading" and len(e.childNodes) > 0 :
                    self.StartHeading = float(e.childNodes[0].nodeValue)
                elif e.localName == "EndLocation" and len(e.childNodes) > 0 :
                    for n in e.childNodes:
                        if n.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.EndLocation = seriesFactory.createObjectByName(n.getAttribute('Series'), n.localName)
                            if self.EndLocation != None:
                                self.EndLocation.unpackFromXMLNode(n, seriesFactory)
                elif e.localName == "EndHeading" and len(e.childNodes) > 0 :
                    self.EndHeading = float(e.childNodes[0].nodeValue)

        return

    def unpackFromDict(self, d, seriesFactory):
        LMCPObject.LMCPObject.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "TaskID":
                self.TaskID = d[key]
            elif key == "OptionID":
                self.OptionID = d[key]
            elif key == "EligibleEntities":
                self.EligibleEntities = []
                for c in d[key]:
                    self.EligibleEntities.append( c )
            elif key == "Cost":
                self.Cost = d[key]
            elif key == "StartLocation":
                self.StartLocation = seriesFactory.unpackFromDict(d[key])
            elif key == "StartHeading":
                self.StartHeading = d[key]
            elif key == "EndLocation":
                self.EndLocation = seriesFactory.unpackFromDict(d[key])
            elif key == "EndHeading":
                self.EndHeading = d[key]

        return

    def get_TaskID(self):
        return self.TaskID

    def set_TaskID(self, value):
        self.TaskID = int( value )

    def get_OptionID(self):
        return self.OptionID

    def set_OptionID(self, value):
        self.OptionID = int( value )

    def get_EligibleEntities(self):
        return self.EligibleEntities

    def get_Cost(self):
        return self.Cost

    def set_Cost(self, value):
        self.Cost = int( value )

    def get_StartLocation(self):
        return self.StartLocation

    def set_StartLocation(self, value):
        self.StartLocation = value 

    def get_StartHeading(self):
        return self.StartHeading

    def set_StartHeading(self, value):
        self.StartHeading = float( value )

    def get_EndLocation(self):
        return self.EndLocation

    def set_EndLocation(self, value):
        self.EndLocation = value 

    def get_EndHeading(self):
        return self.EndHeading

    def set_EndHeading(self, value):
        self.EndHeading = float( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskOption:\n"
        buf +=    "TaskID = " + str( self.TaskID ) + "\n" 
        buf +=    "OptionID = " + str( self.OptionID ) + "\n" 
        buf +=    "EligibleEntities = " + str( self.EligibleEntities ) + "\n" 
        buf +=    "Cost = " + str( self.Cost ) + "\n" 
        buf +=    "StartLocation = " + str( self.StartLocation ) + "\n" 
        buf +=    "StartHeading = " + str( self.StartHeading ) + "\n" 
        buf +=    "EndLocation = " + str( self.EndLocation ) + "\n" 
        buf +=    "EndHeading = " + str( self.EndHeading ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("UXTASK" is None) or ("UXTASK" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/TaskOption")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("UXTASK" + "/TaskOption")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        LMCPObject.LMCPObject.toDictMembers(self, d)
        d['TaskID'] = self.TaskID
        d['OptionID'] = self.OptionID
        d['EligibleEntities'] = []
        for x in self.EligibleEntities:
            d['EligibleEntities'].append(x)
        d['Cost'] = self.Cost
        if self.StartLocation == None:
            d['StartLocation'] = None
        else:
            d['StartLocation'] = self.StartLocation.toDict()
        d['StartHeading'] = self.StartHeading
        if self.EndLocation == None:
            d['EndLocation'] = None
        else:
            d['EndLocation'] = self.EndLocation.toDict()
        d['EndHeading'] = self.EndHeading

        return

    def getLMCPType(self):
        return self.LMCP_TYPE

    def getSeriesName(self):
        return self.SERIES_NAME

    def getSeriesNameID(self):
        return self.SERIES_NAME_ID

    def getSeriesVersion(self):
        return self.SERIES_VERSION

    def toXMLStr(self, ws):
        str = ws + '<TaskOption Series="UXTASK" >\n';
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskOption>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<TaskID>" + str(self.TaskID) + "</TaskID>\n"
        buf += ws + "<OptionID>" + str(self.OptionID) + "</OptionID>\n"
        buf += ws + "<EligibleEntities>\n"
        for x in self.EligibleEntities:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</EligibleEntities>\n"
        buf += ws + "<Cost>" + str(self.Cost) + "</Cost>\n"
        buf += ws + "<StartLocation>\n"
        if self.StartLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.StartLocation.toXMLStr(ws + "    ") 
        buf += ws + "</StartLocation>\n"
        buf += ws + "<StartHeading>" + str(self.StartHeading) + "</StartHeading>\n"
        buf += ws + "<EndLocation>\n"
        if self.EndLocation == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.EndLocation.toXMLStr(ws + "    ") 
        buf += ws + "</EndLocation>\n"
        buf += ws + "<EndHeading>" + str(self.EndHeading) + "</EndHeading>\n"

        return buf
        
