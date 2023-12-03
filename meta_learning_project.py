# -*- coding: utf-8 -*-
"""Meta_Learning_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CqmZfYIfa9KTiSmdgCt0u3Pv7uUAwes8
"""

import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv"
df = pd.read_csv(url)

df["Depression Label"] = 0  # Initialize all rows with 0

for i in range(len(df)):
    if df.loc[i, "depression"] == "Depressed":
        df.loc[i, "Depression Label"] = 1

filename = "UpdatedData.csv"
df.to_csv(filename, index=False)

import pandas as pd

# Read the CSV file
data = pd.read_csv('https://github.com/HeyThatsViv/Predicting-Depression/raw/main/CSVFiles/FullData.csv')

# Add a new column named 'new_column' next to 'depression' column
data['new_column'] = data['depression'].apply(lambda x: 0 if x == 'Not Depressed' else 1)

# Save the updated data to a new CSV file
data.to_csv('updated_file.csv', index=False)

# Print the link to the updated file
print("Updated file:", 'updated_file.csv')

import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv"
df = pd.read_csv(url)

# Loop through each row in the 'depression' column
for index, row in df.iterrows():
    # Get the value in the 'depression' column for the current row
    value = row['depression']

    # Check if the value is 'Not Depressed'
    if value == 'Not Depressed':
        # Set the value in the new column to 0
        df.at[index, 'new_column'] = 0
    else:
        # Set the value in the new column to 1
        df.at[index, 'new_column'] = 1

# Save the updated Excel sheet
df.to_csv('updated_full_data.csv', index=False)

import pandas as pd

# Read the Excel file
df = pd.read_csv('https://github.com/HeyThatsViv/Predicting-Depression/raw/main/CSVFiles/FullData.csv')

# Create a new column 'new_column' and initialize it with 0
df['new_column'] = 0

# Set the value of 'new_column' as 1 if the value of 'depression' is not 'Not Depressed'
df.loc[df['depression'] != 'Not Depressed', 'new_column'] = 1

# Save the updated DataFrame to a new Excel file
df.to_excel('updated_data.xlsx', index=False)

import pandas as pd

# Load the dataset
data = pd.read_csv('https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv')

# Compute the correlation matrix
correlation_matrix = data.corr()

# Print the correlation matrix
print(correlation_matrix)

import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv"
df = pd.read_csv(url)

from sklearn.model_selection import train_test_split

# Handle missing values
df = df.dropna()

# Split the data into input features (X) and target variable (y)
X = df.drop(columns=["depression"])
y = df["depression"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# Load the dataset
dataset_url = 'https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv'
df = pd.read_csv(dataset_url)

# Compute the correlation matrix
correlation_matrix = df.corr()

# Splitting the dataset into input features (X) and target variable (y)
X = df.drop('depression', axis=1)
y = df['depression']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the dataset
dataset_url = 'https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv'
df = pd.read_csv(dataset_url)

# Identify columns with non-numeric (string) values
non_numeric_columns = df.select_dtypes(exclude=['number']).columns
print(non_numeric_columns)

label_encoder = LabelEncoder()
for column in non_numeric_columns:
    df[column] = label_encoder.fit_transform(df[column])

# Split the dataset into input features (X) and target variable (y)
X = df.drop('depression', axis=1)  # Replace 'target_variable_column' with the actual column name
y = df['depression']

# No need to drop non_numeric_columns again, as they have already been converted

df = pd.get_dummies(df, columns=non_numeric_columns, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and evaluate decision tree model
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)
decision_tree_predictions = decision_tree.predict(X_test)
decision_tree_accuracy = accuracy_score(y_test, decision_tree_predictions)

# Build and evaluate random forest model
random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)
random_forest_predictions = random_forest.predict(X_test)
random_forest_accuracy = accuracy_score(y_test, random_forest_predictions)

# Build and evaluate logistic regression model
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)
logistic_regression_predictions = logistic_regression.predict(X_test)
logistic_regression_accuracy = accuracy_score(y_test, logistic_regression_predictions)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the dataset
dataset_url = 'https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv'
df = pd.read_csv(dataset_url)

# Identify columns with non-numeric (string) values
non_numeric_columns = df.select_dtypes(exclude=['number']).columns

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=non_numeric_columns, drop_first=True)

