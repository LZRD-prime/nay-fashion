from flask import Blueprint, redirect, url_for, current_app, request
import stripe

stripe_bp = Blueprint('stripe_bp', __name__, url_prefix='/stripe')

@stripe_bp.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Commande Nay Fashion',
                        },
                        'unit_amount': 2500,  # Montant en centimes (€25.00 ici)
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('main.home', _external=True) + '?success=true',
            cancel_url=url_for('main.home', _external=True) + '?canceled=true',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e), 400
