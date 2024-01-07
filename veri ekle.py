# Öğrenci ID'si varsayılan olarak 1 olarak kabul edilmiştir. Gerçek projede bu değeri ilgili öğrencinin ID'siyle değiştirmelisiniz.
from models import db, Mufredat, Ogrenci, DersHavuzu, Kullanici, DersAcma
from views import app


def get_active_student_courses(student_id):
    # Get the current academic year and semester
    current_academic_year = "2024-2025"  # You may need to dynamically calculate this based on the current date
    current_academic_semester = "Guz"  # You may need to dynamically calculate this based on the current date

    # Query the database to find the active student's enrolled program
    active_student = Ogrenci.query.filter_by(OgrenciID=student_id, Durumu="Aktif").first()

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




with app.app_context():
    ogrenci_id = 4
    # Example usage:
    available_courses = get_active_student_courses(ogrenci_id)

    for course in available_courses:
        print(f"AkademikYil: {course.AkademikYil}, DersAcmaID:{course.DersAcmaID},AkademikDonem:{course.AkademikDonem},MufredatID:{course.MufredatID},Kontenjan:{course.Kontenjan}, OgrElmID:{course.OgrElmID}")
    from datetime import date

