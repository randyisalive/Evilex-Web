from flask import (
    Flask, request, render_template, session, flash, redirect, url_for
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/TrainingCamp')
def camp():
    return render_template('TrainingCamp.html')

@app.route('/TrainingCamp/animation')
def animation():
    return render_template('TrainingCamp/animation.html')


