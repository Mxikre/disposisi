from flask import Blueprint, render_template, request, url_for, redirect
from .models import SuratMasuk, SuratKeluar, Disposisi, db
from flask_login import login_required
from datetime import datetime

bp = Blueprint("main", __name__)

# ---------------- DASHBOARD ----------------
@bp.route("/")
@login_required
def index():
    # Ambil 5 surat masuk terbaru
    surat_terbaru = SuratMasuk.query.order_by(SuratMasuk.tanggal.desc()).limit(5).all()
    return render_template("dashboard.html", surat_terbaru=surat_terbaru)

@bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

# ---------------- SURAT MASUK ----------------
@bp.route("/surat-masuk")
@login_required
def surat_masuk():
    surat = SuratMasuk.query.all()
    return render_template("surat_masuk.html", surat=surat)

# ---------------- SURAT KELUAR ----------------
@bp.route('/surat-keluar')
@login_required
def surat_keluar():
    surat = SuratKeluar.query.order_by(SuratKeluar.tanggal.desc()).all()
    return render_template('surat_keluar_list.html', surat_keluar=surat)

@bp.route('/surat-keluar/tambah', methods=['GET', 'POST'])
@login_required
def tambah_surat_keluar():
    if request.method == 'POST':
        nomor = request.form['nomor_surat']
        tanggal = datetime.strptime(request.form['tanggal'], "%Y-%m-%d").date()
        penerima = request.form['penerima']
        perihal = request.form['perihal']

        surat = SuratKeluar(
            nomor_surat=nomor,
            tanggal=tanggal,
            penerima=penerima,
            perihal=perihal
        )
        db.session.add(surat)
        db.session.commit()

        return redirect(url_for('main.surat_keluar'))

    return render_template(
        'surat_keluar_form.html',
        surat=None,
        action_url=url_for('main.tambah_surat_keluar')
    )

@bp.route('/surat-keluar/<int:id>/cetak')
@login_required
def cetak_surat_keluar(id):
    surat = SuratKeluar.query.get_or_404(id)
    return render_template('surat_keluar_print.html', surat=surat)

# ---------------- INSTANSI ----------------
@bp.route("/instansi")
@login_required
def instansi():
    # TODO: ganti kalau ada model Instansi
    instansi_list = [
        {"nama": "Dinas Pendidikan", "alamat": "Jl. Merdeka No.1"},
        {"nama": "Dinas Kesehatan", "alamat": "Jl. Sehat No.2"},
    ]
    return render_template("instansi.html", instansi_list=instansi_list)

# ---------------- SUMMARY ----------------
@bp.route("/summary")
@login_required
def summary():
    surat_keluar_list = SuratKeluar.query.order_by(SuratKeluar.tanggal.desc()).all()
    return render_template("summary.html", surat_keluar_list=surat_keluar_list)