from flask import render_template,request,redirect,url_for,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import Pitch
from .. import db




@main.route('/')
def index():
      
  
    return render_template('index.html')



@main.route('/')
@login_required
def add_pitches():
    return render_template('about.html')

@main.route('/')
@login_required
def add_comments():
    return render_template('about.html')

@main.route('/')
@login_required
def update_pitches():
    return render_template('about.html')

@main.route('/')
@login_required
def upvote_pitch():
    return render_template('about.html')

@main.route('/')
@login_required
def downvote_pitch():
    return render_template('about.html')
