Steps:
0. Follow "Installation" steps
1. Create a file in addons folder.
2. Create a class
3. Inside that class create a function
4. Save
5. Open gdb and use newly created commands

Function names are mapped to command names.

def MyAwesomeFunction(self,args*):
	.....

Will be called in gdb as:

gdb-peda$ MyAwesomeFunction args ...
