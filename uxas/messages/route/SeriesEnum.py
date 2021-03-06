from lmcp.LMCPObject import *

## ===============================================================================
## Authors: AFRL/RQQA
## Organization: Air Force Research Laboratory, Aerospace Systems Directorate, Power and Control Division
## 
## Copyright (c) 2017 Government of the United State of America, as represented by
## the Secretary of the Air Force.  No copyright is claimed in the United States under
## Title 17, U.S. Code.  All Other Rights Reserved.
## ===============================================================================

## This file was auto-created by LmcpGen. Modifications will be overwritten.

import GraphNode
import GraphEdge
import GraphRegion
import RouteConstraints
import RouteRequest
import RoutePlanRequest
import RoutePlan
import RoutePlanResponse
import RouteResponse
import EgressRouteRequest
import EgressRouteResponse
import RoadPointsConstraints
import RoadPointsRequest
import RoadPointsResponse


SERIES_NAME = "ROUTE"
#Series Name turned into a long for quick comparisons.
SERIES_NAME_ID = 5931053054693474304
SERIES_VERSION = 3


class SeriesEnum:

    def getName(self, type):
        if(type ==  1): return "GraphNode"
        if(type ==  2): return "GraphEdge"
        if(type ==  3): return "GraphRegion"
        if(type ==  4): return "RouteConstraints"
        if(type ==  5): return "RouteRequest"
        if(type ==  6): return "RoutePlanRequest"
        if(type ==  7): return "RoutePlan"
        if(type ==  8): return "RoutePlanResponse"
        if(type ==  9): return "RouteResponse"
        if(type ==  10): return "EgressRouteRequest"
        if(type ==  11): return "EgressRouteResponse"
        if(type ==  12): return "RoadPointsConstraints"
        if(type ==  13): return "RoadPointsRequest"
        if(type ==  14): return "RoadPointsResponse"


    def getType(self, name):
        if ( name == "GraphNode"): return 1
        if ( name == "GraphEdge"): return 2
        if ( name == "GraphRegion"): return 3
        if ( name == "RouteConstraints"): return 4
        if ( name == "RouteRequest"): return 5
        if ( name == "RoutePlanRequest"): return 6
        if ( name == "RoutePlan"): return 7
        if ( name == "RoutePlanResponse"): return 8
        if ( name == "RouteResponse"): return 9
        if ( name == "EgressRouteRequest"): return 10
        if ( name == "EgressRouteResponse"): return 11
        if ( name == "RoadPointsConstraints"): return 12
        if ( name == "RoadPointsRequest"): return 13
        if ( name == "RoadPointsResponse"): return 14

        return -1

    def getInstance(self, type):
        if(type ==  1): return GraphNode.GraphNode()
        if(type ==  2): return GraphEdge.GraphEdge()
        if(type ==  3): return GraphRegion.GraphRegion()
        if(type ==  4): return RouteConstraints.RouteConstraints()
        if(type ==  5): return RouteRequest.RouteRequest()
        if(type ==  6): return RoutePlanRequest.RoutePlanRequest()
        if(type ==  7): return RoutePlan.RoutePlan()
        if(type ==  8): return RoutePlanResponse.RoutePlanResponse()
        if(type ==  9): return RouteResponse.RouteResponse()
        if(type ==  10): return EgressRouteRequest.EgressRouteRequest()
        if(type ==  11): return EgressRouteResponse.EgressRouteResponse()
        if(type ==  12): return RoadPointsConstraints.RoadPointsConstraints()
        if(type ==  13): return RoadPointsRequest.RoadPointsRequest()
        if(type ==  14): return RoadPointsResponse.RoadPointsResponse()

        return None
