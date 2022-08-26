#!/bin/bash 
 
farmoutAnalysisJobs \
 --input-files-per-job=1 \
 --input-dir=/store/user/ms/monoHiggs_2017_miniaod_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_2017_v2/ \
 --extra-inputs=Fall17_17Nov2017_V32_102X_MC.db \
 --extra-usercode-files=cfipython \
 --memory-requirements=4000 \
 --submit-dir=/nfs_scratch/ms/monoHiggs_2017_signalNtuples_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200/ \
 --output-dir=/store/user/ms/monoHiggs_2017_signalNtuples_26May2021/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200/ \
 --base-requirements='TARGET.PoolName == "HEP" && ((MY.RequiresSharedFS =!= true || TARGET.HasAFS_OSG) && (TARGET.OSG_major =!= undefined || TARGET.IS_GLIDEIN =?= true) && (TARGET.HasParrotCVMFS =?= true || (TARGET.UWCMS_CVMFS_Exists && TARGET.CMS_CVMFS_Exists && TARGET.UWCMS_CVMFS_Revision >= 444 && TARGET.CMS_CVMFS_Revision >= 81620))) && ((MY.NoAutoRequirements =?= true || (TARGET.OSglibc_major == 2 && TARGET.OSglibc_minor >= 17 && (MY.HEP_VO =!= "uscms" || TARGET.CMS_CVMFS_Exists && TARGET.UWCMS_CVMFS_Exists)))) && (TARGET.Arch == "X86_64") && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) && (TARGET.HasFileTransfer)' \
 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200 \
 /afs/hep.wisc.edu/home/ms/monoHiggs_2017/CMSSW_10_2_18 \
 $PWD/run_102X_signal2017-farmout.py


