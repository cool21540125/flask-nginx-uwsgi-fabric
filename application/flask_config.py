import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'alsdkfjasldkfjaoiefjj'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        # if you need db connection, edit <db_schema_name>
        SCHEMA_NAME = "<db_schema_name>"
        cls.SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/{schema_name}'.format(schema_name=SCHEMA_NAME)
        print("DB URI : " + cls.SQLALCHEMY_DATABASE_URI)
        app.config.from_object(cls)
