from views import app

from datetime import date
from werkzeug.security import generate_password_hash
from models import *

#
# Örnek kullanıcı verileri
kullanici1 = Kullanici(KullaniciAdi='122123345', Parola='psw123', KullaniciTuru='Ogrenci')
kullanici2 = Kullanici(KullaniciAdi='543321231', Parola='ogrenci_pass', KullaniciTuru='Ogrenci')
kullanici3 = Kullanici(KullaniciAdi='981232765', Parola='ogretim_pass', KullaniciTuru='Ogretim Elemani')

# Örnek öğrenci verileri
ogrenci1 = Ogrenci(BolumID=2, OgrenciNo='122123345', Durumu='Aktif', Adi='Ogrenci11', Soyadi='Soyadi1', TCKimlikNo='1234578921', Cinsiyet='Erkek', DogumTarihi=date(2000, 1, 1), KullaniciID=5)
ogrenci2 = Ogrenci(BolumID=2, OgrenciNo='543321231', Durumu='Aktif', Adi='Ogrenci22', Soyadi='Soyadi2', TCKimlikNo='1098654331', Cinsiyet='Kadin', DogumTarihi=date(1999, 5, 5), KullaniciID=6)
ogrenci3 = Ogrenci(BolumID=1, OgrenciNo='981232765', Durumu='Pasif', Adi='Ogrenci33', Soyadi='Soyadi3', TCKimlikNo='9865432119', Cinsiyet='Erkek', DogumTarihi=date(2001, 10, 10), KullaniciID=7)
# # Örnek Bölüm verileri
bolum1 = Bolum(BolumAdi='Bilgisayar Muhendisligi', ProgramTuru='On Lisans', OgretimTuru='Ogretim', OgrenimDili='Turkce', WebAdresi='www.bilgisayar.com')
bolum2 = Bolum(BolumAdi='Elektrik Muhendisligi', ProgramTuru='Lisans', OgretimTuru='Ogretim', OgrenimDili='Ingilizce', WebAdresi='www.elektrik.com')
bolum3 = Bolum(BolumAdi='Makine Muhendisligi', ProgramTuru='Lisans', OgretimTuru='Ogretim', OgrenimDili='Turkce', WebAdresi='www.makine.com')


# Örnek Öğretim Elemani verileri
ogretim_elemani1 = OgretimElemani(BolumID=1, KurumSicilNo='11111', Unvan='Docent', Adi='Ogretim1', Soyadi='Elemani1', TCKimlikNo='11111111111', Cinsiyet='Erkek', DogumTarihi=date(1980, 1, 1), KullaniciID=3)
ogretim_elemani2 = OgretimElemani(BolumID=2, KurumSicilNo='22222', Unvan='Profesor', Adi='Ogretim2', Soyadi='Elemani2', TCKimlikNo='22222222222', Cinsiyet='Kadin', DogumTarihi=date(1985, 5, 5), KullaniciID=4)
ogretim_elemani3 = OgretimElemani(BolumID=3, KurumSicilNo='33333', Unvan='Yardimci Docent', Adi='Ogretim3', Soyadi='Elemani3', TCKimlikNo='33333333333', Cinsiyet='Erkek', DogumTarihi=date(1990, 10, 10), KullaniciID=5)


# Örnek Derslik verileri
derslik1 = Derslik(DerslikAdi='101', DerslikTuru='Amfi', Kapasite=100)
derslik2 = Derslik(DerslikAdi='202', DerslikTuru='Laboratuvar', Kapasite=30)
derslik3 = Derslik(DerslikAdi='303', DerslikTuru='Sınıf', Kapasite=50)

# Örnek Ders Havuzu verileri
ders_havuzu1 = DersHavuzu(DersKodu='MAT101', DersAdi='Matematik I', DersDili='Turkce', DersSeviyesi='Ilk Yil', DersTuru='Zorunlu', Teorik=3, Uygulama=2, Kredi=5.0, ECTS=6)
ders_havuzu2 = DersHavuzu(DersKodu='PHY201', DersAdi='Fizik II', DersDili='Ingilizce', DersSeviyesi='Ikinci Yil', DersTuru='Secmeli', Teorik=2, Uygulama=3, Kredi=4.0, ECTS=5)
ders_havuzu3 = DersHavuzu(DersKodu='CSE301', DersAdi='Algoritma ve Programlama', DersDili='Turkce', DersSeviyesi='Ucuncu Yil', DersTuru='Zorunlu', Teorik=4, Uygulama=2, Kredi=6.0, ECTS=7)

