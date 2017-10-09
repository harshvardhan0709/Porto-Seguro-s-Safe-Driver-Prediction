# Porto-Seguro-s-Safe-Driver-Prediction

1. Introduction
2. Data preparation
    2.1 Load data
    2.2 Check for missing values
    2.3 Split features and targets from the data
    2.4 Exploratory Visualization
3. Training/Predicting Pipeline
    3.1 Define Gini metric
    3.2 Drop Unnecessary Features
    3.3 Stratified KFold
    3.4 XGBoost
4. Prediction and submission
    4.1 Predict and Submit results

## 1. Introduction
This is a full walkthrough for building the machine learning model for Porto Seguro’s Safe Driver Prediction dataset provided by Porto Seguro. Stratified KFold is used due to inbalance of the output variable. XGBoost is used because it is like the winning ticket for classification problem with formatted data. (XGBoost winning solutions) First, I will prepare the data (driver's information and whether the driver initiated auto insurance or not) then I will focus on prediction.

   ## XGBoost
  
  
## 2. Data Preparation
   
   ## 2.1 Load Data
   ## 2.2 Check for missing values(NaN)
           Fill it with median value of the column
           This does not harm the distribution of the model
   ## 2.3 Split features and targets from the data
   ## 2.4 Exploratory Visualization
        Distribution of targets
              The plot shows that:
                  the target is imbalanced
                  high bias is expected to 0
                  class weight has to be balanced on training
        Correlation matrix
              It can be seen that:
                  ps_calc_* features are not related to target at all.
                  Removing them would prevent the curse of dimensionality.
  ## 3. Training/Predicting Pipeline
    ## 3.1 Define Gini Metric
    ## 3.2 Drop Unnecessary Columns
    ## 3.3 Stratified KFold
            Stratified KFold is used to keep the distribution of each label consistent for each training batch.
    ## 3.4. XGBoost
            Set parameters
  ## 4. Prediction and submission
    ## 4.1. Predict and Submit results
            Define X and y
            Create a submission file
                  This is a pipeline originated from StratifiedShuffleSplit + XGBoost example (0.28)
                  Original Simple XGBoost BTB (0.27+)
            Put submission to csv file
