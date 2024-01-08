# Öğrenci ID'si varsayılan olarak 1 olarak kabul edilmiştir. Gerçek projede bu değeri ilgili öğrencinin ID'siyle değiştirmelisiniz.
from sqlalchemy import asc

from models import db, Mufredat, Ogrenci, DersHavuzu, Kullanici, DersAcma, OgretimElemani, DersAlma, Degerlendirme, \
    Sinav
from views import app

def get_grade_info(numeric_grade):
    if numeric_grade >= 90:
        return 'A', 4.0
    elif numeric_grade >= 85:
        return 'A-', 3.7
    elif numeric_grade >= 80:
        return 'B+', 3.3
    elif numeric_grade >= 75:
        return 'B', 3.0
    elif numeric_grade >= 70:
        return 'B-', 2.7
    elif numeric_grade >= 65:
        return 'C+', 2.3
    elif numeric_grade >= 60:
        return 'C', 2.0
    elif numeric_grade >= 55:
        return 'C-', 1.7
    elif numeric_grade >= 50:
        return 'D', 1.0
    else:
        return 'F', 0.0

def calculate_gano(result_dict):
    semesters_gano = {}
    total_ects = 0
    total_weighted_grade = 0

    for key, value in result_dict.items():
        semester_key = (value['AkademikYil'], value['AkademikDonem'])
        ects = value['DersECTS']
        numeric_grade = value['DortlukNot']

        total_ects += ects
        total_weighted_grade += ects * numeric_grade

        if semester_key not in semesters_gano:
            semesters_gano[semester_key] = {
                'TotalECTS': total_ects,
                'WeightedGrade': total_weighted_grade,
                'GANO': total_weighted_grade / total_ects if total_ects > 0 else 0
            }

    # Add GANO to the result_dict
    for key, value in result_dict.items():
        semester_key = (value['AkademikYil'], value['AkademikDonem'])
        value['GANO'] = semesters_gano[semester_key]['GANO']

    return result_dict


