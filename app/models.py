from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    jabatan = db.Column(db.String(100))
    role = db.Column(db.String(20))  # admin, petugas, penerima
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relasi
    disposisi_dikirim = db.relationship(
        "Disposisi", foreign_keys="Disposisi.pengirim_id", backref="pengirim", lazy=True
    )
    disposisi_diterima = db.relationship(
        "Disposisi", foreign_keys="Disposisi.penerima_id", backref="penerima", lazy=True
    )


class SuratMasuk(db.Model):
    __tablename__ = "surat_masuk"

    id = db.Column(db.Integer, primary_key=True)
    nomor_surat = db.Column(db.String(50))
    tanggal = db.Column(db.Date)
    pengirim = db.Column(db.String(100))
    perihal = db.Column(db.String(200))
    file_scan = db.Column(db.String(200))

    # Relasi
    disposisi = db.relationship("Disposisi", backref="surat", lazy=True)


class SuratKeluar(db.Model):
    __tablename__ = "surat_keluar"

    id = db.Column(db.Integer, primary_key=True)
    nomor_surat = db.Column(db.String(50))
    tanggal = db.Column(db.Date)
    penerima = db.Column(db.String(100))
    perihal = db.Column(db.String(200))
    file_scan = db.Column(db.String(200))


class Disposisi(db.Model):
    __tablename__ = "disposisi"

    id = db.Column(db.Integer, primary_key=True)
    surat_id = db.Column(db.Integer, db.ForeignKey("surat_masuk.id"))
    pengirim_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    penerima_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    instruksi = db.Column(db.String(255))
    status = db.Column(db.String(50), default="Belum Dibaca")
