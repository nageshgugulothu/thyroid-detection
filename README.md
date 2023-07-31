# Thyroid Disease Detection Mlops Project 

## Problem Statement:
Thyroid disease is a common cause of medical diagnosis and prediction, with an onset
that is difficult to forecast in medical research. The thyroid gland is one of our body's
most vital organs. Thyroid hormone releases are responsible for metabolic regulation.
Hyperthyroidism and hypothyroidism are one of the two common diseases of the thyroid
that releases thyroid hormones in regulating the rate of body's metabolism.

The main goal is to predict the estimated risk on a patient's chance of obtaining thyroid
disease or not.


## Objective

The main goal of this project is to predict the estimated risk of a patient obtaining thyroid disease. The prediction model takes various input features related to the patient's health and medical history, and based on that information, it predicts whether the patient is likely to have thyroid disease or not.

## The Approach
The approach of the Thyroid Disease Detection project involves the following steps:

1. Data Collection: Gather a dataset containing relevant features and labels for patients, including information about their age, thyroid hormone levels (TSH, T3, TT4, T4U, FTI), sex, medical history (on_thyroxine, query_on_thyroxine, on_antithyroid_medication, etc.), and the target variable indicating whether the patient has thyroid disease or not.
Dataset link : -  https://archive.ics.uci.edu/dataset/102/thyroid+disease

2. Data Preprocessing: Preprocess the dataset to handle missing values, encode categorical variables, and scale numerical features if necessary. It is essential to clean and prepare the data to make it suitable for training the machine learning model.

3. Model Selection: Choosen the appropriate machine learning model for binary classification, as the goal is to predict whether a patient has thyroid disease or not. Commonly used models include Logistic Regression, Random Forest, Support Vector Machine, Gradient Boosting classifiers etc.

4. Model Training: Split the dataset into training and testing sets. Train the selected machine learning model on the training data using appropriate evaluation metrics (e.g., accuracy, precision, recall, F1-score) to assess the model's performance.

5. Hyperparameter Tuning: Perform hyperparameter tuning to optimize the model's performance. Techniques like Grid Search or Randomized Search can be used to find the best combination of hyperparameters for the chosen model.

6. Model Evaluation: Evaluate the tuned model on the test set to get an unbiased estimate of its performance. Analyze the confusion matrix to understand the model's ability to correctly classify patients with and without thyroid disease.

7. Save Model and Preprocessor: Once the model is trained and tuned, save both the model and the preprocessor (used for data transformation) to disk for later use in the prediction pipeline.

8. Flask API Setup: Create a Flask web application to build the user interface. Define API endpoints to receive user inputs, process the data, and invoke the trained model for making predictions.

9. User Interface: Develop a user-friendly web interface that allows users to input their medical data and get the predicted probability or classification result of having thyroid disease.

10. Deployment: Deploy the Flask application on a AWS web server, allowing users to access and interact with the Thyroid Disease Detection system.

11. Documentation: Provided the comprehensive documentation about the project, including instructions for setting up and running the application, details about the model's performance, and any other relevant information.

## How to Use the Application

The application is implemented as a Flask API, allowing users to interact with the prediction model through a user-friendly web interface. Users can input relevant medical data into the form on the web page, and the model will provide a prediction regarding the likelihood of thyroid disease for that specific patient.


## Project Structure

The project is structured as follows:

- `application.py`: The main Flask application file that defines the web API endpoints and handles user interactions.
- `src/pipeline/prediction_pipeline.py`: Contains the prediction pipeline, which loads the pre-trained model, preprocesses data, and makes predictions.
- `src/utils.py`: Utility functions used in the application.
- `artifacts/`: Directory containing the pre-trained model and preprocessor used in the prediction pipeline.
- `static/`: Directory containing static files such as CSS styles and images for the web interface.
- `templates/`: Directory containing the HTML templates for rendering the web pages.

## Model Performance

The prediction model in this application has been trained on a labeled dataset of patients with thyroid disease. The performance of the model has been evaluated on a separate test dataset. The accuracy and other relevant metrics can be found in the documentation.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or open an issue in the repository.





