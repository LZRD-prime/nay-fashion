from .extensions import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='client')

    def __repr__(self):
        return f"<User {self.email} - {self.role}>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    prix = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Produit {self.nom} - {self.prix}€>"
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_commande = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Order {self.id} - Total : {self.total}€>"
