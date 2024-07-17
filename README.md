# Predicting_faulty_pumps

-------------------------------------------

## Description

This project, "Predicting Faulty Pumps," analyzes the functional status of water pumps across Tanzania. Participants are provided with an extensive dataset that includes various characteristics of water points, such as water quality and construction type. The goal is to predict whether the water pumps are functional, need repairs, or are non-functional. By accurately classifying each water pump, the project aims to improve access to clean, potable water in Tanzania by identifying and addressing malfunctioning pumps.

The core objective of "Predicting Faulty Pumps" is to enable better maintenance and investment decisions in the water infrastructure sector. The insights derived from this analysis will help prioritize repairs, allocate resources efficiently, and ensure reliable water access. Stakeholders, including government agencies and NGOs, will use these findings to streamline efforts towards improving water access and reducing downtime due to pump failures.

Ultimately, the project aims to support sustainable water management practices that can significantly impact public health and economic development in Tanzania.

## Sources

This project was done as part of a competition organized by Driven Data. Driven Data provided the following datasets:

- SubmissionFormat
- Test_set_values
- Training_set_labels
- Training_set_values

For more information about the competition, visit Driven Data:

https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/

## Methodology

Four notebooks were created in order to analyze the data and based on that predict the dependent variable (ie whether or not a pump is functional):

- 1. 00_data_understanding notebook. 

	In this notebook, we imported the Training_set_values dataset. We cleaned the data, 	filled NaNs, explored patterns, and relationships among the variables. Lastly, we 	created graphs for numerical and categorical variables.

- 2. 01_data_preprocessing.

	In this notebook, we imported the data from notebook 00_data_understanding and we 	carried out some transformations on it in order to have a clean dataset to predict. 
	For this, we applyied one hot encoder and target encoder to the categorical columns and 	scaled the numerical columns. 

- 3. 02_model_creation.

	In this notebook, we imported the transformed data from notebook 01_data_preprocessing 	to create our models. We firstly did 2 baselines models (a Logistic Regression one and a 	Decission Tree Classifier). We then, we hypertuned the parameters for both models. And 	at the end we chose to go with the Decision Tree Classifier as our final model. 

- 4. 03_predict.

	In this notebook, we used the Test_set_values dataset. We then applied to it the same 	transformations that were carried out in all the past notebooks. And we then applied the 	Decision Tree Classifier from notebook 02_model_creation to do our final 	predictions on the SubmissionFormat dataset. 

- 5. 04_primary_notebook.

	In this notebook, there is a high level overview of all the steps carried out in this 	project in order to do train and test our model. Moreover, the notebooks contains the 	links to the different notebooks in case the reader wants a deeper understanding of the 	processes. 

## Conclusion

Looking into the distribution of the dependent variable. There is clearly no imbalance, as can be seen below:

![Distribution Functional and Non-functional](/visualizations/bar_graph_target_variable.png)

Moreover, after thoroughly analyzing the datasets using the methodologies outlined in the provided notebooks, we have successfully developed and evaluated two models: a Logistic Regression model and a Decision Tree Classifier. The model selection process, detailed in the 02_model_creation notebook, involved comparing these models based on their Recall metric, ultimately leading us to select the Decisión Tree Classifier as the superior model. 

Here we have the confusion matrix of the Decisión Tree Classifier that was selected:

![Confusion Matrix](/visualizations/confusion_matrix_decision_tree_classifier.png)

As can be seen, the false positive rate (14.48%) is relatively low, meaning fewer resources will be wasted on unnecessary maintenance.

Another metric that we considered to select our model was the area under the curve (AUC). The Decisión Tree Classifier achieved an impressive AUC of 0.87, making it the optimal choice for our predictions. The variables that are most important and that permit us to best descriminate are:

1. waterpoint_type (this variable represents the kind of waterpoint)
2. quantity_group (this variable represents the quantity of water)
3. payment_type (this variable represents the method used to pay for the pump)

![Feature importance](/visualizations/Feature_importance.png)


Our three primary recommendations are as follows:

1. Considering that most of the functional pumps have monthly payment plans or a per bucket, the Tanzanian government can consider modifying the existing payment plans of those pumps where the payments are different from those payment types, so that the chance of the pump being functional can be increased.
2. Considering that almost none of the functional pumps are dry, it is possible to verify which pumps are dry as a proxy variable to know if they are functional or not and thus focus efforts on repairing them.
3. Considering that non-functional pumps have in most cases a waterpoint_type different from cattle trough, communal standpipe, communal standpipe multiple, dam, hand pump and improved spring, it is possible to verify which pumps do not have these waterpoint_types as a proxy variable to know if they are functional or not and thus focus efforts on repairing them.

## Author

My name is Miguel Barriola Arranz. I am an Industrial Engineer and a Duke graduate student in Engineering Management. 
I am currently working in the microchip industry and further expanding my skillset in data science. 

- LinkedIn: https://www.linkedin.com/in/miguel-barriola-arranz/
- Medium: https://medium.com/@mbarriolaarranz

## Technologies

I have used **Python** with Jupyter notebook.

## Project Status

The project is in a development process at this moment. 

## What to find in the repository

There is a folder called notebooks that contains all the used notebooks and a python file named project_functions.py. This file is used to store all the functions that were created in this project.

There is a requirements.txt that contains the information of the libraries used in this project.

There is a .gitignore that allows to exclude files that are of no interest.

There is a results_pdf_files folder that contains the resultant final presentation and the notebook where the analysis was carried out in pdf format.  

