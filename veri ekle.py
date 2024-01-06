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
    print(ogretmen_adi)