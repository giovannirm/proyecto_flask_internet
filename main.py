from app import create_app
from app.db import db

import pandas
from flask import render_template, request, jsonify
# from fileinput import filename

from app.models.models import *

app=create_app()

# Root endpoint
@app.route('/')
def upload():
    return render_template('upload-excel.html')

@app.post('/view')
def view():
 
    # Read the File using Flask request
    file = request.files['file']
    # save file in local directory
    file.save(file.filename)
 
    # Parse the data as a Pandas DataFrame type
    data = pandas.read_excel(file)
 
    # Return HTML snippet that will render the table
    return data.to_html()

if __name__ == "__main__":
    app.run(debug=os.environ.get('FLASK_DEBUG'))