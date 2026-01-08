from src.ml_project.loggers import logging
import sys, os
from src.ml_project.exceptions import CustomException
from dataclasses import dataclass
from src.ml_project.utils import load_db_data
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifects',"train.csv") # creating paths to where we store data from database 
    test_data_path=os.path.join('artifects',"test.csv")
    raw_data_path=os.path.join('artifects',"raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            logging.info("Starting Data Ingestion")
            data=load_db_data()
            logging.info(f" Data Recieved {len(data)}")
            # making artifects directory of not exixts
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            data.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)
            train_data,test_data=train_test_split(data,test_size=0.2, random_state=42)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False, header=True)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False, header=True )
            
            logging.info(f" Data saved successfully  with test_size:{len(test_data)} , and train_size:{len(train_data)} ")
            return{
                self.ingestion_config.test_data_path,
                self.ingestion_config.train_data_path,
                
            }
            
            
            
        except Exception as e:
            raise CustomException("Not Able To Start Ingestion", sys)    
 

