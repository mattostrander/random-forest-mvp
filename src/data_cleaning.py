from sklearn.preprocessing import LabelEncoder

def basic_cleaning(df):
    # Separate predictors and target
    predictors = df.drop(columns=[df.columns[-1]])  # assumes last column is target
    target = df[df.columns[-1]]

    # Handle missing values in predictors
    if predictors.isnull().any().any():
        print("Warning: Missing values detected in predictors. Filling with median values.")
        predictors = predictors.fillna(predictors.median())

    # Warn about non-numeric columns
    non_numeric_cols = predictors.select_dtypes(exclude=['number']).columns
    label_encoders = {}

    if len(non_numeric_cols) > 0:
        print(f"Warning: Non-numeric columns detected: {list(non_numeric_cols)}. Encoding them.")
        for col in non_numeric_cols:
            le = LabelEncoder()
            predictors[col] = le.fit_transform(predictors[col].astype(str))
            label_encoders[col] = le

    # Recombine predictors and target
    df_cleaned = predictors.copy()
    df_cleaned[df.columns[-1]] = target.values

    return df_cleaned, label_encoders

def generate_data_summary(df, target_column):
    print("\n✅ Data Summary:")
    predictors = df.drop(columns=[target_column])
    
    # Number of predictors
    print(f"- {predictors.shape[1]} predictors")

    # Missing values in predictors
    missing = predictors.isnull().sum().sum()
    if missing == 0:
        print(f"- 0 missing predictor values")
    else:
        print(f"- {missing} missing predictor values")

    # Categorical features
    non_numeric_cols = predictors.select_dtypes(exclude=['number']).columns
    if len(non_numeric_cols) == 0:
        print(f"- 0 categorical features (after cleaning)")
    else:
        print(f"- {len(non_numeric_cols)} categorical features still present: {list(non_numeric_cols)}")

    # Target column name
    print(f"- Target column: '{target_column}'\n")
    print("Proceeding to model training...\n")