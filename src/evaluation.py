from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_model(model, X_test, y_test):
    # Predict on test data
    y_pred = model.predict(X_test)

    # Calculate RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Calculate R2 score
    r2 = r2_score(y_test, y_pred)

    metrics = {
        'RMSE': rmse,
        'R2': r2
    }

    return metrics