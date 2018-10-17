from flask import Flask, render_template, request, redirect, jsonify, url_for, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Trainer, TrainerProfile
import os



app = Flask(__name__)


engine = create_engine('sqlite:///trainers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()





@app.route('/home')
def showHomePage():

    return render_template('home1.html')



@app.route('/home/articles/top')
def articlesTop():

    return render_template('topStories.html')

@app.route('/home/articles/second')
def story2():

    return render_template('story2.html')

@app.route('/home/articles/motivation')
def motivation():

    return render_template('motivation_story.html')



@app.route('/home/athletesCelebrities/news')
def news():

    return render_template('news.html')

@app.route('/home/athletesCelebrities/interviews')
def interviews():

    return render_template('interviews.html')

@app.route('/home/athletesCelebrities/girls')
def girls():

    return render_template('girls.html')

@app.route('/home/athletesCelebrities/videos')
def videos():

    return render_template('videos.html')

@app.route('/home/nutrition')
def nutrition():

    return 'This page is for Nutrition'

@app.route('/home/nutrition/healthyrecipes')
def healthyRecipes():

    return render_template('healthy_recipes.html')

@app.route('/home/nutrition/mealplan')
def mealplan():

    return render_template('meal_plan.html')

@app.route('/home/losefat')
def loseFat():

    return render_template('lose_fat.html')

@app.route('/home/nutrition/gainmass')
def gainMass():

    return render_template('gain_mass.html')


@app.route('/home/nutrition/supplement')
def supplement():

    return render_template('supplements.html')

@app.route('/home/features')
def showFeatures():

    return " This page is for Features"    

@app.route('/home/features/gyms')
def showGyms():

    return render_template('gyms.html') 

@app.route('/home/features/Trainers')
def showTrainers():
    trainers = session.query(Trainer).all()
    # return "This page will show all my restaurants"
    return render_template('trainers.html', trainers=trainers)

 

@app.route('/home/features/sportcenters')
def showSportCenters():

    return render_template('sport_centers.html') 

@app.route('/home/features/shops')
def showShops():

    return render_template('shops.html') 

@app.route('/home/features/store')
def store():

    return render_template('store.html') 


@app.route('/home/events')
def events():

    return "This page is for Events"

@app.route('/home/events/event1')
def events1():

    return render_template('event1.html')

@app.route('/home/events/events2')
def events2():


    # return "This page will show all my restaurants"
    return render_template('event2.html')

@app.route('/home/events/events3')
def events3():

    return render_template('event3.html')

@app.route('/home/events/events4')
def events4():

    return render_template('event4.html')

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/home/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names) 

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
