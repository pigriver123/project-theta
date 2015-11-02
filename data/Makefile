data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw.tgz

validate:
	python data.py

unzip:
	tar -xvzf ds005_raw.tgz 
	for i in {1..9}
	do
	for j in {1..3}
	do
	gunzip ds005/sub00${i}/BOLD/task001_run00${j}/bold.nii.gz
	done
	done
	
	for i in {10..16}
	do
	for j in {1..3}
	do
	gunzip ds005/sub0${i}/BOLD/task001_run00${j}/bold.nii.gz
	done
	done
	
