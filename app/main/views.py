from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import Pitch
from .forms import PitchForm


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Make the right first impression"
    return render_template('index.html', title = title)

@main.route('/categories/')
def categories():

    '''
    View categories page function that returns the categories details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(categories)

    return render_template('categories.html', pitches = pitches)

# @main.route('/category/pitch/new/<name>', methods = ['GET','POST'])
# def new_pitch(name):
#     form = PitchForm()
#     # category = get_category(name)

#     if form.validate_on_submit():
#         pitch = form.pitch.data
#         postedOn = form.date.data
#         new_pitch = Pitch(pitch, postedOn)
#         new_pitch.save_pitch()
#         return redirect(url_for('.category',name = category.name ))

#     title = f'{category.name} pitch'
#     return render_template('new_pitch.html',title = title, pitch_form = form, category=category)

    # self, author, category_name, pitch, PostedOn, upVote, downVote