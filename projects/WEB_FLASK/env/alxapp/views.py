from flask import Blueprint, render_template, request_tearing_down
from flask import Flask, request, redirect, url_for
from alxapp.models import Profile
from . import db


views = Blueprint ('views',__name__)

@views.route('/dashboard/<int:profile_id>', methods=['GET', 'POST'])
def dashboard(profile_id):
    profile = Profile.query.get(profile_id)
    return render_template('dashboard.html', profile=profile)

    
@views.route('/profile/<int:profile_id>', methods=['GET', 'POST'])
def edit_profile(profile_id):
    profile = Profile.query.get_or_404(profile_id)

    if request.method == 'POST':
        profile.username = request.form['username']
        profile.height = int(request.form['height'])
        profile.weight = float(request.form['weight'])
        profile.complexion = request.form['complexion']
        profile.age = int(request.form['age'])
        profile.bio = request.form['bio']

        # Save the changes to the database
        db.session.commit()

        return redirect(url_for('views.dashboard', profile_id=profile_id))

    return render_template('edit_profile.html', profile=profile)
    



