from datetime import datetime

import jwt
from flask import Flask, render_template, redirect, url_for, request, Blueprint
from sqlalchemy.orm import aliased

from views import app

from models import Ogrenci, OgretimElemani, Mufredat, db, DersHavuzu, Bolum, DersProgrami, DersAcma, Derslik, DersAlma, \
    Kullanici
from required import redirect_user

ders_islemleri_blueprint = Blueprint('ders-islemleri', __name__, template_folder='templates')


@ders_islemleri_blueprint.route('/mufredat_goruntule', methods=['GET', 'POST'])
def mufredat_goruntule():
    token = request.args.get('token')
    if request.method == 'GET':
        if token:
            try:
                decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
                user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()

                if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                    # selected_akademik_yil = request.form.get('filterAkademikYil')
                    # Öğretim elemanının kayıtlı olduğu bölümdeki müfredat derslerini al
                    course_info = db.session.query(
                        DersHavuzu.DersKodu,
                        DersHavuzu.DersAdi,
                        DersHavuzu.DersTuru,
                        Mufredat.DersDonemi,
                        DersHavuzu.Teorik,
                        DersHavuzu.Uygulama,
                        DersHavuzu.Kredi,
                        DersHavuzu.ECTS,
                        Mufredat.AkademikYil
                    ).join(
                        Mufredat,
                        DersHavuzu.DersID == Mufredat.DersID,
                    ).filter(
                        Mufredat.BolumID == user.BolumID,
                        # Mufredat.AkademikYil == selected_akademik_yil
                        # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
                    ).all()

                    return render_template('ders_islemleri/mufredat_goruntule.html', user=user, token=token,
                                           decoded_token=decoded_token, bolum_mufredat=course_info)
                else:
                    return redirect(url_for('giris-ekrani.login'))
            except jwt.ExpiredSignatureError:
                # Token süresi dolmuş
                return redirect(url_for('giris-ekrani.login'))
            except jwt.InvalidTokenError:
                # Geçersiz token
                return redirect(url_for('giris-ekrani.login'))
        else:
            return redirect(url_for('giris-ekrani.login'))
    if request.method == 'POST':
        if token:
            try:
                decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
                user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()

                if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):

                    selected_akademik_yil = request.form.get('filterAkademikYil')
                    if selected_akademik_yil == 'all':

                        course_info = db.session.query(
                            DersHavuzu.DersKodu,
                            DersHavuzu.DersAdi,
                            DersHavuzu.DersTuru,
                            Mufredat.DersDonemi,
                            DersHavuzu.Teorik,
                            DersHavuzu.Uygulama,
                            DersHavuzu.Kredi,
                            DersHavuzu.ECTS,
                            Mufredat.AkademikYil
                        ).join(
                            Mufredat,
                            DersHavuzu.DersID == Mufredat.DersID
                        ).filter(
                            Mufredat.BolumID == user.BolumID,  # ogretmene ozel olması için

                        ).all()

                        return render_template('ders_islemleri/mufredat_goruntule.html', user=user, token=token,
                                               decoded_token=decoded_token, bolum_mufredat=course_info)
                    else:

                        course_info = db.session.query(
                            DersHavuzu.DersKodu,
                            DersHavuzu.DersAdi,
                            DersHavuzu.DersTuru,
                            Mufredat.DersDonemi,
                            DersHavuzu.Teorik,
                            DersHavuzu.Uygulama,
                            DersHavuzu.Kredi,
                            DersHavuzu.ECTS,
                            Mufredat.AkademikYil
                        ).join(
                            Mufredat,
                            DersHavuzu.DersID == Mufredat.DersID
                        ).filter(
                            Mufredat.BolumID == user.BolumID,
                            Mufredat.AkademikYil == selected_akademik_yil
                            # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
                        ).all()

                        return render_template('ders_islemleri/mufredat_goruntule.html', user=user, token=token,
                                               decoded_token=decoded_token, bolum_mufredat=course_info)

                    # return render_template('ders_islemleri/mufredat_goruntule.html', user=user, token=token, decoded_token=decoded_token, bolum_mufredat=bolum_mufredat)
                else:
                    return redirect(url_for('giris-ekrani.login'))
            except jwt.ExpiredSignatureError:
                # Token süresi dolmuş
                return redirect(url_for('giris-ekrani.login'))
            except jwt.InvalidTokenError:
                # Geçersiz token
                return redirect(url_for('giris-ekrani.login'))
        else:
            return redirect(url_for('giris-ekrani.login'))
