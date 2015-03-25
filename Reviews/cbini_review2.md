#Peer Review Project 2

**Reviewer:** Duncan Fraser 

**Reviewee:** Charlie Bini

[Charlie's project](http://nbviewer.ipython.org/github/cbini/datascience/blob/master/projects/project2/Failure%20Prediction%20Model.ipynb) seeks to predict student's likelihood to fail a course. 

##Project Strengths

* Very organized, and clear. I especially like how you tested a few different models.
* Excellent job predicting outcome!

##Areas for Improvement 

* Perhaps digging a bit deeper on a few of the visualizations would help the reader get a better feel for the data set.
	* For example, perhaps try creating grade histograms by course type, perhaps differences here reveal differences that inform the model.
* Consider providing some visualizations for the test/train and model selection portion of the notebook.
* Consider splitting out the rest of the features from grades.  How does a model using everything besides the test scores look?


##Clarification Questions

* Are there additional pieces of information that you could add in? Such as:
	* Years teacher has taught the course
	* Class year of the student 

##Code Review

* Consider looking at the shape of the data frame as another way to help describe it in the notebook
* Love the general organization and use of simple, clear functions

##Next Steps

* Does removing students with incomplete course info, improve mdoel accuracy?
* Could you flag students who previously failed a course, and add as a feature in the model?