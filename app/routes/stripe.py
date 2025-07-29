from flask import Blueprint

stripe_bp = Blueprint('stripe', __name__)

@stripe_bp.route('/stripe/test')
def stripe_test():
    return "Stripe test route is working!"