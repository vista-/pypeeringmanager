from pynetbox.core.response import Record
from pypeeringmanager.models.peering import AutonomousSystems

class Configurations(Record):
    pass

class Platforms(Record):
    pass

class Routers(Record):
    platform = Platforms
    local_autonomous_system = AutonomousSystems