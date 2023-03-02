import os

def database():
    USER_DB = os.environ.get("USER_DB")
    PASSWORD = os.environ.get("PASSWORD")
    SERVER = os.environ.get("SERVER")
    PORT = os.environ.get("PORT")
    NAME_DB = os.environ.get("NAME_DB")
    DATABASE = os.environ.get("DATABASE")

    if DATABASE == 'mysql':
        # MySQL mysql://usuario:contraseña@servidor/nombre_de_base_de_datos
        # SQLALCHEMY_DATABASE_URI=mysql://root:@localhost/proyecto_flask_internet
        os.environ['SQLALCHEMY_DATABASE_URI']="{}://{}:{}@{}:{}/{}".format(DATABASE, USER_DB, PASSWORD, SERVER, PORT, NAME_DB)
    
    elif DATABASE == 'sqlite':
        # SQLite sqlite:///nombre_de_base_de_datos.sqlite
        # SQLALCHEMY_DATABASE_URI=sqlite:///proyecto_flask_internet.sqlite
        os.environ['SQLALCHEMY_DATABASE_URI']="{}:///{}.sqlite".format(DATABASE, NAME_DB)

    elif DATABASE == 'postgresql':
        # PostgreSQL postgresql://usuario:contraseña@servidor:puerto/nombre_de_base_de_datos
        # SQLALCHEMY_DATABASE_URI=postgresql://postgres:123456@localhost:5432/proyecto_flask_internet
        os.environ['SQLALCHEMY_DATABASE_URI']="{}://{}:{}@{}:{}/{}".format(DATABASE, USER_DB, PASSWORD, SERVER, PORT, NAME_DB)
    
    else:
        print("Tu base de datos no está contemplada en la configuración")

database()