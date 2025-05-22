class Config:
    HOST = '0.0.0.0'
    PORT = 9000
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reservas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
GERENCIAMENTO_API_URL = "http://192.168.15.18:8000/turmas/filtrar/"


