import os
from dotenv import load_dotenv
from google import genai

# تحميل متغيرات البيئة
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("خطأ: لم يتم العثور على GEMINI_API_KEY في ملف .env")
    exit(1)

# إنشاء Client
client = genai.Client(api_key=api_key)

# اختيار النموذج
MODEL_NAME = "gemini-3.5-flash-lite"

# إنشاء جلسة محادثة - تحتفظ بالـ history تلقائياً
chat = client.chats.create(
    model=MODEL_NAME,
    config={
        "system_instruction": "أنت مساعد عربي ودود. أجب بإيجاز ووضوح."
    }
)

print("=" * 50)
print("🤖 Gemini Chat - اكتب 'exit' للخروج")
print("=" * 50)

# حلقة المحادثة
while True:
    # نأخذ سؤال المستخدم
    user_input = input("\nأنت: ").strip()

    # التحقق من أمر الخروج
    if user_input.lower() in ["exit", "quit", "خروج"]:
        print("\n👋 مع السلامة!")
        break

    # تجاهل الأسطر الفارغة
    if not user_input:
        continue

    # إرسال الرسالة للنموذج
    try:
        response = chat.send_message(user_input)
        print(f"\nGemini: {response.text}")
    except Exception as e:
        print(f"\n❌ خطأ: {e}")

# تم تعديلها هنا لتصبح بالحروف الكبيرة MODEL_NAME



