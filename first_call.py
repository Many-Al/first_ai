import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("خطأ: لم يتم العثور على GEMINI_API_KEY في ملف .env")
    exit(1)

client = genai.Client(api_key=api_key)

print("جاري الاتصال بـ Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="اشرح مفهوم الـ API في 3 جمل بسيطة بالعربية",
)

print("\n--- إجابة Gemini ---")
print(response.text)
