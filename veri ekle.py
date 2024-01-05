from sqlalchemy import func, desc

from views import app
from datetime import time, datetime
from datetime import date
from werkzeug.security import generate_password_hash
from models import *
import random
from views import app

from datetime import date
from werkzeug.security import generate_password_hash
from models import *
from faker import Faker

# 'hi_IN' changed the language
fake = Faker('tr_TR')

durum_ = {1: "Aktif", 2: "Pasif"}
sex = {"M": "Erkek", "F": "Kadın"}

# bolum1 = Bolum(
#     BolumAdi='Bilgisayar Mühendisliği',
#     ProgramTuru='On Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='Türkçe',
#     WebAdresi='Bilgisayar-Mühendisliği'.lower()
# )
#
# bolum11 = Bolum(
#     BolumAdi='Bilgisayar Mühendisliği',
#     ProgramTuru='On Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='İngilizce',
#     WebAdresi='Bilgisayar-Mühendisliği'.lower()
# )
# bolum2 = Bolum(
#     BolumAdi='Elektrik Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='Türkçe',
#     WebAdresi='Elektrik Mühendisliği'.lower()
# )
# bolum22 = Bolum(
#     BolumAdi='Elektrik Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='İngilizce',
#     WebAdresi='Elektrik Mühendisliği'.lower()
# )
#
# bolum3 = Bolum(
#     BolumAdi='Elektrik-Elektronik Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='Turkce',
#     WebAdresi='Elektrik-Elektronik Mühendisliği'.lower()
# )
#
# bolum33 = Bolum(
#     BolumAdi='Elektrik-Elektronik Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='İngilizce',
#     WebAdresi='Elektrik-Elektronik Mühendisliği'.lower()
# )
#
# bolum4 = Bolum(
#     BolumAdi='Yazılım Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='İngilizce',
#     WebAdresi='Yazılım-Mühendisliği'.lower()
# )
# bolum44 = Bolum(
#     BolumAdi='Yazılım Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='Türkçe',
#     WebAdresi='Yazılım-Mühendisliği'.lower()
# )
# bolum5 = Bolum(
#     BolumAdi='Endüstri Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='Türkçe',
#     WebAdresi='Endüstri-Mühendisliği'.lower()
# )
# bolum55 = Bolum(
#     BolumAdi='Endüstri Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='İngilizce',
#     WebAdresi='Endüstri-Mühendisliği'.lower()
# )
# bolum6 = Bolum(
#     BolumAdi='Ulaştırma Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='Türkçe',
#     WebAdresi='Ulaştırma-Mühendisliği'.lower()
# )
# bolum66 = Bolum(
#     BolumAdi='Ulaştırma Mühendisliği',
#     ProgramTuru='Lisans',
#     OgretimTuru='Birinci Öğretim',
#     OgrenimDili='İngilizce',
#     WebAdresi='Ulaştırma-Mühendisliği'.lower()
# )
# with app.app_context():
#     db.session.add_all(
#         [bolum1,bolum11,bolum2,bolum22,bolum3,bolum33,bolum4,bolum44,bolum5,bolum55,bolum6,bolum66])
#     db.session.commit()
#


