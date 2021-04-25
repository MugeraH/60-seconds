from flask import render_template,request,redirect,url_for,request,redirect,url_for
from . import main
# from ..models import Todo
# from .. import db




@main.route('/')
def index():
   
  
    return render_template('index.html')



# @main.route('/about')
# def about():
#     return render_template('about.html')
