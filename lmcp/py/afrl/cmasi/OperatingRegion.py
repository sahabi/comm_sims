#! /usr/bin/python

import sys, struct
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



class OperatingRegion(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 39
        self.SERIES_NAME = "CMASI"
        self.FULL_LMCP_TYPE_NAME = "afrl.cmasi.OperatingRegion"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 3

        #Define message fields
        self.ID = 0   #int64
        self.KeepInAreas = []   #int64
        self.KeepOutAreas = []   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.extend(struct.pack(">q", self.ID))
        buffer.extend(struct.pack(">H", len(self.KeepInAreas) ))
        for x in self.KeepInAreas:
            buffer.extend(struct.pack(">q", x ))
        buffer.extend(struct.pack(">H", len(self.KeepOutAreas) ))
        for x in self.KeepOutAreas:
            buffer.extend(struct.pack(">q", x ))

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.ID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        self.KeepInAreas = [None] * _arraylen
        if _arraylen > 0:
            self.KeepInAreas = struct.unpack_from(">" + repr(_arraylen) + "q", buffer, _pos )
            _pos += 8 * _arraylen
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        self.KeepOutAreas = [None] * _arraylen
        if _arraylen > 0:
            self.KeepOutAreas = struct.unpack_from(">" + repr(_arraylen) + "q", buffer, _pos )
            _pos += 8 * _arraylen
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        LMCPObject.LMCPObject.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "ID" and len(e.childNodes) > 0 :
                    self.ID = int(e.childNodes[0].nodeValue)
                elif e.localName == "KeepInAreas" and len(e.childNodes) > 0 :
                    self.KeepInAreas = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.KeepInAreas.append( int(c.childNodes[0].nodeValue) )
                elif e.localName == "KeepOutAreas" and len(e.childNodes) > 0 :
                    self.KeepOutAreas = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.KeepOutAreas.append( int(c.childNodes[0].nodeValue) )

        return

    def unpackFromDict(self, d, seriesFactory):
        LMCPObject.LMCPObject.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "ID":
                self.ID = d[key]
            elif key == "KeepInAreas":
                self.KeepInAreas = []
                for c in d[key]:
                    self.KeepInAreas.append( c )
            elif key == "KeepOutAreas":
                self.KeepOutAreas = []
                for c in d[key]:
                    self.KeepOutAreas.append( c )

        return

    def get_ID(self):
        return self.ID

    def set_ID(self, value):
        self.ID = int( value )

    def get_KeepInAreas(self):
        return self.KeepInAreas

    def get_KeepOutAreas(self):
        return self.KeepOutAreas



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From OperatingRegion:\n"
        buf +=    "ID = " + str( self.ID ) + "\n" 
        buf +=    "KeepInAreas = " + str( self.KeepInAreas ) + "\n" 
        buf +=    "KeepOutAreas = " + str( self.KeepOutAreas ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("CMASI" is None) or ("CMASI" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/OperatingRegion")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("CMASI" + "/OperatingRegion")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        LMCPObject.LMCPObject.toDictMembers(self, d)
        d['ID'] = self.ID
        d['KeepInAreas'] = []
        for x in self.KeepInAreas:
            d['KeepInAreas'].append(x)
        d['KeepOutAreas'] = []
        for x in self.KeepOutAreas:
            d['KeepOutAreas'].append(x)

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
        str = ws + '<OperatingRegion Series="CMASI" >\n';
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</OperatingRegion>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<ID>" + str(self.ID) + "</ID>\n"
        buf += ws + "<KeepInAreas>\n"
        for x in self.KeepInAreas:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</KeepInAreas>\n"
        buf += ws + "<KeepOutAreas>\n"
        for x in self.KeepOutAreas:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</KeepOutAreas>\n"

        return buf
        
