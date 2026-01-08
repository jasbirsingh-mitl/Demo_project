import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_File = f"{datetime.now().strftime('%m-%d_%H-%M-%S')}.log"
LOG_Path=os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_Path, exist_ok=True)
FULL_LOG_PATH=os.path.join(LOG_Path,LOG_File)



# set up logging to file
logging.basicConfig(
     filename=FULL_LOG_PATH,
     level=logging.INFO, 
     format= '[%(asctime)s] {%(lineno)d:%(name)s} %(levelname)s - %(filename)s - %(message)s',
     datefmt='%H:%M:%S'
 )
