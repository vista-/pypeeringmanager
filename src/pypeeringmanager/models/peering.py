from pynetbox.core.response import Record
from pypeeringmanager.models.extras import Tags

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
    from pypeeringmanager.models.bgp import Relationships
    from pypeeringmanager.models.devices import Routers
    autonomous_system = AutonomousSystems
    bgp_group = BGPGroups
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags
    relationship = Relationships
    router = Routers

    def __str__(self):
        return self.ip_address


class InternetExchangePeeringSessions(Record):
    from pypeeringmanager.models.net import Connections
    autonomous_system = AutonomousSystems
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags
    ixp_connection = Connections

    def __str__(self):
        return self.ip_address
