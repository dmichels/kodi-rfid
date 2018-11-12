import sqlite3, click
from flask import Flask, render_template, request, redirect
from . import db

app = Flask(__name__)

db.init_app(app)


@app.route("/")
def index():
    movies = db.get_db().cursor().execute('SELECT * FROM movies').fetchall()
    return render_template('index.html', movies=movies)

@app.route("/add", methods=["POST"])
def add():
    values = request.form['id'], request.form['description'], request.form['player'], request.form['c_id']
    db.get_db().cursor().execute('INSERT INTO movies (id, description, player, c_id) VALUES(?, ?, ?, ?)', values)
    db.get_db().commit()
    
    return redirect('/')

@app.route("/movies/<movie_id>/delete", methods=["POST"])
def delete(movie_id):
    db.get_db().cursor().execute('DELETE FROM movies WHERE id = ?', (movie_id, ))
    db.get_db().commit()

    return redirect('/')