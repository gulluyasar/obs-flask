from views import app
from models import *



with app.app_context():
    danismanlik_bilgileri = Danismanlik.query \
        .join(OgretimElemani, OgretimElemani.OgrElmID == Danismanlik.OgrElmID) \
        .join(Ogrenci, Ogrenci.OgrenciID == Danismanlik.OgrenciID) \
        .filter(Ogrenci.OgrenciID == 50) \
        .add_columns(OgretimElemani.Adi.label("OgretmenAdi")) \
        .first()


    ogretmen_adi = danismanlik_bilgileri.OgretmenAdi
    
    ogrenci_id = 2
    mufredat = Mufredat.query \
        .join(Ogrenci, Ogrenci.BolumID == Mufredat.BolumID) \
        .filter(Ogrenci.OgrenciID == ogrenci_id) \
        .add_columns(Mufredat.AkademikYil.label("AkademikYil"))\
        .first()
    akademik_yil_filtre= mufredat.AkademikYil
    print(akademik_yil_filtre)