# Check if 'depression' is not a numeric column
target_column = 'depression'
if target_column in df.columns:
    # Adjust the target column name based on your data
    target_column_encoded = f'{target_column}_Yes'

    # Splitting the dataset into input features (X) and target variable (y)
    X = df.drop(target_column_encoded, axis=1)
    y = df[target_column_encoded]

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling the input features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Creating an instance of Logistic Regression classifier
    logreg = LogisticRegression()

    # Training the model
    logreg.fit(X_train_scaled, y_train)

    # Creating an instance of SVM classifier
    svm = SVC()

    # Training the model
    svm.fit(X_train_scaled, y_train)

    # Creating an instance of Decision Tree classifier
    dt = DecisionTreeClassifier()

    # Training the model
    dt.fit(X_train_scaled, y_train)

import pandas as pd
from scipy.stats import chi2_contingency

# Step 1: Load the dataset
url = 'https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv'
df = pd.read_csv(url)

# Replace 'target_variable' with the actual target variable column name
target_variable_column = 'depression'
X = df.drop(target_variable_column, axis=1)
y = df[target_variable_column]


# Step 3: Perform chi-square test for each feature
chi2_stats = []
p_values = []
for feature in X.columns:
    contingency_table = pd.crosstab(X[feature], y)
    chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)
    chi2_stats.append(chi2_stat)
    p_values.append(p_value)

# Step 4: Select the features with the highest chi-square statistic
selected_features = pd.DataFrame({'Feature': X.columns, 'Chi2_Stat': chi2_stats, 'P_Value': p_values})
selected_features = selected_features.sort_values(by='Chi2_Stat', ascending=False)

# Display the selected features
print("Selected Features:")
print(selected_features)

# You can choose a threshold for significance, for example, 0.05
significance_threshold = 0.05
significant_features = selected_features[selected_features['P_Value'] < significance_threshold]

# Display significant features
print("\nSignificant Features (p-value < 0.05):")
print(significant_features)

# Continue with your analysis, model building, or any other relevant steps...

import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Step 1: Load the dataset
url = "https://github.com/HeyThatsViv/Predicting-Depression/raw/main/CSVFiles/FullData.csv"
df = pd.read_csv(url)

# Step 2: Separate the features and the target variable
X = df.drop('depression', axis=1)
y = df['depression']

# Step 2.1: Encode categorical variables
categorical_columns = X.select_dtypes(include=['object']).columns
label_encoder = LabelEncoder()

for column in categorical_columns:
    X[column] = label_encoder.fit_transform(X[column])

# You might also consider one-hot encoding if the categorical variables are not ordinal
# X = pd.get_dummies(X, columns=categorical_columns, drop_first=True)

# Step 3: Perform chi-square test for feature selection
selector = SelectKBest(score_func=chi2, k=5)
X_new = selector.fit_transform(X, y)

# Get the selected feature indices
feature_indices = selector.get_support(indices=True)

# Get the selected feature names
selected_features = X.columns[feature_indices]

print("Selected Features:")
print(selected_features)

"""**Meta Learning Model**"""

!wget https://github.com/HeyThatsViv/Predicting-Depression/raw/main/CSVFiles/FullData.csv

