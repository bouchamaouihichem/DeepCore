#!/bin/bash

mkdir data
cd data
xrdcp -r root://eosuser.cern.ch///eos/user/n/nihaubri/DeepCore_data/latest/tdf .
mv */* .
cd ..

#start
singularity run --nv /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fnallpc/fnallpc-docker:tensorflow-2.12.0-gpu-singularity -c "python DeepCore_GPU.py --training --epochs 30 --dir data/"

#continue
#singularity run --nv /cvmfs/unpacked.cern.ch/registry.hub.docker.com/fnallpc/fnallpc-docker:tensorflow-2.12.0-gpu-singularity -c "python DeepCore_GPU.py --training --epochs 30 --dir data/ --continueTraining --epochsstart 30 --weights models/DeepCore_train_ev8069968_ep30.h5 --lr .0004"

#if debug, return tensorboard trace
#cd tflogs
#tar -czvf prof.tar.gz *
#cd ..
#mv tflogs/prof.tar.gz .
