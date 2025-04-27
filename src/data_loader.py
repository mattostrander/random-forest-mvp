import pandas as pd
import os
from sklearn.model_selection import train_test_split

def load_data(filepath, target_column):
    # Check if file exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # Try loading the CSV
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Failed to read CSV file. Error: {e}")

    # Check if target column exists
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in data. Available columns: {list(df.columns)}")

    # Check for missing target values
    if df[target_column].isnull().any():
        raise ValueError(f"Missing values detected in target column '{target_column}'.")

    return df

def split_data(df, target_column, test_size=0.2, random_state=42):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    return X_train, X_test, y_train, y_test