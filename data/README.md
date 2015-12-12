The ds005 dataset, filtered ds005 dataset, and mni templates are stored here. Th
e makefile is written such that:
 
- 'make data' will pull in the appropriate data 
- 'make unzip' will unzip, remove, and rename certain files
- 'make validate' will run data.py to check the hashes of each downloaded file w
ith a master hashlist included, ensuring all downloaded data is correct  

THE COMMANDS SHOULD BE DONE IN THIS ORDER to be successfully validated. The ds00
5 folder contains subfolders for each subject, the most relevant of which are:

- BOLD: raw data of fMRI scans for each of the subjects three runs, as well as d
isplacement/variance data 
- behav: file for each run that contains the onsets, potential gains, potential 
losses, and response of each trial
- model: filtered, processed data of fMRI scans for each of the subjects three r
uns, and the onsets files
-
