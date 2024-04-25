# Heart_Disease_Risk_Prediction - Streamlit_App
Heart Disease Risk Prediction project utilizing Gradient Boosting Machine Learning model trained on Kaggle dataset with data preprocessing techniques and Integrated into a user-friendly web application using Streamlit for easy prediction access.

## Project Overview
This project aims to develop a machine learning model to predict the risk of heart disease based on various parameters such as weight, height, alcohol consumption, dietary habits (fried food and green vegetables), and medical history (smoking, depression, diabetes, cancer). The dataset used for this project is obtained from Kaggle and contains both numerical and categorical data.


# Business Problem Addressed
Heart disease is a major health concern worldwide, and early detection plays a crucial role in prevention and management. By developing a predictive model, healthcare professionals and individuals can assess the risk of heart disease based on personal attributes and lifestyle factors. This can facilitate proactive interventions and lifestyle modifications to mitigate the risk of cardiovascular issues.


# Project Implementation
Exploratory Data Analysis (EDA): Conducted thorough analysis of the dataset to understand the distribution of features, identify correlations, and gain insights into potential predictors of heart disease.
- Data Preprocessing:
Utilized label encoding to convert categorical variables into numerical format.
Handled class imbalance using the Synthetic Minority Over-sampling Technique (SMOTE) to generate synthetic samples for the minority class.
Applied StandardScaler to standardize numerical features and bring them to a similar scale.

- Model Training:
Utilized Gradient Boosting Machine (GBM) algorithm for training the predictive model.
Employed k-fold cross-validation to evaluate model performance and ensure robustness.

- Web Application Development:
Developed a user-friendly web application using Streamlit framework.
Designed the interface to allow users to input their personal attributes and receive the predicted risk of heart disease.


# How to Run the Web Application
- Clone the repository to your local machine.
- Install the required dependencies listed in the requirements.txt file.
- Navigate to the directory containing the source code.
- Run the Streamlit application using the command streamlit run Heart_DiseaseRiskApp.py
- Access the application through the provided URL in your web browser.
- Input the necessary parameters and obtain the predicted risk of heart disease.

Heart_DiseaseRiskApp.py is the streamlit app code hence run the command "pip install -r requirements.txt" to install the required dependencies for the streamlit app.
You may need to install additional libraries for running the jupyter notebooks.

## Code Overview

### Data Preprocessing
- The dataset is loaded from a CSV file using Pandas.
- Information about the dataset is displayed using `info()` method.
- Missing values in the dataset are checked using `isnull().sum()` method.
- The target variable 'Heart_Disease' is separated from the features.
- Categorical columns are identified for label encoding.
- Label encoding is applied to convert categorical variables into numerical format.
- Mapping dictionaries are defined to map encoded values back to original categorical values.
- The data is split into training and testing sets using `train_test_split()` method.

### Handling Class Imbalance
- Synthetic Minority Over-sampling Technique (SMOTE) is applied to handle class imbalance in the training data.
- The resampled target variable value counts are printed to verify the balancing.

### Model Training
- A Gradient Boosting Classifier model is initialized and trained using the resampled training data.
- Model evaluation is performed on both training and testing data using accuracy score.
- Cross-validation is conducted using k-fold cross-validation technique with 5 folds.
- Mean cross-validation score is calculated to assess the model's generalization performance.

### Model Evaluation
- Classification report is generated to display precision, recall, F1-score, and support for each class.
- Confusion matrices are computed for both training and testing data.
- Confusion matrices are visualized using heatmaps for better interpretation.

### Making Predictions system 
- Input data for prediction is provided as a list of feature values.
- The input data is converted into a numpy array and reshaped.
- StandardScaler is used to standardize the input data.
- The trained model is used to make predictions on the scaled input data.

### Web Application Integration
- The trained model and necessary preprocessing steps can be integrated into a web application using frameworks like Streamlit or Flask.
- Users can input their personal attributes through the web interface, and the application will provide the predicted risk of heart disease based on the trained model.


