from app import create_app
from db import db

import pandas as pd
from flask import render_template, request, jsonify
# from fileinput import filename

# Models
from app.models.company import Company
from app.models.department import Departament
from app.models.establishment import Establishment
from app.models.segment import Segment
from app.models.establishment_segment import EstablishmentSegment
from app.models.technology import Technology
from app.models.speed_range import SpeedRange
from app.models.internet_details import InternetDetails

app = create_app()

# @app.get('/fetchall-companies')
# def view_companies():
#     companies = Company.query.all()
#     return companies

@app.route('/')
def index():
    companies = Company.query.all()
    return render_template('index.html', companies = companies)

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

    arr_tec = []
    df_technologies = df['Tecnologia'].drop_duplicates().dropna()
    for i in range(len(df_technologies)):
        arr_tec.append(df_technologies.iloc[i])
        technology = Technology(df_technologies.iloc[i])
        db.session.add(technology)

    arr_spee = []
    df_speed_ranges = df['Rango_velocidad'].drop_duplicates().dropna()
    for i in range(len(df_speed_ranges)):
        arr_spee.append(df_speed_ranges.iloc[i])
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

    arr_est_seg = []
    df_establishment_segment = df[['RUC Empresa', 'Departamento', ' (Segmento)']].drop_duplicates()
    for i in range(len(df_establishment_segment)):
        ruc = df_establishment_segment.iloc[i][0]
        department = df_establishment_segment.iloc[i][1]
        segment = df_establishment_segment.iloc[i][2]
        arr_est_seg.append("company: {}, department: {}, segment: {}".format(ruc, department, segment))

        establishment_id = arr_est.index("company: {}, department: {}".format(ruc, department)) + 1
        segment_id = arr_seg.index(segment) + 1
        
        establishment_segment = EstablishmentSegment(establishment_id, segment_id)
        db.session.add(establishment_segment)

    df_establishment_segment = df[['RUC Empresa', 'Departamento', ' (Segmento)', 'Tecnologia', 'Rango_velocidad']].drop_duplicates()
    for i in range(len(df_establishment_segment)):
        ruc = df_establishment_segment.iloc[i][0]
        department = df_establishment_segment.iloc[i][1]
        segment = df_establishment_segment.iloc[i][2]
        technology = df_establishment_segment.iloc[i][3]
        speed_range = None if pd.isna(df_establishment_segment.iloc[i][4]) else df_establishment_segment.iloc[i][4]

        establishment_segment_id = arr_est_seg.index("company: {}, department: {}, segment: {}".format(ruc, department, segment)) + 1
        technology_id = arr_tec.index(technology) + 1
        if speed_range != None:
            speed_range_id = arr_spee.index(speed_range) + 1
        else:
            speed_range_id = None
        
        internet_detail = InternetDetails(establishment_segment_id, technology_id, speed_range_id)
        db.session.add(internet_detail)

    db.session.commit()

    return render_template('upload-excel.html')

if __name__ == "__main__":
    app.run(debug=os.environ.get('FLASK_DEBUG'))