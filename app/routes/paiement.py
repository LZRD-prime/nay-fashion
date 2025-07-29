import stripe
from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash

paiement_bp = Blueprint('paiement', __name__, url_prefix='/paiement')

@paiement_bp.route('/')
def checkout():
    return render_template('paiement/checkout.html', key=current_app.config['STRIPE_PUBLIC_KEY'])

@paiement_bp.route('/charge', methods=['POST'])
def charge():
    stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

    try:
        charge = stripe.Charge.create(
            amount=2000,  # en centimes => 20.00 €
            currency='eur',
            description='Achat Nay Fashion',
            source=request.form['stripeToken']
        )
        flash('Paiement réussi ! Merci pour votre commande.', 'success')
        return redirect(url_for('main.home'))
    except stripe.error.StripeError as e:
        flash(f'Erreur de paiement : {e.user_message}', 'danger')
        return redirect(url_for('paiement.checkout'))
