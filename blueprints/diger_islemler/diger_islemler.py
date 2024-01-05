from datetime import datetime

import jwt
from flask import Flask, render_template, redirect, url_for, request, Blueprint
from views import app
from models import OgretimElemani, Bolum, db, Danismanlik, Ogrenci, Kullanici
from required import redirect_user

diger_islemler_blueprint = Blueprint('diger-islemler', __name__, template_folder='templates')


# @diger_islemler_blueprint.route('/')
# def ogretmen_ozluk_bilgiler():
#     token = request.args.get('token')
#     print(token)
#     if token:
#         try:
#             decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
#             user_name = decoded_token['user_name']
#             user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
#
#             if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
#                 bolum = Bolum.query.get(user.BolumID)
#
#                 return render_template('diger_islemler/ozluk_bilgileri.html',bolum = bolum,token=token,decoded_token=decoded_token,user=user)
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


@diger_islemler_blueprint.route('/ogretmen_ozluk_bilgiler', methods=['GET', 'POST'])
def ogretmen_ozluk_bilgiler():
    token = request.args.get('token')

    if request.method == 'POST':
        # Handle form submission
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                bolum = Bolum.query.get(user.BolumID)

                user.Adi = request.form['adi']
                user.Soyadi = request.form['soyadi']
                user.TCKimlikNo = request.form['tc_kimlik_no']
                user.DogumTarihi = datetime.strptime(request.form['dogum_tarihi'], '%Y-%m-%d')
                # Save changes to the database
                db.session.commit()
                # Redirect to a profile page or a success page
                return redirect(url_for('diger-islemler.ogretmen_ozluk_bilgiler', token=token))


        except jwt.ExpiredSignatureError:
            # Token is expired
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Invalid token
            return redirect(url_for('giris-ekrani.login'))

    elif token:
        # Handle GET request
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                bolum = Bolum.query.get(user.BolumID)

                return render_template('diger_islemler/ozluk_bilgileri.html', bolum=bolum, token=token,
                                       decoded_token=decoded_token, user=user)
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token is expired
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Invalid token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))


@diger_islemler_blueprint.route('/ogretmen_danismanlik', methods=['GET', 'POST'])
def ogretmen_danismanlik():
    token = request.args.get('token')

    if request.method == 'POST':
        # Handle form submission
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                pass


        except jwt.ExpiredSignatureError:
            # Token is expired
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Invalid token
            return redirect(url_for('giris-ekrani.login'))

    elif token:
        # Handle GET request
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):

                danismanlik_listesi = Danismanlik.query.filter_by(OgrElmID=user.OgrElmID).all()
                ogrenci_listesi = []
                bolum_listesi = []

                for danismanlik in danismanlik_listesi:
                    ogrenci = Ogrenci.query.filter_by(OgrenciID=danismanlik.OgrenciID).first()
                    bolum = Bolum.query.filter_by(BolumID=ogrenci.BolumID).first()
                    ogrenci_listesi.append(ogrenci)
                    bolum_listesi.append(bolum)
                return render_template('diger_islemler/ogretmen_danismanlik.html', user=user, token=token,
                                       decoded_token=decoded_token, ogrenci_listesi=ogrenci_listesi,bolum_listesi=bolum_listesi,adet=len(ogrenci_listesi))
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token is expired
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Invalid token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))

@diger_islemler_blueprint.route('/ogrenci-sil-danismanlik/<int:ogrenci_id>', methods=['GET'])
def ogrenci_sil(ogrenci_id):
    token = request.args.get('token')
    print("gelen",ogrenci_id)
    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # Öğrenci ID ile danışmanlık tablosundan öğrenciyi sil
                danismanlik_listesi = Danismanlik.query.filter_by(OgrElmID=user.OgrElmID).all()
                for ogrenci in danismanlik_listesi:
                    if ogrenci.OgrenciID == ogrenci_id:
                        print("eşlendi",ogrenci.OgrenciID)
                        print("eşlendi",ogrenci.OgrenciID)
                        print("eşlendi",ogrenci.OgrenciID)

                # if danismanlik:
                        db.session.delete(ogrenci)
                        db.session.commit()
                        break
                else:
                    return "Hata"

                return redirect(url_for('diger-islemler.ogretmen_danismanlik', token=token))
            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))


@diger_islemler_blueprint.route('/ogrenci-ekle-danismanlik', methods=['POST'])
def ogrenci_ekle():
    token = request.args.get('token')
    print("geldik hocam")
    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                ogrenciNo = request.form.get('ogrenciNo')
                ogrenci = Ogrenci.query.filter_by(OgrenciNo=ogrenciNo).first()
                if ogrenci:
                    # Check if the student is not already assigned to another advisor
                    existing_danismanlik = Danismanlik.query.filter_by(OgrenciID=ogrenci.OgrenciID).first()
                    print(existing_danismanlik)

                    if existing_danismanlik:
                        return "Error: The student is already assigned to another advisor."
                    else:
                        # Create a new Danismanlik record
                        new_danismanlik = Danismanlik(OgrElmID=user.OgrElmID, OgrenciID=ogrenci.OgrenciID)

                        # Add the new record to the database
                        db.session.add(new_danismanlik)
                        db.session.commit()

                        return redirect(url_for('diger-islemler.ogretmen_danismanlik', token=token))  # Redirect to the appropriate route after adding the student
                else:
                    return "Error: Student not found with the provided student number."


                # else:
                #     return "HATA"

            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))

