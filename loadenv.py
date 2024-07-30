from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv('OPENAI_API_KEY')

# Verify that the API key is loaded
if api_key:
    print("API Key loaded successfully.",api_key)
else:
    print("Failed to load API Key.")