import os
import codecs
import chardet
from collections import defaultdict

# مسار الدليل
dir_path = r"المدونة"

# الحصول على قائمة الملفات
files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# تعريف القاموس
word_count = defaultdict(int)

# التعامل مع الملفات
for file in files:
    try:
        # الحصول على ترميز الملف باستخدام chardet
        with open(file, 'rb') as f:
            result = chardet.detect(f.read())

        # قراءة الملف بالترميز المحدد
        with codecs.open(file, 'r', encoding=result['encoding'], errors='ignore') as f:

            # قراءة الملف وتقسيمه الى كلمات
            words = f.read().split()

            # العد والإحصاء
            for word in words:
                word_count[word] += 1

    except Exception as e:
        print(f"تم تجاهل الملف {file} بسبب الخطأ: {str(e)}")

# تحديد عدد الكلمات في كل ملف
words_per_file = 500000  # تغير هذا العدد حسب الحاجة

# طباعة الكلمات وعددها
i = 0
file_number = 1
file = codecs.open(f"words{file_number}.txt", 'w', encoding='utf8')

for word, count in word_count.items():
    if i >= words_per_file:
        # إغلاق الملف الحالي وفتح ملف جديد
        file.close()
        file_number += 1
        file = codecs.open(f"words{file_number}.txt", 'w', encoding='utf8')
        i = 0
    file.write(f"{word} = {count}\n")
    i += 1
file.close()
