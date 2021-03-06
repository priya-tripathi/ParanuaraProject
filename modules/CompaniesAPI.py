import json

from flask import Blueprint, request, jsonify, render_template

from DBUtils.Companies import CompaniesDAO
from settings import DB_COLLECTION_NAME_COMP, DB_COLLECTION_NAME_PEOPLE, db

companiesAPI = Blueprint('companiesAPI', __name__)
companyDB = CompaniesDAO()
title = "Paranuara"
heading = "Paranuara Planet Data"


@companiesAPI.route("/companies/add/service", methods=['POST'])
def insert_document_company():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            companyDB.post_company(req_data)
            return jsonify({"message": "Service has been added successfully", "status": "success"}), 200
        except Exception as e:
            return jsonify({"message": str(e), "status": "failed"}), 404


@companiesAPI.route('/companies/get/service', methods=['GET'])
def get_companies():
    try:
        get_all_company_data = companyDB.get_all_companies()
        # return jsonify({"Data": get_all_company_data, "status": "success"}), 200
        print()
        return render_template('companies.html', a1=True, get_all_company_data=get_all_company_data, t=title, h=heading)
    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404


@companiesAPI.route('/companies/get/service/first/<string:company_name>', methods=['GET'])
def by_company_name(company_name):
    find_company = {"company": {"$eq": company_name}}
    response = []
    entry_employees = {}
    try:
        documents = db[DB_COLLECTION_NAME_COMP].find(find_company)
        for document in documents:
            document['_id'] = str(document['_id'])
            index_req = document['index']

        find_employees = {"company_id": {"$eq": index_req}}
        docs = db[DB_COLLECTION_NAME_PEOPLE].find(find_employees, {"_id": 0, "name": 1})
        entry_employees[company_name] = []
        if docs.count() > 0:
            for doc in docs:
                entry_employees[company_name].append(doc['name'])
            response.append(entry_employees)
        else:
            response.insert(0, "There are no employees in company " f'{company_name}')
        print(response)
        return render_template('companies.html', a2=company_name, get_all_company_data=response, t=title, h=heading)

    except Exception as e:
        return jsonify({"message": str(e), "status": "failed"}), 404
