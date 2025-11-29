# 📄 Python PDF Merger Utility

Bu proje, belirtilen bir klasördeki tüm PDF dosyalarını otomatik olarak tarayan, isme göre sıralayan ve tek bir çıktı dosyası halinde birleştiren basit ve etkili bir Python aracıdır.

Modern `pypdf` kütüphanesi kullanılarak geliştirilmiştir ve `PdfWriter` sınıfı ile stabil bir birleştirme işlemi sunar.

## 🚀 Özellikler

* **Otomatik Tarama:** Klasördeki `.pdf` uzantılı dosyaları kendisi bulur.
* **Akıllı Sıralama:** Dosyaları alfabetik sıraya göre işler.
* **Hata Yönetimi:** Bozuk dosyaları atlar ve süreci durdurmadan diğer dosyaları birleştirir.
* **Döngü Koruması:** Eğer çıktı dosyası (Birlestirilmis_Dosya.pdf) klasörde zaten varsa, onu tekrar birleştirmeye çalışmaz.

## 🛠️ Kurulum

1.  Bu projeyi bilgisayarınıza indirin (veya `git clone` yapın).
2.  Gerekli Python kütüphanesini kurun:

```bash
pip install pypdf
```

## ✅ Kullanım

1. `KLASOR_YOLU = r"Klasör yolunuzu girin"` Kodda bu kısmı bulup güncelleyin.
bunu yaparken `r` harfini silmeyin.

2. Scripti çalıştırın.