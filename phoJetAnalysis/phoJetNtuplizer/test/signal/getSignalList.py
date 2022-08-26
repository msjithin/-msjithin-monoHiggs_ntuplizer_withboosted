import os
import re

os.popen('ls -d /hdfs/store/user/ms/monoHiggs_2017_miniaod_26May2021/*/* > signal_list')
inputFile=open("signal_list", "r")
sampleList=[]
for lines in inputFile :
    splitLines = lines.split("/")
    #print(splitLines[6])
    tmp_samplelist=splitLines[6][:-7]
    if tmp_samplelist not in sampleList :
        sampleList.append(tmp_samplelist)
    tmpfilename=tmp_samplelist+'.txt'
    if os.path.exists(tmpfilename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
        

    outFile = open(tmpfilename,append_write)
    outFile.write("'file:"+lines.rstrip()+"',"+"\n")
    outFile.close()