@ders_islemleri_blueprint.route('/ogrenci_mufredat_goruntule', methods=['GET', 'POST'])
def ogrenci_mufredat_goruntule():
    token = request.args.get('token')
    if request.method == 'GET':
        if token:
            try:
                decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
                user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()

                if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                    # selected_akademik_yil = request.form.get('filterAkademikYil')
                    # Öğrencinin kayıtlı olduğu bölümdeki müfredat derslerini al
                    course_info = db.session.query(
                        DersHavuzu.DersKodu,
                        DersHavuzu.DersAdi,
                        DersHavuzu.DersTuru,
                        Mufredat.DersDonemi,
                        DersHavuzu.Teorik,
                        DersHavuzu.Uygulama,
                        DersHavuzu.Kredi,
                        DersHavuzu.ECTS,
                        Mufredat.AkademikYil
                    ).join(
                        Mufredat,
                        DersHavuzu.DersID == Mufredat.DersID,
                    ).filter(
                        Mufredat.BolumID == user.BolumID,
                        # Mufredat.AkademikYil == selected_akademik_yil
                        # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
                    ).all()
                    ogrenci_id = user.OgrenciID
                    mufredat = Mufredat.query \
                        .join(Ogrenci, Ogrenci.BolumID == Mufredat.BolumID) \
                        .filter(Ogrenci.OgrenciID == ogrenci_id) \
                        .add_columns(Mufredat.AkademikYil.label("AkademikYil")) \
                        .first()
                    akademik_yil_filtre = mufredat.AkademikYil







                    return render_template('ders_islemleri/ogrenci_mufredat_goruntule.html', user=user, token=token,
                                           decoded_token=decoded_token, bolum_mufredat=course_info, akademik = akademik_yil_filtre)
                else:
                    return redirect(url_for('giris-ekrani.login'))
            except jwt.ExpiredSignatureError:
                # Token süresi dolmuş
                return redirect(url_for('giris-ekrani.login'))
            except jwt.InvalidTokenError:
                # Geçersiz token
                return redirect(url_for('giris-ekrani.login'))
        else:
            return redirect(url_for('giris-ekrani.login'))
    if request.method == 'POST':
        if token:
            try:
                decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
                user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()

                if redirect_user(decoded_token.get('user_type'), 'ogrenci'):

                    selected_akademik_yil = request.form.get('filterAkademikYil')
                    if selected_akademik_yil == 'all':

                        course_info = db.session.query(
                            DersHavuzu.DersKodu,
                            DersHavuzu.DersAdi,
                            DersHavuzu.DersTuru,
                            Mufredat.DersDonemi,
                            DersHavuzu.Teorik,
                            DersHavuzu.Uygulama,
                            DersHavuzu.Kredi,
                            DersHavuzu.ECTS,
                            Mufredat.AkademikYil
                        ).join(
                            Mufredat,
                            DersHavuzu.DersID == Mufredat.DersID
                        ).filter(
                            Mufredat.BolumID == user.BolumID,  # ?ogretmene ozel olması için?

                        ).all()

                        return render_template('ders_islemleri/ogrenci_mufredat_goruntule.html', user=user, token=token,
                                               decoded_token=decoded_token, bolum_mufredat=course_info)
                    else:

                        course_info = db.session.query(
                            DersHavuzu.DersKodu,
                            DersHavuzu.DersAdi,
                            DersHavuzu.DersTuru,
                            Mufredat.DersDonemi,
                            DersHavuzu.Teorik,
                            DersHavuzu.Uygulama,
                            DersHavuzu.Kredi,
                            DersHavuzu.ECTS,
                            Mufredat.AkademikYil
                        ).join(
                            Mufredat,
                            DersHavuzu.DersID == Mufredat.DersID
                        ).filter(
                            Mufredat.BolumID == user.BolumID,
                            Mufredat.AkademikYil == selected_akademik_yil
                            # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
                        ).all()

                        return render_template('ders_islemleri/ogrenci_mufredat_goruntule.html', user=user, token=token,
                                               decoded_token=decoded_token, bolum_mufredat=course_info)

                    # return render_template('ders_islemleri/mufredat_goruntule.html', user=user, token=token, decoded_token=decoded_token, bolum_mufredat=bolum_mufredat)
                else:
                    return redirect(url_for('giris-ekrani.login'))
            except jwt.ExpiredSignatureError:
                # Token süresi dolmuş
                return redirect(url_for('giris-ekrani.login'))
            except jwt.InvalidTokenError:
                # Geçersiz token
                return redirect(url_for('giris-ekrani.login'))
        else:
            return redirect(url_for('giris-ekrani.login'))

