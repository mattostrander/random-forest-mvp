# Random Forest and Linear Regression MVP

![GitHub last commit](https://img.shields.io/github/last-commit/mattostrander/random-forest-mvp)

A lightweight, professional framework for automated regression analysis and reporting.

This MVP pipeline:
- Cleans and validates datasets
- Trains both Random Forest and Linear Regression models
- Automatically selects the best model based on RMSE
- Checks critical Linear Regression assumptions (normality, multicollinearity)
- Generates a polished Markdown report with results and diagnostics

---

## 🚀 Features

- **Automatic Model Selection**  
  Trains Random Forest and Linear Regression models, selects the best performer automatically.

- **Data Cleaning and Validation**  
  Handles missing values, ensures clean and ready datasets.

- **Diagnostics for Linear Regression**  
  Checks for residual normality, homoscedasticity, and multicollinearity (VIF).

- **Professional Report Generation**  
  Produces a clean, human-readable Markdown report including model performance and diagnostic checks.

- **Extensible Design**  
  Modular codebase ready for scaling, hyperparameter tuning, or LLM integration.

---

## 📋 How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/mattostrander/random-forest-mvp.git
    cd random-forest-mvp
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv_regression_mvp
    source venv_regression_mvp/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. (Optional) Update or replace the sample dataset in `data/your_dataset.csv`.

5. Run the MVP pipeline:

    ```bash
    python run_mvp.py
    ```

6. View the generated outputs:
    - **Report:** `reports/report.md`
    - **Residuals Plot:** `reports/residuals_vs_predicted.png` (only for Linear Regression)

---

## 📊 Example Report Output

 
# Regression Model Report

## Performance
- RMSE: 0.102
- R2 Score: 1.000

## Notes
- Model: Linear Regression
- Data: Train/Test Split (80%/20%)

## Diagnostics
No major assumption violations detected.

---

## ⚙️ Requirements

- Python 3.12
- pandas
- numpy
- scikit-learn
- scipy
- statsmodels
- matplotlib

---

## 🧠 Future Enhancements

- Add ElasticNet, Ridge Regression models
- Integrate basic hyperparameter tuning
- Track experiments (e.g., MLflow, Weights & Biases)
- Generate LLM-based executive summaries
- Dockerize for deployment
- Sketch cloud deployment architecture

---

## 📣 About

Built by [Matt Ostrander](https://www.linkedin.com/in/matthewrostrander/)  
as a foundation for Veracity Tree, Inc.'s future machine learning and AI services.

The goal: Deliver clean, assumption-aware machine learning pipelines that clients can trust.

---