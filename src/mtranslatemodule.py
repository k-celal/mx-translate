from mtranslate import translate
import time

def translate_text(text, target_language):
    try:
        translated = translate(text,target_language,"auto")
        return translated
    except Exception as e:
        print(f"Hata oluştu: {e}")
        time.sleep(60)
        return "---------------------------bosluk--------------------------------"  # Hata durumunda belirtilen metin
translated_texts = []
text_file_path = "eng.txt"  # Verilerin olduğu dosya
output_file_path = "turkce1807750.txt"  # Çevirilen metinlerin yazılacağı dosya

with open(text_file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

def MXTranslate(lines,batch_size,start_index=0,):
    i = 0
    print("-----------------ceviri basliyor-------------------")
    for line in lines[start_index:]:
        if i%batch_size==0:
            print(f"{i}. satira kadar yaziliyor")
            with open(output_file_path, "a", encoding="utf-8") as f_out:
                for text in translated_texts[(i-batch_size):(i+1)]:
                    f_out.write(text + "\n")
        source_text = line.strip()
        result = translate_text(source_text, "tr")
        translated_texts.append(result)
        i += 1

MXTranslate(lines=lines,batch_size=1000)