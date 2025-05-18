# gemini_utils.py

import google.generativeai as genai

# Replace with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyBvLL0VGjdAyoS9DlI3WT98BgUMMMiVA7s"

genai.configure(api_key=GEMINI_API_KEY)

def call_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Updated to Gemini 1.5 Flash
    response = model.generate_content(prompt)
    return response.text