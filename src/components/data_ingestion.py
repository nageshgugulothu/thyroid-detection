import os
import sysy
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from sklearn.model_slection import train_test_split

@dataclass
class DataIngestionconfig():
    raw_data_path:str = os.path.join("artifacts", "raw_data.csv")
    train_data_path:str = os.path.join("artifacts", "train_data.csv")
    test_data_path:str = os.path.join('artifacts', "test_data.csv")


class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def intiate_data_ingestion(self):
        logging.info("started data ingestion")
        try:
            df = pd.read_csv(os.path.join("./notebook/data/thyroid.csv"))
            logging.info("Reading data is completed")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path)

            logging.info("Train test split is initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            df.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            df.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
