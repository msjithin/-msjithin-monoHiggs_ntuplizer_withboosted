import os
import fileinput
import sys


# os.popen('ls /hdfs/store/user/ms/monoHiggs_2017_redigi_Jun2021/* -d > sample_list.txt')
# resubmit = []
# with open('sample_list.txt', 'r') as samplefile:
#     for sample in samplefile:
#         sample = sample.rstrip().split('/')[-1]
#         print(sample)
        
#         nfiles = os.popen('ls /hdfs/store/user/ms/monoHiggs_2017_redigi_Jun2021/'+sample+'/* | wc -l')
#         print(nfiles)
#         print('In {} ,  nfiles = {}'.format(sample, nfiles))


def get_redigi():
    import subprocess
    parent = '/hdfs/store/user/ms/monoHiggs_2017_redigi_Jun2021/'
    os.popen('ls '+parent+'* -d > sample_list.txt')
    
    print('Parent dir -- '+parent)
    with open('sample_list.txt', 'r') as samplefile:
        for sample in samplefile:
            sample = sample.rstrip().split('/')[-1]
            output = subprocess.check_output('ls '+parent+sample+'/* | wc -l', shell=True, universal_newlines=True)
            #nfiles =  getNumber.read()
            print('In {} ,  nfiles = {}'.format(sample, output))



def get_aod():
    import subprocess
    parent = '/hdfs/store/user/ms/monoHiggs_2017_aod_Jun21/'
    os.popen('ls '+parent+'* -d > sample_list.txt')
    nDone = 0
    print('Parent dir -- '+parent)
    with open('sample_list.txt', 'r') as samplefile:
        for sample in samplefile:
            sample = sample.rstrip().split('/')[-1]
            output = subprocess.check_output('ls '+parent+sample+'/* | wc -l', shell=True, universal_newlines=True)
            #nfiles =  getNumber.read()
            print('In {} ,  nfiles = {}'.format(sample, output))
            nDone += 1
    print('Number of samples done = ', nDone)
        
def get_miniaod():
    import subprocess
    parent = '/hdfs/store/user/ms/monoHiggs_2017_miniaod_Jun21/'
    os.popen('ls '+parent+'* -d > sample_list.txt')
    nDone = 0
    print('Parent dir -- '+parent)
    with open('sample_list.txt', 'r') as samplefile:
        for sample in samplefile:
            sample = sample.rstrip().split('/')[-1]
            output = subprocess.check_output('ls '+parent+sample+'/* | wc -l', shell=True, universal_newlines=True)
            #nfiles =  getNumber.read()
            print('In {} ,  nfiles = {}'.format(sample, output))
            nDone += 1
    print('Number of samples done = ', nDone)
        
def get_ntuples():
    import subprocess
    parent = '/hdfs/store/user/ms/monoHiggs_2017_signalNtuples_June2022/'
    os.popen('ls '+parent+'* -d > sample_list.txt')
    nDone = 0
    print('Parent dir -- '+parent)
    with open('sample_list.txt', 'r') as samplefile:
        for sample in samplefile:
            sample = sample.rstrip().split('/')[-1]
            output = subprocess.check_output('ls '+parent+sample+'/* | wc -l', shell=True, universal_newlines=True)
            #nfiles =  getNumber.read()
            print('In {} ,  nfiles = {}'.format(sample, output))
            nDone += 1
    print('Number of samples done = ', nDone)



get_ntuples()
