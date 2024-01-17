# DeepCore Framework

This repository contains the code and instructions related to the DeepCore2.0 framework. The Ntuplizer makes the training samples used for DeepCore2.0 trainings and the workflows are used to evaluate DeepCore2.0 models. This repository will include instructions to run the complete framework from scratch. More information and documentation about DeepCore2.0 can be found in the Twiki: https://twiki.cern.ch/twiki/bin/view/CMSPublic/TrackingPOGRun3DeepCoreV2

## 1) The Ntuplizer (Ntuplizer/DeepCoreTraining)
## A) Introduction:
- The Ntuplizer consists of 2 steps: 
	- Step 1 extract the relevant information from the GEN-SIM and AODSIM of the dataset you picked for DeepCore training
		- The name of these files are inadequately named Ntuplizer_output_*.root where * is a number
	- Step 2 takes the Ntuplizer_output_*.root file, and used the information inside to output the training samples
		- The name of the files is DeepCoreTrainingSample_*.root
	- Unless you are using a new dataset, you typically need to rerun only step2 of the Ntuplizer
	  	- e.g: implementing pixel size fix, 1/pt -> pt fix ..etc only required running step 2
	- Different files:
	  	- Edit test_DeepCorePrepareInput.py and test_DeepCorePrepareInput_crab.py for step 1 of the Ntuplizer
		- Edit test_DeepCoreNtuplizer.py and test_DeepCoreNtuplizer_crab.py for step 2 of the Ntuplizer
		- Edit DeepCoreNtuplizer.cc to adjust things pertaining to the training samples (step 2)
		  	- pixel size fix, saving pt instead of 1/pt, adding new variables in the training sample..

- I used CMSSW_12_1_1,  but you should use whatever cms release is compatible with your dataset
  	- You can read off the dataset (e.g: /`RelValTTbar_14TeV/CMSSW_12_4_0-124X_mcRun3_2022_realistic_v5-v1/NANOAODSIM` ---> CMSSW_12_4_0)
	- Note: may need to change one line in DeepCoreNtuplizer.cc (static const int ->const int ) to compile with CMSSW_12_6_4
- `cmsrel CMSSW_12_1_1`
- `cd CMSSW_12_1_1/src/`
- `scram b -j 8`
- `cmsenv`
- if you haven't setup up Github with your CERN/fermilab account, please do that (adjust details accordingly):
	- `git config --global user.name "Hichem Bouchamaoui"`
	- `git config --global user.email "bouchamaouihichem@gmail.com"`
	- `git config --global user.github bouchamaouihichem`
- `git cms-addpkg RecoTracker`
- `cd RecoTracker/`
- copy Ntuplizer folder from the DeepCore repo (Ntuplizer/DeepCoreTraining)
- Go back to src to compile : 
	- `cd ..`
	- `scram b -j 8`
- `cmsenv`
- `voms-proxy-init --voms cms`

## C) Running the Ntuplizer (after fresh login):
- `cmsenv`
- `voms-proxy-init --voms cms`
- Edit the files for step 1 of the Ntuplizer as needed
	- Check the Deep Dive into Ntuplizer files section before proceeding.
- `crab submit test_DeepCorePrepareInput_crab.py` 
- once the jobs are done running, edit the files for step 2 of the Ntuplizer as needed (specifically the output dataset name form step 1)
- `crab submit test_DeepCoreNtuplizer_crab.py`
- Once the jobs are done running, you can find the training samples in your eos directory

