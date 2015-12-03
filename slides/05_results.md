# Results

## Behavioral Analysis

- Fit Logistic regression model on the behavioral data
\begin{equation}
\textrm{log}\frac{p(X)}{1-p(X)} = \beta_0 + \beta_{loss} *X_{loss} + \beta_{gain} * X_{gain}
\end{equation}
where the response are categorical variable indicating acceptance or rejection of a gamble.

- Calculate the behavioral loss aversion
\begin{equation}
\lambda = -\beta_{loss} / \beta_{gain}
\end{equation}

- Model diagnosis
\begin{itemize}
\item Accuracy of Logistic models on the training set:\\
median = 89.78\% min = 80.97\% max = 99.21\%
\item Accuracy using 10-fold cross-validation: \\
median = 89.86\% min = 79.92\% max = 98.45\%
\end{itemize}

## Behavioral Analysis (Continued)

\begin{figure}
\caption{Box plot of the behavioral loss aversion $\lambda$ }
\centering
\includegraphics[scale=0.27]{../paper/figures/lambda_boxplot.png}
\end{figure}
The behavioral loss aversion $\lambda$ (median=1.94, mean=2.18) indicate that participants are indifferent to gambles whose gain are appoxiamtely twice as the loss. 

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
        \includegraphics[scale=0.25]{../paper/figures/sub2gain_heatmap.png}
    \caption{Coefficients of the gain values for subject 2}
\end{figure}

## Linear Regression on fMRI data (continued)
\begin{figure}[H]
    \centering
        \includegraphics[scale=0.25]{../paper/figures/sub2loss_heatmap.png}
    \caption{Coefficients of the loss values for subject 2}
\end{figure}

## Linear Regression on fMRI data (continued)
\begin{figure}[H]
    \centering
        \includegraphics[scale=0.25]{../paper/figures/sub2diff_heatmap.png}
    \caption{Difference between gain and loss coefficients for subject 2}
\end{figure}

## Linear Regression on fMRI data (continued)
 - Plan
 - Calculate the t statistics for each voxel, subset all the voxels with significant coefficients
 - Produce heat maps of the t statistics for the gain and loss coefficients of each voxel
 - Identify regions that have significant brain activation.

## Mixed-effects Model on fMRI data

- ANOVA test for each subject each voxels, grouping by runs
\par
The high proportion of significant F-test (after Bonferroni correction 
under 0.05 significant level) shows that mixed effects model may perform well 
when collapsing three runs into one model. 
\begin{figure}[H]
\caption{Box plot of the proportion of significant ANOVA test}
\centering
\includegraphics[scale=0.45]{../paper/figures/anova_prop.png}
\end{figure}

## Mixed-effects Model on fMRI data (Continued)

For each voxel $i$, we fit the following mixed-effects models, note that here we only include the intercept term for random effects. 

\begin{eqnarray}
Y_{i, k} & = & \beta_{i, 0} + \beta_{i,1} *X_{ldrift} + \beta_{i, 2} * X_{qdrift} + \beta_{i, loss} *X_{loss}\nonumber\\
&&  + \beta_{i, gain} * X_{gain}  + \gamma _{i, k} + \epsilon_{i, k}, \quad k =1, 2, 3
\end{eqnarray}

Then we calculate the neural loss aversion $\eta_i$:

\begin{equation}
\eta_i = (-\beta_{loss}) - \beta_{gain}
\end{equation}

The mixed-effects model for each subject yielded a a median of 9.4\% (min=6.4\%, 
max=21.5\%) and 8.3\% (min=4.6\%, max=15.4\%) of proportion of significant 
coefficient for gain and loss separately. 

## Mixed-effects Model on fMRI data (Continued)
\begin{figure}[H]
\caption{heatmap of coefficient of gain for subject 002}
\centering
\includegraphics[scale=0.22]{../paper/figures/sub002_lme_beta_gain.png}
\end{figure}
