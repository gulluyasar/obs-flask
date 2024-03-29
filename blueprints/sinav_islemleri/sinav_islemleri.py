from datetime import datetime

import jwt
from flask import Flask, render_template, redirect, url_for, request, Blueprint
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

from models import Ogrenci, OgretimElemani, Sinav, DersAcma, DersAlma, Degerlendirme, DersHavuzu, Mufredat, db, Derslik, Bolum
from required import redirect_user
from views import app

sinav_islemleri_blueprint = Blueprint('sinav-islemleri', __name__, template_folder='templates')


@sinav_islemleri_blueprint.route('/sinav-takvimi-ogretmen', )
def sinav_takvimi_ogretmen():
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user_name = decoded_token['user_name']
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # exams = Sinav.query.join(DersAcma).filter(Sinav.OgrElmID == user.OgrElmID).all()
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
                        OgretimElemani.BolumID == user.BolumID,
                        DersAcma.AkademikYil == donem,  # Adjust the academic year as needed
                    )
                    .order_by(desc(Sinav.SinavTarihi),
                              desc(Sinav.SinavSaati))  # Order by exam date and time in descending order
                    .all()
                )

                # Print the results

                return render_template(
                    'sinav_islemleri/sinav_takvimi_ogretmen.html',
                    user=user,
                    token=token,
                    decoded_token=decoded_token, exams=active_semester_exams

                )
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
@sinav_islemleri_blueprint.route('/ogretmen_sinav_tanimla', )
def ogretmen_sinav_tanimla():
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user_name = decoded_token['user_name']
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # exams = Sinav.query.join(DersAcma).filter(Sinav.OgrElmID == user.OgrElmID).all()
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
                        OgretimElemani.BolumID == user.BolumID,
                        DersAcma.AkademikYil == donem,  # Adjust the academic year as needed
                    )
                    .order_by(desc(Sinav.SinavTarihi),
                              desc(Sinav.SinavSaati))  # Order by exam date and time in descending order
                    .all()
                )

                # Print the results

                return render_template(
                    'sinav_islemleri/sinav_takvimi_ogretmen.html',
                    user=user,
                    token=token,
                    decoded_token=decoded_token, exams=active_semester_exams

                )
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
@sinav_islemleri_blueprint.route('/ogrenci_sinav-takvimi', )
def ogrenci_sinav_takvimi():
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user_name = decoded_token['user_name']
            user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"

            if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                # exams = Sinav.query.join(DersAcma).filter(Sinav.OgrElmID == user.OgrElmID).all()
                ogrenci = Ogrenci.query.get(user.OgrenciID)
                aktif_sinav = (
                    db.session.query(
                        DersHavuzu.DersKodu,
                        DersHavuzu.DersAdi,
                        Sinav.SinavTuru,
                        Sinav.SinavTarihi,
                        Sinav.SinavSaati,
                        Sinav.DerslikID
                    )
                    .join(Mufredat, DersHavuzu.DersID == Mufredat.DersID)
                    .join(DersAcma, Mufredat.MufredatID == DersAcma.MufredatID)
                    .join(Sinav, DersAcma.DersAcmaID == Sinav.DersAcmaID)
                    .join(Derslik, Sinav.DerslikID == Derslik.DerslikID)
                    .join(DersAlma, DersAcma.DersAcmaID == DersAlma.DersAcmaID)
                    .filter(DersAlma.OgrenciID == user.OgrenciID)
                    .order_by(Sinav.SinavTarihi, Sinav.SinavSaati)
                    .all()
                )

                # Print the results

                return render_template(
                    'sinav_islemleri/ogrenci_sinav_takvimi.html',
                    user=user,
                    token=token,
                    decoded_token=decoded_token, sinav=aktif_sinav

                )
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
@sinav_islemleri_blueprint.route('/ogrenci_sinav-notlari', )
def ogrenci_sinav_notlari():
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user_name = decoded_token['user_name']
            user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            simdi = datetime.now()
            # Yılı al
            suanki_yil = simdi.year
            donem = f"{suanki_yil}-{suanki_yil + 1}"

            if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                # exams = Sinav.query.join(DersAcma).filter(Sinav.OgrElmID == user.OgrElmID).all()
                ogrenci = Ogrenci.query.get(user.OgrenciID)
                aktif_sinav = (
                    db.session.query(
                        DersHavuzu.DersKodu,
                        DersHavuzu.DersAdi,
                        Sinav.SinavTuru,
                        Sinav.EtkiOrani,
                        Degerlendirme.SinavNotu,
                    )
                    .join(DersAcma,DersHavuzu.DersID == DersAcma.MufredatID)  # Buradaki DersID'yi doğru alana göre güncelleyin
                    .join(Sinav, DersAcma.DersAcmaID == Sinav.DersAcmaID)
                    .join(Degerlendirme, Sinav.SinavID == Degerlendirme.SinavID)
                    .join(DersAlma, Degerlendirme.OgrenciID == DersAlma.OgrenciID)
                    .filter(DersAlma.OgrenciID == user.OgrenciID)
                    .distinct()
                    .all()
                )

                # Print the results

                return render_template(
                    'sinav_islemleri/ogrenci_sinav_notlari.html',
                    user=user,
                    token=token,
                    decoded_token=decoded_token, sinav=aktif_sinav

                )
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

# @sinav_islemleri_blueprint.route('/sinav-notlari-giris',methods=['GET','POST'])
# def sinav_not_giris_ogretmen():
#     token = request.args.get('token')
#
#     if token:
#         try:
#             decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
#             user_name = decoded_token['user_name']
#             user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
#             simdi = datetime.now()
#             # Yılı al
#             suanki_yil = simdi.year
#             donem = f"{suanki_yil}-{suanki_yil + 1}"
#
#
#             if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
#                 # exams = Sinav.query.join(DersAcma).filter(Sinav.OgrElmID == user.OgrElmID).all()
#                 if request.method == 'POST':
#
#                     return render_template(
#                         'sinav_islemleri/sinav_takvimi_ogretmen.html',
#                         user=user,
#                         token=token,
#                         decoded_token=decoded_token, exams=active_semester_exams
#
#                     )
#             else:
#                 return redirect(url_for('giris-ekrani.login'))
#         except jwt.ExpiredSignatureError:
#             # Token süresi dolmuş
#             return redirect(url_for('giris-ekrani.login'))
#         except jwt.InvalidTokenError:
#             # Geçersiz token
#             return redirect(url_for('giris-ekrani.login'))
#     else:
#         return redirect(url_for('giris-ekrani.login'))
