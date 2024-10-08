import sys
import requests
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QComboBox
from PyQt5.QtCore import QTimer

class MutercimApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mütercim - Anlık Çeviri")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        
        # Dil seçim menüsü
        self.language_label = QLabel("Çeviri Dili Seçin:")
        self.layout.addWidget(self.language_label)

        self.language_combo = QComboBox()
        self.language_combo.addItems(["İngilizce", "Fransızca", "Almanca", "İspanyolca", "İtalyanca"])
        self.layout.addWidget(self.language_combo)

        # Başlık
        self.input_label = QLabel("Kopyalanan Metin:")
        self.layout.addWidget(self.input_label)

        # Girdi metin kutusu
        self.input_text = QTextEdit()
        self.layout.addWidget(self.input_text)

        # Çeviri başlığı
        self.output_label = QLabel("Çeviri:")
        self.layout.addWidget(self.output_label)

        # Çıktı metin kutusu
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout.addWidget(self.output_text)

        self.setLayout(self.layout)

        # Önceki metni tutmak için değişken
        self.previous_text = ""
        
        # Her 1000 ms'de bir panoyu kontrol etmek için bir zamanlayıcı ayarlıyoruz
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_clipboard)
        self.timer.start(1000)  # 1 saniyede bir kontrol et

        # Stil ayarları
        self.setStyle()

    def setStyle(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                margin: 10px 0;
                color: #333333;
            }
            QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                background-color: #ffffff;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
            QTextEdit:focus {
                border: 1px solid #007BFF;
                background-color: #e9f7fe;
                box-shadow: 0 2px 10px rgba(0, 123, 255, 0.3);
            }
            QComboBox {
                border: 1px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                background-color: #ffffff;
            }
            QComboBox:focus {
                border: 1px solid #007BFF;
            }
            QComboBox::drop-down {
                border: none; /* Açılır menü okunu özelleştirmek için kullanılabilir */
            }
            QComboBox:hover {
                border: 1px solid #007BFF;
            }
            QComboBox QAbstractItemView {
                background-color: #ffffff; /* Açılır menü arka plan rengi */
                selection-background-color: #007BFF; /* Seçim arka plan rengi */
                selection-color: #ffffff; /* Seçim metin rengi */
                color: #333333; /* Varsayılan metin rengi */
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #007BFF; /* Hover durumu için arka plan rengi */
                color: #ffffff; /* Hover durumunda metin rengi */
            }
        """)

    def check_clipboard(self):
        current_text = pyperclip.paste()
        if current_text != self.previous_text:
            self.previous_text = current_text
            self.input_text.setPlainText(current_text)
            self.translate_text(current_text)

    def translate_text(self, text):
        if text:
            # Seçilen dili al
            selected_language = self.language_combo.currentText()
            language_mapping = {
                "İngilizce": "en|tr",
                "Fransızca": "fr|tr",
                "Almanca": "de|tr",
                "İspanyolca": "es|tr",
                "İtalyanca": "it|tr"
            }
            lang_pair = language_mapping[selected_language]

            url = "https://api.mymemory.translated.net/get"
            params = {
                "q": text,
                "langpair": lang_pair
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                result = response.json()
                translated_text = result['responseData']['translatedText']
                self.output_text.setPlainText(translated_text)
            else:
                self.output_text.setPlainText("Çeviri alınamadı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MutercimApp()
    window.show()
    sys.exit(app.exec_())
