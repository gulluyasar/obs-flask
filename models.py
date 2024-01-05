from datetime import datetime, date
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.metadata.clear()

def create_tables():
    db.create_all()

class Kullanici(db.Model):
    __tablename__ = 'kullanici'

    KullaniciID = db.Column(db.Integer, primary_key=True)
    KullaniciAdi = db.Column(db.String(255), nullable=False)
    Parola = db.Column(db.String(255), nullable=False)
    KullaniciTuru = db.Column(db.String(50), nullable=False)

    def __init__(self, KullaniciAdi, Parola, KullaniciTuru):
        self.KullaniciAdi = KullaniciAdi
        self.Parola = generate_password_hash(Parola)
        self.KullaniciTuru = KullaniciTuru

    def is_active(self):
        return True

class Ogrenci(db.Model):
    __tablename__ = 'ogrenci'

    OgrenciID = db.Column(db.Integer, primary_key=True)
    BolumID = db.Column(db.Integer, db.ForeignKey('bolum.BolumID'), nullable=False)
    OgrenciNo = db.Column(db.String(20), nullable=False)
    Durumu = db.Column(db.String(50), nullable=False)
    KayitTarihi = db.Column(db.Date, default=date(day=10,month=10,year=2023))
    AyrilmaTarihi = db.Column(db.Date,default=None)
    Adi = db.Column(db.String(50), nullable=False)
    Soyadi = db.Column(db.String(50), nullable=False)
    TCKimlikNo = db.Column(db.String(11), nullable=False, unique=True)
    Cinsiyet = db.Column(db.String(10), nullable=False)
    DogumTarihi = db.Column(db.Date, nullable=False)
    KullaniciID = db.Column(db.Integer, db.ForeignKey('kullanici.KullaniciID'), nullable=False)

    def __init__(self, BolumID, OgrenciNo, Durumu, Adi, Soyadi, TCKimlikNo, Cinsiyet, DogumTarihi, KullaniciID,KayitTarihi=date(day=10,month=10,year=2023),AyrilmaTarihi=None):
        self.BolumID = BolumID
        self.OgrenciNo = OgrenciNo
        self.Durumu = Durumu
        self.Adi = Adi
        self.Soyadi = Soyadi
        self.TCKimlikNo = TCKimlikNo
        self.Cinsiyet = Cinsiyet
        self.DogumTarihi = DogumTarihi
        self.KullaniciID = KullaniciID
        self.KayitTarihi = KayitTarihi
        self.AyrilmaTarihi = AyrilmaTarihi


class Bolum(db.Model):
    __tablename__ = 'bolum'

    BolumID = db.Column(db.Integer, primary_key=True)
    BolumAdi = db.Column(db.String(255), nullable=False)
    ProgramTuru = db.Column(db.String(50), nullable=False)
    OgretimTuru = db.Column(db.String(50), nullable=False)
    OgrenimDili = db.Column(db.String(50), nullable=False)
    WebAdresi = db.Column(db.String(255))

    def __init__(self, BolumAdi, ProgramTuru, OgretimTuru, OgrenimDili, WebAdresi):
        self.BolumAdi = BolumAdi
        self.ProgramTuru = ProgramTuru
        self.OgretimTuru = OgretimTuru
        self.OgrenimDili = OgrenimDili
        self.WebAdresi = WebAdresi

class DersHavuzu(db.Model):
    __tablename__ = 'ders_havuzu'

    DersID = db.Column(db.Integer, primary_key=True)
    DersKodu = db.Column(db.String(20), nullable=False, unique=True)
    DersAdi = db.Column(db.String(100), nullable=False)
    DersDili = db.Column(db.String(20), nullable=False)
    DersSeviyesi = db.Column(db.String(20), nullable=False)
    DersTuru = db.Column(db.String(20), nullable=False)
    Teorik = db.Column(db.Integer, nullable=False)
    Uygulama = db.Column(db.Integer, nullable=False)
    Kredi = db.Column(db.Float, nullable=False)
    ECTS = db.Column(db.Integer, nullable=False)

    def __init__(self, DersKodu, DersAdi, DersDili, DersSeviyesi, DersTuru, Teorik, Uygulama, Kredi, ECTS):
        self.DersKodu = DersKodu
        self.DersAdi = DersAdi
        self.DersDili = DersDili
        self.DersSeviyesi = DersSeviyesi
        self.DersTuru = DersTuru
        self.Teorik = Teorik
        self.Uygulama = Uygulama
        self.Kredi = Kredi
        self.ECTS = ECTS


