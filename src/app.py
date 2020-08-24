from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models

class Payment(db.Model):

    INSERTED = "inserted"
    CONSUMED = "consumed"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10))

    def set_inserted(self):
        self.status = self.INSERTED

    def set_consumed(self):
        self.status = self.CONSUMED

    def to_json(self):
        return { "id": self.id, "status": self.status }


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# API functions

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    p = Payment(**data)
    db.session.add(p)
    db.session.commit()
    return jsonify(p.to_json())


@app.route('/list', methods=['GET'])
def list():
    ps = Payment.query.all()
    return jsonify([p.to_json() for p in ps])


@app.route('/update/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    p = Payment.query.get(id)

    new_status = data.get('status')

    if new_status == Payment.INSERTED:
        p.set_inserted()
    elif new_status == Payment.CONSUMED:
        p.set_consumed()

    db.session.add(p)
    db.session.commit()

    return jsonify(p.to_json())


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    p = Payment.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify(p.to_json())


@app.route('/status', methods=['GET'])
def healthcheck():
    return "ok", 200

if __name__ == "__main__":
    db.init_app(app)
    db.app = app
    db.create_all()
    app.run()
