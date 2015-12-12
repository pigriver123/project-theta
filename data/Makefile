.PHONY: data validate unzip test

data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw.tgz
	wget http://nipy.bic.berkeley.edu/rcsds/ds005_mnifunc.tar
	wget http://nipy.bic.berkeley.edu/rcsds/mni_icbm152_nlin_asym_09c_2mm.tar.gz

validate:
	python data.py

unzip:
	tar -xvzf ds005_raw.tgz 
	tar -xvf ds005_mnifunc.tar
	tar -xvzf mni_icbm152_nlin_asym_09c_2mm.tar.gz
	rm ds005_raw.tgz
	rm ds005_mnifunc.tar
	rm mni_icbm152_nlin_asym_09c_2mm.tar.gz
	mv mni_icbm152_nlin_asym_09c_2mm templates
	mv templates/mni_icbm152_t1_tal_nlin_asym_09c_2mm.nii templates/mni_standard.nii

test:
	nosetests data/tests -w ..
