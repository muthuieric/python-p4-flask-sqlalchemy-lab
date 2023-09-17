#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)

    if not animal:
        response_body = '<h1>404 animal not found</h1>'
        response = make_response(response_body, 404)
        return response    

    response_body = f'''
        <h1>Animal View</h1>
        <ul>
            <li>ID: {animal.id}</li>
            <li>Name: {animal.name}</li>
            <li>Species: {animal.species}</li>
            <li>Zookeeper: {animal.zookeeper.name}</li>
            <li>Enclosure: {animal.enclosure.environment}</li>
        </ul>
    '''
    response = make_response(response_body, 200)

    return response 


    # return ''
@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)

    if not zookeeper:
        response_body = '<h1>404 zookeeper not found</h1>'
        response = make_response(response_body, 404)
        return response

    animal_list = [
        f'<li>ID: {zookeeper.id}</li>',
        f'<li>Name: {zookeeper.name}</li>',
        f'<li>Birthday: {zookeeper.birthday}</li>'
    ]

    for animal in zookeeper.animals:
        animal_list.append(f'<li>Animal: {animal.name}</li>')

    response_body = f'''
    <h1>Zookeeper View</h1>
    <ul>
        {''.join(animal_list)}
    </ul>
    '''

    response = make_response(response_body, 200)

    return response


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)

    if not enclosure:
        response_body = '<h1>404 enclosure not found</h1>'
        response = make_response(response_body, 404)
        return response
    


    animal_list2 = [
        f'<li>ID: {enclosure.id}</li>',
        f'<li>Environment: {enclosure.environment}</li>',
        f'<li>Open to Visitors: {enclosure.open_to_visitors}</li>'
    ]

    for animal in enclosure.animals:
        animal_list2.append(f'<li>Animal: {animal.name}</li>')

    response_body = f'''
    <h1>Enclosure View</h1>
    <ul>
        {''.join(animal_list2)}
    </ul>
    '''

    response = make_response(response_body, 200)

    return response
   

if __name__ == '__main__':
    app.run(port=5555, debug=True)