# Örnek Müfredat verileri
mufredat1 = Mufredat(BolumID=1, DersID=1, AkademikYil='2023-2024', AkademikDonem='Guz', DersDonemi=1)
mufredat2 = Mufredat(BolumID=2, DersID=2, AkademikYil='2023-2024', AkademikDonem='Bahar', DersDonemi=2)
mufredat3 = Mufredat(BolumID=3, DersID=3, AkademikYil='2023-2024', AkademikDonem='Guz', DersDonemi=1)

# Örnek Ders Acma verileri
ders_acma1 = DersAcma(AkademikYil='2023-2024', AkademikDonem='Guz', MufredatID=1, Kontenjan=50, OgrElmID=1)
ders_acma2 = DersAcma(AkademikYil='2023-2024', AkademikDonem='Bahar', MufredatID=2, Kontenjan=40, OgrElmID=2)
ders_acma3 = DersAcma(AkademikYil='2023-2024', AkademikDonem='Guz', MufredatID=3, Kontenjan=30, OgrElmID=3)

# Örnek Ders Alma verileri
ders_alma1 = DersAlma(DersAcmaID=1, OgrenciID=1, Durum='Basarili')
ders_alma2 = DersAlma(DersAcmaID=2, OgrenciID=2, Durum='Devamsiz')
ders_alma3 = DersAlma(DersAcmaID=3, OgrenciID=3, Durum='Devamsiz')

# Örnek Sınav verileri
sinav1 = Sinav(DersAcmaID=1, SinavTuru='Final', EtkiOrani=40, SinavTarihi=date(2024, 1, 15), SinavSaati='14:00:00', DerslikID=1, OgrElmID=1)
sinav2 = Sinav(DersAcmaID=2, SinavTuru='Vize', EtkiOrani=30, SinavTarihi=date(2024, 4, 1), SinavSaati='10:00:00', DerslikID=2, OgrElmID=2)
sinav3 = Sinav(DersAcmaID=3, SinavTuru='Final', EtkiOrani=40, SinavTarihi=date(2024, 1, 15), SinavSaati='14:00:00', DerslikID=3, OgrElmID=3)

# Örnek Değerlendirme verileri
degerlendirme1 = Degerlendirme(SinavID=1, OgrenciID=1, SinavNotu=85.5)
degerlendirme2 = Degerlendirme(SinavID=2, OgrenciID=2, SinavNotu=65.0)
degerlendirme3 = Degerlendirme(SinavID=3, OgrenciID=3, SinavNotu=75.0)

# Örnek Ders Programı verileri
ders_programi1 = DersProgrami(DersAcmaID=1, DerslikID=1, DersGunu='Pazartesi', DersSaati=1)
ders_programi2 = DersProgrami(DersAcmaID=2, DerslikID=2, DersGunu='Salı', DersSaati=2)
ders_programi3 = DersProgrami(DersAcmaID=3, DerslikID=3, DersGunu='Cuma', DersSaati=3)

# Örnek Danışmanlık verileri
danismanlik1 = Danismanlik(OgrElmID=1, OgrenciID=1)
danismanlik2 = Danismanlik(OgrElmID=2, OgrenciID=2)
danismanlik3 = Danismanlik(OgrElmID=3, OgrenciID=3)

# Veritabanına eklemek için

with app.app_context():
    db.session.add_all([kullanici1, kullanici2, kullanici3, bolum1, bolum2, bolum3, ogrenci1, ogrenci2, ogrenci3, ogretim_elemani1, ogretim_elemani2, ogretim_elemani3])
    # db.session.add_all([ogrenci1, ogrenci2, ogrenci3,kullanici1, kullanici2, kullanici3])
    db.session.commit()
# from models import Bolum,Kullanici,Ogrenci
# with app.app_context():
#     ogrenci_sorgusu = db.session.query(Ogrenci).filter_by(OgrenciNo='122123345').first()
#     if ogrenci_sorgusu:
#         kullanici_sorgusu = db.session.query(Kullanici).filter_by(KullaniciID=ogrenci_sorgusu.KullaniciID).first()
#         if kullanici_sorgusu:
#             print("Kullanıcı Adı:", kullanici_sorgusu.KullaniciAdi)
#             print("Kullanıcı Adı:", ogrenci_sorgusu.Adi)
#         else:
#             print("Kullanıcı bulunamadı.")
#     else:
#         print("Öğrenci bulunamadı.")


