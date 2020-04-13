import os

from dotenv import load_dotenv
from flask import redirect, render_template, request, url_for

from app import app
from models import Country, Region

load_dotenv()
API_KEY = os.getenv('API_KEY')


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        country_id = request.form['country']
        if country_id != '':
            country = Country.query.filter_by(id=country_id).first_or_404()
            return redirect(url_for(
                'choose_region',
                country_slug=country.alpha_2
            ))

    return render_template(
        'input.html',
        field_name='country',
        items=Country.query.order_by('name').all()
    )


@app.route('/<country_slug>', methods=['POST', 'GET'])
def choose_region(country_slug):

    country = Country.query.filter_by(alpha_2=country_slug).first_or_404()

    if request.method == 'POST':
        region_id = request.form['region']
        if region_id != '':
            return redirect(url_for(
                'choose_city',
                country_slug=country.alpha_2,
                region_id=region_id
            ))

    return render_template(
        'input.html',
        field_name='region',
        items=sorted(country.regions, key=lambda region: region.name),
        backlink=url_for('index')
    )


@app.route('/<country_slug>/<region_id>', methods=['POST', 'GET'])
def choose_city(country_slug, region_id):
    region = Region.query.filter_by(id=region_id).first_or_404()

    return render_template(
        'input.html',
        field_name='city',
        items=sorted(region.cities, key=lambda city: city.name),
        backlink=url_for('choose_region', country_slug=country_slug)
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
