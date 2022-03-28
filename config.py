import os

#CREANDO ENTORNO DE DESARROLLO (Para que no este en el archivo main)
class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentCofig(Config):
    DEBUG = True