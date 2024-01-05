from datetime import datetime

import jwt
from flask import Flask, render_template, redirect, url_for, request, Blueprint, flash

from required import redirect_user
from views import app
from models import Ogrenci, Bolum, Kullanici, db, OgretimElemani, Danismanlik
# from sqlalchemy.orm import Paginator
from sqlalchemy_paginator import Paginator

ogretmen_anasayfa_blueprint = Blueprint('ogretmen', __name__, template_folder='templates')


@ogretmen_anasayfa_blueprint.route('/')
def index():
    token = request.args.get('token')
    ogrenci_bilgileri = Ogrenci.query.all()
    bolum_isimleri = [bolum.BolumAdi for bolum in Bolum.query.all()]
    bolumler = Bolum.query.all()
    bolum_isimleri_form = [bolum for bolum in bolumler]
    bolum_isimleri_form_adet=len(bolum_isimleri_form)
    kullanici_isimleri = [kullanici.KullaniciAdi for kullanici in Kullanici.query.all()]

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            user_name = decoded_token['user_name']
            user = OgretimElemani.query.filter_by(KullaniciID=decoded_token['user_id']).first()

            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):

                return render_template(
                    'ogretmen/anasayfa.html',
                    user=user,
                    token=token,
                    decoded_token=decoded_token,
                    ogrenci_bilgileri=ogrenci_bilgileri,
                    bolum_isimleri=bolum_isimleri,
                    bolum_isimleri_form=bolum_isimleri_form,
                    bolum_isimleri_form_adet=bolum_isimleri_form_adet,
                    kullanici_isimleri=kullanici_isimleri,
                    adet=len(ogrenci_bilgileri)
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


@ogretmen_anasayfa_blueprint.route('/ogrenci-duzenle/<int:ogrenci_id>', methods=['GET', 'POST'])
def ogrenci_duzenle(ogrenci_id):
    token = request.args.get('token')
    ogrenci_bilgileri = Ogrenci.query.all()
    bolum_isimleri = [bolum.BolumAdi for bolum in Bolum.query.all()]
    kullanici_isimleri = [kullanici.KullaniciAdi for kullanici in Kullanici.query.all()]

    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):

                if request.method == 'GET':
                    ogrenci = Ogrenci.query.get(ogrenci_id)
                    bolum_isimleri = Bolum.query.all()
                    return render_template('ogretmen/anasayfa.html', token=token, ogrenci=ogrenci,
                                           bolum_isimleri=bolum_isimleri)

                else:

                    try:

                        adi = request.form['adi']
                        soyadi = request.form['soyadi']
                        ogrenci_no = request.form['ogrenci_no']
                        durumu = request.form['durumu']
                        kayitTarihi = request.form['kayitTarihi']
                        ayrilmaTarihi = request.form['ayrilmaTarihi']
                        tckimlikNo = request.form['tckimlikNo']
                        cinsiyet = request.form['cinsiyet']
                        dogumTarihi = request.form['dogumTarihi']
                        kullaniciAdi = request.form['kullaniciAdi']
                        bolumID = request.form['bolumID']  # Eklenen bolumID alanını al
                        # bolum = Bolum.query.filter_by(BolumAdi=bolumAdi).first()
                        # bolumID = bolum.BolumID

                        kayitTarihi = datetime.strptime(kayitTarihi, '%Y-%m-%d').date()

                        ayrilmaTarihi = datetime.strptime(ayrilmaTarihi,
                                                          '%Y-%m-%d') if ayrilmaTarihi and ayrilmaTarihi != 'None' else None
                        dogumTarihi = datetime.strptime(request.form['dogumTarihi'], '%Y-%m-%d')

                        ogrenci = Ogrenci.query.get(ogrenci_id)
                        ogrenci.Adi = adi
                        ogrenci.Soyadi = soyadi
                        ogrenci.OgrenciNo = ogrenci_no
                        ogrenci.Durumu = durumu
                        ogrenci.KayitTarihi = kayitTarihi
                        ogrenci.AyrilmaTarihi = ayrilmaTarihi
                        ogrenci.TCKimlikNo = tckimlikNo
                        ogrenci.Cinsiyet = cinsiyet
                        ogrenci.DogumTarihi = dogumTarihi
                        ogrenci.KullaniciAdi = kullaniciAdi
                        ogrenci.BolumID = bolumID
                        db.session.commit()
                        # Başarılı güncelleme durumunda bir sayfaya yönlendirme yapabilirsiniz
                        return redirect(url_for('ogretmen.index', token=token))

                    except Exception as e:
                        print(e)
                        return f"{e}"

            else:
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            # Geçersiz token
            print("Geçersiz token")
            return redirect(url_for('giris-ekrani.login'))
    else:
        print("token yok")
        return redirect(url_for('giris-ekrani.login'))


