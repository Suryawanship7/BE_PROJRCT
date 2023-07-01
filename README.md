# BE_PROJRCT
GitHub Repository: Credit Card Default Loan Prediction

This GitHub repository contains code for a credit card default loan prediction application. The application uses the LightGBM machine learning library and Flask web framework to train a binary classification model and make predictions on user inputs.

The repository includes the following files:

1. `credit_card.csv`: The dataset used for training and testing the model. It contains features such as credit limit, payment history, bill amounts, and payment amounts.

2. `trained_model.joblib`: A joblib file that stores the trained LightGBM model. This file is generated after training the model and is used for making predictions.

3. `app.py`: The main Python file that defines the Flask application. It contains the routes for rendering the home page (`index.html`) and handling the prediction request (`/predict`).

4. `templates/index.html`: The HTML template for the home page. It includes a form where users can enter their credit card details.

5. `templates/result.html`: The HTML template for the result page. It displays the prediction result returned by the model.

To use the application, follow these steps:

1. Install the required dependencies: pandas, LightGBM, Flask, and joblib.

2. Run the Flask application by executing the command `python app.py` in the terminal.

3. Open a web browser and go to `http://localhost:5000` to access the application.

4. Enter the required credit card details in the form and click the "Predict" button.

5. The application will make predictions using the trained model and display the result on the result page.

The code is organized in a modular manner, making it easy to understand and extend. It demonstrates how to load data, train a LightGBM model, save and load the model using joblib, and integrate the model into a web application using Flask.

This repository serves as a practical example of using machine learning techniques to predict credit card default loan status and provides a starting point for further development or research in this area.
