data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw.tgz
<<<<<<< HEAD

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
	
=======
	tar -xvzf ds005_raw.tgz
	#wget http://nipy.bic.berkeley.edu/rcsds/ds005_mnifunc.tar
	#tar -xvf ds005_mnifunc.tar
	rm ds005_raw.tgz
	#rm ds005_mnifunc.tar

validate:
	python data.py	
>>>>>>> a96098ccbb47c304f972e54f9161165806dc04f1
