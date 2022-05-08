from flask import Flask
from db.models import db
from db.default_content import setup_all
import configparser
import logging


logging.basicConfig(filename='choraldb.log', level=logging.DEBUG)


def main():
    conf = configparser.ConfigParser()
    conf.read('choraldb.ini')

    app = Flask(__name__)
    # TODO: OPTION TO WRITE TO CONFIG
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' \
        '{0}:{1}@{2}:{3}/{4}'.format(conf['MYSQL']['user'],
                                     conf['MYSQL']['password'],
                                     conf['MYSQL']['host'],
                                     conf['MYSQL']['port'],
                                     conf['MYSQL']['database'])
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        logging.info('Created database model')
        setup_all(db)


if __name__ == '__main__':
    main()
