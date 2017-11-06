###############################################################
# Cassiel_NetIDs.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports

from enum import IntEnum

###############################################################
# Class

class NetID(IntEnum):
	SERVER = 0
	ALL_CLIENTS = 1
	FIRST_CLIENT = 1000