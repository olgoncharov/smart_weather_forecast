from app import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    alpha_2 = db.Column(db.String(2))
    alpha_3 = db.Column(db.String(3))


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    geocode = db.Column(db.String(5))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship(
        'Country',
        backref=db.backref('regions', lazy=True)
    )


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    lat = db.Column(db.String(10))
    lng = db.Column(db.String(10))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    region = db.relationship(
        'Region',
        backref=db.backref('cities', lazy=True)
    )
