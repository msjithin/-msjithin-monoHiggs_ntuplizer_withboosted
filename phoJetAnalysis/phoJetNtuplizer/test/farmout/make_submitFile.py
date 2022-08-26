import os
import fileinput
import sys
import re

#/hdfs/store/user/ms/MonoHiggs_2017_signalSample_AOD/2HDMa_bb_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600-AOD_submit
#/hdfs/store/user/ms/monoHiggs_2017_miniaod_Jun21/
writeString="""
farmoutAnalysisJobs \\
 --input-files-per-job=1 \\
 --input-dir=/store/user/ms/monoHiggs_2017_miniaod_May22/{miniaod}/ \\
 --extra-inputs=Fall17_17Nov2017_V32_102X_MC.db \\
 --extra-usercode-files=cfipython \\
 --memory-requirements=4000 \\
 --submit-dir=/nfs_scratch/ms/monoHiggs_2017_signalNtuples_June2022/{sample}/ \\
 --output-dir=/store/user/ms/monoHiggs_2017_signalNtuples_June2022/{sample}/ \\
 monoHiggs_2017_signalNtuples_June2022/{sample} \\
 /afs/hep.wisc.edu/home/ms/monoHiggs_2017/CMSSW_10_2_18 \\
 $PWD/run_102X_signal2017-farmout.py

"""
# first lest get the directories list
os.popen('ls -d /hdfs/store/user/ms/monoHiggs_2017_miniaod_May22/2HDMa_bb_sinp_0p35_tanb_1p0_mXd_10_MH3* > miniaod_dir_list') 
# open file to write commands to 
outFile = open('signal_farmoutSubmit.sh', 'w')
# open dir list file
file1 = open('miniaod_dir_list', 'r') 
count = 0
outFile.write('#!/bin/bash \n ')

for line in file1: 
    count +=1
    line=line.split("/")[-1] 
    sampleName=line.split("-monoHiggsTauTau")[0]
    outFile.write(writeString.format( miniaod=line.strip(), sample=sampleName.strip()))

file1.close()
outFile.close()


print """
created signal_farmoutSubmit.sh
do 
  bash signal_farmoutSubmit.sh

"""
