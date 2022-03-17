from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/artist')
def topartist():
    names = ['Beyonce', 'Rihanna', 'Nicki Minaj', 'Drake', "Cardi B"]
    return render_template('artist.html',top_artist=names)


@app.route('/movies')
def topmovies():
    names = ['Hangover', 'Dream Girls', 'Norbit', 'Sinister', 'Jeepers Creepers']
    return render_template('movies.html',top_movies=names)