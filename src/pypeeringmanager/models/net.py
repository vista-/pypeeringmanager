from pynetbox.core.response import Record

class Connections(Record):
    @property
    def internet_exchange_point(self):
        from pypeeringmanager.models.peering import InternetExchanges
        return InternetExchanges

    @property
    def router(self):
        from pypeeringmanager.models.devices import Routers
        return Routers
