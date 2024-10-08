import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTextEdit, QLabel, QPushButton)
from PyQt5.QtCore import QTimer, Qt

# Çeviri fonksiyonu
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
        return None  # Hata durumunda None döndür

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Ana pencere ayarları
        self.setWindowTitle("Mütercim - Anlık Çeviri Uygulaması")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()
        
        # Panoyu izlemek için zamanlayıcı başlat
        self.clipboard = QApplication.clipboard()
        self.previous_text = ""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_clipboard)
        self.timer.start(1000)  # Her saniyede bir kontrol et

        # Tema durumu
        self.dark_mode = True
        self.set_dark_theme()  # Uygulama açıldığında karanlık temayı ayarla

    def init_ui(self):
        # Ana layout
        self.main_layout = QVBoxLayout()

        # Başlık
        self.title_label = QLabel("Mütercim - Anlık Çeviri Uygulaması")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            color: #ffffff;  /* Karanlık temada beyaz, açık temada siyah olacak */
        """)
        self.main_layout.addWidget(self.title_label)

        # Sonuç alanı
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Çeviri burada görünecek...")
        self.result_text.setStyleSheet("""
            background-color: #1e1e1e;
            color: #f9f9f9;
            border: 1px solid #555555;
            font-size: 14px;
            padding: 10px;
            border-radius: 10px;
        """)
        self.main_layout.addWidget(self.result_text)

        # Tema değiştirme butonu
        self.theme_button = QPushButton("Tema Değiştir", self)
        self.theme_button.setStyleSheet("""
            QPushButton {
                background-color: #3a3a3a;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 10px;
                font-size: 14px;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
                border-color: #777777;
                font-size: 15px;
            }
        """)
        self.theme_button.clicked.connect(self.toggle_theme)
        self.main_layout.addWidget(self.theme_button)

        # Ana layout'ı ayarla
        self.setLayout(self.main_layout)

    # Clipboard'u kontrol et
    def check_clipboard(self):
        current_text = self.clipboard.text().strip()  # Panodaki metni al
        if current_text and current_text != self.previous_text:  # Değişiklik varsa
            self.previous_text = current_text  # Önceki metni güncelle
            translated_text = translate_text(current_text)  # Çevir
            if translated_text is not None:  # API'den sonuç alınabilirse
                self.result_text.setText(translated_text)  # Sonucu göster
            else:
                self.result_text.setText("Çeviri API'sinde bir hata oluştu.")  # Hata mesajı göster

    # Tema değiştirme fonksiyonu
    def toggle_theme(self):
        if self.dark_mode:
            self.set_light_theme()
            self.dark_mode = False
        else:
            self.set_dark_theme()
            self.dark_mode = True

    # Light tema
    def set_light_theme(self):
        self.setStyleSheet("background-color: #ffffff; color: #333333;")
        self.title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            color: #000000;  /* Açık temada siyah başlık */
        """)
        self.result_text.setStyleSheet("""
            background-color: #f0f0f0;
            color: #333333;
            border: 1px solid #dddddd;
            font-size: 14px;
            padding: 10px;
            border-radius: 10px;
        """)
        self.theme_button.setStyleSheet("""
            QPushButton {
                background-color: #dddddd;
                color: #333333;
                border: 1px solid #aaaaaa;
                padding: 10px;
                font-size: 14px;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                background-color: #cccccc;
                border-color: #999999;
                font-size: 15px;
            }
        """)

    # Dark tema
    def set_dark_theme(self):
        self.setStyleSheet("background-color: #2b2b2b; color: #f9f9f9;")
        self.title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            color: #ffffff;  /* Karanlık temada beyaz başlık */
        """)
        self.result_text.setStyleSheet("""
            background-color: #1e1e1e;
            color: #f9f9f9;
            border: 1px solid #555555;
            font-size: 14px;
            padding: 10px;
            border-radius: 10px;
        """)
        self.theme_button.setStyleSheet("""
            QPushButton {
                background-color: #3a3a3a;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 10px;
                font-size: 14px;
                border-radius: 10px;
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
                border-color: #777777;
                font-size: 15px;
            }
        """)

# Uygulama başlatma
def main():
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
