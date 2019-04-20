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

@main.route('/pickUpLines/')
def pickUpLines():

    '''
    View categories page function that returns the pickUpLines category details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(pickUpLines)

    return render_template('pickUpLines.html', pitches = pitches)

@main.route('/interview/')
def interview():

    '''
    View categories page function that returns the interview category details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(interview)

    return render_template('interview.html', pitches = pitches)

@main.route('/product/')
def product():

    '''
    View categories page function that returns the product category details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(product)

    return render_template('product.html', pitches = pitches)

@main.route('/promotion/')
def promotion():

    '''
    View categories page function that returns the promotion category details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(promotion)

    return render_template('promotion.html', pitches = pitches)

@main.route('/business/')
def business():

    '''
    View categories page function that returns the business category details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(business)

    return render_template('business.html', pitches = pitches)

@main.route('/tech/')
def tech():

    '''
    View categories page function that returns the tech category details page and its data
    '''

    # category = get_category(name)
    pitches = Pitch.get_pitches(tech)

    return render_template('tech.html', pitches = pitches)

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