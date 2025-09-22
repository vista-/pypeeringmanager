from pynetbox.core.response import Record

class Connections(Record):
    from pypeeringmanager.models.peering import InternetExchanges
    from pypeeringmanager.models.devices import Routers

    internet_exchange_point = InternetExchanges
    router = Routers