class Mufredat(db.Model):
    __tablename__ = 'mufredat'

    MufredatID = db.Column(db.Integer, primary_key=True)
    BolumID = db.Column(db.Integer, db.ForeignKey('bolum.BolumID'), nullable=False)
    DersID = db.Column(db.Integer, db.ForeignKey('ders_havuzu.DersID'), nullable=False)
    AkademikYil = db.Column(db.String(20), nullable=False)
    AkademikDonem = db.Column(db.String(20), nullable=False)
    DersDonemi = db.Column(db.Integer, nullable=False)

    def __init__(self, BolumID, DersID, AkademikYil, AkademikDonem, DersDonemi):
        self.BolumID = BolumID
        self.DersID = DersID
        self.AkademikYil = AkademikYil
        self.AkademikDonem = AkademikDonem
        self.DersDonemi = DersDonemi


class OgretimElemani(db.Model):
    __tablename__ = 'ogretim_elemani'

    OgrElmID = db.Column(db.Integer, primary_key=True)
    BolumID = db.Column(db.Integer, db.ForeignKey('bolum.BolumID'), nullable=False)
    KurumSicilNo = db.Column(db.String(20), nullable=False, unique=True)
    Unvan = db.Column(db.String(50), nullable=False)
    Adi = db.Column(db.String(50), nullable=False)
    Soyadi = db.Column(db.String(50), nullable=False)
    TCKimlikNo = db.Column(db.String(11), nullable=False, unique=True)
    Cinsiyet = db.Column(db.String(10), nullable=False)
    DogumTarihi = db.Column(db.Date, nullable=False)
    KullaniciID = db.Column(db.Integer, db.ForeignKey('kullanici.KullaniciID'), nullable=False)

    def __init__(self, BolumID, KurumSicilNo, Unvan, Adi, Soyadi, TCKimlikNo, Cinsiyet, DogumTarihi, KullaniciID):
        self.BolumID = BolumID
        self.KurumSicilNo = KurumSicilNo
        self.Unvan = Unvan
        self.Adi = Adi
        self.Soyadi = Soyadi
        self.TCKimlikNo = TCKimlikNo
        self.Cinsiyet = Cinsiyet
        self.DogumTarihi = DogumTarihi
        self.KullaniciID = KullaniciID


class Derslik(db.Model):
    __tablename__ = 'derslik'

    DerslikID = db.Column(db.Integer, primary_key=True)
    DerslikAdi = db.Column(db.String(50), nullable=False)
    DerslikTuru = db.Column(db.String(20), nullable=False)
    Kapasite = db.Column(db.Integer, nullable=False)

    def __init__(self, DerslikAdi, DerslikTuru, Kapasite):
        self.DerslikAdi = DerslikAdi
        self.DerslikTuru = DerslikTuru
        self.Kapasite = Kapasite


class DersProgrami(db.Model):
    __tablename__ = 'ders_programi'

    DersPrgID = db.Column(db.Integer, primary_key=True)
    DersAcmaID = db.Column(db.Integer, db.ForeignKey('ders_acma.DersAcmaID'), nullable=False)
    DerslikID = db.Column(db.Integer, db.ForeignKey('derslik.DerslikID'), nullable=False)
    DersGunu = db.Column(db.String(20), nullable=False)
    DersSaati = db.Column(db.Integer, nullable=False)

    @staticmethod
    def check_schedule_conflict(ders_acma_id, derslik_id, ders_gunu, ders_saati):
        existing_program = DersProgrami.query.filter_by(DerslikID=derslik_id, DersGunu=ders_gunu, DersSaati=ders_saati).first()
        if existing_program:
            return False
        existing_teacher_program = DersProgrami.query.join(DersAcma).filter(
            DersProgrami.DersGunu == ders_gunu,
            DersProgrami.DersSaati == ders_saati,
            DersAcma.OgrElmID == DersAcma.OgrElmID,
            DersProgrami.DersPrgID != ders_acma_id
        ).first()
        if existing_teacher_program:
            return False


        ders_acma = DersAcma.query.get(ders_acma_id)
        existing_same_semester_program = DersProgrami.query.join(DersAcma).filter(
            DersAcma.DersID == ders_acma.DersID,
            DersProgrami.DersGunu == ders_gunu,
            DersProgrami.DersSaati == ders_saati,
            DersProgrami.DersPrgID != ders_acma_id
        ).first()
        if existing_same_semester_program:
            return False

        return True

    def __init__(self, DersAcmaID, DerslikID, DersGunu, DersSaati):
        self.DersAcmaID = DersAcmaID
        self.DerslikID = DerslikID
        self.DersGunu = DersGunu
        self.DersSaati = DersSaati


