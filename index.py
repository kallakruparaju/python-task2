#!/usr/bin/python3
import subprocess
import cgi
print("content-type:text/html\n\n")
form=cgi.FieldStorage()
cmd=form.getvalue("x")
if("cal" in cmd or "run calender" in cmd or "this month calender" in cmd or "cal"in cmd ):
	z=subprocess.getoutput("cal")
	print(z)
elif("date" in cmd or "run date" or "today date"):
	y=subprocess.getoutput("date")
	print(y)

