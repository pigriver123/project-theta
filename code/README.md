##CODE

The code folder contains two subdirectories. Utils contains our functions for 
analysis, our functions for graphing, and our tests. Scripts contains the 
scripts that utilize these functions.

Our makefile is written such that when run from the code directory:

- 'make test' will run the tests inside utils/tests to check our functions
- 'make coverage' will check the coverage of our functions
