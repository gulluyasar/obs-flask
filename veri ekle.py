# Öğrenci ID'si varsayılan olarak 1 olarak kabul edilmiştir. Gerçek projede bu değeri ilgili öğrencinin ID'siyle değiştirmelisiniz.
from models import db, Mufredat, Ogrenci, DersHavuzu, Kullanici
from views import app

with app.app_context():
    ogrenci_id = 2

    # Öğrenci bilgilerini al
    ogrenci = Ogrenci.query.get(ogrenci_id)

    # Öğrencinin bağlı olduğu müfredat bilgisini al
    #mufredat = Mufredat.query.filter_by(BolumID=ogrenci.BolumID).first()

    # MufredatID ile bağlantılı olan ders bilgilerini çek

    ogrenci = Ogrenci.query.get(ogrenci_id)

    if ogrenci:
        kullanici = Kullanici.query.get(ogrenci.KullaniciID)

        if kullanici:
            akademik_yil = kullanici.AkademikYil

            # Mufredat tablosundan ders bilgilerini çekme işlemleri
            mufredat = Mufredat.query.filter_by(BolumID=ogrenci.BolumID, AkademikYil=akademik_yil).first()

            if mufredat:
                ders_bilgileri = (
                    db.session.query(
                        DersHavuzu.DersKodu,
                        DersHavuzu.DersAdi,
                        DersHavuzu.DersTuru,
                        DersHavuzu.Teorik,
                        DersHavuzu.Uygulama,
                        DersHavuzu.Kredi,
                        DersHavuzu.ECTS
                    )
                    .join(Mufredat, Mufredat.DersID == DersHavuzu.DersID)
                    .filter(
                        Mufredat.BolumID == ogrenci.BolumID,
                        Mufredat.AkademikYil == akademik_yil,
                        Mufredat.AkademikDonem == ogrenci.AkademikDonem
                    )
                    .all()
                )

                # Ders bilgilerini yazdırma
                for ders_kodu, ders_adi, ders_turu, teorik, uygulama, kredi, ects in ders_bilgileri:
                    print(f"Ders Kodu: {ders_kodu}")
                    print(f"Ders Adı: {ders_adi}")
                    print(f"Ders Türü: {ders_turu}")
                    print(f"Teorik Saat: {teorik}")
                    print(f"Uygulama Saat: {uygulama}")
                    print(f"Kredi: {kredi}")
                    print(f"ECTS: {ects}")
                    print("-" * 30)
            else:
                print("Mufredat bulunamadı.")
        else:
            print("Kullanıcı bilgisi bulunamadı.")
    else:
        print("Öğrenci bulunamadı.")


