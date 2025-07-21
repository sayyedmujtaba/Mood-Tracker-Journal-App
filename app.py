from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory list to store mood entries.
# Note: This data will be lost when the application restarts.
moods = []

@app.route("/")
def home():
    """Renders the main landing page."""
    return render_template("index.html")

@app.route("/about")
def about():
    """Renders the about page with information about the app."""
    return render_template("about.html")

@app.route("/add-mood", methods=["GET", "POST"])
def add_mood():
    """
    Handles mood submission.
    GET: Displays the form to add a new mood.
    POST: Processes the submitted mood and adds it to the list.
    """
    if request.method == "POST":
        mood = request.form["mood"]
        moods.append(mood)
        return redirect(url_for("show_moods"))
    return render_template("add_mood.html")

@app.route("/moods")
def show_moods():
    """Displays all the moods that have been submitted."""
    return render_template("moods.html", moods=moods)

if __name__ == "__main__":
    # Runs the Flask application with the development server.
    # debug=True enables auto-reloading and a debugger.
    app.run(debug=True)