@ders_islemleri_blueprint.route('/ogretmen_donem_dersler_goruntule')
def donem_dersler_goruntule():
    token = request.args.get('token')
    if token:
        try:

            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"
            print(donem)

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # selected_akademik_yil = request.form.get('filterAkademikYil')
                # Öğretim elemanının kayıtlı olduğu bölümdeki müfredat derslerini al

                course_info = db.session.query(
                    DersHavuzu.DersKodu,
                    DersHavuzu.DersAdi,
                    DersHavuzu.DersTuru,
                    Mufredat.DersDonemi,
                    DersHavuzu.Teorik,
                    DersHavuzu.Uygulama,
                    DersHavuzu.Kredi,
                    DersHavuzu.ECTS,
                    Mufredat.AkademikYil
                ).join(
                    Mufredat,
                    DersHavuzu.DersID == Mufredat.DersID,
                ).filter(
                    Mufredat.BolumID == user.BolumID,
                    Mufredat.AkademikYil == donem
                    # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
                ).all()
                print(course_info)
                bolum = Bolum.query.filter_by(BolumID=user.BolumID).first()
                bolum_adi = bolum.BolumAdi
                print()

                return render_template('ders_islemleri/ogretmen_donem_dersler_goruntule.html', user=user, token=token,
                                       decoded_token=decoded_token, bolum_mufredat=course_info, bolum_adi=bolum_adi)
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))

@ders_islemleri_blueprint.route('/ogrenci_donem_dersler_goruntule')
def ogrenci_donem_dersler_goruntule():
    token = request.args.get('token')
    if token:
        try:

            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"
            print(donem)

            if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                # selected_akademik_yil = request.form.get('filterAkademikYil')
                # Öğrencinin kayıtlı olduğu bölümdeki müfredat derslerini al


                course_info = db.session.query(
                    DersHavuzu.DersKodu,
                    DersHavuzu.DersAdi,
                    DersHavuzu.DersTuru,
                    Mufredat.DersDonemi,
                    DersHavuzu.Teorik,
                    DersHavuzu.Uygulama,
                    DersHavuzu.Kredi,
                    DersHavuzu.ECTS,
                    Mufredat.AkademikYil
                ).join(
                    Mufredat,
                    DersHavuzu.DersID == Mufredat.DersID,
                ).filter(
                    Mufredat.BolumID == user.BolumID,
                    Mufredat.AkademikYil == donem
                    # Add conditions if needed, e.g., filtering by BolumID or AkademikYil
                ).all()
                print(course_info)
                bolum = Bolum.query.filter_by(BolumID=user.BolumID).first()
                bolum_adi = bolum.BolumAdi
                ogrenci = Ogrenci.query.get(user.OgrenciID)
                ders_alma_query = (
                    db.session.query(DersAlma, DersAcma, OgretimElemani)
                    .join(DersAcma, DersAlma.DersAcmaID == DersAcma.DersAcmaID)
                    .join(OgretimElemani, DersAcma.OgrElmID == OgretimElemani.OgrElmID)
                    .filter(DersAlma.OgrenciID == user.OgrenciID)
                    .add_columns(OgretimElemani.Adi.label("OgretmenAdi")) \
                        .add_columns(OgretimElemani.Soyadi.label("OgretmenSoyadi")) \
                        .add_columns(OgretimElemani.Unvan.label("OgretmenUnvani")) \
                        .first()

                )
                ogretmen_adi = ders_alma_query.OgretmenAdi
                ogretmen_soyadi = ders_alma_query.OgretmenSoyadi
                ogretmen_unvan = ders_alma_query.OgretmenUnvani




                return render_template('ders_islemleri/ogrenci_donem_dersler_goruntule.html', user=user, token=token,
                                       decoded_token=decoded_token, bolum_mufredat=course_info, bolum_adi=bolum_adi, adi=ogretmen_adi, soyadi=ogretmen_soyadi, unvan= ogretmen_unvan)
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))

