import CRABClient
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
### Request Name
#config.General.requestName = 'DeepCore_11923_step3_JC'
#config.General.requestName = 'DeepCore_11923_step3_DC10'
config.General.requestName = 'DeepCore_11923_step3_DC221'

config.General.workArea = 'workflow_crab_11923'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'

### Config files
config.JobType.psetName = 'cmsDriver_step3.py'

#config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores=8
config.JobType.maxMemoryMB=20000

config.section_("Data")
config.Data.inputDataset = '/DeepCore_11923_BPIX/hboucham-DeepCore_11923_BPIX_step12-f25c8477fd659ec2e90394fa24b51906/USER' # DAS name of the published input dataset
config.Data.splitting = 'FileBased'
config.Data.inputDBS = 'phys03' # input DBS: typically 'phys03' for privately produced and published datasets and 'global' for official datasets
config.Data.unitsPerJob = 1 # number of unit per job, here it's 1 file
config.Data.publication = False # no publicatuion necessary since step4 is local

### output tag
#config.Data.outputDatasetTag = 'DeepCore_11923_step3_JC'
#config.Data.outputDatasetTag = 'DeepCore_11923_step3_DC10'
config.Data.outputDatasetTag = 'DeepCore_11923_step3_DC221'

config.section_("Site")
#config.Site.storageSite = 'T3_CH_CERNBOX'
config.Site.storageSite = 'T3_US_FNALLPC'

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False'] # Forcing jobs to run in the site where the input dataset is located (Fermilab)

