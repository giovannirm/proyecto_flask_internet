from app import create_app
from app.db import db
from flask import request, jsonify
from datetime import date

from app.models.models import *

app=create_app()

@app.route('/',) #ruta raiz
def index():
    return "Hola mensaje de prueba"
    
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)