@ders_islemleri_blueprint.route('/ogretmen_ders_programi')
def ogretmen_ders_programi():
    token = request.args.get('token')
    if token:
        try:

            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

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
                #     OgretimElemani.OgrElmID == user.OgrElmID
                # ).all()
                # yeni sorgu aşağıda
                ders_programlari = db.session.query(
                    DersHavuzu.DersKodu,
                    DersHavuzu.DersAdi,
                    DersHavuzu.Teorik,
                    DersHavuzu.Uygulama,
                    DersProgrami.DersGunu,
                    DersProgrami.DersSaati,
                    Derslik.DerslikAdi,
                    Bolum.BolumAdi
                ).join(
                    Mufredat, DersHavuzu.DersID == Mufredat.DersID
                ).join(
                    DersAcma, DersAcma.MufredatID == Mufredat.MufredatID  # Adjusted join condition
                ).join(
                    DersProgrami, DersAcma.DersAcmaID == DersProgrami.DersAcmaID
                ).join(
                    Derslik, DersProgrami.DerslikID == Derslik.DerslikID
                ).join(
                    Bolum, Ogrenci.BolumID == Bolum.BolumID
                ).filter(
                    Ogrenci.OgrenciID == 4  # 4 yazzan kısım  öğrenci id si
                ).all()

                print(ders_programlari)
                ders_saatleri = [
                    "9", "10", "11", "12", "13",
                    "14", "15", "16", "17", "18"
                ]
                return render_template('ders_islemleri/ogretmen_ders_programi.html', ders_programlari=ders_programlari,user=user, token=token,ders_saatleri=ders_saatleri,
                                       decoded_token=decoded_token,gunler=gunler)

            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))
@ders_islemleri_blueprint.route('/ogrenci_ders_programi')
def ogrenci_ders_programi():
    token = request.args.get('token')
    if token:
        try:

            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"

            if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

                ders_programlari = db.session.query(
                    DersHavuzu.DersKodu,
                    DersHavuzu.DersAdi,
                    DersHavuzu.Teorik,
                    DersHavuzu.Uygulama,
                    DersProgrami.DersGunu,
                    DersProgrami.DersSaati,
                    Derslik.DerslikAdi,
                    Bolum.BolumAdi
                ).join(
                    Mufredat, DersHavuzu.DersID == Mufredat.DersID
                ).join(
                    DersAcma, DersAcma.MufredatID == Mufredat.MufredatID  # Adjusted join condition
                ).join(
                    DersProgrami, DersAcma.DersAcmaID == DersProgrami.DersAcmaID
                ).join(
                    Derslik, DersProgrami.DerslikID == Derslik.DerslikID
                ).join(
                    Bolum, Ogrenci.BolumID == Bolum.BolumID
                ).filter(
                    Ogrenci.OgrenciID == 4  # 4 yazzan kısım  öğrenci id si
                ).all()

                ders_saatleri = [
                    "9", "10", "11", "12", "13",
                    "14", "15", "16", "17", "18"
                ]
                return render_template('ders_islemleri/ogrenci_ders_programi.html', ders_programlari=ders_programlari,user=user, token=token,ders_saatleri=ders_saatleri,
                                       decoded_token=decoded_token,gunler=gunler)

            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))


@ders_islemleri_blueprint.route('/ogretmen_ders_kayit')
def ogretmen_ders_kayit_goruntule():
    token = request.args.get('token')
    if token:
        try:

            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                courses_taught = DersAcma.query.filter_by(OgrElmID=user.OgrElmID).all()

                # Prepare a dictionary to store course and student information
                courses_taught = (
                    db.session.query(DersAcma, DersHavuzu)
                    .join(Mufredat, DersAcma.MufredatID == Mufredat.MufredatID)
                    .join(DersHavuzu, Mufredat.DersID == DersHavuzu.DersID)
                    .filter(DersAcma.OgrElmID == 11)
                    .all()
                )

                # Prepare a dictionary to store course and student information
                course_student_info = {}

                for course, ders_havuzu in courses_taught:
                    # Retrieve the list of students registered for each course
                    students_registered = (
                        db.session.query(Ogrenci, DersAlma)
                        .join(DersAlma, Ogrenci.OgrenciID == DersAlma.OgrenciID)
                        .filter(DersAlma.DersAcmaID == course.DersAcmaID)
                        .all()
                    )

                    # Store course and student information in the dictionary
                    course_student_info[course] = {
                        'DersKodu': ders_havuzu.DersKodu,
                        'DersAdi': ders_havuzu.DersAdi,
                        'DersTuru': ders_havuzu.DersTuru,
                        'Teorik': ders_havuzu.Teorik,
                        'Uygulama': ders_havuzu.Uygulama,
                        'Kredi': ders_havuzu.Kredi,
                        'ECTS': ders_havuzu.ECTS,
                        'students': students_registered
                    }


                return render_template('ders_islemleri/ders_kayitlari.html', user=user, token=token,
                                       decoded_token=decoded_token, course_student_info=course_student_info)


            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))
