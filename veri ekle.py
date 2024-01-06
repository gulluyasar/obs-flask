from views import app
from models import *



with app.app_context():
    # danismanlik_bilgileri = Danismanlik.query \
    #     .join(OgretimElemani, OgretimElemani.OgrElmID == Danismanlik.OgrElmID) \
    #     .join(Ogrenci, Ogrenci.OgrenciID == Danismanlik.OgrenciID) \
    #     .filter(Ogrenci.OgrenciID == 50) \
    #     .add_columns(OgretimElemani.Adi.label("OgretmenAdi")) \
    #     .first()
    #
    #
    # ogretmen_adi = danismanlik_bilgileri.OgretmenAdi
    #
    # ogrenci_id = 2
    # mufredat = Mufredat.query \
    #     .join(Ogrenci, Ogrenci.BolumID == Mufredat.BolumID) \
    #     .filter(Ogrenci.OgrenciID == ogrenci_id) \
    #     .add_columns(Mufredat.AkademikYil.label("AkademikYil"))\
    #     .first()
    # akademik_yil_filtre= mufredat.AkademikYil
    # print(akademik_yil_filtre)
    simdi = datetime.now()
    # Yılı al
    suanki_yil = simdi.year
    donem = f"{suanki_yil}-{suanki_yil + 1}"
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
        Ogrenci.OgrenciID == 4 # 4 yazzan kısım  öğrenci id si
    ).all()
    print(ders_programlari)
    ders_saatleri = [
        "9", "10", "11", "12", "13",
        "14", "15", "16", "17", "18"
    ]
