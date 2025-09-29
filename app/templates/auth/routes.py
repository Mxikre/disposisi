from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

bp = Blueprint("auth", __name__)

# ---------------- LOGIN ----------------
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username != "admin" or password != "123":
            flash("Username atau password salah", "danger")
            return redirect(url_for("auth.login"))

        flash("Login berhasil!", "success")
        # nanti bisa pakai login_user(user) kalau pakai flask-login
        return redirect(url_for("main.dashboard"))

    return render_template("login.html")

# ---------------- LOGOUT ----------------
@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Anda berhasil logout", "info")
    return redirect(url_for("auth.login"))
