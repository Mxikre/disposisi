from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Buat app dan context
app = create_app()
with app.app_context():
    # Cek dulu apakah admin sudah ada
    if not User.query.filter_by(username="admin").first():
        admin = User(
            nama="Administrator",
            jabatan="Admin",
            role="admin",
            username="admin",
            password=generate_password_hash("admin123")
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ User admin berhasil ditambahkan!")
    else:
        print("⚠️ User admin sudah ada, tidak ditambahkan lagi.")
