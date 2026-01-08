from src.ml_project.loggers import logging
import sys
import os 
from src.ml_project.exceptions import CustomException
from dataclasses import dataclass
import pandas as pd
import mysql.connector

from dotenv import load_dotenv
import pymysql
load_dotenv()
def sql_connection():
    try:
        logging.info("starting Preparing connection")
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")
        port = os.getenv("DB_PORT", 3306)
        
        # Validate required variables
        if not all([host, user, password, database]):
            raise CustomException("Missing required database environment variables.", sys)
        logging.info("starting Preparing connection step 2")
        # Create MySQL connection
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=int(port)
        )
        logging.info("starting Preparing connection step 3", conn)
        logging.info("connected successfully")
        return conn
    
    except Exception as e:
        raise CustomException("Failed To establish connection", sys)
        


def load_db_data():
    try:
        logging.info("Reading data from mysql Database")
        # df = pd.read_csv( r"C:\Users\jasbir.singh02\OneDrive - Motherson Group\Desktop\student_performance.csv",index_col="student_id")
        conn=sql_connection()
        df = pd.read_sql("SELECT * From students", conn)
        
        logging.info("Reading data Success! from mysql Database")
        return df
    except Exception as e:
        raise CustomException("Not able to load data from my sql ",sys)
    
load_db_data()



    