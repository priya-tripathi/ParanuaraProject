import json

from DBUtils import DBUtil
from settings import mongodb, DB_COLLECTION_NAME_PEOPLE, db


class PeopleDAO(DBUtil.DBUtil):
    def __init__(self):
        db = mongodb
        DBUtil.DBUtil.__init__(self, db)
        self.collection_people = db[DB_COLLECTION_NAME_PEOPLE]

    def post_people(self, people_data):
        self.collection_people.insert_many(people_data)

    def get_all_people(self):
        response = []
        print("hi")
        documents = self.collection_people.find()
        print(documents)
        for document in documents:
            response.append(document)
        return response

    def get_info_twopeople(self, one, two):
        first_person = {"name": {"$eq": one}}
        second_person = {"name": {"$eq": two}}
        docs_one = list(
            self.collection_people.find(first_person, {"_id": 0, "name": 1, "age": 1, "address": 1, "phone": 1}))
        docs_two = list(
            self.collection_people.find(second_person,
                                        {"_id": 0, "name": 1, "age": 1, "address": 1, "phone": 1}))
        response = []
        friends_one = list(self.collection_people.find(first_person, {"_id": 0, "friends": 1}))
        friends_two = list(self.collection_people.find(second_person, {"_id": 0, "friends": 1}))
        list1 = []
        list2 = []
        commonList = []
        for doc_x in docs_one:
            response.append(doc_x)
        for doc_y in docs_two:
            response.append(doc_y)
        for x in friends_one:
            for a in x['friends']:
                list1.append(a['index'])
        for y in friends_two:
            for a in y['friends']:
                list2.append(a['index'])
        for m in list1:
            for n in list2:
                if m == n:
                    commonList.append(m)
                    break
        entry = {}
        # key = f'commonFriends of {one} and {two}'
        entry["common"] = []
        has_died = False
        eye_color = "brown"
        print(commonList)
        for z in commonList:
            match_quality = {"index": {"$eq": commonList[z]}, "has_died": {"$in": [has_died, "___wrong"]},
                             "eyeColor": {"$in": [eye_color, "___wrong"]}}
            res1 = list(db[DB_COLLECTION_NAME_PEOPLE].find(match_quality, {"_id": 0, "name": 1, }))
            for res in res1:
                entry["common"].append(res['name'])
        response.append(entry)
        print(response)
        return response

    def get_info_by_name(self, one):
        response = []
        person_query = {"name": {"$eq": one}}
        entry = {}

        docs = self.collection_people.find(person_query,
                                           {"_id": 0, "name": 1, "age": 1, "favouriteFood": 1})
        with open('resources/fruits.json', 'r') as fruits:
            data_fruits = fruits.read()
        for doc in docs:
            entry["name"] = doc['name']
            entry["age"] = doc['age']
            entry['fruits'] = []
            entry['vegetables'] = []
            for a in doc['favouriteFood']:
                x = data_fruits.find(a)
                if x >= 0:
                    entry['fruits'].append(a)
                else:
                    entry['vegetables'].append(a)

        response.append(entry)
        return response
