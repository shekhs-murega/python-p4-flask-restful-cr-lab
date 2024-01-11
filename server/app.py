from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


class Plants(Resource):
    def get(self):
        plant_dicts = [plant.to_dict() for plant in Plant.query.all()]
        return make_response(plant_dicts, 200)

    def post(self):
        data = request.get_json()
        new_plant = Plant(
            name=data.get('name'),
            image=data.get('image'),
            price=data.get('price')
        )
        db.session.add(new_plant)
        db.session.commit()
        new_plant_dict = new_plant.to_dict()
        return make_response(new_plant_dict, 201)


api.add_resource(Plants, '/plants')


class PlantByID(Resource):
    def get(self, id):
        plant = Plant.query.get(id)
        if not plant:
            return make_response({"error": "Plant not found"}, 404)

        plant_dict = plant.to_dict()
        return make_response(plant_dict, 200)


api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
