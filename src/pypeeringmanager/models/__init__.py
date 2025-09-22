# Load all model modules
from . import bgp
from . import devices
from . import extras
from . import messaging
from . import net
from . import peeringdb
from . import peering

# Import relations last to wire cross-dependencies
from .relations import *