import uproot
import h5py
import numpy as np
import glob
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf
import pdb
import multiprocessing

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

def ROOTToOneTFRec(rootfiles,oname,chunksize):
    if len(rootfiles)==0:
        return
    options = tf.io.TFRecordOptions(compression_type="ZLIB",compression_level=1)
    writer = tf.io.TFRecordWriter(oname,options=options)
    
    index=0
    for cycle in range(1,9):
        print(cycle)
        for chunk in uproot.iterate(["{}:{}/{};{}".format(rootfilename,inputModuleName,inputTreeName,str(cycle)) for rootfilename in rootfiles],branches,step_size=chunksize,library="np"):
            nev = len(chunk["trackProb"])
            
            target_prob = np.reshape(chunk["trackProb"], (nev,jetDim,jetDim,overlapNum,1))
            target_prob = np.concatenate([target_prob,chunk["trackPar"][:,:,:,:,-1:]],axis=4)
            cdict = {}
            cdict["cluster_measured"] = tf.convert_to_tensor(chunk["cluster_measured"][:,:,:,0:layNum].astype(np.float16)) #remove endcap layers for now
            cdict["jet_eta"] = tf.convert_to_tensor(chunk["jet_eta"].astype(np.float16))
            cdict["jet_pt"] = tf.convert_to_tensor(chunk["jet_pt"].astype(np.float16))
            cdict["trackPar"] = tf.convert_to_tensor(chunk["trackPar"].astype(np.float16))
            cdict["trackProb"] = tf.convert_to_tensor(target_prob.astype(np.float16))
            for i in range(nev):
                
                record = tf.train.Example(features=tf.train.Features(feature={
                    'cluster_measured': tf.train.Feature( bytes_list=tf.train.BytesList(value=[tf.io.serialize_tensor(cdict['cluster_measured'][i]).numpy() ])),
                    'jet_eta': tf.train.Feature( bytes_list=tf.train.BytesList(value=[tf.io.serialize_tensor(cdict['jet_eta'][i]).numpy()])),
                    'jet_pt': tf.train.Feature( bytes_list=tf.train.BytesList(value=[tf.io.serialize_tensor(cdict['jet_pt'][i]).numpy()])),
                    'trackPar': tf.train.Feature(bytes_list=tf.train.BytesList(value=[tf.io.serialize_tensor(cdict['trackPar'][i]).numpy()])),
                    'trackProb': tf.train.Feature(bytes_list=tf.train.BytesList(value=[tf.io.serialize_tensor(cdict['trackProb'][i]).numpy()]))

                })).SerializeToString()
                writer.write(record)
            #break

def runAsync(files,oname,batchsize,Nprocs):
    #print("files",files)
    pool = multiprocessing.Pool(Nprocs)
    splitfiles = [[] for x in range(Nprocs)]
    for i,fname in enumerate(files):
        splitfiles[i%Nprocs].append(fname)
    results = []
    for i in range(Nprocs):
        result = pool.apply_async( ROOTToOneTFRec, args=(splitfiles[i], oname+str(i), batchsize) )
        results.append( result )
    print(results)
    [result.wait() for result in results]

h5dir="/eos/user/n/nihaubri/DeepCore_data/latest/tdf/"
train_path = "/eos/user/n/nihaubri/DeepCore_data/latest/TrainingSamples/training/*.root*"
val_path = "/eos/user/n/nihaubri/DeepCore_data/latest/TrainingSamples/validation/*.root*"

runAsync(glob.glob(train_path),h5dir+"train.tfr",512,6)
runAsync(glob.glob(val_path),h5dir+"val.tfr",512,6)
