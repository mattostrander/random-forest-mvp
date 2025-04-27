def generate_report(metrics, model_type, output_path='reports/report.md'):
    report_content = f""" 
# Regression Model Report

## Performance
- RMSE: {metrics['RMSE']:.3f}
- R2 Score: {metrics['R2']:.3f}

## Notes
- Model: {model_type.replace('_', ' ').title()}
- Data: Train/Test Split (80%/20%)
"""
    with open(output_path, 'w') as f:
        f.write(report_content)