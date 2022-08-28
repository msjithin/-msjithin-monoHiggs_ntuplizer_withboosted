
# monoHiggs ntuplizer with boosted taus
# for 2017 dataset
Instructions from Tau POG  
https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Running_of_the_bug_fix_version_o

```
cmsrel CMSSW_10_2_22 # or CMSSW_10_6_17
cd CMSSW_10_2_22/src # or CMSSW_10_6_17/src
cmsenv
```

#### add MVA DM code and xml training files
```
git cms-merge-topic -u cms-tau-pog:CMSSW_10_2_X_tau-pog_MVAdm # or cms-tau-pog:CMSSW_10_6_X_tau-pog_MVAdm
```
#### compile
```
scramv1 b -j 8
```

Reference  
https://github.com/abdollah110/ggAnalysis/   
https://github.com/varuns23/phoJetAnalysis/ 




To clone this repo
```
git clone https://github.com/msjithin/monoHiggs_ntuplizer_withboosted.git .
```
