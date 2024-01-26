import uproot
import h5py
import numpy as np
import glob

#path="Training0217/training/DeepCoreTrainingSample_11.root"
#path="Training0217/training/DeepCoreTrainingSample_"

inputModuleName= "DeepCoreNtuplizerTest"
inputTreeName= "DeepCoreNtuplizerTree"
branches = ["cluster_measured","jet_eta","jet_pt","trackPar","trackProb"]
batch_size=64
layNum = 4
jetDim = 30
overlapNum=3
dtype='f2'
branch_shapes = {'cluster_measured': [-1,jetDim,jetDim,layNum], 'jet_eta': [-1], 'jet_pt': [-1], 'trackPar': [-1,jetDim,jetDim,overlapNum,6],'trackProb': [-1,jetDim,jetDim,3,2]}

def ROOTToOneHDF5(rootglob,oname,chunksize):
    #first get nrows from root 
    totrows=0
    for cycle in range(1,9):
        for chunk in uproot.iterate("{}:{}/{};{}".format(rootglob,inputModuleName,inputTreeName,str(cycle)),['jet_eta'],step_size=100000,library="np"):
            totrows+=chunk['jet_eta'].shape[0]
    totrows=totrows-totrows%chunksize #throw out edge batch
    print(totrows)

    #create hdf5 file
    with h5py.File(oname,'w',libver='latest') as ofile:
        for branch in branches:
            oshape = branch_shapes[branch]
            oshape[0]=totrows
            chunkshape=list(oshape)
            chunkshape[0]=chunksize
            oshape=tuple(oshape)
            chunkshape=tuple(chunkshape)

            ofile.create_dataset(branch,shape=oshape,compression='gzip',dtype=dtype,chunks=chunkshape) #specify chunk size 

        #now add all rootfiles to hdf5 file
        index=0
        for cycle in range(1,9):
            print(cycle)
            for chunk in uproot.iterate("{}:{}/{};{}".format(rootglob,inputModuleName,inputTreeName,str(cycle)),branches,step_size=chunksize,library="np"):
                nev = len(chunk["trackProb"])
                if nev!=batch_size: continue
                target_prob = np.reshape(chunk["trackProb"], (nev,jetDim,jetDim,overlapNum,1))
                target_prob = np.concatenate([target_prob,chunk["trackPar"][:,:,:,:,-1:]],axis=4)

                cdict = {}
                cdict["cluster_measured"] = chunk["cluster_measured"][:,:,:,0:layNum].astype(np.float16) #remove endcap layers for now
                cdict["jet_eta"] = chunk["jet_eta"].astype(np.float16)
                cdict["jet_pt"] = chunk["jet_pt"].astype(np.float16)
                cdict["trackPar"] = chunk["trackPar"].astype(np.float16)
                cdict["trackProb"] = target_prob.astype(np.float16)

                for branch in branches:
                    ofile[branch][index:index+chunksize]=cdict[branch]
                index+=chunksize

        #remove empty space left by incomplete chunks
        for branch in branches:
            oshape=list(branch_shapes[branch])
            oshape[0]=index
            oshape=tuple(oshape)
            ofile[branch].resize(oshape)
#fileToHDF5(path+"11.root") #fileToHDF5(path+"12.root") #mergeHDF5("Deep*.hdf5","sum.hdf5") ROOTToOneHDF5("Training0217/training/DeepCoreTrainingSample_*root","sum.hdf5",64) 

h5dir="/storage/local/data1/gpuscratch/njh/DeepCore_data/DeepCore_Training/"
ROOTToOneHDF5("/storage/local/data1/gpuscratch/njh/DeepCore_data/DeepCore_Training/TrainingSamples/training/*11.root",h5dir+"onetftrain.hdf5",64)
#ROOTToOneHDF5("/storage/local/data1/gpuscratch/njh/DeepCore_data/DeepCore_Training/TrainingSamples/training/*root",h5dir+"train.hdf5",64)
#ROOTToOneHDF5("/storage/local/data1/gpuscratch/njh/DeepCore_data/DeepCore_Training/TrainingSamples/validation/*root",h5dir+"val.hdf5",64)
