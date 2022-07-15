from flask import Flask
from config import conexion
from models.participante import Participante
from flask_cors import CORS


from controllers.participante import ParticipanteController

# environ > retorna todas las variables de entorno de .env en forma de diccionario
from os import environ

# carga todas las variables declaradas en el archivo .env como si fuesen
    # variables de entorno para que puedan ser accedidas desde el metodo environ
from dotenv import load_dotenv

from flask_restful import Api
# Sirve para la contruccion de los controladores

load_dotenv()

app = Flask(__name__)
CORS(app)
api=Api(app)
# URI dialect://usuario:password@host:puerto/base_de_datos
# La siguiente linea sirve para la conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] =environ['DATABASE_URL']

# SQLAlchemy hace un seguimiento a las modificaciones que haremos a la bd pero
    # actualmente tiene un valor predeterminado sin embargo en futuras versiones
    # se tendra que indicar si queremos hacer el seguimiento
app.config['SQLALCHEMY_TRACK_MODIFICACTIONS']=False
# inicializo mi conexion de mi sqlalchemy con la base de datos PERO todavia no me he conectado
conexion.init_app(app)

# se ejecuta la conexion y se crearan las tablas PERO si no hay ningun tabla a crear entonces no lanzara error de credenciales invalidas
# conexion.create_all(app=app)


# Definicion de rutas usando Flask-Restful
api.add_resource(ParticipanteController, '/participantes')


if __name__ == '__main__':
    app.run(debug=True)