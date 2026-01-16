# 📄 Python PDF Merger Utility

Bu proje, belirtilen bir klasördeki tüm PDF dosyalarını otomatik olarak tarayan, **insan mantığına uygun şekilde (doğal sıralama ile)** sıralayan ve tek bir çıktı dosyası halinde birleştiren güçlü bir Python aracıdır.

Modern **`pypdf`** kütüphanesi kullanılarak geliştirilmiştir. `PdfWriter` sınıfı sayesinde büyük dosyalarda bile yüksek performanslı ve stabil bir birleştirme işlemi sunar.

## 🚀 Özellikler

* **🔍 Otomatik Tarama:** Klasördeki `.pdf` uzantılı dosyaları kendisi bulur ve listeler.
* **🔢 Doğal Sıralama (Natural Sort):** Dosyaları standart bilgisayar sıralamasıyla (1, 10, 2) değil, **sayısal büyüklüğe göre (1, 2, 10)** sıralar.
    * *Örn:* `Rapor_2.pdf` dosyası artık `Rapor_10.pdf` dosyasından önce gelir.
* **🛡️ Hata Yönetimi:** Bozuk veya okunamayan dosyaları atlar, süreci durdurmadan diğer dosyaları birleştirmeye devam eder.
* **🔄 Döngü Koruması:** Eğer çıktı dosyası (Varsayılan: `Birlestirilmis_Dosya.pdf`) klasörde zaten varsa, onu tekrar işleme dahil etmez.
* **🧹 Akıllı Temizlik:** Dosya isimlerindeki gereksiz boşlukları (Örn: "Dosya 1 .pdf") yoksayarak doğru sıralama yapar.

## 🛠️ Kurulum

1.  Bu projeyi bilgisayarınıza indirin (veya `git clone` yapın).
2.  Gerekli Python kütüphanesini kurun:
    ```bash
    pip install pypdf
    ```

## ✅ Kullanım

1.  Python dosyasını açın.
2.  `KLASOR_YOLU` değişkenini kendi PDF klasörünüzün yoluyla güncelleyin:
    ```python
    KLASOR_YOLU = r"C:\Kullanici\Belgeler\PDFlerim"
    # Not: Başındaki 'r' harfini silmeyin.
    ```
3.  Scripti çalıştırın:
    ```bash
    python main.py
    ```

## 📝 Notlar
* Program, dosya ismindeki sayıları (digit) algılamak için Regex kullanır.
* Unicode karakterler (², ① vb.) sıralamayı bozmaz, sadece standart rakamlar (0-9) sıralama için baz alınır.
