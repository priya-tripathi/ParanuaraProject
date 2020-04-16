from flask import Flask

from modules import CompaniesAPI, PeopleAPI

app = Flask(__name__)
app.register_blueprint(CompaniesAPI.companiesAPI)
app.register_blueprint(PeopleAPI.peopleAPI)
if __name__ == '__main__':
    app.run()
