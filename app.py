from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)      #Initializing the flask app

FEATURES = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
]


@app.route("/")
def home():
    return render_template("index.html", prediction=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = [float(request.form[feature]) for feature in FEATURES]
        data = pd.DataFrame([values], columns=FEATURES)

        prediction_pipeline = PredictionPipeline()
        prediction = prediction_pipeline.predict(data)[0]

        return render_template(
            "index.html",
            prediction=round(float(prediction), 2),
            form_data=request.form,
        )
    except Exception as e:
        return render_template(
            "index.html",
            prediction=None,
            error=f"Prediction failed: {e}",
            form_data=request.form,
        )

@app.route('/train', methods = ['GET'])  #Route to train the pipeline
def training():
    os.system('python main.py')
    return 'training successful!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
