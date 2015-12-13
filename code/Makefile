.PHONY: clean test verbose coverage

clean:
	find .. -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" -o -name "testnib.nii.gz" -o -name "temp.txt" | xargs rm -f

test:
	nosetests code/utils/tests -w ..

verbose:
	nosetests -v code/utils/tests -w ..


coverage:
	nosetests code/utils/tests -w .. --with-coverage --cover-package=utils/functions

# Analysis commands

histogram:
	python scripts/find_mask_threshold.py

diagnostics:
	python scripts/graph_lindiag_script.py
	python scripts/findoutlier.py
	python scripts/graphoutlier.py

logistic:
	python scripts/logistic.py

smoothing:
	python scripts/make_smooth_graphs.py

glm:
	python scripts/regression_script.py

mixedmodel:
	python scripts/lme_script.py

analyses:
	make histogram
	make smoothing
	make glm
	make logistic
	make diagnostics
	make mixedmodel
