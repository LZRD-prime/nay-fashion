import stripe
from flask import Blueprint, render_template, current_app, redirect, url_for

paiement_bp = Blueprint('paiement', __name__, url_prefix='/paiement')

stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

@paiement_bp.route('/')
def checkout():
    return render_template('paiement/checkout.html')

@paiement_bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'Commande Nay Fashion',
                },
                'unit_amount': 2000,  # Montant en centimes : 20,00€
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('main.home', _external=True) + '?success=true',
        cancel_url=url_for('paiement.checkout', _external=True),
    )
    return redirect(session.url, code=303)
