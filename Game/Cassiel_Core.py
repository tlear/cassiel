###############################################################
# Cassiel_Core.py
# (C) Tom Moore 2017
###############################################################

###############################################################
# Imports
import pyglet
import sys
import thread

from Network.Cassiel_NetIDs import NetID
from Server.Cassiel_Server import Cassiel_Server
from Client.Cassiel_Client import Cassiel_Client
from Network.Cassiel_Network import Cassiel_Network
from Window.Cassiel_Window import Cassiel_Window

###############################################################
# Functions

def main(argv):
	if (len(argv) == 1):
		print "No arguments!"
		pass
	
	# Handle arguments
	for arg in argv[1:]:
		if (arg == "-s"):
			Cassiel_Network.isServer = True
		elif (arg == "-c"):
			Cassiel_Network.isServer = False
			
	# Set up client and run it		
	
	# Set up server and run it
	if (Cassiel_Network.isServer):
		Cassiel_Network.server = Cassiel_Server()
		Cassiel_Network.server.start()
		
	client = Cassiel_Client(NetID.FIRST_CLIENT)
	window = client.window
	pyglet.app.run()
	client.start()

if __name__ == "__main__":
    main(sys.argv)