class DersAcma(db.Model):
    __tablename__ = 'ders_acma'

    DersAcmaID = db.Column(db.Integer, primary_key=True)
    AkademikYil = db.Column(db.String(20), nullable=False)
    AkademikDonem = db.Column(db.String(20), nullable=False)
    MufredatID = db.Column(db.Integer, db.ForeignKey('mufredat.MufredatID'), nullable=False)
    Kontenjan = db.Column(db.Integer, nullable=False)
    OgrElmID = db.Column(db.Integer, db.ForeignKey('ogretim_elemani.OgrElmID'), nullable=False)

    def __init__(self, AkademikYil, AkademikDonem, MufredatID, Kontenjan, OgrElmID):
        self.AkademikYil = AkademikYil
        self.AkademikDonem = AkademikDonem
        self.MufredatID = MufredatID
        self.Kontenjan = Kontenjan
        self.OgrElmID = OgrElmID


class DersAlma(db.Model):
    __tablename__ = 'ders_alma'

    DersAlmaID = db.Column(db.Integer, primary_key=True)
    DersAcmaID = db.Column(db.Integer, db.ForeignKey('ders_acma.DersAcmaID'), nullable=False)
    OgrenciID = db.Column(db.Integer, db.ForeignKey('ogrenci.OgrenciID'), nullable=False)
    Durum = db.Column(db.String(20), nullable=False)

    def __init__(self, DersAcmaID, OgrenciID, Durum):
        self.DersAcmaID = DersAcmaID
        self.OgrenciID = OgrenciID
        self.Durum = Durum


class Sinav(db.Model):
    __tablename__ = 'sinav'

    SinavID = db.Column(db.Integer, primary_key=True)
    DersAcmaID = db.Column(db.Integer, db.ForeignKey('ders_acma.DersAcmaID'), nullable=False)
    SinavTuru = db.Column(db.String(20), nullable=False)
    EtkiOrani = db.Column(db.Integer, nullable=False)
    SinavTarihi = db.Column(db.Date, nullable=False)
    SinavSaati = db.Column(db.Time, nullable=False)
    DerslikID = db.Column(db.Integer, db.ForeignKey('derslik.DerslikID'), nullable=False)
    OgrElmID = db.Column(db.Integer, db.ForeignKey('ogretim_elemani.OgrElmID'), nullable=False)

    def __init__(self, DersAcmaID, SinavTuru, EtkiOrani, SinavTarihi, SinavSaati, DerslikID, OgrElmID):
        self.DersAcmaID = DersAcmaID
        self.SinavTuru = SinavTuru
        self.EtkiOrani = EtkiOrani
        self.SinavTarihi = SinavTarihi
        self.SinavSaati = SinavSaati
        self.DerslikID = DerslikID
        self.OgrElmID = OgrElmID


class Degerlendirme(db.Model):
    __tablename__ = 'degerlendirme'

    DegerlendirmeID = db.Column(db.Integer, primary_key=True)
    SinavID = db.Column(db.Integer, db.ForeignKey('sinav.SinavID'), nullable=False)
    OgrenciID = db.Column(db.Integer, db.ForeignKey('ogrenci.OgrenciID'), nullable=False)
    SinavNotu = db.Column(db.Float, nullable=False)

    def __init__(self, SinavID, OgrenciID, SinavNotu):
        self.SinavID = SinavID
        self.OgrenciID = OgrenciID
        self.SinavNotu = SinavNotu


class Danismanlik(db.Model):
    __tablename__ = 'danismanlik'

    DanismanlikID = db.Column(db.Integer, primary_key=True)
    OgrElmID = db.Column(db.Integer, db.ForeignKey('ogretim_elemani.OgrElmID'), nullable=False)
    OgrenciID = db.Column(db.Integer, db.ForeignKey('ogrenci.OgrenciID'), unique=True, nullable=False)

    @staticmethod
    def check_danisman_limit(ogrenci_id):
        existing_danisman = Danismanlik.query.filter_by(OgrenciID=ogrenci_id).first()
        return existing_danisman is None

    def __init__(self, OgrElmID, OgrenciID):
        self.OgrElmID = OgrElmID
        self.OgrenciID = OgrenciID

