from flask import Blueprint, request, jsonify

from DBUtils.People import PeopleDAO
from settings import DB_COLLECTION_NAME_PEOPLE

peopleAPI = Blueprint('peopleAPI', __name__)
peopleDB = PeopleDAO()

@peopleAPI.route("/people/add/service", methods=['POST'])
def insert_document_people():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            peopleDB.post_company(req_data)
            return jsonify({"message": "Service has been added successfully", "status": "success"}), 200
        except Exception as e:
            return jsonify({"message": str(e), "status": "failed"}), 404

@peopleAPI.route('/people/get/service', methods=['GET'])
def get_people():

    try:
        get_all_people_data = peopleDB.get_all_people()
        return jsonify({"Data": get_all_people_data, "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404

@peopleAPI.route('/people/get/service/second/<string:one>,<string:two>', methods=['GET'])
def by_twopersons(one, two):
    try:
        get_info_people_data = peopleDB.get_info_twopeople(one,two)
        # return jsonify({"Data": get_info_people_data, "status": "success"}), 200
        return get_info_people_data
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404

@peopleAPI.route('/people/get/service/third/<string:one>', methods=['GET'])
def by_oneperson(one):
    try:
        get_info_by_name = peopleDB.get_info_by_name(one)
        return get_info_by_name
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404
