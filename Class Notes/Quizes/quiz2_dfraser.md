#Machine Learning / SKLearn Quiz (Quiz 2)

1. Given the following machine learning matrix, fit each of the following algorithms into their respective places. Some may have multiple.

    .               | continuous                  | categorical
    ---------------:|:---------------------------:|:--------------------
    supervised      | regression (i)              | classification (ii)     
    unsupervised    | dimension reduction (iii)   | clustering (iv)

    Algorithms:
    * Ordinary Least Squares - *i*
    * Logistic Regression - *ii*
    * Naive Bayes - *ii*
    * Decision Trees - *i, ii*
    * Support Vector Machines - *i, ii*
    * K Nearest Neighbors - *ii*
    * K Means - *iv*
    * Principal Component Analysis (Matrix Decomposition) - *iii*

2. Given the 4 entities in the matrix above, describe a problem / example we worked on in class for each, and provide one idea on your own.
    i. We used a data-set containing brain and body weight information to predict sleep time in class. You could also create a model to predict the listing price of a hotel room based on square-footage, distance from key landmarks.
    ii.
    iii.
    iv.

3. All sklearn prediction objects have functions akin to fit(), transform(), predict(), and fit_transform(). Explain each in their most general terms.
    * fit() - *given a feature set, this fits the model, if there is a target you can train fit against the value it should predict.*
    * transform() - *Takes a matrix and returns a different matrix, based on the parameters passed*
    * predict() - *takes a previously fitted model and applies the model to a data set to generate the predictive output (could assign a probability, a value or a classification)*
    * fit_transform() - *Fits the data, returns a new matrix*

3. Two of the above algorithms can use kernels (in their sklearn context)
    a. Explain what a kernel does - *A kernel is a tranformation that allows for an better pattern recognition with otherwise inseperable data*
    b. Which are the two algorithms that use kernels? - *Support Vector Machines, Principle Component Analysis*

4. One of the above algorithms is most obviously not a linear solution to classification (it does not draw straight decision lines). Which algorithm is it, and how does it decide on decision lines?
    * *K Nearest Neighbors relies on distance and is therefore generative, to predict clusters that should be classified together.*

5. You are working on microarray (DNA) samples where number of observations (n) is 5 and number of features (m) is > 10,000.
    1. Describe a supervised and unsupervised technique in order to reduce the number of features in the samples to those that are most significant.
        * Supervised: Lasso
        * Unsupervised: Principle Component Analysis
    2. Compare the two techniques in their solution.

6. Below is a table of Gini Importance (Normalized to 1) in predicting rent in New York City.
    1. Which algorithm uses Gini Importance? - *Decision Trees.*
    2. Interpret the table. - *The most information gained in terms of predicting a classification for this specific decision tree comes from square footage.*

    Feature           | GiniImportance
    :-----------------|:--------------
    bedrooms          | 0.211
    bathrooms         | 0.005
    sqft              | 0.532
    distance subway   | 0.198
    distance columbus | 0.017
    nearby pizza      | 0.042

7. What is the Receiving Operator Characteristic Curve? What two metrics is it composed of?
    * The ROC curve measures Accuracy on the y-axis and K on the x-axis.

9. How does a grid search work? Use an example algorithm from above to help explain it.
    * The grid search helps optimize an algorithm by passing a range of possible values across a number of the customizable elements of a model (Kernel, K, C, Max Depth, Max Leaves etc) and determines the best settings based on a predermined performance metric (e.g. R-squared, AUC)

10. Three parts:
    1. What's your strongest "takeaway" from machine learning and this segment of the course? - *Machine learning relies on human decision-making and proper application. It can be powerful, but only if used under the proper conditions and interpretted in the correct manner.*
    2. Given a 2 dimensional figure where y=effort to learn and x=immediate usefulness, and slope = 1, what is one algorithm that felt above the slope (more effort to learn than usefulness) and one algorithm that felt below the slope (more usefulness than effort to learn)?
    3. What's one question you still have about machine learning?