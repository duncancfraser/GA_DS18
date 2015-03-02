#Peer Review Project 1
Reviewer: Duncan Fraser 
Reviewee: James Gatewood
[James's project](http://nbviewer.ipython.org/github/gatewj/GADataScience/blob/master/CondominiumAnalysis.ipynb) focuses on NYC condo prices and market values.  

##Project Strengths

* Great organization.  Very clear, fantastic use of markdown to summarize at various points throughout the notebook.
* Excellent job contextualizing the dataset ahead of the analysis, helps ground what we're looking at.
* ggplots look great, and help show some relationships between different features in the dataset. Great job labeling the axes!

##Areas for Improvement 

* I did not entirely understand why you ran a regression on the estimated gross income and the income per square foot.  I assume these are too closely related (e.g. the estimated is likely derived from the income per sq ft) for it to make sense to run a regression.

##Clarification Questions

* What is the full market value based upon? 
* Does this include data from all five boroughs?

##Code Review

* Consider iterating through the header to clean up.  It looks like the part you removed was the same across each one, so you should be able to select the part of the string you're interested in keeping.
* For the QQ plots, consider making more efficient with a for loop.

##Next Steps

* Overlaying other neighborhood features to see what influences gross income and market value outside of the building itself.
* Consider using mapping applications or plotting longitude and lattitude to help us see where in the city all of this is happening.
