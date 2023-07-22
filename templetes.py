import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s - %(message)s]')

list_of_files = [
    
    ".github/workflows/main.yaml",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/exception.py",
    f"src/logger.py",
    f"src/utils.py",
    f"src/pipline/__init__.py",
    f"src/pipline/prediction_pipline.py",
    f"src/pipline/training_pipline.py",
    f"notebook/data/test.csv",
    f"notebook/EDA.ipynb",
    "README.md",
    "requirements.txt",
    ".gitignore",
    "setup.py",
    "Dockerfile"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} : file name : {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file {filepath}")

    else:
        logging.info(f" {filename} is already exits")


