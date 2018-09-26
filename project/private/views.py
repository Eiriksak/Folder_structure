from flask import render_template, Blueprint, request, redirect, url_for, flash, session, jsonify
import pytest
from project import db
from project.models import Bananer, Epler
from sqlalchemy import update, func
import requests

################
#### config ####
################
private_blueprint = Blueprint('private', __name__)


################
#### routes ####
################

@private_blueprint.route('/', methods=['GET', 'POST'] )
def index():
    print("er i index")
    if request.method == 'POST':
        print(request.form['submit_button'])
        if request.form['submit_button'] == 'banan':

            new_banana = Bananer("Banan") # Lager ny rad i bananer tabellen og setter inn values
            db.session.add(new_banana)
            db.session.commit()

        if request.form['submit_button'] == 'eple':
            new_apple = Epler(1)
            db.session.add(new_apple)
            db.session.commit()

        if request.form['submit_button'] == 'print_db':
            alle_epler = Epler.query.all()
            alle_bananer = Bananer.query.all()

            for epler in alle_epler:
                print(epler.amount)

            for bananer in alle_bananer:
                print(bananer.type)

            return render_template("main.html", bananer= alle_bananer, epler= alle_epler)


        return render_template("main.html")

    else:
        return render_template("main.html")