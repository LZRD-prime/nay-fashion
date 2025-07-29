from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app.models import Produit
from app.extensions import db

panier_bp = Blueprint('panier', __name__, url_prefix='/panier')


# Afficher le panier
@panier_bp.route('/')
def afficher_panier():
    panier = session.get('panier', {})
    produits = []
    total = 0

    for produit_id, quantite in panier.items():
        produit = Produit.query.get(int(produit_id))
        if produit:
            sous_total = produit.prix * quantite
            total += sous_total
            produits.append({
                'id': produit.id,
                'nom': produit.nom,
                'prix': produit.prix,
                'quantite': quantite,
                'sous_total': sous_total
            })

    return render_template('panier/panier.html', produits=produits, total=round(total, 2))


# Ajouter un produit
@panier_bp.route('/ajouter/<int:produit_id>')
def ajouter_au_panier(produit_id):
    panier = session.get('panier', {})
    panier[str(produit_id)] = panier.get(str(produit_id), 0) + 1
    session['panier'] = panier
    flash('Produit ajouté au panier.', 'success')
    return redirect(url_for('main.home'))


# Supprimer un produit
@panier_bp.route('/supprimer/<int:produit_id>')
def supprimer_du_panier(produit_id):
    panier = session.get('panier', {})
    produit_id = str(produit_id)
    if produit_id in panier:
        panier.pop(produit_id)
        session['panier'] = panier
        flash('Produit retiré du panier.', 'info')
    return redirect(url_for('panier.afficher_panier'))


# Vider le panier
@panier_bp.route('/vider')
def vider_panier():
    session.pop('panier', None)
    flash('Panier vidé.', 'info')
    return redirect(url_for('panier.afficher_panier'))
