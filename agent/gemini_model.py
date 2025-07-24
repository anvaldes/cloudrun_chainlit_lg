import google.generativeai as genai

genai.configure()
model = genai.GenerativeModel("models/gemini-1.5-pro")
chat = model.start_chat(history=[])

print("✅ Gemini cargado correctamente")

__all__ = ["chat"]
