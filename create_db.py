from freelancehub import db
from freelancehub import create_app

app = create_app()

with app.app_context():
    db.create_all()
