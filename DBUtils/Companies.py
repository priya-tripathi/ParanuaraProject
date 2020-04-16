import json

from DBUtils import DBUtil
from settings import mongodb, DB_COLLECTION_NAME_COMP


class CompaniesDAO(DBUtil.DBUtil):
    def __init__(self):
        db = mongodb
        DBUtil.DBUtil.__init__(self, db)
        self.collection_companies = db[DB_COLLECTION_NAME_COMP]

    def post_company(self, req_data):
        return self.collection_companies.insert_many(req_data)

    def get_all_companies(self):
        response = []
        documents = self.collection_companies.find()
        for document in documents:
            document['_id'] = str(document['_id'])
            response.append(document)
        return json.dumps(response)

