import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'DeepCore_11923_step12' #name of the job, adjust for each step
config.General.workArea = 'workflows_crab_11923' ##name of your local crab dir, same for a given workflow
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'cmsDriver_step12.py' #name of the cms config file
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores=8 # number of threads, 8 is fastest
config.JobType.maxMemoryMB=20000 #memory used, use 20000MB for faster jobs, but it may stay idle for longer

config.section_("Data")
config.Data.outputPrimaryDataset = 'DeepCore_11923' #name of the dir in your eos where the files are located, same for a given workflow
config.Data.splitting = 'EventBased' # splitting of files
config.Data.unitsPerJob = 100 #QCD # number of events per job
#config.Data.unitsPerJob = 200 #TTbar
NJOBS = 10 #QCD # number of jobs
#NJOBS = 50 #TTbar
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'DeepCore_11923_step12' # partial name of dataset when published, adjust for each step

config.section_("Site")

#config.Site.storageSite = 'T3_CH_CERNBOX'
config.Site.storageSite = 'T3_US_FNALLPC' # site where files stored
