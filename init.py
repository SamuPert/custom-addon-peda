from os import scandir, path
import inspect
import pkgutil


# point to absolute path of peda.py
PEDAFILE = os.path.abspath(os.path.expanduser(__file__))

ADDONS_DIR = 'custom-addons-peda'
DIR_NAME = 'addons'
MODULES_ABS_DIR = os.path.abspath( os.path.dirname(PEDAFILE) + '/..' ) + "/{}/{}/".format(ADDONS_DIR,DIR_NAME)

if os.path.islink(PEDAFILE):
    PEDAFILE = os.readlink(PEDAFILE)
sys.path.insert(0, MODULES_ABS_DIR )

# Add to PEDA
#for cmd in dexter_addon.commands:
print('========= Dext3r98 Addon =========')
for current_class in scandir( MODULES_ABS_DIR ):
	#print(current_class.path.split('/')[-1])
	# print( dir(current_class['__class__']) )
	if current_class.path in ['.','..'] or current_class.path.split('/')[-1].strip() == '__pycache__' or os.path.isdir(current_class.path):
		continue
	#print( inspect.getmembers(inspect))
	#name = inspect.getmodulename(mf)
	#	for name, obj in inspect.getmembers():

	module = inspect.getmodulename(current_class.path)
#	module = MODULES_ABS_DIR + module
	# print ('============ MODULE ============')
	# print (module)
	# print ('================================')

	PARSED_CLASSES = []

	PARSED_ELEMENTS = [ c for c in inspect.getmembers( __import__(  module, fromlist=['']) ) ]
	for c in PARSED_ELEMENTS:
		if inspect.isclass(c[1]):
			PARSED_CLASSES.append(c)

	# print ('============ CLASSES ============')
	# print (', '.join( [ c[0] for c in PARSED_CLASSES ] ))
	# print ('================================')
	#	print (PARSED_CLASSES)

	PARSED_FUNCTIONS = []
	for cl in PARSED_CLASSES:
		# print ('============ CLASS {} ============'.format(cl[0]))
		tmp_elements = inspect.getmembers(cl[1])
		for el in tmp_elements:
			if inspect.isfunction(el[1]) and callable(el[1]) and not el[0].startswith("_"):
				# print( '# {}'.format(el[0]) )
				PARSED_FUNCTIONS.append(el)
		# print ('========= END CLASS {} ===========')

	print('Loaded commands: {}'.format(', '.join([c[0] for c in PARSED_FUNCTIONS])) )
	#print(PARSED_FUNCTIONS)

	# MAP EACH FUNCTION TO A NEW COMMAND IN PEDA
	for tmp_function in PARSED_FUNCTIONS:
		pedacmd.commands.append(tmp_function[0])
		setattr(PEDACmd, tmp_function[0], tmp_function[1])
		func = getattr(pedacmd, tmp_function[0])
		func.__func__.__doc__ = func.__doc__.replace("MYNAME", tmp_function[0])
		if tmp_function[0] not in ["help", "show", "set"]:
			Alias(tmp_function[0], "peda %s" % tmp_function[0], 0)

print('==================================')
