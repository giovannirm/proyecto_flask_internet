from app import db, create_app

import pandas as pd
from flask import render_template, jsonify
import os

# Schemas
from app.schemas import *

app = create_app()

# Datatable en la ruta raíz
@app.route('/')
def index():
    upload_data()
    companies = Company.query.all()
    return render_template('index.html', companies = companies)

# Endpoint para ver las empresas que existen 
@app.route('/companies', methods=['GET'])
def get_companies():
    companies = Company.query.all()

    if companies:
        return companies_schema.dump(companies)
    
    return jsonify({'message':'No hay compañías'})

# Endpoint para ver las tecnologías, velocidad por empresa
@app.route('/internet-details', methods=['GET'])
def get_internet_details():
    companies = Company.query.all()

    result = []
    for company in companies:
        speed_ranges = []
        technologies = []
        for establishment in company.establishments:
            for headquarter in establishment.establishments_segment:
                for detail in headquarter.internet_details:
                    speed_ranges.append(speed_range_schema.dump(detail.speed_range))
                    technologies.append(technology_schema.dump(detail.technology))

        result.append({
            "company": company_schema.dump(company),
            "speed_ranges": speed_ranges,
            "technologies": technologies
        })
    if result != []:
        return result
    
    return jsonify({'message':'No hay detalles de internet'})

# Endpoint para ver las sedes que existen
@app.route('/headquarters', methods=['GET'])
def get_headquarters():
    headquarters = Establishment.query.all()
    result = []
    for headquarter in headquarters:
        company = Company.query.filter_by(id=headquarter.company_id).first()
        department = Departament.query.filter_by(id=headquarter.department_id).first()
        
        result.append({
            "headquarter": headquarter.id,
            "company": company_schema.dump(company),
            "department": department_schema.dump(department)
        })
    if result != []:
        return result
        
    return jsonify({'message':'No hay sedes disponibles'})


@app.route('/technologies/<id>', methods=['GET'])
def view_technology(id):
    technology = Technology.query.get(id)

    if technology:
        return technology_schema.dump(technology)
    
    return jsonify({'message':'No hay tecnologías'})

# Endpoint para ver las empresas que se encuentran en cada departamento
@app.route('/companies_department/<id>', methods=['GET'])
def view_companies_department(id):
    department = Departament.query.get(id)

    companies = []
    for establishment in department.establishments:
        companies.append(company_schema.dump(establishment.company))

    result = {
        "department": department_schema.dump(department),
        "companies": companies   
    }
    
    if result != []:
        return result
    
    return jsonify({'message':'No hay departamentos registrados'})

def upload_data():

    db.session.commit()
    db.drop_all()
    db.create_all()

    xls = pd.ExcelFile('data_internet.xlsx')
    df = xls.parse(xls.sheet_names[0])

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

if __name__ == "__main__":
    app.run(debug=os.environ.get('FLASK_DEBUG'))