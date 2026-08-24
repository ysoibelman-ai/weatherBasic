from dotenv import load_dotenv
import os
from requests import get

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

main()

    
