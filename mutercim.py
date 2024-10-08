#!/usr/bin/env python3

import requests
import tkinter as tk
from tkinter import scrolledtext, ttk
import pyperclip
import time
import threading

# Başlangıçta karanlık tema
dark_theme = True

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

def toggle_theme():
    global dark_theme
    if dark_theme:
        # Açık tema ayarları
        root.configure(bg="#F5F5F5")
        title_label.config(bg="#F5F5F5", fg="#333")
        result_area.config(bg="#FFFFFF", fg="#333")
        theme_button.config(bg="#4CAF50", fg="white")
        theme_button.config(text="Karanlık Temaya Geç")
    else:
        # Karanlık tema ayarları
        root.configure(bg="#2E2E2E")
        title_label.config(bg="#2E2E2E", fg="#FFFFFF")
        result_area.config(bg="#444444", fg="#FFFFFF")
        theme_button.config(bg="#FF5722", fg="white")
        theme_button.config(text="Açık Temaya Geç")
    dark_theme = not dark_theme

# Arayüz oluşturma
root = tk.Tk()
root.title("Mütercim - Metin Çeviri Uygulaması")
root.geometry("600x400")  # Uygulama boyutu

# Karanlık tema ayarları
root.configure(bg="#2E2E2E")  # Arka plan rengi

# Tema ayarları
style = ttk.Style()
style.theme_use("clam")  # Temayı değiştirin
style.configure("TLabel", font=("Arial", 12))

# Başlık
title_label = tk.Label(root, text="Mütercim - Anlık Çeviri Uygulaması", font=("Arial", 18, "bold"), bg="#2E2E2E", fg="#FFFFFF")
title_label.pack(pady=20)

# Sonuç alanı
result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, state=tk.DISABLED, bg="#444444", fg="#FFFFFF")
result_area.pack(pady=10, padx=10)

# Tema değiştirme butonu
theme_button = tk.Button(root, text="Açık Temaya Geç", command=toggle_theme, bg="#FF5722", fg="white", font=("Arial", 12), relief="flat")
theme_button.pack(pady=10)

# Buton hover etkisi için fonksiyon
def on_enter(e):
    theme_button.config(bg="#FF784E")  # Hover rengi

def on_leave(e):
    if dark_theme:
        theme_button.config(bg="#FF5722")  # Karanlık tema rengi
    else:
        theme_button.config(bg="#4CAF50")  # Açık tema rengi

# Buton üzerine gelince renk değiştirme
theme_button.bind("<Enter>", on_enter)
theme_button.bind("<Leave>", on_leave)

# Klip monitörünü ayrı bir thread'de başlat
threading.Thread(target=monitor_clipboard, daemon=True).start()

# Uygulamanın ana döngüsünü başlat
root.mainloop()
