import os 
import sys
import pandas as pd
import numpy as np
import pickle


from src.logger import logging
from src.exception import CustomException

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import LabelEncoder

def save_model(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_model(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)


def evaluate_model(file_path):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        model_report = {}

        # Encode categorical target variable if present
        label_encoder = LabelEncoder()
        if isinstance(y_train[0], str):
            y_train = label_encoder.fit_transform(y_train)
            y_test = label_encoder.transform(y_test)

        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)

            # Calculate R2 score
            test_model_score = r2_score(y_test, y_test_pred)
            model_report[model_name] = test_model_score

        return model_report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
