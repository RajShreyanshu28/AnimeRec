from flask import Flask, render_template, request

import anime_rec as ar

app = Flask(__name__, static_folder='static')

@app.route("/", methods = ['POST', 'GET'])

def hello():
    recommended_movies = []
    if request.method == "POST":
        moviename = request.form['animename']
        rec = ar.recommend(moviename)
        
        if not rec:
            print(f"No recommendations found for {moviename}.")
            recommended_movies = []
        else:
            print(f"Recommended movies for {moviename}: {rec}")
            recommended_movies = rec

    return render_template("Firstpage.html", recommended_movies = recommended_movies)

if __name__ == "__main__":
    app.run(debug = True)
# @app.route("/sub" ,methods = "POST")
# def submit():
#     # html to python conversion
#     if request.method == "POST":
#         name = request.form["animename"]
    
#     # python to html
#     return render_template("Secondpage.html", n = name)





