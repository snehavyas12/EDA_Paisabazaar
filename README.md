# Data-Driven Insights into Creditworthiness: An Exploratory Analysis of Paisabazaar Customer Data

This project studies Paisabazaar dataset to analyze customer financial and behavioral data to uncover the key factors influencing individual credit scores with the aim of improving credit risk evaluation.

The dataset includes 100k+ customers data. The financial dataset has 28 crucial features which capture customer's personal, behavioral and financial attributes. The dataset overview includes checking every column and its datatype. 

Then the data is cleaned and standardized. Columns are preprocessed to make them analysis ready. 

The project carries on with extensive data profiling. The target feature is credit scores which is categorical, and all the other feature (categorical/numerical) are studied using unique() and value_counts().

Outliers’ detection and handling includes all the extensive ways to handle outliers. The proportion of outliers per column is extracted. Based on that, we cap them, and log transform them. 

As the data is ready for analysis, we Perform Univariate, Bivariate and Multivariate Analysis on the data. Some analysis involved feature engineering.

The project culminates with results and recommendations such as: Paisabazaar must be aware of the red flags of customers with poor scores as they are prone to defaulting which is proven from study of number of loans, Debt-to-income ratio and credit scores. Moreover, customers with 'Standard' scores can be pushed in 'Good' scores category by appropriate strategy. 

