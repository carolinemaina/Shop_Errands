from flask import Flask
import mysql.connector

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # MySQL connection setup
    def get_db_connection():
        conn = mysql.connector.connect(
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            host=app.config['MYSQL_HOST'],
            database=app.config['MYSQL_DB']
        )
        return conn
    app.get_db_connection = get_db_connection

    with app.app_context():
        from . import routes
        return app
