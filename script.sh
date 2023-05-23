#!/bin/bash

#SBATCH -p nvidia
#SBATCH --gres=gpu:2

#Max wallTime for the job
#SBATCH -t 30:00:00


#Resource requiremenmt commands end here

# Output and error files
#SBATCH -o Errors/job.%J.out
#SBATCH -e Errors/job.%J.err


module purge 

source /share/apps/NYUAD/miniconda/3-4.11.0/bin/activate

conda activate tf-env2


#echo $LD_LIBRARY_PATH

#Execute the code
#python test.py
python main.py "../Database/TrainSet" "../Database/TestSet"