#!/bin/bash
#BSUB -n 72                     # number of processors
#BSUB -P pti-ca                     # queue name
#BSUB -We 12:00
#BSUB -o out.%J                     # output file
#BSUB -R 'span[ptile=36]'


[[ -r /glb/apps/hpc/Lmod/etc/profile.d/z01_lmod-hpcs.sh  ]] && . /glb/apps/hpc/Lmod/etc/profile.d/z01_lmod-hpcs.sh
ml load VASP/5.4.1.24-intel-2017.02

mpirun vasp_std  
 

