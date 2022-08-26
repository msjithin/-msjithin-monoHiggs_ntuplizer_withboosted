#fin = open("run_102X_signal2017.py", "rt")
#output file to write the result to
#fout = open("out.txt", "wt")
#for each line in the input file
  #                                         2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_100_MH2_200_MHC_200-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  39128 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_150_MH2_200_MHC_200-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  46428 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_100_MH2_300_MHC_300-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  47596 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_300_MH4_150_MH2_300_MHC_300-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  35332 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_100_MH2_400_MHC_400-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  60152 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_150_MH2_400_MHC_400-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  34456 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_200_MH2_400_MHC_400-MINIAOD_submit_.txt
  # -rw-rw-r--  1 ms ms  32704 May 27 13:29 2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_250_MH2_400_MHC_400-MINIAOD_submit_.txt
sampleName = "2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_400_MH4_100_MH2_400_MHC_400-MINIAOD_submit_.txt"
inputFile=open(sampleName, "r")
i=1
for fileNamelines in inputFile :
    fout = open("run_Signal2017_"+str(i)+".py", "wt")
    fin = open("run_102X_signal2017.py", "rt")
    data = fin.read()
    data = data.replace('InputFileNameHere', fileNamelines)
    data = data.replace('Ntuple_signal.root', 'Ntuple_signal_'+str(i)+'.root')
    fout.write(data)
    fin.close()
    fout.close()
    i+=1
    
#close input and output files
#fin.close()
#fout.close()