# with app.app_context():
#     for i in range(1, 100):
#         if i % 2 == 0:  # ogrenci
#             fake = Faker('tr_TR')
#             id_k = fake.unique.random_number(digits=9)
#             zar = random.randint(1, 2)
#             profile = fake.simple_profile()
#
#             kullanici = Kullanici(
#                 KullaniciAdi=str(id_k),
#                 Parola=fake.password(),
#                 KullaniciTuru='Ogrenci'
#             )
#             db.session.add(kullanici)
#             db.session.commit()
#             durum = durum_.get(zar)
#             ayrilma_tarihi = None
#             if durum_.get(zar) == "Pasif":
#                 kayit_tarihi = datetime.today().date()  # Güncel tarih
#
#                 ayrilma_tarihi = fake.date_between(start_date=kayit_tarihi, end_date='today')
#
#             ogrenci = Ogrenci(
#                 BolumID=random.randint(1, 13),
#                 OgrenciNo=str(id_k),
#                 Durumu=durum,
#                 Adi=profile['name'],
#                 Soyadi=fake.last_name(),
#                 TCKimlikNo=''.join([str(random.randint(1, 9)) for _ in range(11)]),  # Rastgele 11 basamaklı TC Kimlik No
#                 Cinsiyet=sex.get(profile['sex']),
#                 DogumTarihi=profile['birthdate'],
#                 KullaniciID=kullanici.KullaniciID,
#                 AyrilmaTarihi=ayrilma_tarihi,
#             )
#             db.session.add(ogrenci)
#             db.session.commit()
#
#         elif i %5==0:  # ogretmen
#             fake = Faker('tr_TR')
#
#             profile = fake.simple_profile()
#
#             ogretim_kullanici = Kullanici(KullaniciAdi=str(fake.unique.random_number(digits=9)),
#                                           Parola=generate_password_hash(fake.password()),
#                                           KullaniciTuru='Ogretim Elemani')
#
#             db.session.add(ogretim_kullanici)
#             db.session.commit()
#             academic_titles = ['Doçent', 'Doktor','Profesör', 'Yrd. Doç. Dr.', 'Araştırma Görevlisi']
#
#             ogretim_elemani = OgretimElemani(
#                 BolumID=random.randint(1, 5),
#                 KurumSicilNo=ogretim_kullanici.KullaniciAdi,
#                 Unvan=fake.random_element(elements=academic_titles),
#                 Adi=fake.first_name(),
#                 Soyadi=fake.last_name(),
#                 TCKimlikNo=''.join([str(random.randint(1, 9)) for _ in range(11)]),
#                 Cinsiyet=fake.random_element(elements=('Erkek', 'Kadın')),
#                 DogumTarihi=fake.date_of_birth(minimum_age=30, maximum_age=60),
#                 KullaniciID=ogretim_kullanici.KullaniciID
#             )
#
#             db.session.add(ogretim_elemani)
#             db.session.commit()
#         else:
#             pass

