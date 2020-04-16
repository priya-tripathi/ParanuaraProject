# ParanuaraProject
Download python from https://www.python.org/downloads/

Download MongoDB from https://www.mongodb.com/download-center#community

Install Flask & pymongo

pip install Flask

pip install pymongo

Before running the mongodb instance, we must create a data folder and run below command in command prompt.

"C:\Program Files\MongoDB\Server\4.0\bin\mongod.exe" --dbpath="C:\mongo-data"

Here C:\mongo-data folder is used for saving mongodb files.

By default, it is listening the port 27017.

Download/Clone source code from Github
Run main.py in Command prompt.

python main.py

Our local web server is running in the port 5000 by default.

The API provides these end points:(decorater has been used to provide routing links.
- Given a company name, the API needs to return all their employees. Also there is solution to situation when a company has no employees
- Given 2 people names, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

Happy coding with Flask and MongoDB and RestAPIs!!!
