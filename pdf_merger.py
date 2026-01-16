import os
import sys
import re

# Kütüphane kontrolü
try:
    # PdfMerger yerine PdfWriter ve PdfReader kullanıyoruz. Çünkü uzun denemelerime rağmen pdfmergeri çalıştıramadım.
    from pypdf import PdfWriter, PdfReader
except ImportError:
    print("HATA: pypdf kütüphanesi eksik. Terminale 'python -m pip install pypdf' yaz.")
    sys.exit()

# ---------------- AYARLAR ----------------
# Buraya pdf'lerin bulunduğu klasörün pathini yazın.
KLASOR_YOLU = r"C:\Users\ztalh\OneDrive\Desktop\Bilgisayar\pdf_birlestirici_klasör"

# Çıktı dosyasının adı, istediğiniz şekilde güncelleyebilirsiniz.
CIKTI_ISMI = "Birlestirilmis_Dosya.pdf"

def natural_sort(dosya_adi):
    return tuple(
        int(c) if c.isdecimal() else c.lower().strip()  #Okunulabilirlik açısından tuple'ı böyle yazdım.  (isdecimal() ile isdigit()'te okunan ama konumuzla alakasız olan unicodelardan kurtulucaz.)
        for c in re.split(r'(\d+)', dosya_adi)) #Bu yenilik sayesinde 2 < 10 gibi alfabetik digit sıralama sorunu yaşamayacağız. (küçükten büyüğe sıralıyoruz ama 10 2 den önce geliyordu önceden.)

def pdf_birlestir():
    # 1. Klasör Kontrolü
    if not os.path.exists(KLASOR_YOLU):
        print(f"❌ HATA: Klasör bulunamadı: {KLASOR_YOLU}")
        return

    # 2. PDF Dosyalarını Listeleme
    tum_dosyalar = os.listdir(KLASOR_YOLU)
    pdf_dosyalari = [f for f in tum_dosyalar if f.lower().endswith('.pdf')]

    # Çıktı dosyası zaten varsa listeye alma
    if CIKTI_ISMI in pdf_dosyalari:
        pdf_dosyalari.remove(CIKTI_ISMI)

    if not pdf_dosyalari:
        print("⚠️  Bu klasörde hiç PDF dosyası yok!")
        return

    pdf_dosyalari.sort(key=natural_sort) #pdflerin sıralanabilir olması durumuna dikkat edin.


    # 3. Yazma İşlemi (Writer Kullanarak)
    writer = PdfWriter()
    print(f"\n📂 Çalışılan Klasör: {KLASOR_YOLU}")
    print(f"📄 Toplam {len(pdf_dosyalari)} adet PDF işleniyor...\n")

    for dosya_adi in pdf_dosyalari:
        tam_yol = os.path.join(KLASOR_YOLU, dosya_adi)
        
        try:
            # Her dosyayı Reader ile açıp Writer'a ekliyoruz
            reader = PdfReader(tam_yol)
            
            # YÖNTEM: append metodu reader nesnesini direkt alır ve sayfaları ekler
            writer.append(reader)
            
            print(f"  OK -> {dosya_adi} ({len(reader.pages)} sayfa)")
            
        except Exception as e:
            print(f"  ❌ HATA -> {dosya_adi} okunamadı. ({e})")

    # 4. Dosyayı Kaydetme
    kayit_yolu = os.path.join(KLASOR_YOLU, CIKTI_ISMI)
    try:
        with open(kayit_yolu, "wb") as cikti_dosyasi:
            writer.write(cikti_dosyasi)
        
        print("-" * 30)
        print(f"✅ İŞLEM BAŞARILI! (PdfWriter kullanıldı)")
        print(f"Dosya: {kayit_yolu}")
        
    except PermissionError:
        print("❌ HATA: Dosya kaydedilemedi! PDF açık olabilir, kapatıp tekrar dene.")
    except Exception as e:
        print(f"❌ BEKLENMEYEN HATA: {e}")

if __name__ == "__main__":
    pdf_birlestir()
