from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

from models import db, create_tables, Kullanici
from blueprints.ogrenci_anasayfa.ogrenci_anasayfa import ogrenci_anasayfa_blueprint
from blueprints.ogretmen_anasayfa.ogretmen_anasayfa import ogretmen_anasayfa_blueprint
from blueprints.belgeler.belgeler import belgeler_blueprint
from blueprints.ders_islemleri.ders_islemleri import ders_islemleri_blueprint
from blueprints.diger_islemler.diger_islemler import diger_islemler_blueprint
from blueprints.sinav_islemleri.sinav_islemleri import sinav_islemleri_blueprint
from blueprints.giris_ekrani.giris_ekrani import giris_ekrani_blueprint

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///obs.db'
app.secret_key = "x-urMqZO>`ev,W*f'5Sgmp<in!8+j2Ez"

db.init_app(app)


with app.app_context():
    db.create_all()

app.register_blueprint(giris_ekrani_blueprint,url_prefix='/obs')
app.register_blueprint(ogrenci_anasayfa_blueprint, url_prefix='/obs/ogrenci')
app.register_blueprint(ogretmen_anasayfa_blueprint, url_prefix='/obs/ogretmen/')
app.register_blueprint(belgeler_blueprint,url_prefix='/obs/belgeler')
app.register_blueprint(ders_islemleri_blueprint,url_prefix='/obs/ders-islemleri')
app.register_blueprint(diger_islemler_blueprint,url_prefix='/obs/diger-islemler')
app.register_blueprint(sinav_islemleri_blueprint,url_prefix='/obs/sinav-islemleri')


