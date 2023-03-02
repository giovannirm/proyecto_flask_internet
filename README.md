# ADAPTACIÓN Y MODELAMIENTO CON FLASK Y MYSQL-API REST

Crear entorno virtual

```console
    virtualenv env
```
Instalar dependencias

```console
    pip install -r requirements.txt
```

Credenciales .env

```bash
    SECRET_KEY="my-secret-key"
    FLASK_APP=main.py
    FLASK_DEBUG=1
    FLASK_ENV=FLASK_DEVELOPMENT
    SQLALCHEMY_DATABASE_URI=sqlite:///proyecto_flask_internet.sqlite
```

Link de mi [Diagrama E-R](https://dbdiagram.io/d/63ed8710296d97641d814f23)

```console
    https://dbdiagram.io/d/63ed8710296d97641d814f23
```

## 🚀 End points

### Endpoint para ver las empresas que existen
```console
    http://localhost:5000/companies/
``` 

### Endpoint para ver las empresas que existen
```console
    http://localhost:5000/deparments/
```


### Endpoint para ver las empresas que se encuentran en cada departamento
```console
    http://localhost:5000/deparments/company/<company_id>
    http://localhost:5000/deparments/company/10
```


### Endpoint para ver las sedes que existen
```console
    http://localhost:5000/establishments/
```


### Endpoint para ver las tecnologías, velocidad por empresa
```console
    http://localhost:5000/internet_details/
```

### Endpoint para ver las tecnologías que existen 
```console
    http://localhost:5000/technologies/
```

### Endpoint para ver las tecnologías por id
```console
    http://localhost:5000/technologies/<technology_id>
    http://localhost:5000/technologies/1
```