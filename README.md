# GR_adaptation_scripts

This repository contains scripts for simulations in 'Local Adaptations under Genetic Rescue' , please check the paper for specific details in our study.

Scripts here contain those used for simulations with SLiM (*.slim files) and for follow up data analysis and plotting. slim scripts here were written based on manual of SLiM v3.0 and run with SLiM-4.

## hard_sweep
This folder contains slim scripts for simulations supposing a Mendelian trait under hard sweep. Note that all parameters that we have varied in our study are marked in slim scripts, different scenarios could be replicated by changing input files and parameters.

## soft_sweep
This folder contains slim scripts for simulations supposing a Mendelian trait under soft sweep. Again, all varied parameters are marked in slim scripts.

## stabilizing
This folder contains slim scripts for simulations supposing a polygenic trait under stabilizing selection. Note that effect sizes of mutations under stabilizing selection are not contained in the outputFull file of SLiM, thus a seperate output containing the information should be kept along the simulation process. For example, after running
```
./slim simulation_script.slim > slim.out 
```
I used ```extract_effect_44000/60000.py```to extract information from slim.out, then introduce it to next step simulation script and reset effect sizes for those mutations.
