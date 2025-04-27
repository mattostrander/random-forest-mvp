from src.data_loader import load_data, split_data
from src.data_cleaning import basic_cleaning, generate_data_summary
from src.model import train_model
from src.evaluation import evaluate_model
from src.report_generator import generate_report

def main():
    filepath = 'data/your_dataset.csv'  # Adjust if needed
    target_column = 'target'  # Adjust if needed
    model_type = 'random_forest'  # or 'linear_regression'

    # 1. Load data
    df = load_data(filepath, target_column)

    # 2. Clean data
    df_cleaned, _ = basic_cleaning(df)

    # 3. Validate/ summarize data
    generate_data_summary(df_cleaned, target_column)

    # 4. Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(df_cleaned, target_column)

    # 5. Train model on training set
    model = train_model(X_train, y_train)

    # 6. Evaluate model on test set
    metrics = evaluate_model(model, X_test, y_test)

    # 7. Generate report
    generate_report(metrics, model_type=model_type)

if __name__ == "__main__":
    main()