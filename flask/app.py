from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['CareerMatch'] 
collection_faculties_kfMGTU = db['kfMGTU']
collection_universities = db['universities']
collection_faculties_KSU = db['KSU']

@app.route('/universities_one', methods=['GET'])
def get_all_universities():

    name = request.args.get('name')

    universities = list(collection_universities.find({'name': name}, {'_id': 0}))
    if universities:
        return jsonify(universities)
    else:
        return('Not found')


@app.route('/universities', methods = ['GET'])
def get_all():
    universities = list(collection_universities.find({}, {'_id': 0}))
    return jsonify(universities)


@app.route('/faculties_kfmgtu', methods = ['GET'])
def get_all_faculties_kfMGTU():

    name_key = request.args.get('name_key')

    faculties = list(collection_faculties_kfMGTU.find({'name_key': name_key}, {'_id': 0}))
    if faculties:
        return jsonify(faculties)
    else:
        return ('Not found')


@app.route('/faculties_ksu', methods = ['GET'])
def get_all_faculties_KSU():

    name_key = request.args.get('name_key')

    faculties = list(collection_faculties_KSU.find({'name_key': name_key}, {'_id': 0}))
    if faculties:
        return jsonify(faculties)
    else:
        return ('Not found')


if __name__ == '__main__':
    app.run(debug=True)