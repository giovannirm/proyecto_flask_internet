# ADAPTACIÓN Y MODELAMIENTO CON FLASK Y MYSQL-API REST

### Crear entorno virtual

```console
    virtualenv env
```
### Instalar dependencias

```console
    pip install -r requirements.txt
```

### Modificar el archivo .env_copy por .env

Agregar sus credenciales user_db, password y name_db en el archivo .env

```bash
    SECRET_KEY=""
    FLASK_APP=main.py
    FLASK_DEBUG=1
    FLASK_ENV=FLASK_DEVELOPMENT

    # DATABASE INFORMATION FOR POSTGRESQL
    DATABASE=postgresql
    USER_DB=user_db
    PASSWORD=password
    SERVER=localhost
    PORT=5432
    NAME_DB=name_db

    # DATABASE INFORMATION FOR SQLITE
    DATABASE=sqlite
    USER_DB=
    PASSWORD=
    SERVER=
    PORT=
    NAME_DB=name_db

    # DATABASE INFORMATION FOR MYSQL
    DATABASE=mysql
    USER_DB=user_db
    PASSWORD=password
    SERVER=localhost
    PORT=
    NAME_DB=name_db
```

El valor que contenga NAME_DB será la base de datos que deberán crear en su gestor de base de datos ya sea para MySQL o PostgreSQL

### Link de mi [Diagrama E-R](https://dbdiagram.io/d/63ed8710296d97641d814f23)

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

### Para crear la imagen en Docker, ejecutar lo siguiente desde la raíz del proyecto

```console
    docker build -t proyecto_flask_internet .
```