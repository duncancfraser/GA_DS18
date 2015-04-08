#Decision Trees
##What data problem does it solve?

* Classification, supervised.
* Regression, supervised.

##How do we evaluate performance performance

* Accuracy: measure of 
* Confusion matrix:
* ROC Curve: Plooting trye positive rate over false positive rate, determines accuracy of positives and negatives.

##What is the output?

* Regression: y = averages at nodes.
* Classification: y = purity at each node (probability measure).

##What is interpretable of the algorithm?

* Feature importance: measures information gain, normalized to 1.
* Rule sets: graphviz! Decisions and rules.

##How is it prone to overfitting?

Allowing the decision tree to be too long creates more subsets, which means the training set will be incredibly accurate, but the test set will be significantly worse.

##How is it customizable?

* Max depth: maximum number of nodes
* Min Samples Split: minimum number of samples in a split. Must be 2, can increase.
* Min Samples Leaf: minimum number of samples in a leaf. Pay attention to variance in the data set!