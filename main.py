from app import create_app
from app.db import db

import pandas as pd
from flask import render_template, request, jsonify
# from fileinput import filename

from app.models.models import *

app=create_app()

# Root endpoint
@app.route('/upload-excel')
def upload():
    return render_template('upload-excel.html')

@app.post('/view')
def view():
 
    # Read the File using Flask request
    file = request.files['file']
    # save file in local directory
    file.save(file.filename)
 
    # Parse the data as a Pandas DataFrame type
    data = pd.read_excel(file)
 
    # Return HTML snippet that will render the table
    return data.to_html()

@app.route('/upload-departments')
def upload_departments():

    db.session.commit()
    db.drop_all()
    db.create_all()

    xls = pd.ExcelFile('data_internet.xlsx')
    df = xls.parse(xls.sheet_names[0])

    # for row in df.itertuples():
    #     print(row[0])

    # for row in df.itertuples():
    #     print(row[0])

    arr_dep = []
    df_departments = df['Departamento'].drop_duplicates().dropna()
    for i in range(len(df_departments)):
        arr_dep.append(df_departments.iloc[i])
        department = Departament(df_departments.iloc[i])
        db.session.add(department)

    arr_seg = []
    df_segments = df[' (Segmento)'].drop_duplicates().dropna()
    for i in range(len(df_segments)):
        arr_seg.append(df_segments.iloc[i])
        segment = Segment(df_segments.iloc[i])
        db.session.add(segment)

    df_technologies = df['Tecnologia'].drop_duplicates().dropna()
    for i in range(len(df_technologies)):
        technology = Technology(df_technologies.iloc[i])
        db.session.add(technology)

    df_speed_ranges = df['Rango_velocidad'].drop_duplicates().dropna()
    for i in range(len(df_speed_ranges)):
        speed_range = SpeedRange(df_speed_ranges.iloc[i])
        db.session.add(speed_range)

    arr_com = []
    df_companies = df[['RUC Empresa', 'Nombre Empresa', 'Estado SUNAT']].drop_duplicates()
    for i in range(len(df_companies)):
        ruc = str(df_companies.iloc[i][0])
        arr_com.append(ruc)
        name = df_companies.iloc[i][1]
        status_sunat = df_companies.iloc[i][2] == 'ACTIVO'
        company = Company(ruc, name, status_sunat)
        db.session.add(company)

    arr_est = []
    df_establishments = df[['RUC Empresa', 'Departamento']].drop_duplicates()
    for i in range(len(df_establishments)):
        ruc = str(df_establishments.iloc[i][0])
        department = df_establishments.iloc[i][1]
        arr_est.append("company: {}, department: {}".format(ruc, department))

        company_id = arr_com.index(ruc) + 1
        department_id = arr_dep.index(department) + 1

        establishment = Establishment(company_id, department_id)
        db.session.add(establishment)

    df_establishment_segment = df[['RUC Empresa', 'Departamento', ' (Segmento)']].drop_duplicates()
    for i in range(len(df_establishment_segment)):
        ruc = df_establishment_segment.iloc[i][0]
        department = df_establishment_segment.iloc[i][1]
        segment = df_establishment_segment.iloc[i][2]

        establishment_id = arr_est.index("company: {}, department: {}".format(ruc, department)) + 1
        segment_id = arr_seg.index(segment) + 1
        
        establishment_segment = EstablishmentSegment(establishment_id, segment_id)
        db.session.add(establishment_segment)

    db.session.commit()

    return render_template('upload-excel.html')

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=os.environ.get('FLASK_DEBUG'))