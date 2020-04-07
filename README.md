# GR_adaptation_scripts

This repository contains scripts for simulations in 'Local Adaptations under Genetic Rescue' , please check the paper for specific details on our study.

Scripts here contain those used for simulations with SLiM (*.slim files) and for follow up data analysis and plotting.

## hard_sweep
This folder contains slim scripts for simulations supposing a Mendelian trait under hard sweep. Note that all parameters that we have varied in our study are marked in slim scripts, different scenarios could be replicated by changing input files and parameters.

## soft_sweep
This folder contains slim scripts for simulations supposing a Mendelian trait under soft sweep. Also, all varied parameters are marked in slim scripts.

## stabilizing
This folder contains slim scripts for simulations supposing a polygenic trait under stabilizing selection. Note that effect size of mutations are not contained in the outputFull file of SLiM output, thus a seperate output containing the information should be kept along the simulation process. See more explanation in Details.txt.
