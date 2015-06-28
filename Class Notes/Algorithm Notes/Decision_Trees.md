#Decision Trees
##What data problem does it solve?

* Classification, supervised.
* Regression, supervised.

##How do we evaluate performance performance

* Accuracy: correctly predicted observations over total number of observations 
* Confusion matrix: Shows the matrix of correctly and incorrectly predicted values.
* Receiver Operating Characteristic (ROC) Curve: Plotting true positive rate over false positive rate, determines accuracy of positives and negatives.

##What is the output?

* Regression: y = averages at nodes.
* Classification: y = purity at each node (probability measure).

##What is interpretable of the algorithm?

* Feature importance: measures information gain, normalized to 1.
* Rule sets: graphviz! Decisions and rules.

##How is it prone to overfitting?

Allowing the decision tree to be too long/deep leading to overfitting on training set, but the significantly worse test results.

##How is it customizable?

* Max depth: maximum number of nodes.
* Min Samples Split: minimum number of samples in a split. Must be 2, can increase.
* Min Samples Leaf: minimum number of samples in a leaf. Pay attention to variance in the data set.