@ogretmen_anasayfa_blueprint.route('/ogrenci-sil/<int:ogrenci_id>', methods=['GET'])
def ogrenci_sil(ogrenci_id):
    token = request.args.get('token')

    if token:
        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            if redirect_user(decoded_token.get('user_type'), 'ogretim elemani'):
                # Öğrenci ID ile öğrenciyi bul ve sil
                ogrenci = Ogrenci.query.get(ogrenci_id)

                if ogrenci:
                    kullanici = Kullanici.query.get(ogrenci_id)
                    danismanlik = Danismanlik.query.get(ogrenci_id)
                    db.session.delete(ogrenci)
                    db.session.delete(danismanlik)
                    db.session.delete(kullanici)
                    db.session.commit()
                    flash('Öğrenci başarıyla silindi.', 'success')
                else:
                    flash('Öğrenci bulunamadı.', 'danger')

                return redirect(url_for('ogretmen.index', token=token))
            else:
                flash('Yetkisiz erişim.', 'danger')
                return redirect(url_for('giris-ekrani.login'))
        except jwt.ExpiredSignatureError:
            flash('Token süresi dolmuş.', 'danger')
            return redirect(url_for('giris-ekrani.login'))
        except jwt.InvalidTokenError:
            flash('Geçersiz token.', 'danger')
            return redirect(url_for('giris-ekrani.login'))
    else:
        flash('Token yok.', 'danger')
        return redirect(url_for('giris-ekrani.login'))


@ogretmen_anasayfa_blueprint.route('/ogrenci_ekle', methods=['POST'])
def ogrenci_ekle():
    token = request.args.get('token')
    if request.method == 'POST':
        # Formdan gelen verileri al
        bolumID = request.form.get('bolumID')
        ogrenciNo = request.form.get('ogrenciNo')
        durumu = request.form.get('durumu')
        adi = request.form.get('adi')
        soyadi = request.form.get('soyadi')
        tckimlikNo = request.form.get('tckimlikNo')
        cinsiyet = request.form.get('cinsiyet')
        dogumTarihi = request.form.get('dogumTarihi')
        kayitTarihi = request.form.get('kayitTarihi')
        ayrilmaTarihi = request.form.get('ayrilmaTarihi')

        # Diğer form alanlarına göre gerekli verileri al

        # Bölüm adından bölüm ID'sini çek
        # bolum = Bolum.query.filter_by(BolumAdi=bolum_adi).first()
        #
        # if not bolum:
        #     Böyle bir bölüm yoksa, hata sayfasına yönlendir
            # return "hata"

        # Kullanıcı adını ve parolasını belirle
        kullanici_adi = ogrenciNo
        parola = tckimlikNo  # Kullanıcı parolasını TC numarasına eşitle

        # Kullanıcıyı ekleyip kullanıcı ID'sini al
        kullanici = Kullanici(KullaniciAdi=kullanici_adi, Parola=parola, KullaniciTuru='Ogrenci')
        db.session.add(kullanici)
        db.session.commit()

        kayit_tarihi = datetime.strptime(kayitTarihi, '%Y-%m-%d').date() if kayitTarihi else datetime.today().date()
        ayrilma_tarihi = datetime.strptime(ayrilmaTarihi, '%Y-%m-%d').date() if ayrilmaTarihi else None
        dogum_tarihi = datetime.strptime(dogumTarihi, '%Y-%m-%d').date()

        # Öğrenciyi eklemek
        ogrenci = Ogrenci(
            BolumID=bolumID,
            OgrenciNo=ogrenciNo,
            Durumu=durumu,
            Adi=adi,
            Soyadi=soyadi,
            TCKimlikNo=tckimlikNo,
            Cinsiyet=cinsiyet,
            DogumTarihi=dogum_tarihi,
            KullaniciID=kullanici.KullaniciID,
            KayitTarihi=kayit_tarihi,
            AyrilmaTarihi=ayrilma_tarihi
        )
        db.session.add(ogrenci)
        db.session.commit()

        # Öğrenci başarıyla eklenirse, ana sayfaya yönlendir
        return redirect(url_for('ogretmen.index', token=token))

    return redirect(url_for('ogretmen.index'))
