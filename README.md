# Custom Addon creator for gdb-peda 

Add your custom commands into gdb-peda in a easy way.

## Installation
```
git clone https://github.com/SamuelePerticarari/custom-addon-peda.git ~/custom-addons-peda
echo "source ~/custom-addons-peda/init.py" >> ~/.gdbinit
```

## Create custom commands
Steps:

0.  Follow "Installation" steps.
1.  Create a file in addons folder.
2.  Create a class in that file.
3.  Inside that class create a function.
4.  Save.
5.  Open gdb and use newly created commands.

## How can i use my custom commands?

`Custom commands are displayed in gdb when it's launched.`
```Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
========= Dext3r98 Addon =========
Loaded commands: MyPedaCommand, hacktheplanet
==================================
Reading symbols from uaf...(no debugging symbols found)...done.
gdb-peda$ 
```

Commands are mapped to function names.

```python
def MyAwesomeFunction(self,args*):
	.....
	return True
```
Will be called in gdb as:

```gdb
gdb-peda$ MyAwesomeFunction args ...
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
