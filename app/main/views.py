from flask import render_template,request,redirect,url_for,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import Pitch,Comment,User
from .. import db,photos
from .forms import UpdateProfile,PitchForm,CommentsForm




@main.route('/')
def index():
    pitches_list= Pitch.query.all()
    print(pitches_list)
    return render_template('index.html',pitches_list=pitches_list)



@main.route('/new_pitch',methods= ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(pitch=pitch,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html',form=form)


@main.route('/comment/<int:pitch_id>',methods = ['GET','POST'])
@login_required
def add_comment(pitch_id):
    form = CommentsForm()
    pitch = Pitch.query.get(pitch_id)
    comments_list = Comment.get_comments(pitch_id)
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comment()
        return redirect(url_for('.add_comment', pitch_id = pitch_id))
    return render_template('comments.html',form=form,comments_list=comments_list)





@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))




# @main.route('/')
# @login_required
# def update_pitches():
#     return render_template('about.html')

# @main.route('/')
# @login_required
# def upvote_pitch():
#     return render_template('about.html')

# @main.route('/')
# @login_required
# def downvote_pitch():
#     return render_template('about.html')
