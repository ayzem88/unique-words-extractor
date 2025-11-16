import os
import chardet

folder_path = r"المدونة"
total_word_count = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder_path, filename)

        with open(filepath, 'rb') as f:
            result = chardet.detect(f.read())
        
        with open(filepath, encoding=result['encoding'], errors='ignore') as f:
            word_count = len(f.read().split())
            total_word_count += word_count

print(f"The total word count for all text files is {total_word_count}")
