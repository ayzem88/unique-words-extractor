import os
import codecs
import chardet
from collections import defaultdict, deque
from concurrent import futures

def process_file(file):
    # الحصول على ترميز الملف باستخدام chardet
    try:
        with open(file, 'rb') as f:
            result = chardet.detect(f.read())
        
        # قراءة الملف بالترميز المحدد
        with codecs.open(file, 'r', encoding=result['encoding'], errors='ignore') as f:
            # قراءة الملف وتقسيمه إلى كلمات
            words = f.read().split()
            # العد والإحصاء
            word_count = defaultdict(int)
            for word in words:
                word_count[word] += 1
    except Exception as e:
        print(f"تم تجاهل الملف {file} بسبب الخطأ: {str(e)}")
        return {}
    return word_count

# مسار الدليل
dir_path = r"E:"

# الحصول على قائمة الملفات
files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# تعريف القاموس العام لتجميع جميع الكلمات
total_word_count = defaultdict(int)

# التعامل مع الملفات باستخدام البرمجة المتعددة الخيوط
with futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_to_file = {executor.submit(process_file, file): file for file in files}
    for future in futures.as_completed(future_to_file):
        file = future_to_file[future]
        try:
            file_word_count = future.result()
            for word, count in file_word_count.items():
                total_word_count[word] += count
        except Exception as exc:
            print(f"تم تجاهل الملف {file} بسبب الخطأ: {str(exc)}")

# تحديد عدد الكلمات في كل ملف
words_per_file = 500000  # تغير هذا العدد حسب الحاجة

# تحويل القاموس إلى قائمة مرتبة
word_items = sorted(total_word_count.items(), key=lambda x: x[0])

# استخدام deque للتنقل بين الصفوف لأنها أسرع من القائمة
rows = deque(word_items)

# طباعة الكلمات وعددها إلى ملفات نصية
file_number = 1
file = None
try:
    file = codecs.open(f"words{file_number}.txt", 'w', encoding='utf8')

    while rows:
        for _ in range(words_per_file):
            if rows:  # افحص إذا كانت هناك كلمات متبقية
                word, count = rows.popleft()
                file.write(f"{word} = {count}\n")
        # إغلاق الملف الحالي وفتح ملف جديد إذا كان هناك المزيد من الكلمات
        file.close()
        file_number += 1
        if rows:  # افحص إذا كان هناك كلمات أخرى لتكتبها في ملف جديد
            file = codecs.open(f"words{file_number}.txt", 'w', encoding='utf8')

finally:
    if file and not file.closed:
        file.close()
