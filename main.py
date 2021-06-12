import code, sys

white = "\033[0;37m"
variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)
shell.interact(banner=white + '''Python 3.8.2 (default, Feb 26 2020, 02:56:10)
[GCC 5.4.0 20160609] on %s
Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.''' % (sys.platform))
