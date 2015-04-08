#K Means
##What data problem does it solve?

Creates clusters based on proximity. Unsupervised.

##How do we evaluate performance?

Cohesion within a cluster and seperation between clusters.

R-squared, mean squared error when regressing.

##What is the output?

Solves for similarity based on distance.

##What is interpretable of the algorithm?

The classification output:
  * What features are they based on
  * What do the clusters look like

##How is it prone to overfitting?

Too many neighbors

##How is it customizable?

* K: the number of neighbors to consider
* Distances: Minkowski (Manhattan or Euclid), Jaccad