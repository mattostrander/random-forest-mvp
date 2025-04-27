# Random Forest MVP

![GitHub last commit](https://img.shields.io/github/last-commit/mattostrander/random-forest-mvp)

This project is a Minimal Viable Product (MVP) for an automated regression analysis pipeline using a Random Forest Regressor.

## Features
- Load structured datasets (CSV)
- Perform basic data cleaning and feature encoding
- Train a Random Forest Regressor on training data
- Evaluate model performance (RMSE, R²) on held-out test data
- Generate a Markdown report summarizing results

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/mattostrander/random-forest-mvp.git
    cd random-forest-mvp
    ```

2. Create and activate a Python virtual environment:
    ```bash
    python3 -m venv venv_regression_mvp
    source venv_regression_mvp/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Place your dataset CSV into the `data/` directory.

5. Run the project:
    ```bash
    python run_mvp.py
    ```

## Requirements
- Python 3.12
- pandas
- numpy
- scikit-learn

---