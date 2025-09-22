from pynetbox.core.response import Record

class Connections(Record):
    internet_exchange_point = None  # to be set in relations.py
    router = None  # to be set in relations.py