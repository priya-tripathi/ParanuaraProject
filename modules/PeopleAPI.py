from flask import Blueprint, request, jsonify, render_template

from DBUtils.People import PeopleDAO

peopleAPI = Blueprint('peopleAPI', __name__)
peopleDB = PeopleDAO()
title = "Paranuara"
heading = "Paranuara Planet Data"


@peopleAPI.route("/people/add/service", methods=['POST'])
def insert_document_people():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            peopleDB.post_company(req_data)
            return jsonify({"message": "Service has been added successfully", "status": "success"}), 200
        except Exception as e:
            return jsonify({"message": str(e), "status": "failed"}), 404


# @peopleAPI.route("/")
@peopleAPI.route('/people/get/service', methods=['GET'])
def get_people():
    try:
        get_all_people_data = peopleDB.get_all_people()
        # print(get_all_people_data)
        # return jsonify({"Data": get_all_people_data, "status": "success"}), 200
        return render_template('people.html', a3=True, get_all_people_data=get_all_people_data, t=title, h=heading)
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404


@peopleAPI.route('/people/get/service/second/<string:one>,<string:two>', methods=['GET'])
def by_twopersons(one, two):
    try:
        get_info_people_data = peopleDB.get_info_twopeople(one, two)
        # return jsonify({"Data": get_info_people_data, "status": "success"}), 200
        return render_template('people.html', a1=one, a2=two, get_info_people_data=get_info_people_data, t=title,
                               h=heading)
        # return get_info_people_data
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404


@peopleAPI.route('/people/get/service/third/<string:one>', methods=['GET'])
def by_oneperson(one):
    try:
        get_info_by_name = peopleDB.get_info_by_name(one)
        return render_template('people.html', a1=one, a4=True, get_info_people_data=get_info_by_name, t=title,
                               h=heading)
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404