## D) Deep Dive into Ntuplizer files:
### a) test_DeepCorePrepareInput.py: (Ntuplizer step 1): 
- Things that might need editing:
	- adjust era if needed: Changed era to eras.Run3 in L5 as shown in this [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCmsDriverEras). Also potentially relevant [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Trigger_development_for_Run_3).
	- adjust tag name if needed: Changed global tag to auto:phase1_2021_realistic in L72 as shown in this [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Setup_for_Running_on_MC_and_Data)
	- Adjust output filename to Ntuplizer_output1.root in L55
			- Don't forget to edit the other crab file, though the other crab job takes the publication name of the jobs rather than the files path
			- It would be nice to adjust step 1 ouput file name form  Ntuplizer_output1.root to Ntuplizer_step1.root
	- Changes I made between DeepCore 2 and DeepCore 1 that you probably don't need to worry about, but included here for completeness:
		- Add missing parenthesis missing in test_DeepCorePrepareInput.py L41
		- Comment out module in test_DeepCorePrepareInput.py (`HLTrigger.Configuration.HLT_2018v32_cff`) since it doesn't seem to be necessary. If it is necessary in the future look in this [Twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Setup_for_Running_on_MC_and_Data).
	- Note: Don't bother editing input files here since the input files specified in the crab config will be the ones used.
 ### b) test_DeepCorePrepareInput_crab.py: (Ntuplizer step 1): 
 - Things that you must edit:
	- Change Request name in L4 to reflect the date or dataset: `config.General.requestName = 'DeepCorePrepareInput1224'`
	- Change Output dataset name if you want: `config.Data.outputDatasetTag = 'DeepCoreNtuplizerInput'`
	- edit in AODSIM and GEN-SIM or GEN-SIM-DIGI-RAW files L13-L14
		- `config.Data.inputDataset = '/RelValQCD_Pt_1800_2400_14/CMSSW_12_0_0_pre3-PU_120X_mcRun3_2021_realistic_v1_aodsim-v1/AODSIM'`
		- `config.Data.secondaryInputDataset = '/RelValQCD_Pt_1800_2400_14/CMSSW_12_0_0_pre3-PU_120X_mcRun3_2021_realistic_v1-v1/GEN-SIM`
	- Adjust total number of events and event per job:
		- Edited L25-L26 to specify number of jobs and units per jobs: (don't use the same numbers, these numbers assume a dataset of with 9000 events, you'll probably be using one with 1M+ )
			- `config.Data.unitsPerJob = 1000`
			- `NJOBS = 9`
			- `config.Data.totalUnits = config.Data.unitsPerJob * NJOBS`
		- PS: don't use the same numbers, these numbers assume a dataset of with 9* 1000 = 9000 9000 events, you'll probably be using one with 1M+ . In my experience, 1k events per job is ideal but 5k works.
		- Potentially might need: `config.Data.splitting = 'EventBased'` in certain situations
	- relevant [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile) for crab config file
	- When using Track Pog eos space (mainly due to storage reasons), need to:
		- adjust site in L32 to `T2_CH_CERN`
		- add line: `config.Data.outLFNDirBase = '/store/group/phys_tracking/Hichemb/DeepCoreNtuplizer/'`
			- because the full dir is: `/eos/cms/store/group/phys_tracking/Hichemb/DeepCoreNtuplizer`
		- check if there is space beforehand using: `eos quota /eos/cms/store/group/phys_tracking/`
- Other changes you can ignore:
  	- Deleted L28 since outdated: crab will automatically put output in your eos directory
### c) test_DeepCoreNtuplizer.py: (Ntuplizer step 2):
- Global tag adjustments:
	- Remove  L16 and add these 2 lines:
		- `from Configuration.AlCa.GlobalTag import GlobalTag`
		- `process.GlobalTag = GlobalTag(process.GlobalTag,'auto:phase1_2021_realistic','')`
	- This update guarantees that the config file will find the appropriate detector condition depending on the cmssw version of the dataset according to [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Setup_for_Running_on_MC_and_Data)
		- "It is vital that the correct GlobalTag is used. One can take advantage of special GT keywords in [autoCond.py](https://github.com/cms-sw/cmssw/blob/master/Configuration/AlCa/python/autoCond.py) to specify a type of GT; autoCond.py then resolves to the appropriate GT for the CMSSW release that's being used. We use "`auto:phase1_2021_realistic`" for MC, and "`auto:run3_hlt`" for Data."
- edit output file name in L60 if needed
- adjust number of threads and streams in L30-L31 to 8 to match crab config file.
### d) test_DeepCoreNtuplizer_crab.py: (Ntuplizer step 2):
- edit input file L14: 
	- published dataset name of the output of step1 on DBS (phys03) for DeepCore2.0: `/RelValQCD_Pt_1800_2400_14/hboucham-DeepCoreNtuplizerInput-e101c270c65c32f52437c2373244ff6e/USER`
	- You need to find the name of the dataset published in DBS. To do that you can look at the end of the crab.log file of the jobs you submitted in step 1: (e.g: `crab_projects/crab_DeepCorePrepareInput/crab.log`)
		- Alternatively you can copy it from the output of the crab status command 
