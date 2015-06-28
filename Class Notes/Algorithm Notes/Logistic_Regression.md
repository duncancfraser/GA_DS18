#Logistic Regression

##What data problem does it solve?

Classification, supervised.

##How do we evaluate performance performance

* Accuracy: number correct over total number of observations
* Correlation, chi-squared test

##What is the output?

Probability coefficient: to assign either 0 or 1 for each row determine a threshold (usually .5).

##What is interpretable of the algorithm?

* Coefficients (log-odds) - when these features show up what are the odds of something occuring?
* Average results (rate of occurance) given no information

##How is it prone to overfitting?

Similar concerns to linear regression

##How is it customizable?

Alpha: adjusts the weight given to features (e.g. if weighting of training set doesn't reflect feature influence for future features).