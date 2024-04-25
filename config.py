import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY ='p425pUx|!kgu69s4S`w>52(<\gB]4Q'
    DEBUG = os.environ.get('FLASK_DEBUG') == 'True'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db '

    # SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')






