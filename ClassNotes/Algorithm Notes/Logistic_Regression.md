#Logistic Regression

##What data problem does it solve?

Categorical (usually binary), supervised (we know the target)

##How do we evaluate performance performance

Accuracy: number correct over total number of observations
Correlation, chi-squared test (feature)

##What is the output?

Probability. In order to assign either 0 or 1 for each row need to decide on a threshold, usually .5

##What is interpretable of the algorithm?

Coefficients (log-odds) - when these features show up what are the odds of something occuring?
Average results given no information

##How is it prone to overfitting?

Similar concerns to linear regression

##How is it customizable?

Alpha, can adjust the weight to improve predicition (e.g. if weighting of training set doesn't reflect feature influence for future features).