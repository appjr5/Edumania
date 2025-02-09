import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Access variables
my_api_key = os.getenv('GEMINI_API')

# print(my_api_key)
genai.configure(api_key= my_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)