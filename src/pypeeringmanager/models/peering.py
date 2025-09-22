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
    local_autonomous_system = AutonomousSystems
    tags = Tags

class DirectPeeringSessions(Record):
    autonomous_system = AutonomousSystems
    bgp_group = BGPGroups
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    local_autonomous_system = AutonomousSystems
    relationship = None  # to be set in relations.py
    router = None  # to be set in relations.py
    connection = None  # to be set in relations.py
    tags = Tags

    def __str__(self):
        return self.ip_address


class InternetExchangePeeringSessions(Record):
    autonomous_system = AutonomousSystems
    import_routing_policies = RoutingPolicies
    export_routing_policies = RoutingPolicies
    tags = Tags
    ixp_connection = None  # to be set in relations.py

    def __str__(self):
        return self.ip_address
