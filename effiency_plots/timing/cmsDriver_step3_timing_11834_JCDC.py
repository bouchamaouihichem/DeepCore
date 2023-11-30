# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 -s RAW2DIGI,RECO:reconstruction_trackingOnly --conditions 130X_mcRun3_2023_realistic_relvals2023D_v1 --beamspot Realistic25ns13p6TeVEarly2023Collision --datatier AOD --eventcontent AOD --geometry DB:Extended --era Run3 --procModifiers seedingDeepCore --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_13_0_0_pre4-130X_mcRun3_2022_realistic_v2-v1/GEN-SIM -n 1 --python_filename cmsDriver_step3.py --filein file:step2.root --fileout file:step3.root --customise Validation/Performance/TimeMemoryInfo.py --no_exec RAW2DIGI,RECO:reconstruction_trackingOnly,ENDJOB
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.ProcessModifiers.seedingDeepCore_cff import seedingDeepCore

process = cms.Process('RECO',Run3,seedingDeepCore)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_1.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_2.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_3.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_4.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_5.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_6.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_7.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_8.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_9.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_10.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_11.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_12.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_13.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_14.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_15.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_16.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_17.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_18.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_19.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_20.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_21.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_22.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_23.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_24.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_25.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_26.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_27.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_28.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_29.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_30.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_31.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_32.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_33.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_34.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_35.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_36.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_37.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_38.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_39.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_40.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_41.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_42.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_43.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_44.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_45.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_46.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_47.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_48.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_49.root",
      "file:/eos/uscms/store/user/hichemb/DeepCore_11834_step12_bpixnojc/DeepCore_11834_step12_bpixnojc/230828_202435/0000/step2_50.root"),
    secondaryFileNames = cms.untracked.vstring()
)

      # Input source
#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:step2.root'),
#    secondaryFileNames = cms.untracked.vstring()
#)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AOD'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.AODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_relvals2023D_v1', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Validation.Performance.TimeMemoryInfo
from Validation.Performance.TimeMemoryInfo import customise 

#call to customisation function customise imported from Validation.Performance.TimeMemoryInfo
process = customise(process)

# End of customisation functions


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
# remove any instance of the FastTimerService
if 'FastTimerService' in process.__dict__:
     del process.FastTimerService

# instrument the menu with the FastTimerService
process.load( "HLTrigger.Timer.FastTimerService_cfi" )
#
# print a text summary at the end of the job
process.FastTimerService.printEventSummary        = False
process.FastTimerService.printRunSummary          = False
process.FastTimerService.printJobSummary          = True
#
# enable DQM plots
process.FastTimerService.enableDQM                = True
#
# enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
process.FastTimerService.enableDQMbyPath          = True
#
#     # enable per-module DQM plots
process.FastTimerService.enableDQMbyModule        = True
#
# enable DQM plots vs lumisection
process.FastTimerService.enableDQMbyLumiSection   = True
process.FastTimerService.dqmLumiSectionsRange     = 2500 # lumisections (23.31 s)
#
# set the time resolution of the DQM plots
process.FastTimerService.dqmTimeRange             = 1000.   # ms
process.FastTimerService.dqmTimeResolution        =    5.   # ms
process.FastTimerService.dqmPathTimeRange         =  100.   # ms
process.FastTimerService.dqmPathTimeResolution    =    0.5  # ms
process.FastTimerService.dqmModuleTimeRange       =   40.   # ms
process.FastTimerService.dqmModuleTimeResolution  =    0.2  # ms
#
# set the base DQM folder for the plots
process.FastTimerService.dqmPath                  = "HLT/TimerService"
process.FastTimerService.enableDQMbyProcesses     = False

# FastTimerService client
process.load('HLTrigger.Timer.fastTimerServiceClient_cfi')
process.fastTimerServiceClient.dqmPath = "HLT/TimerService"

# DQM file saver
process.load('DQMServices.Components.DQMFileSaver_cfi')
process.dqmSaver.workflow = "/HLT/FastTimerService/All"

process.DQMFileSaverOutput = cms.EndPath( process.fastTimerServiceClient  + process.dqmSaver )