- Adjust total number of events and event per job:
	- You can use the same numbers you used for step 1 of the Ntuplizer, which would require copying the same line and using EventLumiBased split. However it's easier to use Filebased split in this case and have 1 file per job
		- Note that if you have some outdated files that you published in step 1 and deleted later, crab will still attempt to submit these jobs, which will result in some jobs failing. For example I have deleted the outdated Ntuplizer step 1 output files and kept the up to date ones (360), so when I submit jobs for step 2, crab reports that 360/562 jobs completed, which is the right number. If this is confusing them talk to me.
- adjust site in L25 to `T3_US_FNALLPC`
- Other changes you can ignore:
	- edit python file used in L10: test_DeepCoreNtuplizer.py
		- used to be `NNClustSeedInputSimHit_config.py`
	- Delete L19 since outdated: crab will automatically put output in your eos directory.

## 2) DeepCore2.0 (training/):
## A) Introduction:
Once you have the training samples from the Ntuplizer, remember to split them into training/validation/testing. The training of DeepCore2.0 is typically done on Fermilab GPUs, but a Condor setup available. There are 2 versions of DeepCore.py: One compatible with FNAL GPUs (singularity environment) and one that isn't, that is mainly used to produce parameter plots. The training can be re-started from a given epoch after adjusting hyperparameters and you can look at the loss plots at the end of each training step. Once a training is complete you can load that model (.h5 or .hdf5) in the DeepCore notebook and make some validation plots comparing targets and predictions. Score plots will allow you to determine an appropriate prediction threshold, parameter plots will help you evaluate how good your training is at prediction track parameters (dx, dy, deta, dphi, pt) and teh ROC curve will help you compare different trainings. You can also visualize the adc, target and predictied TCPs for a few merged clusters the 4 BPIX layers. 

## B) Set up (Fermilab GPUs):
- ssh to any FNAL gpu server (1/2/3): `ssh hichemb@cmslpcgpu1.fnal.gov -Y`
- Make a temporary (30 days) directory for your files using: `mkdir /storage/local/data1/gpuscratch/hichemb/`
	- Or put files to write/ read from in that directory, you can look for it using:  `/usr/bin/find /storage/local/data1/gpuscratch`
	- Check that the space is not full using: `df -H`
- clone repo: `git clone git@github.com:bouchamaouihichem/DeepCore.git`
- copy training samples to scratch directory: `cp -r /eos/uscms/store/user/hichemb/DeepCore_Training/`
  	- The reason we include everything in the scratch directory is because this will improve the training speed.
