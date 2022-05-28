"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, redirect
from models import db, connect_db, Cupcake 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secrets'

connect_db(app)

@app.route('/')
def home_page():
    #all_cupcakes = Cupcake.query.all()
    return render_template('index.html')#, all_cupcakes=all_cupcakes)

@app.route('/api/cupcakes')
def test():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all() ]

    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def new_cupcake():
    data = request.json
    new_cupcake = Cupcake(flavor=data['flavor'], size=data['size'], rating=data['rating'], image=data['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor  = request.json.get('flavor', cupcake.flavor)
    cupcake.size  = request.json.get('size', cupcake.size)
    cupcake.rating  = request.json.get('rating', cupcake.rating)
    cupcake.image  = request.json.get('image', cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcakes(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="cupcake deleted")