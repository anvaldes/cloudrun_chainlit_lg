import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("models/gemini-1.5-pro")
chat = model.start_chat(history=[])

print("✅ Gemini cargado correctamente")

__all__ = ["chat"]
