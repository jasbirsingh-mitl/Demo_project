from src.ml_project.loggers import logging
from src.ml_project.components.data_transform import function
from src.ml_project.exceptions import CustomException
import sys
from src.ml_project.components.data_ingestion import DataIngestion

if __name__=="__main__":
    a = function()
    
    logging.info("here is my logger main ")
    try:
        data_ingestion=DataIngestion()
        res=data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion is completed  stored at {res}")
        
        
    except Exception as e:
        logging.info("it is Custom Exception")
        raise CustomException(e,sys)  
    
        
    