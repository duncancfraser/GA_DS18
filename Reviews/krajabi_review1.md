#Peer Review Project 1

*Reviewer:* Duncan Fraser 

*Reviewee:* Kiyan Rajabi

[Kiyans's project](http://nbviewer.ipython.org/github/krajabi/ga_assignments/blob/master/Project%201%20%E2%80%94%20Exploratory%20Data%20Analysis%20%281%29.ipynb) explores different factors leading to death in NYC in 2011.  

##Project Strengths

* I found your outline of questions at the top of the notebook helpful in framing the notebook.
* Sorting by count to view top causes of death - smart quick way to see how causes of death vary by ethnicity and gender.
* Love the visualizations at the end. Very nice way to summarize. Cool to see the trend for heart disease drop.

##Areas for Improvement 

* Hard to understand what the other non-numeric columns are besides when you work with one of them.  Listing out a more summary information about the original dataset (e.g., header info, count, where it was collected etc) would help.
* As you subset from the original dataframe, I think additional information on the subset dataframes (e.g. describe) would help contextualize the subset.


##Clarification Questions

* How were these death-types classified? Is there a more granular category below?
* Why did you decided to focus only on 2011 (as opposed to another year)?

##Code Review

* Try using a little more markdown for narrative pieces of notebook to make it more readable.
* Code overall clean and straightforward.  
* You could've thrown in some more complicated python to generate your top death by ethnicity tables more efficiently.


##Next Steps

* Consider looking at changes in death types as a percent of total deaths that year. 
* It would be interesting do a similar plot to what you did for overtime trends for 2011 deaths by ethnicity.
* Can you pull out any correlations from this dataset?  You've explored some interesting differences, I would be interested to see if you can dig deeper on those relationships.
