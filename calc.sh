#!/bin/sh
#SBATCH -J test
#SBATCH -D /mnt/scratch/users/kostya_2100/calc
#SBATCH -o test.out
#SBATCH -e test.err
#SBATCH -t 00:15:00
#SBATCH -p test
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH -N 5
#SBATCH --exclude=
#SBATCH --nodelist=
hostname
df
date

module load impi/5.0.0.028 intel/15.0.3
mpiexec.hydra -perhost $SLURM_NTASKS_PER_NODE -n $(($SLURM_JOB_NUM_NODES*$SLURM_NTASKS_PER_NODE)) ./prog_bug.exe
