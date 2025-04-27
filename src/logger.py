import logging
import os
from datetime import datetime

LogFile = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LogsPath = os.path.join(os.getcwd(),"logs")
os.makedirs(LogsPath, exist_ok=True)

LogFilePath = os.path.join(LogsPath,LogFile)

logging.basicConfig(
    filename=LogFilePath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    )