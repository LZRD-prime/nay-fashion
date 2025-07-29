# app/auth/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.extensions import db, bcrypt
from flask_login import login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Connexion réussie', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Email ou mot de passe incorrect', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Déconnecté avec succès", "info")
    return redirect(url_for('main.home'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password, role='client')
        db.session.add(user)
        db.session.commit()
        flash('Compte créé ! Vous pouvez maintenant vous connecter.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
