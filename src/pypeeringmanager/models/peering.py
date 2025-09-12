from pynetbox.core.response import Record
from pypeeringmanager.models.devices import Routers
from pypeeringmanager.models.bgp import Relationships
from pypeeringmanager.models.extras import Tags
from pypeeringmanager.models.net import Connections

class RoutingPolicies(Record):
    pass


class Communities(Record):
    tags = Tags


class AutonomousSystems(Record):
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags


class BGPGroups(Record):
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    communities = Communities
    tags = Tags


class InternetExchanges(Record):
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    communities = Communities
    local_atutonomous_system = AutonomousSystems
    tags = Tags


class DirectPeeringSessions(Record):
    autonomous_system = AutonomousSystems
    bgp_group = BGPGroups
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    router =  Routers
    relationship = Relationships
    tags = Tags

    def __str__(self):
        return self.ip_address


class InternetExchangePeeringSessions(Record):
    autonomous_system = AutonomousSystems
    ixp_connection = Connections
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags

    def __str__(self):
        return self.ip_address
