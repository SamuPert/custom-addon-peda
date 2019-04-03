#
#       PEDA - Python Exploit Development Assistance for GDB
#

class SampleAddon(object):


	def hacktheplanet(self, *args):
		# Put here usage example
		"""-
======= Help page hacktheplanet =======
hacktheplanet Function
======================================="""

		print( "ARGS: " + ", ".join(args) )

		return True




	def MyPedaCommand(self, *args):
		# Put here usage example
		"""-
======= Help page MyPedaCommand =======
MyPedaCommand Function
======================================="""
		if len(args) > 0 and args[0].lower().strip() == 'help':
			MyPedaCommand()
			return

		print( "ARGS: " + ", ".join(args) )

		return True