@ders_islemleri_blueprint.route('/ogrenci_ders_kayit')
def ogrenci_ders_kayit_goruntule():
    token = request.args.get('token')
    if token:
        try:

            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                #courses_taught = DersAcma.query.filter_by(OgrElmID=user.OgrElmID).all()
                # Prepare a dictionary to store course and student information
                current_academic_year = "2024-2025"
                current_academic_semester = "Guz"
                active_student = Ogrenci.query.filter_by(OgrenciID=user.OgrenciID, Durumu="Aktif").first()
                # from datetime import date
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
                        course_info_list = []

                        for course in active_student_courses:
                            ders = DersHavuzu.query.get(course.DersAcmaID)
                            ogretmen = OgretimElemani.query.get(course.OgrElmID)
                            course_info = {
                                "AkademikYil": course.AkademikYil,
                                "DersAcmaID": course.DersAcmaID,
                                "AkademikDonem": course.AkademikDonem,
                                "MufredatID": course.MufredatID,
                                "Kontenjan": course.Kontenjan,
                                "OgrElmID": course.OgrElmID,
                                "DersKodu": ders.DersKodu,
                                "DersAdi": ders.DersAdi,
                                "DersTuru": ders.DersTuru,
                                "Teorik": ders.Teorik,
                                "Uygulama": ders.Uygulama,
                                "Kredi": ders.Kredi,
                                "ECTS": ders.ECTS,
                                "OgrAdi": f"{ogretmen.Unvan} {ogretmen.Adi} {ogretmen.Soyadi}"
                            }
                return []
                from datetime import date
                ogrenci_id = user.OgrenciID
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




                return render_template('ders_islemleri/ogrenci_ders_kayit.html', user=user, token=token,
                                       decoded_token=decoded_token, course_info=active_student_courses)


            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))


@ders_islemleri_blueprint.route('/ogretmen_ders_kayit_onayla/<int:ders_alma_id>', methods=['GET'])
def ogrenci_onayla(ders_alma_id):
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # Öğrenci ID ile öğrenciyi bul ve sil
                ders_alma = DersAlma.query.get(ders_alma_id)  # Assuming DersAlma is the correct model

                if ders_alma:
                    # Update the status or perform any other actions
                    ders_alma.Durum = 'Basarili'
                    # Commit the changes to the database
                    db.session.commit()

                    return redirect(url_for('ders-islemleri.ogretmen_ders_kayit_goruntule', token=token))
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))

@ders_islemleri_blueprint.route('/ogretmen_ders_kayit_reddet/<int:ders_alma_id>', methods=['GET'])
def ogrenci_reddet(ders_alma_id):
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # Öğrenci ID ile öğrenciyi bul ve sil
                ders_alma = DersAlma.query.get(ders_alma_id)  # Assuming DersAlma is the correct model

                if ders_alma:
                    # Update the status or perform any other actions
                    ders_alma.Durum = 'Basarisiz'
                    # Commit the changes to the database
                    db.session.commit()

                    return redirect(url_for('ders-islemleri.ogretmen_ders_kayit_goruntule', token=token))
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))

@ders_islemleri_blueprint.route('/ogretmen_ders_kayit_beklet/<int:ders_alma_id>', methods=['GET'])
def ogrenci_beklet(ders_alma_id):
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # Öğrenci ID ile öğrenciyi bul ve sil
                ders_alma = DersAlma.query.get(ders_alma_id)  # Assuming DersAlma is the correct model

                if ders_alma:
                    # Update the status or perform any other actions
                    ders_alma.Durum = 'Devamsiz'
                    # Commit the changes to the database
                    db.session.commit()

                    return redirect(url_for('ders-islemleri.ogretmen_ders_kayit_goruntule', token=token))
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))



