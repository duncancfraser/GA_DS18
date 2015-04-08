#Naive Bayes
##What data problem does it solve?

Classification, supervised learning problem.

##How do we evaluate performance performance

* Accuracy: measure of correctly predicted over all observations.
* Confusion Matrix: a matrix of true values versus predicted values

##What is the output?

Probability of y, given a set of features variable (opposite of logistic regression)

##What is interpretable of the algorithm?

* 'Bayes coefficient': Probability of feature showing up, given a target variable
* A priori: probability of y (not related to features)

##How is it prone to overfitting?

All features treated independently.  
It does better with small data-sets, predicts fine on larger data sets, but coefficients tend be less useful.

##How is it customizable?

* Alpha: can assume types of regularizations

* Two NB types:
	1 Bernoulli: based on presence (binomial) 
	2 Multinomial: counting approach