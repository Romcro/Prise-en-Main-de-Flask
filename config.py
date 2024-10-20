import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_cle_secrete_pour_dev'
    DEBUG = True
