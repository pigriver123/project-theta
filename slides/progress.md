% Project Theta Progress Report
% Brian Qiu, Benjamin Hsieh, Siyao Chang, Boying Gong, Jiang Zhu
% November 12, 2015

# Background

## The Paper

- from OpenFMRI.org
- ds005

## The Data

- 16 subjects
- 4 conditions per subject

# Initial work

## EDA

- downloaded data
- simple plots, summary statistics

# Plan

## Models and analysis

- Behavioral analysis

Logistic regression model on the behavioral data:

\begin{equation}
logit(Y_{resp}) = \beta_0 + \beta_{loss} *X_{loss} + \beta_{gain} * X_{gain}  + \epsilon
\end{equation}

Calculate the the behavioral loss aversion:

\begin{equation}
\lambda = -\beta_{loss} / \beta_{gain}
\end{equation}

## Models and analysis (Continued)

- Linear Regression on BOLD data

For each voxel $i$, we fit a multiple linear model:

\begin{equation}
Y_{i} = \beta_{i, 0} + \beta_{i, loss} *X_{loss} + \beta_{i, gain} * X_{gain}  + \epsilon_i
\end{equation}

For each voxel, we calculate the neural loss aversion $\eta_i$:

\begin{equation}
\eta_i = (-\beta_{loss}) - \beta_{gain}
\end{equation}

## Models and analysis (Continued)

- Whole brain analysis of correlation between neural activity and behavioral response across participants

Examine the relationship between neural activity and behavioral using the following regression model:

\begin{equation}
\lambda = \alpha_0 + \alpha_1 * \eta + \epsilon
\end{equation}

## Models and analysis (Continued)

- Inferences on Data

1. Test the normal assumption of residuals in linear models

2. Test of significance of coefficients

3. Calculate the (adjusted) R squares.

## Explanation on model simplification

- Use of Data

Leave out the regressor euclidean distance to indifference

- Simplification of regression on BOLD data

Perform simple linear models rather than mixed effect models

## Issues with analyses and potential solutions

- Selecting specific regions to further explore correlation between neural and behavioral activity

1. Further research on brain 

2. Look for regions with most significant neural loss aversion and regression coefficients

- Producing heat map

Need to map bold data onto standard brain

# Our Process

## Hardest part of process?
- Working with the FMRI data and trying to understand our paper
- Keeping up with documentation 

## Success in overcoming these obstacles?
- Using git workflows to raise issue and problems for the group.
- Limited success in the FMRI part, still figuring things out. 

# Our Process Part 2
## Issues facing the team?
- Debugging each other's code when travis CI fails in a pull request
- Addressing this by meeting up for teamwork or ask for help

## Most helpful?
- Python/numpy, lab sections with git workflows

## Most confusing?
- FMRI lectures

# Our Process Part 3

## What do you need to do to successfully complete the project?
- Have a clear idea of what we can get done
- Make work as reproducible as possible

## Diffuculty in reproducibility?
- Very frustrating if Travis fails on a pull request
- Remembering to write documentation in the scripts
- Test functions for plotting functions are hard to write/assert
- With a lot of work we may be able to get most of it reproducible

## Remaining weeks:
- Mostly unstructured time would be helpful
- Could cover:
  - Software tools like statmodels, make
  - More regression: linear and logistic
