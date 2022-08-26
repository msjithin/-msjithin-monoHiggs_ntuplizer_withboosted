import os
import re

os.popen('ls run_Signal2017_*.py > submitlist')
inputFile=open("submitlist", "r")
submitfile=open("submitfile.sh", "w")
for lines in inputFile:
    submitfile.write('eval `cmsRun signal/'+lines.strip()+"`   \n")

submitfile.close()
