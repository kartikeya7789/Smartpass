from database import SessionLocal
from models import User


def detect_role(email):

    email = email.lower()

    if "warden@" in email:
        return "warden"
    elif "security@" in email:
        return "security"
    else:
        return "student"


def login_or_register(name, email, password):

    db = SessionLocal()

    if not email or "@nitj.ac.in" not in email.lower():
        return None, "❌ Invalid User — Use NITJ Email Only"

    user = db.query(User).filter_by(email=email).first()

    if user:
        if user.password == password:

            return {
                "username": user.username,
                "email": user.email,
                "role": user.role
            }, f"✅ Logged in as {user.role}"

        else:
            return None, "❌ Wrong Password"

    if not name:
        return None, "❌ Enter your name"

    role = detect_role(email)

    new_user = User(
        username=name,
        email=email,
        password=password,
        role=role
    )

    db.add(new_user)
    db.commit()

    return {
        "username": name,
        "email": email,
        "role": role
    }, f"🎉 Account Created as {role}"