- Make a new directory for the training, copy training sample from eos, run the training:
	- `mkdir Training1103`
	- `cd Training1103`
	- You need to manually split training data into training and validation (not testing!) by making a directory
		- This means you need  to get an 80-20 split using file sizes or number of events
		- Note that training output gives you the number of files used for training and validation to double check
	- Then you should edit L516 to the path of your training files and L517 to the path of your validation files
  - Set up singularity environment as shown in this [FNAL page](https://uscms.org/uscms_at_work/computing/setup/gpu.shtml)

## C) Running DeepCore Training (Fermilab GPUs):
- `ssh hichemb@cmslpcgpu1.fnal.gov -Y`
- cd to `Training1103/` in scratch directory
- `screen` 
- `apptainer run -p --nv --bind /uscms/homes/h/hichemb/ --bind /cvmfs --bind /storage/local/data1/gpuscratch/hichemb/ /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fnallpc/fnallpc-docker:tensorflow-latest-gpu-singularity`
	- adjust this command accordingly
- Run DeepCore training command (details below)
- Ctrl + A + D
- logount and reconnect later to check on training by cd to the same directory then running: `screen -r`
  	- Disclaimer: you're not supposed to use the interactive GPUs for multidays trainings
  	- You can check if training is running using: `ps ahux | grep hichemb`
  	- You kill background process when you know the process ID (PID): `kill -9 'PID'`
- Training output:
  	- `weights.XXX.hdf5`: This is your model after every epoch.
  	- `DeepCore_train_XXX.h5`: This is your model at the end of the training step you ran. You can use this file to make predictions in DeepCore.py or with the DeepCore notebook.
  	- `DeepCore_mode_XXX.h5`: This is your model as well, however thsi file is the one you will subsequently use when running workflows. Don't confuse thse 2 files.
  	- `loss_file_XXX.pdf`: This pdf contains your loss plots.
  	- `loss_plots_XXX.pdf`/`loss_plots_full_XXX.csv`: These files need to be loaded in the next training step so you can replot the loss function from the first epoch.
- Example of DeepCore2.0 Training commands:
    	- 1-5 epochs: `nohup python ../training/DeepCore_GPU.py --training --epochs 5 > Training23_0622_1-5.log`
	- 6-10 epochs: `nohup python ../training/DeepCore_GPU.py --training --continueTraining --epochs 5 --epochsstart 5 --weights weights.5-1.3783.hdf5 --csv loss_plots_0_5.csv >  Training23_0622_6-10.log`
    	- 11-15 epochs: `nohup python ../training/DeepCore_GPU.py --training --continueTraining --epochs 5 --epochsstart 10 --weights weights.10-1.3783.hdf5 --csv loss_plots_full_0_10.csv >  Training23_0622_11-15.log`
- **Once a training step is complete, don't forget to backup your work since files in the gpuscratch are deleted after 30 days.**
 
## D) Running DeepCore Testing:
- You can run testing anywhere (not singularity), but make sure you have enough memory to load the test sample, which is why I typically run it on FNAL gpu servers.
- Adjust a few things in `DeepCore.py` before Testing:
  	- Edit L756 to use the appropriate model (.h5).
  	- Edit the prediction threshold, which you should have determine at this point after producing the Score plots in the DeepCore notebook.
  	- Make sure the architecture, hyperparameters, loss functions used in DeepCore.py are the same as `DeepCore_GPU.py`
- Testing Output:
  	- `DeepCore_prediction_XXX.npz`: file containing target and predictions used to make histos in root.
  	- `DeepCore_mapValidation_XXX.root`: contains pixels maps for a few merged clusters.
  	- `parameter_file_XXX.pdf`: contains parameter plots (target distribution, predistion distribution, residuals distribution and 2D plots of prediction vs target) for all track parameters (dx, dy, deta, dphi, pt).
- Example of DeepCore2.0 Training command using a testing sample file as input: `nohup python ../training/DeepCore.py --input ../../DeepCore_Training/TestingSamples/DeepCoreTestingSample.root --predict --output > Validation23_0622.log &`

## 3) Workflows (Convert_h5_to_pb/ and efficiency_plots/)
## A) model.h5 to model.pb conversion:
- After completing a training and obtaining the `DeepCore_model_XXX.h5` file (**do NOT use `DeepCore_train_XXX.h5` for this**), you need to use `DeepCore/Convert_h5_to_pb/h5_to_pb.py` to convert your model to .pb (model extension used in CMSSW workflows)
	- Due to compatibility issues, I run it the following way, but you can run it locally if you use the appropriate python, tensorflow and keras versions
		- ssh to fermilab gpu server, and copy the relevant script and .h5 file there (clone the DeepCore repo if you haven't done so).
		- Edit `h5_to_pb.py`: adjust path of input file and name and directory of output file
		- Run singularity environment and run the script: 
			- `apptainer run -p --nv --bind /uscms/homes/h/hichemb/ --bind /cvmfs --bind /storage/local/data1/gpuscratch/hichemb/ /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fnallpc/fnallpc-docker:tensorflow-latest-gpu-singularity`
			- `python h5_to_pb.py`
		- Copy `DeepCore_model_XXX.pb` to `DeepCore/efficiency_plots`
  
## B) Setup:
-  Use one of the latest CMSSW versions to avoid errors running workflows : `cmsrel CMSSW_13_0_11`
	- mainly so we can use latest detector condition with BPIX holes: `--conditions 130X_mcRun3_2023_realistic_relvals2023D_v1`
- `cd CMSSW_13_0_11/src/`
- `scram b -j 8 `
	- git cms-addpkg will not work/ take a long time otherwise
- `cmsenv`
- `voms-proxy-init -voms cms`
- `git cms-addpkg RecoTracker`
- `git cms-addpkg Configuration/DataProcessing`
- `git cms-addpkg Validation/RecoTrack`
- `scram b -j 8`
- `cp -r ~/nobackup/princeton/project2/CMSSW_10_2_5/src/DeepCore/effiency_plots/ .`
- Necessary directory to load model when running crab jobs: `cp -r effiency_plots/data RecoTracker/TkSeedGenerator/`
- Use latest version of DeepCoreSeedGenerator.cc : `cp effiency_plots/DeepCoreSeedGenerator.cc RecoTracker/TkSeedGenerator/plugins/DeepCoreSeedGenerator.cc`
- Use latest version of JetCoreRegionalStep_cff.py : `cp effiency_plots/JetCoreRegionalStep_cff.py RecoTracker/IterativeTracking/python/JetCoreRegionalStep_cff.py`
- Adjust [JetCoreRegionalStep_cff.py](https://github.com/cms-sw/cmssw/blob/dc2b480cfd4dba1c83d67100362b03759c314553/RecoTracker/IterativeTracking/python/JetCoreRegionalStep_cff.py#L13-L16) if needed:
	- disable jetcore outside of barrel by editing `RecoTracker/IterativeTracking/python/JetCoreRegionalStep_cff.py`:
		- `jetsForCoreTracking = cms.EDFilter('CandPtrSelector', src = cms.InputTag('ak4CaloJetsForTrk'), cut = cms.string('pt     > 100 && abs(eta) < 1.4'), filter = cms.bool(False))`
		- `jetsForCoreTrackingBarrel = jetsForCoreTracking.clone( cut = 'pt > 100 && abs(eta) < 1.4' )`
		- `jetsForCoreTrackingEndcap = jetsForCoreTracking.clone( cut = 'pt > 10000000 && abs(eta) < 1.4' )`
	- Enable jetcore + deepcore in the barrel and jetcore in the endcaps by editing `RecoTracker/IterativeTracking/python/JetCoreRegionalStep_cff.py`:
		- `jetsForCoreTracking = cms.EDFilter('CandPtrSelector', src = cms.InputTag('ak4CaloJetsForTrk'), cut = cms.string('pt   > 100 && abs(eta) < 2.5), filter = cms.bool(False))`
		- `jetsForCoreTrackingBarrel = jetsForCoreTracking.clone( cut = 'pt > 100 && abs(eta) < 1.4' )`
		- `jetsForCoreTrackingEndcap = jetsForCoreTracking.clone( cut = 'pt > 100 && abs(eta) < 2.5' )`
		- `MaxCand` can be edited in L161 for JetCore and DeepCore seperately			
- adjust true particle selection to ignore the ones outside barrel by editing [Validation/RecoTrack/python/TrackingParticleSelectionsForEfficiency_cff.py](github.com/cms-sw/cmssw/blob/87aa86684413a8056be46ed8bc1377e4c9954d66/Validation/RecoTrack/python/TrackingParticleSelectionsForEfficiency_cff.py)
	- change min/max eta to -1.4/1.4: L10-14 and L34-35
	- You can also change true track selection here: 
		- e.g change min pt to 10 GeV: L12 and L26 (This is an example, don't change minpt in a normal workflow!)
	- You'll need to rerun all the workflow to undo changes here
- Change x axis binning for efficiency vs R plots:
  	- Edit [Validation/RecoTrack/python/plotting/trackingPlots.py](https://github.com/cms-sw/cmssw/blob/93e2e3051588c8f931cb559201d76f9edafdb9ec/Validation/RecoTrack/python/plotting/trackingPlots.py):
		- change L213 in from `common=dict(xlog=True)` to `common=dict(xlog=False, xmin=0, xmax = 20)`
		- This will change the axis to linear instead of log and adjust the range from 0 to 20
		- It will NOT change the bins themselves
  	- Edit [Validation/RecoTrack/src/MTVHistoProducerAlgoForTracker.cc](github.com/cms-sw/cmssw/blob/87aa86684413a8056be46ed8bc1377e4c9954d66/Validation/RecoTrack/python/TrackingParticleSelectionsForEfficiency_cff.py):
		- change L194 to false so the bins are not logs
		- change L193 to N adjust bin width such that:
			- bin width = 100cm/N, so for 1 cm bins N = 100
			- I recommend picking N = 200 for 0.5cm bins
	- To change binning for other plots, follow similar steps.
	- It's better to make this change during the initial setup, but if you forgot, you can make these changes, compile and rerun step3 for the binning to changed
- Change y axis range for all plots:
	- Edit `Validation/RecoTrack/python/plotting/trackingPlots.py`:
		- change L23 to adjust max eff for all plots
		- change L181-L187 to adjust max eff/fake for pt and eta plots (ymax=)
- to see all other commands to adjust plots:
	- vim [Validation/RecoTrack/python/plotting/plotting.py](https://github.com/cms-sw/cmssw/blob/87aa86684413a8056be46ed8bc1377e4c9954d66/Validation/RecoTrack/python/plotting/plotting.py)
- `scram b -j 8`

## C) Runnning Workflows using Crab:
- ssh and cd to `effiency_plots/`
- `cmsenv`
- `voms-proxy-init -voms cms`
- make workflow crab directory by copying available template: 
	- `cp -r crab_test/ crab_11923`
	- `cd crab_11923`
- Print out the each command needed for running a workflow (4 steps)
	- `nohup runTheMatrix.py -w upgrade -l 11923.17 --command='-n 1' -j 8 -t 4 --dryRun > test.log`
	- This will not run the workflow, but give you the cmsDriver commands needed.
- Run step 1 + 2 command to obtain `cmsDriver_step12.py`:
	- Adjust the command below by replacing condition, pileup, pileup sample..etc using the commands for step 1 and 2 of the workflow as reference:
		- for example if the workflow you are running does not include pileup, then remove that part from the command above (as well as pileup_input)
		- Also you can adjust the pileup input sample if the default one is giving you errors because it is not available
	- **[Run modified version, not this exact line!]**  `cmsDriver.py QCD_Pt_1800_2400_14TeV_TuneCP5_cfi -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2022 --conditions auto:phase1_2022_realistic --beamspot Realistic25ns13p6TeVEarly2022Collision --datatier GEN-SIM-DIGI-RAW --eventcontent FEVTDEBUGHLT -n 1 --geometry DB:Extended --era Run3 --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_13_0_0_pre4-130X_mcRun3_2022_realistic_v2-v1/GEN-SIM --python_filename cmsDriver_step12.py --fileout file:step2.root > log_step12.txt`
 - Edit step12 crab config file (`cmsDriver_step12.py`):  
	- `input = cms.untracked.int32(10000),`
	- `numberOfThreads = cms.untracked.uint32(8),`
	- `annotation = cms.untracked.string('QCD_Pt_1800_2400_14TeV_TuneCP5_cfi nevts:10000'),`
- Edit step12 crab submit file (`step12_crab.py`) as needed:
	- specify name, number of jobs..etc (`:%s/12034/11923/gc` to replace with vim)
	- Adjust lines as needed depending on QCD or Ttbar
	- make sure the name is not long and does not contain "."
- `crab submit step12_crab.py`
 	- This will generate the GEN,SIM,RAW of the specified workflow. You will only need to run Step1+2 once for each workflow. Step 3 is the RECO step and uses diffent models (JetCore or DeepCore) depending on the changes you make.
	- save the publication dir since you will need it in the crab submit file for step 3
	- check status with: `crab status -d workflows_crab_11923/crab_DeepCore_11923_step12`
- before running step 3, adjust `DeepCoreSeedGenerator.cc`:
	- make sure model is in the appropriate dir: `../RecoTracker/TkSeedGenerator/data/DeepCore/`
	- adjust file to use appropriate model and thresholds (changes needed in about 5 lines)
- run step3 to obtain crab config:
	- **[Run modified version, not this exact line!]** `cmsDriver.py step3  -ss RAW2DIGI,L1Reco,RECO,RECOSIM,PAT,NANO,VALIDATION:@standardValidation+@miniAODValidation,DQM:@standardDQM+@ExtraHLT+@miniAODDQM+@nanoAODDQM --conditions auto:phase1_2022_realistic --datatier GEN-SIM-RECO,MINIAODSIM,NANOAODSIM,DQMIO --eventcontent RECOSIM,MINIAODSIM,NANOEDMAODSIM,DQM --geometry DB:Extended --era Run3 --procModifiers seedingDeepCore --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_13_0_0_pre4-130X_mcRun3_2022_realistic_v2-v1/GEN-SIM -n 1  --nThreads 8 --python_filename cmsDriver_step3.py --filein  file:step2.root  --fileout file:step3.root  > log_step3.txt`
- edit step3 crab config file (`cmsDriver_step3.py`): 
	- `input = cms.untracked.int32(10000),`
	- `numberOfThreads = cms.untracked.uint32(8),`
	- `annotation = cms.untracked.string('QCD_Pt_1800_2400_14TeV_TuneCP5_cfi nevts:10000'),`
	- To run Jetcore:
		- comment out `from Configuration.ProcessModifiers.seedingDeepCore_cff import seedingDeepCore`
		- replace `process = cms.Process('RECO',Run3,seedingDeepCore) by process = cms.Process('RECO',Run3)`
   		- you can make the JetCore cmsDriver.py config file by running step3 without `--procModifiers seedingDeepCore`
	- To run different DeepCore model, adjust `DeepCoreSeedGenerator.cc` and **compile** (`scram b -j 8` from src/) 
- edit step3 crab config file (`step3_crab.py`):
	- specify names, input dataset ..etc (`:%s/12034/12312/gc`)
	- Adjust names as needed depending on model: DeepCore213, DeepCore10 or JetCore
- `crab submit step3_crab.py`
	- `crab status -d workflow_crab_13723/crab_DeepCore_13723_step3_DC213`
- Before running step 4, you need to add the files together and you cannot hadd. Make `step3_files/` directory in `crab_11923/` and run these commands:
	- copy step3 root files from eos: `cp /eos/uscms/store/user/hichemb/DeepCore_11923_step12_1k/DeepCore_11923_s3_1k_jetcore/230318_210317/0000/step3_inDQM_* .`
	- `python3 ../../../Configuration/DataProcessing/test/RunMerge.py --input-files=file:step3_inDQM_1.root,file:step3_inDQM_2.root,file:step3_inDQM_3.root,file:step3_inDQM_4.root,file:step3_inDQM_5.root,file:step3_inDQM_6.root,file:step3_inDQM_7.root,file:step3_inDQM_8.root,file:step3_inDQM_9.root,file:step3_inDQM_10.root --output-file=Merged.root --dqmroot`
   		- Note that you need to adjust number of input files as needed
	- `cmsRun -j FrameworkJobReport.xml RunMergeCfg.py`
   	- `cp Merged.root ../`
 - Run step4 after double checking you are using the right model and thresholds:
   	- **[Run modified version, not this exact line!]** `cmsDriver.py step4  -s HARVESTING:@standardValidation+@standardDQM+@ExtraHLT+@miniAODValidation+@miniAODDQM+@nanoAODDQM --conditions auto:phase1_2022_realistic --mc  --geometry DB:Extended --scenario pp --filetype DQM --era Run3 --procModifiers seedingDeepCore --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_13_0_0_pre4-130X_mcRun3_2022_realistic_v2-v1/GEN-SIM -n 1000 --nThreads 8 --filein file:Merged.root --fileout file:step4.root  > log_step4.txt`
   	  - to run jetcore, just delete `--procModifiers seedingDeepCore`
- rename DQM file and move it: `mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root DQM_plots/11923_DC221.root`

## D) Making effciciency/fake rate plots and publishing them:  
- Once you get the `DQM_XXX.root` files you can make the efficiency plots. I recommend setting up an online CERN website to host them so it's easier to share with the group as well as Track POG and CERN people in general (details below).
- cd to DMQ_plots/ and run:  `makeTrackValidationPlots.py --extended JetCore_11723.root DeepCore2.0_11723.root`
	- `--extended` includes more plots (e.g: bunch of distributions)
- Backup workflow (`DQM.root`):
	- `mkdir /eos/uscms/store/user/hichemb/workflows/JetCore_1k_11634`
	- `cp *.root /eos/uscms/store/user/hichemb/workflows/JetCore_1k_11634`
- copy plots to my eos directory: 
	- `mkdir /eos/uscms/store/user/hichemb/efficiency_plots/11634.17/`
	- `cp -r plots/* /eos/uscms/store/user/hichemb/efficiency_plots/11634.17`
- login to lxplus and make adjustments to index.html:
	- `ssh hboucham@lxplus.cern.ch -YC`
	- `mkdir /eos/user/h/hboucham/www_hichem/11634.17`
	- from fermilab copy plots: `scp -r plots/* hboucham@lxplus.cern.ch:/eos/user/h/hboucham/www_hichem/11634.17`
	- `vim /eos/user/h/hboucham/www_hichem/index.html`
		- add line:  ```<li style ="font-size:25px;"><a href="11634.17/index.html">Worflow 11634.17</a></li>```
	- `vim /eos/user/h/hboucham/www_hichem/11634.17/index.html`: copy full workflow name and include cmssw version under <body>:
		- ```Workflow: 11634.17 2021_seedingDeepCore+TTbar_14TeV_TuneCP5_GenSim+Digi+RecoNano+HARVESTNano```
		- ```<br> CMSSW_12_6_0_pre2 -n 1000```
		- ```<br> Comparison between JetCore and DeepCore2.0```
	- Look at the plots on your personal website: https://hboucham.web.cern.ch/
- Alternatively (especially convenient for testing),  you can copy the efficiency plots to your local machine faster and just double click on index.html
	- from local machine: `scp -r hichemb@cmslpc-sl7.fnal.gov:/uscms_data/d3/hichemb/princeton/project2/workflow_10k/CMSSW_13_0_11/src/effiency_plots/crab_11923_barrel_10k/DQM_plots/plots /mnt/c/Users/bouch/DeepCore_plots/Barrel_JC_DC1_DC2_comparison`
   	- or open pdf if you have X11 forwarding enabled in your ssh.config locally: `gio open plot.pdf`

## E) Running workflows for Timing Studies:
- The reference  workflow to evaluate the time it takes to reconstruct tracks with a given model is workflow 11834.17 and 10k events (compatible with 13_0_0_pre4 )
	- refer to the usual steps to run a workflow until step 3
- Run the modified step 3 command below:
	- **[Run modified version, not this exact line!]** `cmsDriver.py step3 -s RAW2DIGI,RECO:reconstruction_trackingOnly --conditions 130X_mcRun3_2023_realistic_relvals2023D_v1 --beamspot Realistic25ns13p6TeVEarly2023Collision --datatier AOD --eventcontent AOD --geometry DB:Extended --era Run3  --procModifiers seedingDeepCore --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_13_0_0_pre4-130X_mcRun3_2022_realistic_v2-v1/GEN-SIM -n 1 --python_filename cmsDriver_step3.py --filein file:step2.root --fileout file:step3.root --customise Validation/Performance/TimeMemoryInfo.py --no_exec RAW2DIGI,RECO:reconstruction_trackingOnly,ENDJOB`
	- This command runs much faster since it only uses specific modules from the track reconstruction
	- adjust as needed for different workflows
	- remove `--procModifiers seedingDeepCore` when running with JetCore
 - Edit `cmsDriver_step3.py`:
	- `input = cms.untracked.int32(10000),`
	- include the appropriate path to the inputs files (step12 output in your eos)
	- Copy the lines in the Timing Service [Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/FastTimerService) at the very end 
		- you're not using a separate harvesting job so you'll need to apply small changes as instructed in the Twiki
- Adjust the model you're using by editing `DeepCoreSeedGenerator.cc` and compiling 
- `cmsRun cmsDriver_step3.py`
	- The Timing information will be printed out after all 10k events are processed
   	- make sure you run the same machine (e.g: cmslpc104) and that it is not in use (check that with command: top)
   	- Normalize modules timing by looking at a module that is independent of the model used (JetCore or DeepCore2.0) like "ConvTrackCandidates"
	- For some reason I can't pipe output of this command to a log file in csh, so use bash:
		- `bash`
		- `nohup cmsRun cmsDriver_step3.py > step3_timing.txt &`

## F) CERN website setup:
- Make a directory on lxplus eos (from your lxplus account): `mkdir /eos/user/h/hboucham/www`
- Copy files from fermilab to that lxplus directory: `rsync -r /eos/uscms/store/user/hichemb/11923.17/plots/* hboucham@lxplus.cern.ch:/eos/user/h/hboucham/www`
- Go to [CERNBox](https://cernbox.docs.cern.ch) to share access to this folder on webeos following these instructions
- Go to this [WebEOS](https://webservices-portal.web.cern.ch/webeos/) and make the website following [these rules](https://webeos.docs.cern.ch/create_site/), e.g:
	- test
	- test-deepcore-efficiency-plots
	- Link to efficiency plots of workflow 11923.17 comparing the efficiency plots of DeepCore barrel model 2017 (DQM_1) to DeepCore barrel model 2022 (DQM_2)
	- /eos/user/h/hboucham/www
	- Wait a few minutes, website is: https://test-deepcore-efficiency-plots.web.cern.ch
- Alternatively, you want to make a personal website in the future where you can host all your plots for each workflow and more
	- personal
	- Hboucham
	- website containing Hichem's work on DeepCore and more
	- eos/user/h/hboucham/www_hichem
	- Wait a few minutes, website is:  https://hboucham.web.cern.ch/
	- Customize your website using html 







