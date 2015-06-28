"""
1. What's the primary difference between the following two ipython magic (%)
commands?
"""
# Both allow for matplotlib figures to be generated directly in the ipython notebook
%matplotlib inline # This only imports from matplotlib and is more lightweight
%pylab inline # This is an older command and imports packages from matplotlib and numpy

"""
2.  We have a file called "ads_performance.csv" which includes the following
header rows, and one row and the end that sums the total of the dataset.

Google Adwords Perfomance
February 16 2015, February 22 2015
Brand
date, ad_id, strategy_group, description, spend, spend_wfees, impressions, clicks
02/16/2015, 1772, 'team_bananas', 'Did you know there are 100s of bananas? Click here to find out more!', 23.75, 24.33, 107771, 10

Write the pd.read_csv function that would ignore the additional headers, use the
correct header for the column names, and ignore the very last row.
"""
# Assuming this script is in the same directory as the file:
ads = pd.read_csv(ads_performance.csv, header=3, skip_footer=1)

"""
3. With the ads dataset stored in name `ads`, write code that'd create a subset
of just ad_id 200 where the spend was more than 30 dollars

subset = ads...(some_code)...
"""
subset = ads[ads.ad_id == 200, ads.spend > 30]

"""
4. We want to aggregate the sum of spend by day and ad. What code would return
back that dataset?
"""
day_ad_pivot = ads.pivot_table(values='spend',
                 columns='day',
                 index='ad',
                 aggfunc='sum')

"""
5. Explain what the following code block is doing, line by line.
"""
import matplotlib.pyplot as plt # imports the pyplot package from the matplotlib library aliased as plt
from __future__ import division # imports the division function from a future version of python to automatically create floats when performing division

ads['ctr'] = ads['clicks'] / ads['impressions'] # adding a column to ads called ctr (click thru rate) that is calculated as the clicks for each index divided by the impressions

fig = plt.figure() # defining a figure space
plt.subplot(1, 2, 1) # delineates a subplot in the figure space with one row and two columns and delineates this is the first plot in the space
plt.hist(ads.spend) # Places a histogram of the spend from the ads dataframe in the plot space

plt.subplot(1, 2, 2) # delineates a subplot in the figure space with one row and two columns and delineates this is the second plot in the space
plt.plt(ads.spend, ads.ctr, 'g.') # plots a green scattergram of ad spend and ad click thru rate
plt.show() # shows the figure


"""
6-8. Imagine we're viewing the following coefficient table for the following
regression:

(ad_id1772 is either 1 or 0, meaning it was ad 1772, or it was not)
'spend ~ impressions + clicks + ad_id1772'

column          coefficient         pvalue
y_intercept     0.02                0.000
impressions     0.00057             0.038
clicks          0.976               0.78
ad_id1772      -0.5                 0.02


6. How much can we assume the ad cost to place online, based on it having
   no impressions?
7. Which part of the model seems insignificant to solving for cost? 
8. What effect does ad 1772 have on the cost of the ad?

"""
# 6. 2 cents
# 7. clicks
# 8. makes it cheaper by 50 cents

"""
9. What does a Trellis plot allow you to do?
What python library does theTrellis plot come from?
"""
#Trellis allows you to quickly visualize the relationship between all the features in a dataframe, it comes from the pandas library

"""
10. What does the reset_index() function do on a DataFrame?
Describe an instance you might need to use it.
"""
# Reset index is useful when you have a multi index groupby that you want to convert back to a dataframe

