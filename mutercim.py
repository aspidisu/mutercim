import requests
import pyperclip
import time
import tkinter as tk
from tkinter import ttk

def translate_text(text):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": "en|tr"  
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        translated_text = response.json().get('responseData', {}).get('translatedText', '')
        return translated_text
    else:
        print("Çeviri API'sinde bir hata oluştu.")
        return None

def update_translation():
    current_text = pyperclip.paste()  #
    if current_text and current_text != previous_text.get():
        translated_label.config(text="Çeviri yapılıyor...")  
        translated_text = translate_text(current_text)
        if translated_text:
            translated_label.config(text=translated_text)  
        previous_text.set(current_text) 
    root.after(1000, update_translation) 

root = tk.Tk()
root.title("Mütercim - Anlık Çeviri Uygulaması")

title_label = tk.Label(root, text="Mütercim - Anlık Çeviri", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

translated_label = tk.Label(root, text="", wraplength=400, justify="left", font=("Arial", 12))
translated_label.pack(pady=20)

previous_text = tk.StringVar()

update_translation()

root.mainloop()
