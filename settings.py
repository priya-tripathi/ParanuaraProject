import configparser
import ssl

from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('config.ini')

host_name = config['MONGODB']['DB_HOST']
DB_COLLECTION_NAME_COMP = config['MONGODB']['DB_COLLECTION_NAME_COMP']
DB_COLLECTION_NAME_PEOPLE = config['MONGODB']['DB_COLLECTION_NAME_PEOPLE']
try:
    client = MongoClient(host_name, ssl_cert_reqs=ssl.CERT_NONE)
except Exception as e:
    raise e
else:
    mongodb = client.Paradb
    db = mongodb

