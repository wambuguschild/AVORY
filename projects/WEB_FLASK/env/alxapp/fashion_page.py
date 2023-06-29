from flask import Flask, render_template, request, Blueprint
import random
from flask import Flask, request, redirect, url_for

fashion = Blueprint('fashion',__name__)


# Define the available picture options
pictures = {
    'official': [
        {'filename': 'sample1.jpg', 'width': 200},
        {'filename': 'sample2.jpg', 'width': 200},
        {'filename': 'sample3.jpg', 'width': 200}
    ],
    'casual': [
        {'filename': 'sample4.jpg', 'width': 200},
        {'filename': 'sample5.jpg', 'width': 200},
        {'filename': 'sample6.jpg', 'width': 200}
    ]
}


# Define the route for the main page
@fashion.route('/')
def home():
    # Check if the user has clicked on an option
    selected_option = request.args.get('option')
    
    if selected_option in pictures:
        # If an option is selected, display the corresponding pictures
        selected_pictures = pictures[selected_option]
    else:
        # If no option is selected, display random pictures
        selected_pictures = random.choice(list(pictures.values()))

    return render_template('explore.html', pictures=selected_pictures)

# Define the route for the official pictures page
@fashion.route('/official')
def official():
    return render_template('official.html', pictures=pictures['official'])

# Define the route for the casual pictures page
@fashion.route('/casual')
def casual():
    return render_template('casual.html', pictures=pictures['casual'])

