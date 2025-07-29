from flask import Blueprint, render_template
from flask_login import login_required
from app.models import User, Produit, Order  # Assure-toi d’avoir ces modèles

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Tableau de bord principal
@admin_bp.route('/')
@login_required
def dashboard():
    total_users = User.query.count()
    total_orders = Order.query.count()
    total_products = Produit.query.count()

    return render_template('admin/dashboard.html',
                           users=total_users,
                           orders=total_orders,
                           products=total_products)

# Liste des utilisateurs
@admin_bp.route('/utilisateurs')
@login_required
def utilisateurs():
    users = User.query.all()
    return render_template('admin/utilisateurs.html', users=users)

# Liste des produits
@admin_bp.route('/produits')
@login_required
def produits():
    products = Produit.query.all()
    return render_template('admin/produits.html', products=products)
