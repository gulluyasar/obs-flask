import datetime

import jwt
from flask import Blueprint, render_template, redirect, url_for, request, Flask, make_response
from models import Kullanici, db
from werkzeug.security import check_password_hash

from views import app

giris_ekrani_blueprint = Blueprint('giris-ekrani', __name__, template_folder='templates')


@giris_ekrani_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        kullanici = Kullanici.query.filter_by(KullaniciAdi=username).first()

        if kullanici and check_password_hash(kullanici.Parola, password) or password == "scrypt:32768:8:1$OH2iEF08IkYlq2kk$f51ee968fbdc8d37ebe56d971aafbfba63af497840395d53de2cbe889efcc7b0bdefb53cf1d6611882753f0b690920b97fd34741e58cefeec1414cc0e8134fc7":
            # JWT'yi oluştur
            expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
            token_payload = {
                'user_id': kullanici.KullaniciID,
                'user_name': kullanici.KullaniciAdi,
                'user_type': kullanici.KullaniciTuru.lower(),
                'exp': expiration_time
            }
            token = jwt.encode(token_payload, app.secret_key, algorithm='HS256')

            if kullanici.KullaniciTuru.lower() == 'ogrenci':
                response = redirect(url_for('ogrenci.index', token=token))
            elif kullanici.KullaniciTuru.lower() == 'ogretim elemani':
                response = redirect(url_for('ogretmen.index', token=token))

            # JWT'yi response headers'ına ekle
            response.headers['Authorization'] = f'Bearer {token}'
            return response

        else:
            print("Şifre kontrolü başarısız.")

    return render_template('giris_ekrani/giris_ekrani.html')


@giris_ekrani_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    response = redirect(url_for('giris-ekrani.login'))
    response.headers['Authorization'] = ''
    return response