def transkript_bilgisi_al(ogrenci_id):
    """
    Öğrenci Bilgileri (Adı, soyadı, kurumsal bilgileri)
 Dersin Kodu ve Adı
 Dersin Türü (Seçmeli, Zorunlu)
 Teorik (T), Uygulama (U), Kredi (K) ve ECTS
 Dörtlük Not Sistemi ve Harf Notu
 GANO (Genel Akademik Not Ortalaması)

    :param ogrenci_id:
    :return:
    """
    result_dictionary = {}
    degerlendirme_bilgileri = Degerlendirme.query.filter_by(OgrenciID=ogrenci_id).all()
    for degerlendirme in degerlendirme_bilgileri:
        sinav_id = degerlendirme.SinavID
        sinav_notu = degerlendirme.SinavNotu

        harf_notu, dortluk_not = get_grade_info(sinav_notu)

        sinav_bilgileri = Sinav.query.filter_by(SinavID=sinav_id).all()

        for sinav in sinav_bilgileri:
            ders_acma_id = sinav.DersAcmaID

            ders_Acma_bilgileri = DersAcma.query.filter_by(DersAcmaID=ders_acma_id).first()
            # müfredat_bilgileri = Mufredat.query.filter_by(MufredatID=ders_Acma_bilgileri.DersAcmaID).all()
            müfredat_bilgileri = Mufredat.query.filter_by(MufredatID=ders_Acma_bilgileri.DersAcmaID).order_by(
                asc(Mufredat.DersDonemi)).all()

            for müfredat in müfredat_bilgileri:
                müfredat_id = müfredat.MufredatID
                ders_id = müfredat.DersID
                bolum_id = müfredat.BolumID
                akademik_yil = müfredat.AkademikYil
                akademik_donem = müfredat.AkademikDonem
                ders_donemi = müfredat.DersDonemi

                ders_havuzu_bilgileri = DersHavuzu.query.filter_by(DersID=ders_id).first()

                ders_kodu = ders_havuzu_bilgileri.DersKodu
                ders_adi = ders_havuzu_bilgileri.DersAdi
                ders_dili = ders_havuzu_bilgileri.DersDili
                ders_seviyesi = ders_havuzu_bilgileri.DersSeviyesi
                ders_teorik = ders_havuzu_bilgileri.Teorik
                ders_uygulama = ders_havuzu_bilgileri.Uygulama
                ders_turu = ders_havuzu_bilgileri.DersTuru
                ders_kredi = ders_havuzu_bilgileri.Kredi
                ders_ects = ders_havuzu_bilgileri.ECTS

                print(f"Sinav ID: {sinav_id}, Sinav Notu: {sinav_notu}")
                print(f"Harf Notu: {harf_notu}, Dörtlük Not: {dortluk_not}")
                print(f"Ders Acma ID: {ders_acma_id}")
                print(f"Mufredat ID: {müfredat_id}, Ders ID: {ders_id}, Bolum ID: {bolum_id}")
                print(f"Akademik Yil: {akademik_yil}, Akademik Donem: {akademik_donem}, Ders Donemi: {ders_donemi}")
                print(f"Ders Kodu: {ders_kodu}, Ders Adi: {ders_adi}")
                print(f"Ders Dili: {ders_dili}, Ders Seviyesi: {ders_seviyesi}")
                print(f"Ders Teorik: {ders_teorik}, Ders Uygulama: {ders_uygulama}")
                print(f"Ders Turu: {ders_turu}, Ders Kredi: {ders_kredi}, Ders ECTS: {ders_ects}")
                print("\n")

                result_dictionary[sinav_id] = {
                    'SinavID': sinav_id,
                    'SinavNotu': sinav_notu,
                    'HarfNotu': harf_notu,
                    'DortlukNot': dortluk_not,
                    'DersAcmaID': ders_acma_id,
                    'MufredatID': müfredat_id,
                    'DersID': ders_id,
                    'BolumID': bolum_id,
                    'AkademikYil': akademik_yil,
                    'AkademikDonem': akademik_donem,
                    'DersDonemi': ders_donemi,
                    'DersKodu': ders_kodu,
                    'DersAdi': ders_adi,
                    'DersDili': ders_dili,
                    'DersSeviyesi': ders_seviyesi,
                    'DersTeorik': ders_teorik,
                    'DersUygulama': ders_uygulama,
                    'DersTuru': ders_turu,
                    'DersKredi': ders_kredi,
                    'DersECTS': ders_ects
                }

    result_dictionary = calculate_gano(result_dictionary)

    return result_dictionary


#
with app.app_context():
    result_dictionary = transkript_bilgisi_al(4)
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    import pandas as pd

    # Assuming `result_dictionary` is defined as in your code

    # Convert result dictionary to DataFrame
    df = pd.DataFrame.from_dict(result_dictionary, orient='index')

    # Create a table for the transcript
    transcript_table = pd.DataFrame({
        'Ders Kodu': df['DersKodu'],
        'Ders Adı': df['DersAdi'],
        'Kredi': df['DersKredi'],
        'Not': df['SinavNotu'],
        'Harf': df['HarfNotu'],
        'Ders Donemi': df['DersDonemi']
    })

    # Create a table for the general information
    general_info_table = pd.DataFrame({
        'T.C.': ['Bandırma Onyedi Eylül Üniversitesi'],
        'Adı Soyadı': ['HALİL UMUT YALÇIN'],
        'T.C. Kimlik No': ['39100692594'],
        'Öğrenci No': ['201505018'],
        'Bölüm / Program': ['Yazılım Mühendisliği'],
        'GNO': ['2,69'],  # Replace with the actual GNO
        'ANO': ['2,69'],  # Replace with the actual ANO
        # Add other information fields as needed
    })

    # Group transcript table by semester
    grouped_transcript = transcript_table.groupby('Ders Donemi')

    # Create a PDF file
    pdf = canvas.Canvas('combined_info.pdf', pagesize=letter)
    for semester, group_df in grouped_transcript:
        combined_df = pd.concat([general_info_table, group_df], axis=1)

        # Draw the table on the PDF
        combined_df = combined_df.reset_index(drop=True)
        pdf.drawTable(combined_df.values, x=50, y=500)

        # Start a new page for the next semester
        pdf.showPage()

    # Save the PDF file
    pdf.save()

    # The 'combined_info.pdf' file will now contain information for each semester in a tabular format.

