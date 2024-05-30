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

	In this notebook, we imported the transformed data from notebook 01_data_preprocessing 	to create our models. We firstly did 2 baselines models (a Logistic Regression one and a 	Decission Tree Classifier). We then, we hypertuned the parameters for both models. And 	at the end we chose to go with the decision tree as our final model. 

- 4. 03_predict.

	In this notebook, we used the Test_set_values dataset. We then applied to it the same 	transformations that were carried out in all the past notebooks. And we then applied the 	Decision Tree Classifier model from notebook 02_model_creation to do our final 	predictions on the SubmissionFormat dataset. 

## Conclusion

Looking into the distribution of the dependent variable. There is clearly no imbalance, as can be seen below:

![Distribution Functional and Non-functional](/visualizations/bar_graph_target_variable.png)

Moreover, after thoroughly analyzing the datasets using the methodologies outlined in the provided notebooks, we have successfully developed and evaluated two models: a Logistic Regression model and a Decision Tree classifier. The model selection process, detailed in the 02_model_creation notebook, involved comparing these models based on their evaluation metrics, ultimately leading us to select the Decision Tree classifier as the superior model. 

Here we have the confusion matrix of the Decision Tree Classifier model that was selected:

![Confusion Matrix](/visualizations/confusion_matrix_decision_tree_classifier
.png)

As can be seen, the false positive rate (6.72%) is relatively low, meaning fewer resources will be wasted on unnecessary maintenance.

Another metric that we considered to select our model was the area under the curve (AUC). The Decision Tree model achieved an impressive AUC of 0.85, making it the optimal choice for our predictions. The variables that are most important and that permit us to best descriminate are:

1. waterpoint_type
2. quantity_group
3. payment_type

![Feature importance](/visualizations/Feature_importance.png)


Our three primary recommendations are as follows:

1. The Tanzanian government should consider aligning the payment plans of water pumps with the more common monthly or per bucket payment plans used by most functional pumps to increase their chances of being functional.

2. Using the presence of dry pumps as an indicator can help identify non-functional pumps, allowing efforts to be focused on repairing these specific pumps.

3. Identifying pumps that do not have common functional waterpoint types (such as cattle trough, communal standpipe, etc.) can serve as a proxy to determine non-functional pumps and prioritize them for repairs.

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

There is a folder called notebooks that contains all the necessary analysis.

There is a requirements.txt that contains the information of the libraries used in this project.

There is a .gitignore that allows to exclude files that are of no interest.

There is a results_pdf_files folder that contains the resultant final presentation and the notebook where the analysis was carried out in pdf format.  

