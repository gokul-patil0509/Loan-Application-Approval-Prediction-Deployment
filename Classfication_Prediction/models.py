from django.db import models
import pandas as pd
import pickle


### Loading the dataset
df = pd.read_csv('loan_prediction.csv')

# --- Data Preprocessing ---
# Arrange columns in below order
df = df[['Loan_Status', 'ApplicantIncome', 'CoapplicantIncome', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'LoanAmount',
         'Loan_Amount_Term', 'Property_Area']]

# Replace target column in 0's and 1's
df['Loan_Status'].replace('Yes', 1,inplace=True)
df['Loan_Status'].replace('No', 0,inplace=True)

# Converting categorical features using OneHotEncoding method
df = pd.get_dummies(df,drop_first=True)

# independent and dependent features
X = df.iloc[:,1:]
y = df.iloc[:,0]

# Splitting the data into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

# --- Model Building ---
# RandomForest Classifier Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

# Creating a pickle file for the classifier
filename = 'loan-approval-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))
