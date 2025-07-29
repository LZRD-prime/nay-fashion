# app/routes/routes.py

from flask import render_template
from flask import Blueprint

# Création du blueprint principal (main = pages publiques)
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/paiement')
def paiement():
    return render_template('paiement.html')
