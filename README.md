
# Mütercim - Anlık Çeviri Uygulaması

**Mütercim**, kopyaladığınız metinleri anlık olarak İngilizce'den Türkçe'ye çeviren bir masaüstü uygulamasıdır. Uygulama, Tkinter kullanarak basit bir arayüz sunar ve `MyMemory` çeviri API'sini kullanarak çevirileri gerçekleştirir.

## Özellikler

- Kopyalanan metinler otomatik olarak algılanır.
- İngilizce'den Türkçe'ye anında çeviri yapılır.
- Çeviri işlemi sırasında kullanıcıya "Çeviri yapılıyor..." mesajı gösterilir.
- Sonuçlar, basit ve anlaşılır bir arayüzde kullanıcıya sunulur.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

- `requests`: API istekleri için kullanılır.
- `pyperclip`: Kopyalanan metni almak için kullanılır.
- `tkinter`: Basit bir GUI (Grafik Kullanıcı Arayüzü) oluşturmak için kullanılır.

## Kurulum

1. **Depoyu Klonlayın veya Dosyaları İndirin:**

   ```bash
   git clone https://github.com/aspidisu/mutercim
   cd mutercim
   ```

2. **Gerekli Kütüphaneleri Yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı Çalıştırın:**

   ```bash
   python mutercim.py
   ```

## Kullanım

1. **Metni Kopyalayın:**
   Bilgisayarınızda herhangi bir metni kopyaladığınızda, uygulama otomatik olarak metni algılar.

2. **Anlık Çeviri:**
   Kopyalanan metin İngilizce ise, metin Türkçe'ye çevrilir ve ekranda gösterilir.

## Çeviri API'si

Bu uygulama, [MyMemory](https://mymemory.translated.net/) API'sini kullanarak İngilizce metinleri Türkçe'ye çevirmektedir.