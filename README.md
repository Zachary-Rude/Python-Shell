# **Python Shell**

The Python Shell, recreated using Python's `code` and `sys` modules.
The `code` module is imported for its ```python
InteractiveConsole()
``` object that is used to create the shell,
and the `sys` module is imported for its `platform` variable that is used
for showing the OS name showed in the real Python Shell. Just like
in the real one, if the user is on Windows, then it has the value `win32`, on macOS, iOS,
and iPadOS, it has the value `darwin` (which is *very* unusual), and, finally, on Unix
and all Unix-like operating systems (Linux, Android, Chrome OS, etc.), it has the value
`linux`.

## __Source Code__

```python
import code, sys

white = "\033[0;37m"
variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)
shell.interact(banner=white + '''Python 3.8.2 (default, Feb 26 2020, 02:56:10)
[GCC 5.4.0 20160609] on %s
Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.''' % (sys.platform))
```
