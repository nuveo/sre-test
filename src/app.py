from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models

class BaseModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    def to_json(self):
        return { "id": self.id }


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    bm = BaseModel(**data)
    db.session.add(bm)
    db.session.commit()
    return jsonify(bm.to_json())


@app.route('/read/<id>', methods=['GET'])
def read(id):
    bm = BaseModel.query.get(id)

    return jsonify(bm.to_json())


@app.route('/update/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    bm = BaseModel.query.get(id)
    for key, value in data.items():
        setattr(bm, key, value)
    db.session.add(bm)
    db.session.commit()

    return jsonify(bm.to_json())


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    bm = BaseModel.query.get(id)
    db.session.delete(bm)
    db.session.commit()
    return jsonify(bm.to_json())


@app.route('/status', methods=['GET'])
def status():
    msg = {'status': 'Ok!'}
    return msg


if __name__ == "__main__":
    db.init_app(app)
    db.app = app
    db.create_all()
    app.run()
