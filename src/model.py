from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train, model_type='random_forest'):
    if model_type == 'random_forest':
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    elif model_type == 'linear_regression':
        model = LinearRegression()
    else:
        raise ValueError(f"Unsupported model_type: {model_type}")

    model.fit(X_train, y_train)
    return model