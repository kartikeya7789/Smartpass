from database import SessionLocal
from models import User

db = SessionLocal()

db.add(User(username="student1", password="123", role="student"))
db.add(User(username="warden1", password="123", role="warden"))
db.add(User(username="security1", password="123", role="security"))

db.commit()
print("Users Added")
