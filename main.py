from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests, json
import urllib

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbadditifsalimentaires.db'

db = SQLAlchemy(app)

class tableofadd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    niveaudanger = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(255), nullable=False)
    famille = db.Column(db.String(255), nullable=False)

resource_fields = {
    'id': fields.Integer,
    'niveaudanger': fields.String,
    'numero': fields.String,
    'nom': fields.String,
    'famille': fields.String
}


class HelloWorld(Resource):
    @marshal_with(resource_fields)
    def get(self):
        r = requests.get('https://7aaf70ba6534.ngrok.io/jsonFiles/additif.json')
        result = r.json()
        q= [i['numero'] for i in result]
        peter = tableofadd.query.filter(tableofadd.numero.in_(q)).all()
        return peter
        #return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
