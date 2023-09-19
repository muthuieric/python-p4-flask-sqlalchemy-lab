from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import date


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    birthday = db.Column(db.Date)
    
    # Establish a one-to-many relationship with animals
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(255))
    open_to_visitors = db.Column(db.Boolean)

    # Establish a one-to-many relationship with animals
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    species = db.Column(db.String(255))

    # Define foreign key relationships
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

