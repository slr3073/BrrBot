import os
from dotenv import load_dotenv

load_dotenv()

def getToken():
    return os.getenv("TOKEN")
