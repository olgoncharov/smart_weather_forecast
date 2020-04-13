from sqlalchemy.orm import relationship

from app import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    alpha_2 = db.Column(db.String(2), unique=True)
    alpha_3 = db.Column(db.String(3), unique=True)

    regions = relationship('Region', backref='country')


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    cities = relationship('City', backref='region')


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
