# Results

## Behaviral Analysis

## Linear Regression on fMRI data
 - Model
\begin{equation}
\begin{split}
Y_{i} = & \beta_{i, 0} + \beta_{i,gain} *X_{gain} + \beta_{i, loss} * X_{loss} \\
 & + \beta_{i, ldrift} *X_{ldrift} + \beta_{i, qdrift} * X_{qdrift}  + \epsilon_i
\end{split}
\end{equation}
where $Y_{i}$ is the BOLD data of voxel $i$,  $X_{ldrift}$ and $X_{qdrift}$ are linear and quadratic drift terms.

## Linear Regression on fMRI data (continued)
 - Interested in the coefficients of parametric gain and parametric loss regressor
 - Get a general idea of how potential gains and potential losses affect brain activation
 - Plot heat maps for gain and loss coefficients, identify the areas that have large coefficients
 - Identify regions with significant activation and regions that show a significant correlation between brain activation and potential gains/losses
 - Compute the neural loss aversion
\begin{equation}
\eta_i = (-\beta_{loss}) - \beta_{gain}
\end{equation}

## Linear Regression on fMRI data (continued)
\begin{figure}[H]
    \centering
        \includegraphics[scale=0.25]{../draft/figures/sub2gain_heatmap.png}
    \caption{Coefficients of the gain values for subject 2}
\end{figure}

## Linear Regression on fMRI data (continued)
\begin{figure}[H]
    \centering
        \includegraphics[scale=0.25]{../draft/figures/sub2loss_heatmap.png}
    \caption{Coefficients of the loss values for subject 2}
\end{figure}

## Linear Regression on fMRI data (continued)
\begin{figure}[H]
    \centering
        \includegraphics[scale=0.25]{../draft/figures/sub2diff_heatmap.png}
    \caption{Difference between gain and loss coefficients for subject 2}
\end{figure}

## Linear Regression on fMRI data (continued)
 - Plan
 - Calculate the t statistics for each voxel, subset all the voxels with significant coefficients
 - Produce heat maps of the t statistics for the gain and loss coefficients of each voxel
 - Identify regions that have significant brain activation.


## Mixed-effects Model on fMRI data
