#!/usr/bin/python
import os
print(os.getcwd())
os.system('date')
print(dir(os))
help(os)

from datetime import date
now = date.today()
print(now.strftime("%m-%d-%Y . %d %b %Y is a %A on the %d day of %B."))

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)

