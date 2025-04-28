from src.data_loader import load_data, split_data
from src.data_cleaning import basic_cleaning, generate_data_summary
from src.model import train_model
from src.evaluation import evaluate_model
from src.report_generator import generate_report

def main():
    filepath = 'data/your_dataset.csv'
    target_column = 'target'

    # 1. Load and clean data
    df = load_data(filepath, target_column)
    df_cleaned, _ = basic_cleaning(df)
    generate_data_summary(df_cleaned, target_column)
    X_train, X_test, y_train, y_test = split_data(df_cleaned, target_column)

    # 2. Train Random Forest
    rf_model = train_model(X_train, y_train, model_type='random_forest')
    rf_metrics = evaluate_model(rf_model, X_test, y_test)

    # 3. Train Linear Regression
    lr_model = train_model(X_train, y_train, model_type='linear_regression')
    lr_metrics = evaluate_model(lr_model, X_test, y_test)

    # 4. Compare models
    if rf_metrics['RMSE'] < lr_metrics['RMSE']:
        best_model = rf_model
        best_metrics = rf_metrics
        best_model_type = 'random_forest'
    else:
        best_model = lr_model
        best_metrics = lr_metrics
        best_model_type = 'linear_regression'

    # 5. Generate report for best model
    generate_report(best_metrics, model_type=best_model_type)

if __name__ == "__main__":
    main()