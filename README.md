# مستخرج الكلمات الفريدة من المدونة / Unique Words Extractor

<div dir="rtl">

## نظرة عامة

أداة متقدمة لاستخراج الكلمات الفريدة من المدونات النصية العربية. تدعم معالجة ملفات متعددة وإحصاء الكلمات بشكل متوازي.

## المميزات

- 🔍 **استخراج الكلمات الفريدة**: استخراج جميع الكلمات الفريدة من المدونة
- 📊 **إحصاء الكلمات**: إحصاء عدد تكرار كل كلمة
- ⚡ **معالجة متوازية**: معالجة متعددة الملفات بشكل متوازي
- 🧹 **تنظيف النصوص**: تنظيف النصوص وفق رموز محددة
- 📁 **معالجة المجلدات**: معالجة جميع الملفات في مجلد واحد

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- chardet (للكشف عن الترميز)

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/unique-words-extractor.git
cd unique-words-extractor
```

2. قم بتثبيت المتطلبات:
```bash
pip install chardet
```

## الاستخدام

### النسخة المطورة

```bash
python "مستخرج الكلمات الفريدة - المطور.py"
```

### النسخة البسيطة

```bash
python "مستخرج الكلمات الفريدة - بسيط.py"
```

### تنظيف النصوص

```bash
python "منظف النصوص وفق رموز محددة.py"
```

## هيكل المشروع

```
مستخرج الكلمات الفريدة من المدونة/
├── مستخرج الكلمات الفريدة - المطور.py
├── مستخرج الكلمات الفريدة - بسيط.py
├── إحصاء عدد كل الكلمات في المجلد.py
├── جمع الملفات في ملف.py
└── منظف النصوص وفق رموز محددة.py
```

## الملفات الرئيسية

- **مستخرج الكلمات الفريدة - المطور.py**: النسخة المطورة مع معالجة متوازية
- **مستخرج الكلمات الفريدة - بسيط.py**: النسخة البسيطة
- **منظف النصوص وفق رموز محددة.py**: تنظيف النصوص

## ملاحظات مهمة

⚠️ **ملاحظة**: 
- البرنامج يدعم الكشف التلقائي عن ترميز الملفات
- يمكن تحديد عدد الكلمات في كل ملف مخرجات
- المعالجة المتوازية تسرع العملية بشكل كبير

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] تحسين الأداء
- [ ] دعم المزيد من صيغ الملفات
- [ ] تصدير النتائج بصيغ متعددة

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

An advanced tool for extracting unique words from Arabic text corpora. Supports processing multiple files and counting words in parallel.

## Features

- 🔍 **Extract Unique Words**: Extract all unique words from corpus
- 📊 **Word Counting**: Count frequency of each word
- ⚡ **Parallel Processing**: Process multiple files in parallel
- 🧹 **Text Cleaning**: Clean texts according to specified symbols
- 📁 **Folder Processing**: Process all files in a folder

## Installation

### Requirements

- Python 3.7 or later
- chardet (for encoding detection)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/unique-words-extractor.git
cd unique-words-extractor
```

2. Install requirements:
```bash
pip install chardet
```

## Usage

### Advanced Version

```bash
python "مستخرج الكلمات الفريدة - المطور.py"
```

### Simple Version

```bash
python "مستخرج الكلمات الفريدة - بسيط.py"
```

### Clean Texts

```bash
python "منظف النصوص وفق رموز محددة.py"
```

## Project Structure

```
unique-words-extractor/
├── مستخرج الكلمات الفريدة - المطور.py
├── مستخرج الكلمات الفريدة - بسيط.py
├── إحصاء عدد كل الكلمات في المجلد.py
├── جمع الملفات في ملف.py
└── منظف النصوص وفق رموز محددة.py
```

## Main Files

- **مستخرج الكلمات الفريدة - المطور.py**: Advanced version with parallel processing
- **مستخرج الكلمات الفريدة - بسيط.py**: Simple version
- **منظف النصوص وفق رموز محددة.py**: Text cleaning

## Important Notes

⚠️ **Note**: 
- The program supports automatic encoding detection
- You can specify the number of words in each output file
- Parallel processing significantly speeds up the process

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Performance improvements
- [ ] Support for more file formats
- [ ] Export results in multiple formats

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

