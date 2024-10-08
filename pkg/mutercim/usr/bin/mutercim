#!/usr/bin/env python3

import requests
import tkinter as tk
from tkinter import scrolledtext
import pyperclip
import time
import threading

def translate_text(text):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": "en|tr"  # İngilizceden Türkçeye çeviri
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        translated_text = response.json().get('responseData', {}).get('translatedText', '')
        return translated_text
    else:
        return "Çeviri API'sinde bir hata oluştu."

def monitor_clipboard():
    previous_text = ""
    while True:
        current_text = pyperclip.paste()  # Kopyalanan metni al
        if current_text and current_text != previous_text:
            translated_text = translate_text(current_text)  # Çevir
            result_area.config(state=tk.NORMAL)  # Sonuç alanını etkinleştir
            result_area.delete("1.0", tk.END)  # Önceki sonuçları temizle
            result_area.insert(tk.END, translated_text)  # Yeni sonucu ekle
            result_area.config(state=tk.DISABLED)  # Sonuç alanını devre dışı bırak
            previous_text = current_text  # Son metni güncelle
        time.sleep(1)  # 1 saniye bekle

# Arayüz oluşturma
root = tk.Tk()
root.title("Mütercim - Metin Çeviri Uygulaması")

# Sonuç alanı
result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
result_area.pack(pady=10)

# Klip monitörünü ayrı bir thread'de başlat
threading.Thread(target=monitor_clipboard, daemon=True).start()

root.mainloop()
