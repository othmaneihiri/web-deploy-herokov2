from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests, json
import urllib



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbadditifsalimentaires.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class tableofadd(db.Model):
    Num = db.Column(db.String(10), primary_key=True, nullable=False)
    Nom = db.Column(db.String(150), nullable=True)
    Descriptions = db.Column(db.String(600), nullable=True)
    Halal_Haram = db.Column(db.String(5), nullable=True)
    DJA_mg_kg_mc = db.Column(db.String(5), nullable=True)
    Concen_tration_maximum =  db.Column(db.String(10), nullable=True)
    Toxicit = db.Column(db.String(40), nullable=True)
    Types = db.Column(db.String(40), nullable=True)
    Conseil =  db.Column(db.String(400), nullable=True)



resource_fields = {
    'Num': fields.String,
    'Nom': fields.String,
    'Descriptions': fields.String,
    'Halal_Haram': fields.String,
    'DJA_mg_kg_mc': fields.String,
    'Concen_tration_maximum': fields.String,
    'Toxicit': fields.String,
    'Types': fields.String,
    'Conseil': fields.String
}


class HelloWorld(Resource):
    @marshal_with(resource_fields)
    def get(self):
        r = requests.get('https://7aaf70ba6534.ngrok.io/jsonFiles/additif.json')
        result = r.json()
        q= [i['numero'] for i in result] 
        peter = tableofadd.query.filter(tableofadd.Num.in_(q)).all()
        return peter

    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
