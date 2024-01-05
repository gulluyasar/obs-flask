import datetime

from models import Ogrenci
from required import redirect_user
from views import app

import jwt
from flask import Flask, render_template, redirect, url_for, request, Blueprint, session
ogrenci_anasayfa_blueprint = Blueprint('ogrenci', __name__, template_folder='templates')


@ogrenci_anasayfa_blueprint.route('/')
def index():
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user = Ogrenci.query.filter_by(KullaniciID=decoded_token['user_id']).first()

            if redirect_user(decoded_token.get('user_type'), 'ogrenci'):
                return render_template('ogrenci/anasayfa.html',user=user, token=token, decoded_token=decoded_token)
            else:return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            return redirect(url_for('giris-ekrani.login'))
    else:
        return redirect(url_for('giris-ekrani.login'))