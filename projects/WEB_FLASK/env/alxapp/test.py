from alxapp import *
from alxapp.models import Profile

def seed_database():
    # Create instances of Profile model with data
    profile1 = Profile(username='user1', height=180, weight=70, complexion='Fair', age=25, bio='Profile 1 bio')
    profile2 = Profile(username='user2', height=170, weight=65, complexion='Medium', age=30, bio='Profile 2 bio')

    # Add instances to the session
    db.session.add(profile1)
    db.session.add(profile2)

    # Commit the changes to the database
    db.session.commit()
    print('Database seeding completed.')

# Create the Flask application
app = create_app()

# Initialize the database
#db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Seed the database with data
with app.app_context():
    seed_database()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