"""# Preprocessing the Dataset

To preprocess the dataset, we will perform the following steps:

1. Load the dataset
2. Handle missing values
3. Encode categorical variables
4. Split the dataset into training and testing sets

Let's start by loading the dataset.

Implementing the Robust Meta Learning Model
To implement the Robust Meta Learning Model, we will follow the steps below:

Load the dataset from the provided link.
Preprocess the dataset by handling missing values, encoding categorical variables, and splitting the dataset into training and testing sets.
Load the pre-trained machine learning model from the provided link.
Train the meta learning model using the training set.
Evaluate the meta learning model using the testing set.
Generate predictions using the meta learning model.
Let's implement these steps in code.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

# Step 1: Load the dataset
dataset_url = "https://raw.githubusercontent.com/HeyThatsViv/Predicting-Depression/main/CSVFiles/FullData.csv"
data = pd.read_csv(dataset_url)

# Print unique values in the specified columns
categorical_columns = ['gender', 'marital_status']
for column in categorical_columns:
    print(f"Unique values in {column}: {data[column].unique()}")

# Step 2: Preprocess the dataset
# Assuming the dataset is already cleaned and doesn't have missing values

# Use OneHotEncoder for one-hot encoding of categorical columns with string values
encoder = OneHotEncoder(drop='first', sparse=False)

# Filter categorical columns that contain string values
categorical_columns_with_strings = [col for col in categorical_columns if data[col].dtype == 'O']

# Apply one-hot encoding only to columns with string values
if categorical_columns_with_strings:
    data_encoded = pd.DataFrame(encoder.fit_transform(data[categorical_columns_with_strings]))
    data_encoded.columns = encoder.get_feature_names_out(categorical_columns_with_strings)

    # Concatenate the one-hot encoded columns with the original dataset
    data = pd.concat([data, data_encoded], axis=1)

    # Drop the original categorical columns
    data.drop(categorical_columns_with_strings, axis=1, inplace=True)

# Filter numeric columns
numeric_columns = [col for col in data.columns if data[col].dtype != 'O']

# Split the dataset into training and testing sets
X = data[numeric_columns]
y = data['depression']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the base model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 4: Train the meta learning model
meta_model = VotingClassifier(estimators=[('model', model)], voting='soft')
meta_model.fit(X_train, y_train)

# Step 5: Evaluate the meta learning model
y_pred = meta_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Step 6: Generate predictions using the meta learning model
# Note: You'll need to prepare your new data for prediction and use the `predict` method.

# Example: Preparing new data for prediction (replace this with your actual new data)
new_data = X_test.sample(5, random_state=42)  # You can replace this with your new data

# Use the `predict` method to generate predictions
new_predictions = meta_model.predict(new_data)

# Display the new data and predictions
new_data_with_predictions = new_data.copy()
new_data_with_predictions['Predictions'] = new_predictions
print("New Data with Predictions:")
print(new_data_with_predictions)

"""Robust Meta Learning Model"""

X_train.columns = X_train.columns.astype(str)

!pip install fileupload

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from google.colab import files
import io

# Step 1: Ask the user to upload the testing dataset file
upload = files.upload()

# Step 2: Read the testing dataset from the uploaded file
uploaded_filename = next(iter(upload.keys()))
test_data = pd.read_csv(io.StringIO(upload[uploaded_filename].decode('utf-8')))

# Display the first few rows of the testing dataset
test_data.head()

# Step 3: Preprocess the testing data
def preprocess_data(data):
    # Assuming the dataset is already cleaned and doesn't have missing values

    # Use OneHotEncoder for one-hot encoding of categorical columns with string values
    encoder = OneHotEncoder(drop='first', sparse=False)

    # Filter categorical columns that contain string values
    categorical_columns_with_strings = [col for col in data.columns if data[col].dtype == 'O']

    # Apply one-hot encoding only to columns with string values
    if categorical_columns_with_strings:
        data_encoded = pd.DataFrame(encoder.fit_transform(data[categorical_columns_with_strings]))
        data_encoded.columns = encoder.get_feature_names_out(categorical_columns_with_strings)

        # Concatenate the one-hot encoded columns with the original dataset
        data = pd.concat([data, data_encoded], axis=1)

        # Drop the original categorical columns
        data.drop(categorical_columns_with_strings, axis=1, inplace=True)

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

    return data

# Step 4: Preprocess the testing data
processed_test_data = preprocess_data(test_data)

# Step 5: Load the pre-trained machine learning model
# Placeholder model for testing
model = RandomForestClassifier()

# Step 6: Train the meta learning model
meta_model = model  # Placeholder for now

# Assuming X_train and y_train are your training data
# You should replace this with the actual training data
# Here, for demonstration purposes, we are using the testing data for training
X_train, X_test, y_train, y_test = train_test_split(processed_test_data.drop('depression', axis=1), processed_test_data['depression'], test_size=0.2, random_state=42)
meta_model.fit(X_train, y_train)

# Step 7: Predict outcomes on the entire testing data
final_predictions = meta_model.predict(processed_test_data.drop('depression', axis=1))

# Step 8: Display the final predictions
final_results = pd.DataFrame({
    'SEQN': processed_test_data['SEQN'],
    'Predictions': final_predictions
})
final_results

"""Testing the Models"""