from application import db
from application.models import Todo

db.drop_all()
db.create_all()
