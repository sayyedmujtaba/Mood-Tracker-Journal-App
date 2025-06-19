from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

moods = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add-mood", methods=["GET", "POST"])
def add_mood():
    if request.method == "POST":
        mood = request.form["mood"]
        moods.append(mood)
        return redirect(url_for("show_moods"))
    return render_template("add_mood.html")

@app.route("/moods")
def show_moods():
    return render_template("moods.html", moods=moods)

if __name__ == "__main__":
    app.run(debug=True)