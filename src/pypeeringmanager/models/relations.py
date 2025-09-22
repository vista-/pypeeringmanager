"""
Relations between models that would otherwise cause circular imports.
This module should only contain cross-model wiring.
"""

from pypeeringmanager.models.bgp import Relationships
from pypeeringmanager.models.devices import Routers
from pypeeringmanager.models.peering import DirectPeeringSessions, InternetExchangePeeringSessions
from pypeeringmanager.models.peering import AutonomousSystems
from pypeeringmanager.models.net import Connections
from pypeeringmanager.models.peeringdb import InternetExchanges

# Wire cross-dependencies here
Routers.local_autonomous_system = AutonomousSystems

DirectPeeringSessions.router = Routers
DirectPeeringSessions.relationship = Relationships
DirectPeeringSessions.connection = Connections

Connections.internet_exchange_point = InternetExchanges
Connections.router = Routers

InternetExchangePeeringSessions.ixp_connection = Connections
