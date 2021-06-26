import os
import random
from subprocess import call
from datetime import date
import datetime


path = os.getcwd()

def calcdate():
    d0 = date(2021, 6, 13)
    current_time = datetime.datetime.now() 
    d1 = date(current_time.year,current_time.month,current_time.day)
    
    delta = d1 - d0
    
    return(delta.days)

rstart = calcdate()

filelist = []

for root, dirs, files in os.walk(path):

    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for file in files:
        if file!="commitbot.py":
            
            if rstart == 1:
                quit()
            gitfile = os.path.join(root, file)
            call(['git','add',gitfile])

            rnum = random.randint(rstart-4, rstart)
            rstart = rstart - 1
            dstr = str(rnum) + " day ago"

            call(['git', 'commit', '--date', dstr, '-m', 'added solution'])
