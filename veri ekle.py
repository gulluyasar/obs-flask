# Öğrenci ID'si varsayılan olarak 1 olarak kabul edilmiştir. Gerçek projede bu değeri ilgili öğrencinin ID'siyle değiştirmelisiniz.
from models import db, Mufredat, Ogrenci, DersHavuzu, Kullanici, DersAcma, OgretimElemani
from views import app




def get_active_student_courses(student_id):
    current_academic_year = "2024-2025"
    current_academic_semester = "Guz"
    active_student = Ogrenci.query.filter_by(OgrenciID=student_id, Durumu="Aktif").first()

    #from datetime import date
    if active_student:
        # Query the database to find the curriculum (mufredat) for the active student's program
        curriculum = Mufredat.query.filter_by(BolumID=active_student.BolumID).first()
        curriculum
        if curriculum:
            # Query the database to find the courses in the current academic year and semester
            active_student_courses = DersAcma.query.join(Mufredat).filter(
                Mufredat.MufredatID == curriculum.MufredatID,
                DersAcma.AkademikYil == current_academic_year,
                DersAcma.AkademikDonem == current_academic_semester
            ).all()

            return active_student_courses

    return []
    from datetime import date
with app.app_context():
        ogrenci_id = 2

        # Example usage:
        available_courses = get_active_student_courses(ogrenci_id)

        for course in available_courses:
            mufredat = Mufredat.query.filter_by(MufredatID=course.MufredatID).first()
            ogretmen = OgretimElemani.query.filter_by(OgrElmID=course.OgrElmID).first()
            ders = DersHavuzu.query.filter_by(DersID=mufredat.DersID).first()

            print(f"AkademikYil: {course.AkademikYil},\n "
                  f"DersAcmaID:{course.DersAcmaID},\n"
                  f"AkademikDonem:{course.AkademikDonem},\n"
                  f"MufredatID:{course.MufredatID},\n"
                  f"Kontenjan:{course.Kontenjan},\n "
                  f"OgrElmID:{course.OgrElmID}\n",
                  "---- Diğer Bilgiler -----\n"
                  f"Dersin Kodu:{ders.DersKodu}\n",
                  f"Dersin Adı:{ders.DersAdi}\n",
                  f"Dersin Türü:{ders.DersTuru}\n",
                  f"Teorik:{ders.Teorik}\n",
                  f"Uygulama:{ders.Uygulama}\n",
                  f"Kredi:{ders.Kredi}\n",
                  f"ECTS:{ders.ECTS}\n",

                  f"OgrAdi:{ogretmen.Unvan} {ogretmen.Adi} {ogretmen.Soyadi}\n",
                  "***********************"
                  )

            # for döngüsünün üzerinde boş liste açıp yukarıdaki bilgileri liste içine ekleyebilirsin. bu listeyi de view e gönderip ekranda liste[i][0] gibi indisler ile ekranda gösterebilirsin
            # ben bir kaç öğrencide denedim genelliği boş 4 olan id de sadece 1 çıktı geliyor

