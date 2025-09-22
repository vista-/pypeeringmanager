from pynetbox.core.response import Record

class Configurations(Record):
    pass

class Platforms(Record):
    pass

class Routers(Record):
    platform = Platforms

    @property
    def local_autonomous_system(self):
        from pypeeringmanager.models.peering import AutonomousSystems
        return AutonomousSystems
