from src import database, app
from src.models import Usuario, Foto

with app.app_context():
    database.create_all()