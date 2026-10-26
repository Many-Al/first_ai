# استيراد المكتبات اللازمة
import os
from dotenv import load_dotenv
import google.generativeai as genai

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# قراءة API key من المتغيرات
api_key = os.getenv("GEMINI_API_KEY")

# التحقق من أن المفتاح موجود
if not api_key:
    print("خطأ: لم يتم العثور على GEMINI_API_KEY في ملف .env")
    exit(1)

# إعداد Gemini SDK بالمفتاح
genai.configure(api_key=api_key)

# اختيار النموذج - flash سريع ومجاني
model = genai.GenerativeModel("gemini-3.5-flash")

# إرسال سؤال للنموذج
print("جاري الاتصال بـ Gemini...")
response = model.generate_content("اشرح مفهوم الـ API في 3 جمل بسيطة بالعربية")

# طباعة الإجابة
print("\n--- إجابة Gemini ---")
print(response.text)
