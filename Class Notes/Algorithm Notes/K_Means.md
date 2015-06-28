#K Means
##What data problem does it solve?

Creates proximity-based clusters, unsupervised.

##How do we evaluate performance?

* Cohesion within a cluster  
* Seperation between clusters
* R-squared, mean squared error when regressing

##What is the output?

Solves for similarity based on proximity/distance.

##What is interpretable of the algorithm?

The classification output:
  * Features used in the model
  * Cluster appearance

##How is it prone to overfitting?

Too many neighbors.

##How is it customizable?

* K: the number of neighbors to consider
* Distances: Minkowski (Manhattan or Euclid), Jaccad