from flask import Flask, request, render_template, jsonify, session
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            data = CustomData(
                age=float(request.form.get('age')),
                TSH=float(request.form.get('TSH')),
                T3=float(request.form.get('T3')),
                TT4=float(request.form.get('TT4')),
                T4U=float(request.form.get('T4U')),
                FTI=float(request.form.get('FTI')),
                sex=request.form.get('sex'),
                on_thyroxine=request.form.get('on_thyroxine'),
                query_on_thyroxine=request.form.get('query_on_thyroxine'),
                on_antithyroid_medication=request.form.get('on_antithyroid_medication'),
                sick=request.form.get('sick'),
                pregnant=request.form.get('pregnant'),
                thyroid_surgery=request.form.get('thyroid_surgery'),
                I131_treatment=request.form.get('I131_treatment'),
                query_hypothyroid=request.form.get('query_hypothyroid'),
                query_hyperthyroid=request.form.get('query_hyperthyroid'),
                lithium=request.form.get('lithium'),
                goitre=request.form.get('goitre'),
                tumor=request.form.get('tumor'),
                hypopituitary=request.form.get('hypopituitary'),
                psych=request.form.get('psych')
            )

            pred_df = data.get_data_as_dataframe()

            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(pred_df)

            result_color = 'blue' if pred == 'hypothyroid' else 'yellow'

            return render_template('index.html', pred=pred, pred_df=pred_df, result_color=result_color)

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    
