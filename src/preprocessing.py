# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import mutual_info_regression


# Load Dataset
url = "https://docs.google.com/spreadsheets/d/1-1Ldoe-DwZTL77tdMtRgZAIzeAzs0jh3/export?format=csv&gid=2089618187"
df = pd.read_csv(url)

# Inspect the Data 
print(df.info())
print(df.describe(include='all'))
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
print(df.head())
df.dtypes

# Check Missing Values 
print("Missing Values: \n", df.isnull().sum())

# Check for Duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")

# Column wise Value Counts
print(df['Attrition'].value_counts())
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())
    print("-" * 40)

# Drop Columns with no Predictive Powers
df = df.drop(['emp no', 'Over18'], axis=1)

# Apply Label Encoding Column by Column
label_encode_cols = ['CF_age band', 'CF_attrition label', 'Attrition', 'Gender', 'Over Time', 'Education']
for col in label_encode_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Apply One-hot Encoding
onehot_encode_cols = ['Department', 'Education Field', 'Job Role', 'Marital Status']
df_encoded = pd.get_dummies(df, columns=onehot_encode_cols, drop_first=True)

# Inspect the Data 
print(df_encoded.info())
print(df_encoded.describe(include='all'))
print(df_encoded.columns)

# Separate Feature and Target
X = df_encoded.drop(columns=['Attrition'])
y = df_encoded['Attrition']

# Encoding Missed Column
le = LabelEncoder()
X['Business Travel'] = le.fit_transform(X['Business Travel'])

# Remove leakage features
X = X.drop(['CF_attrition label', 'CF_current Employee'], axis=1)

# Features Selection Using Mutual Information
mutual_info_scores = mutual_info_regression(X, y)

# Create a DataFrame to view results
mi_df = pd.DataFrame({
    'Feature': X.columns,
    'Mutual_Information': mutual_info_scores
}).sort_values('Mutual_Information', ascending=False)
print(mi_df)

# Keeping features with MI > 0.01 (removes 16 zero-importance features)
selected_features = mi_df[mi_df['Mutual_Information'] > 0.01]['Feature'].tolist()
X_selected = X[selected_features]
print(f"Reduced from {X.shape[1]} to {len(selected_features)} features")

# Check correlation among your selected features
corr_matrix = X_selected.corr()
high_corr = corr_matrix[(corr_matrix > 0.8) & (corr_matrix < 1.0)].stack()
print(high_corr)

# Remove the less important feature from each correlated pair
X_final = X_selected.drop(['Department_Sales', 'Job Level'], axis=1)
print(f"Final feature count: {X_final.shape[1]} features")

# Combine features and target into one dataset
final_dataset = X_final.copy()
final_dataset['Attrition'] = y

# Save as single CSV file 
final_dataset.to_csv(r'deployment\employee-attrition-prediction\data\processed\processed_attrition_data.csv', index=False)
