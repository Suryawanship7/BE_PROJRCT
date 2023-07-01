from flask import Flask, render_template, request
import pandas as pd
import lightgbm as lgb
import joblib

app = Flask(__name__)

# Load the trained model from the .joblib file
model = joblib.load('templates\trained_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user inputs from the form
    limit_bal = int(request.form['limit_bal'])
    pay_0 = int(request.form['pay_0'])
    pay_2 = int(request.form['pay_2'])
    bill_amt1 = int(request.form['bill_amt1'])
    bill_amt2 = int(request.form['bill_amt2'])
    pay_amt1 = int(request.form['pay_amt1'])
    pay_amt2 = int(request.form['pay_amt2'])
    pay_amt4 = int(request.form['pay_amt4'])

    # Create a DataFrame with the user inputs
    data = pd.DataFrame({
        'LIMIT_BAL': [limit_bal],
        'PAY_0': [pay_0],
        'PAY_2': [pay_2],
        'BILL_AMT1': [bill_amt1],
        'BILL_AMT2': [bill_amt2],
        'PAY_AMT1': [pay_amt1],
        'PAY_AMT2': [pay_amt2],
        'PAY_AMT4': [pay_amt4]
    })

    # Make predictions with the loaded model
    predictions = model.predict(data)

    # Convert the predictions to binary values (0 or 1)
    binary_predictions = [int(prediction >= 0.5) for prediction in predictions]

    # Render the predicted values on the result page
    return render_template('result.html', prediction=binary_predictions[0])

if __name__ == '__main__':
    app.run(debug=True)
