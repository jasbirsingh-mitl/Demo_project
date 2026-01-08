import os
from pathlib import Path
import logging

project_name="ml_project"

logging.basicConfig(
    level=logging.INFO  # ensure INFO and above are show
)

files=[
    ".github/workflows/.gitkeep",
     f'src/__init__.py',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/pipelines/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transform.py',
    f'src/{project_name}/components/model_training.py',
    f'src/{project_name}/components/model_monitoring.py',
    f'src/{project_name}/pipelines/model_training_pipe.py',
    f'src/{project_name}/components/prediction_pipe.py',
    f'src/{project_name}/exceptions.py',
    f'src/{project_name}/loggers.py',
    f'src/{project_name}/utils.py',
    "app.py",
    "Dockerfile",
   "setup.py",
    "requirements.txt" 
    
    
    
    
]

for filepath in files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath) # it split diretory name and filename  eg diretory=src\ml_project\components and filename=data_ingestion.py
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir}, for the {filename}")
    
        
    
    if  (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
         logging.info(f"file already exists {filename}")        