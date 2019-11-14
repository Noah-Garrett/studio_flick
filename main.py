from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    movie2 = get_random_movie()
    if movie2 == movie:
        movie2="Rerun of yesterday's movie: " + movie 
    # build the response string
    content ="<img src=https://camo.githubusercontent.com/13810476397f65a733165f312f48db775faa0365/68747470733a2f2f692e696d6775722e636f6d2f3531636354536f2e676966>"
    content += "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    content += "<h3>Tomorrow's Movie</h3>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "</ul>"
    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    movie_list=["The Matrix", "Forgetting Sarah Marshal","Dracula 3000","White Castle","THE EINTRE UNEDITED LORD OF THE RINGS TRILOGY + THE HOBBIT! GET A COMFY CHAIR AND CALL OFF WORK!"]
    rando_num=random.randrange(5)
    rando_flick=movie_list[rando_num]
    return rando_flick


app.run()