with app.app_context():



    # Örnek Derslik verileri
    # derslik1 = Derslik(DerslikAdi='101', DerslikTuru='Amfi', Kapasite=100)
    # derslik2 = Derslik(DerslikAdi='202', DerslikTuru='Laboratuvar', Kapasite=30)
    # derslik3 = Derslik(DerslikAdi='303', DerslikTuru='Sınıf', Kapasite=50)
    #
    # derslikler = []
    #
    # for i in range(20):  # 3 adet derslik oluştur
    #     derslik = Derslik(
    #         DerslikAdi=fake.unique.random_number(digits=3),
    #         DerslikTuru=fake.random_element(elements=('Amfi', 'Laboratuvar', 'Sınıf')),
    #         Kapasite=random.randint(20, 100)  # Kapasiteyi 20 ile 100 arasında rastgele seç
    #     )
    #     derslikler.append(derslik)
    #
    # for derslik in derslikler:
    #     db.session.add(derslik)
    # #
    # db.session.commit()

    # sinavlar = []
    #
    # for ders_acma_id in range(1, 36):  # DersAcmaID'leri güncelleyin
    #     sinav_turu = random.choice(['Vize', 'Final'])  # Rastgele Vize ya da Final seçimi
    #     etki_orani = random.randint(20, 50)  # Rastgele etki oranı (20 ile 50 arasında)
    #     sinav_tarihi = date(2024, random.randint(1, 12), random.randint(1, 28))  # Rastgele tarih
    #     sinav_saati = f"{random.randint(8, 18)}:00:00"  # Rastgele saat (8 ile 18 arasında)
    #     derslik_id = random.randint(1, 20)  # DerslikID'leri güncelleyin
    #     ogr_elm_id = random.randint(1, 11)  # OgrElmID'leri güncelleyin
    #
    #
    #     sinav_saati= time(
    #             hour=random.randint(8, 18),
    #             minute=random.randint(0, 59),
    #             second=random.randint(0, 59)
    #         )
    #     sinav = Sinav(
    #         DersAcmaID=ders_acma_id,
    #         SinavTuru=sinav_turu,
    #         EtkiOrani=etki_orani,
    #         SinavTarihi=sinav_tarihi,
    #         SinavSaati=sinav_saati,
    #         DerslikID=derslik_id,
    #         OgrElmID=ogr_elm_id
    #     )
    #
    #     sinavlar.append(sinav)

    # ogrenci_sayisi = 51
    # sinav_sayisi = 35
    #
    # # Değerlendirme verilerini oluştur
    # degerlendirmeler = []
    #
    # for ogrenci_id in range(1, ogrenci_sayisi + 1):
    #     for sinav_id in range(1, sinav_sayisi + 1):
    #         sinav_notu = round(random.uniform(50.0, 100.0), 1)  # 50.0 ile 100.0 arasında rastgele bir not
    #
    #         degerlendirme = Degerlendirme(
    #             SinavID=sinav_id,
    #             OgrenciID=ogrenci_id,
    #             SinavNotu=sinav_notu
    #         )
    #
    #         degerlendirmeler.append(degerlendirme)

    # Öğrenci ve öğretim elemanı sayılarını belirleyin
    # ders_acma_sayisi = 35
    # derslik_sayisi = 20
    # ders_gunleri = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']
    #
    # # Rastgele ders programları oluştur
    # ders_programlari = []
    #
    # for ders_acma_id in range(1, ders_acma_sayisi + 1):
    #     derslik_id = random.randint(1, derslik_sayisi)
    #     ders_gunu = random.choice(ders_gunleri)
    #     ders_saati = random.randint(9, 17)  # 1 ile 5 arasında rastgele bir saat
    #
    #     ders_programi = DersProgrami(
    #         DersAcmaID=ders_acma_id,
    #         DerslikID=derslik_id,
    #         DersGunu=ders_gunu,
    #         DersSaati=ders_saati
    #     )
    #
    #     ders_programlari.append(ders_programi)
    # ogrenci_sayisi = 51
    # ogretim_elemani_sayisi = 11
    #
    # # Öğrenci ve öğretim elemanı kimlik numaralarını oluştur
    # ogrenci_ids = list(range(1, ogrenci_sayisi + 1))
    # ogretim_elemani_ids = list(range(1, ogretim_elemani_sayisi + 1))
    #
    # # Danışmanlık verilerini oluştur
    # danismanliklar = []
    #
    # for ogrenci_id in ogrenci_ids:
    #     # Her öğrenciye bir danışman atamak için rastgele bir öğretim elemanı seç
    #     danisman_id = random.choice(ogretim_elemani_ids)
    #
    #     danismanlik = Danismanlik(OgrElmID=danisman_id, OgrenciID=ogrenci_id)
    #     danismanliklar.append(danismanlik)
    #
    # for mufredat in danismanliklar:
    #     db.session.add(mufredat)
    #
    # db.session.commit()
    # result = db.session.query(OgretimElemani, func.count(Mufredat.DersID).label('ToplamDersSayisi')) \
    #     .join(Mufredat, Mufredat.BolumID == OgretimElemani.BolumID) \
    #     .group_by(OgretimElemani.OgrElmID) \
    #     .order_by(func.count(Mufredat.DersID).desc()) \
    #     .first()
    # print(result)
    # ders_programlari = db.session.query(
    #     DersHavuzu.DersKodu,
    #     DersHavuzu.DersAdi,
    #     DersHavuzu.Teorik,
    #     DersHavuzu.Uygulama,
    #     DersProgrami.DersGunu,
    #     DersProgrami.DersSaati,
    #     Derslik.DerslikAdi,
    #     Bolum.BolumAdi
    # ).join(
    #     Mufredat, DersHavuzu.DersID == Mufredat.DersID
    # ).join(
    #     DersAcma, DersAcma.MufredatID == Mufredat.MufredatID  # Adjusted join condition
    # ).join(
    #     DersProgrami, DersAcma.DersAcmaID == DersProgrami.DersAcmaID
    # ).join(
    #     Derslik, DersProgrami.DerslikID == Derslik.DerslikID
    # ).join(
    #     OgretimElemani, DersAcma.OgrElmID == OgretimElemani.OgrElmID
    # ).join(
    #     Bolum, OgretimElemani.BolumID == Bolum.BolumID
    # ).filter(
    #     OgretimElemani.OgrElmID == "11"
    # ).all()
    #
    # print(ders_programlari)
    # courses_taught = (
    #     db.session.query(DersAcma, DersHavuzu)
    #     .join(Mufredat, DersAcma.MufredatID == Mufredat.MufredatID)
    #     .join(DersHavuzu, Mufredat.DersID == DersHavuzu.DersID)
    #     .filter(DersAcma.OgrElmID == 11)
    #     .all()
    # )

    # exams_info = (
    #     db.session.query(Sinav, DersAcma, Ogrenci, DersHavuzu)
    #     .join(DersAcma, Sinav.DersAcmaID == DersAcma.DersAcmaID)
    #     .join(OgretimElemani, DersAcma.OgrElmID == OgretimElemani.OgrElmID)
    #     .join(Mufredat, DersAcma.MufredatID == Mufredat.MufredatID)
    #     .join(DersHavuzu, Mufredat.DersID == DersHavuzu.DersID)
    #     .filter(OgretimElemani.OgrElmID == 2)
    #     .all()
    # )
    # print(exams_info)
    from sqlalchemy.orm import aliased


    # Assuming that you have an instance of Flask SQLAlchemy named 'db'
    # Assuming you have established the relationship between Sinav and OgretimElemani using OgrElmID
    # You can adjust this according to your actual relationships

    # Get the exams given by the academic staff during the active semester
    active_semester_exams = (
        db.session.query(
            Sinav.SinavID,
            Bolum.BolumAdi,
            DersHavuzu.DersKodu,
            DersHavuzu.DersAdi,
            Sinav.SinavTuru,
            Sinav.SinavTarihi,
            Sinav.SinavSaati,
            Sinav.DerslikID


        )
        .join(OgretimElemani, Bolum.BolumID == OgretimElemani.BolumID)
        .join(DersAcma, OgretimElemani.OgrElmID == DersAcma.OgrElmID)
        .join(Sinav, DersAcma.DersAcmaID == Sinav.DersAcmaID)
        .join(Mufredat, DersAcma.MufredatID == Mufredat.MufredatID)
        .join(DersHavuzu, Mufredat.DersID == DersHavuzu.DersID)
        .filter(
            OgretimElemani.BolumID == 3,
            DersAcma.AkademikYil == '2024-2025',  # Adjust the academic year as needed
        )
        .order_by(desc(Sinav.SinavTarihi), desc(Sinav.SinavSaati))  # Order by exam date and time in descending order
        .all()
    )

    # Print the results
    for result in active_semester_exams:
        print(
            f"Sinav id = {result.SinavID}Department: {result.BolumAdi}, Course Code: {result.DersKodu}, Course Name: {result.DersAdi}, Exam Type: {result.SinavTuru} Sınav tarihi: {result.SinavTarihi},Sınav tarihi: {result.SinavSaati}, Derslik: {result.DerslikID}",
        )
    # Prepare a dictionary to store course and student information

    # course_student_info = {}
    #
    # for course, ders_havuzu in courses_taught:
    #     print(course)
    #     # Retrieve the list of students registered for each course
    #     students_registered = (
    #         db.session.query(Ogrenci, DersAlma)
    #         .join(DersAlma, Ogrenci.OgrenciID == DersAlma.OgrenciID)
    #         .filter(DersAlma.DersAcmaID == course.DersAcmaID)
    #         .all()
    #     )
    #
    #     # Store course and student information in the dictionary
    #     course_student_info[course] = {
    #         'DersKodu': ders_havuzu.DersKodu,
    #         'DersAdi': ders_havuzu.DersAdi,
    #         'DersTuru': ders_havuzu.DersTuru,
    #         'Teorik': ders_havuzu.Teorik,
    #         'Uygulama': ders_havuzu.Uygulama,
    #         'Kredi': ders_havuzu.Kredi,
    #         'ECTS': ders_havuzu.ECTS,
    #         'students': students_registered
    #     }
    #
    # print(course_student_info)
    #
    # if result:
    #     ogretim_elemani = result.OgretimElemani
    #     print(ogretim_elemani.BolumID)
    #     kullanici = Kullanici.query.get(ogretim_elemani.KullaniciID)
    #
    #     if kullanici:
    #         print(kullanici.KullaniciID, kullanici.Parola)
    # if ogretim_elemani:

    # course_info = db.session.query(
    #     DersHavuzu.DersKodu,
    #     DersHavuzu.DersAdi,
    #     DersHavuzu.DersTuru,
    #     Mufredat.DersDonemi,
    #     DersHavuzu.Teorik,
    #     DersHavuzu.Uygulama,
    #     DersHavuzu.Kredi,
    #     DersHavuzu.ECTS,
    #     Mufredat.AkademikYil
    # ).join(
    #     Mufredat,
    #     DersHavuzu.DersID == Mufredat.DersID
    # ).filter(
    #     # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
    # ).all()
    # print()





    #     kullanici = Kullanici.query.get(ogretim_elemani.KullaniciID)
    #     if kullanici:
    #         print(kullanici.KullaniciID, kullanici.Parola)
    # fake = Faker()
    # #
    # ogrenci_sayisi = 45
    # ders_acma_sayisi = 35
    #
    # # Durumlar
    # durumlar = ['Basarili', 'Devamsiz', 'Basarisiz']
    #
    # # Ders alma verilerini oluştur
    # ders_alma_listesi = []
    #
    # for ogrenci_id in range(1, ogrenci_sayisi + 1):
    #     for ders_acma_id in range(1, ders_acma_sayisi + 1):
    #         durum = random.choice(durumlar)
    #
    #         ders_alma = DersAlma(
    #             DersAcmaID=ders_acma_id,
    #             OgrenciID=ogrenci_id,
    #             Durum=durum
    #         )
    #
    #         ders_alma_listesi.append(ders_alma)
    #
    # for mufredat in ders_alma_listesi:
    #     db.session.add(mufredat)
    #
    # db.session.commit()
    # ders_acmalar = []
    #
    # for mufredat_id in range(1, 35 + 1):
    #     akademik_yil = fake.random_element(elements=['2023-2024', '2024-2025', '2025-2026'])
    #     akademik_donem = random.choice(['Guz', 'Bahar'])
    #     kontenjan = random.randint(20, 50)
    #     ogr_elm_id = random.randint(1, 11)  # Öğretim elemanı ID'leri
    #
    #     ders_acma = DersAcma(
    #         AkademikYil=akademik_yil,
    #         AkademikDonem=akademik_donem,
    #         MufredatID=mufredat_id,
    #         Kontenjan=kontenjan,
    #         OgrElmID=ogr_elm_id
    #     )
    #
    #     ders_acmalar.append(ders_acma)
    # for mufredat in ders_acmalar:
    #     db.session.add(mufredat)
    #
    # db.session.commit()



    # ders_havuzlari = []
    #
    # for i in range(35):  # 3 adet ders havuzu oluştur
    #     t = random.randint(2, 5)
    #     u = random.randint(1, 3)
    #     ders_havuzu = DersHavuzu(
    #         DersKodu=fake.unique.random_number(digits=6),
    #         DersAdi=fake.random_element(elements= ['Bilgisayar Mimarisi', 'Elektrik Devre Analizi', 'Makine Elementleri', 'Termodinamik', 'Bilgisayar Ağları', 'Yapay Zeka', 'Robotik']),
    #         DersDili=fake.random_element(elements=('Turkce', 'Ingilizce')),
    #         DersSeviyesi=fake.random_element(elements=('Ilk Yil', 'Ikinci Yil', 'Ucuncu Yil')),
    #         DersTuru=fake.random_element(elements=('Zorunlu', 'Secmeli')),
    #         Teorik=t,
    #         Uygulama=u,
    #         Kredi=t+int(u/2),  # 3.0 ile 6.0 arasında rastgele ondalıklı sayı
    #         ECTS=random.randint(4, 8)
    #     )
    #     ders_havuzlari.append(ders_havuzu)
    #
    # mufredatlar = []
    # bolum_sayisi = 12
    # ders_sayisi = 35
    #
    # for ders_havuzu in ders_havuzlari:
    #     mufredat = Mufredat(
    #         BolumID=random.randint(1,bolum_sayisi),
    #         DersID=random.randint(1,ders_sayisi),
    #         AkademikYil=fake.random_element(elements=['2023-2024', '2024-2025', '2025-2026']),
    #         AkademikDonem=fake.random_element(elements=['Guz', 'Bahar']),
    #         DersDonemi=random.randint(1, 8)  # Ders donemi 1 veya 2 olabilir
    #     )
    #     mufredatlar.append(mufredat)
    #
    # for mufredat in mufredatlar:
    #     db.session.add(mufredat)
    # # Bölüm sayısını ve ders sayısını güncelleyebilirsiniz
    #
    # db.session.commit()
    # k_adi=101
    #
    # ogretim_kullanici = Kullanici(KullaniciAdi=str(k_adi),
    #                                           Parola="101",
    #                                           KullaniciTuru='Ogretim Elemani')
    #
    # db.session.add(ogretim_kullanici)
    # db.session.commit()
    #
    # academic_titles = ['Doçent', 'Doktor','Profesör', 'Yrd. Doç. Dr.', 'Araştırma Görevlisi']
    #
    # ogretim_elemani = OgretimElemani(
    #     BolumID=random.randint(1, 5),
    #     KurumSicilNo=ogretim_kullanici.KullaniciAdi,
    #     Unvan=fake.random_element(elements=academic_titles),
    #     Adi=fake.first_name(),
    #     Soyadi=fake.last_name(),
    #     TCKimlikNo=''.join([str(random.randint(1, 9)) for _ in range(11)]),
    #     Cinsiyet=fake.random_element(elements=('Erkek', 'Kadın')),
    #     DogumTarihi=fake.date_of_birth(minimum_age=30, maximum_age=60),
    #     KullaniciID=ogretim_kullanici.KullaniciID
    # )
    #
    # db.session.add(ogretim_elemani)
    # db.session.commit()