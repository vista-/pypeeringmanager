from pynetbox.core.response import Record

class Configurations(Record):
    pass

class Platforms(Record):
    pass

class Routers(Record):
    from pypeeringmanager.models.peering import AutonomousSystems
    platform = Platforms
    local_autonomous_system = AutonomousSystems
    pass