from pynetbox.core.response import Record
from pypeeringmanager.models.peering import InternetExchanges
from pypeeringmanager.models.devices import Routers

class Connections(Record):
    internet_exchange_point = InternetExchanges
    router =  Routers
