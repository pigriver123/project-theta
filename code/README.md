## CODE

The code folder contains two subdirectories. Utils contains our functions for 
analysis, our functions for graphing, and our tests. Scripts contains the 
scripts that utilize these functions.
## Data Analysis

The Makefile contains the following commands: `clean`, `test`, `verbose` and`coverage` (run from code directory):

- `make test`: Runs function tests in utils/tests on functions that are associated with analyzing the data (in utils/functions).
- `make verbose`: Verbose version of `make test`.
- `make clean`: Cleans for temporary files generate by script runs or test runs.
- `make coverage`: Generates a coverage report of functions used in analysis.

## Instructions of Generating Analysis and Figures

Possible edit??