from flask import Flask, render_template, url_for, request, redirect
from word_manager import WordManager

app = Flask(__name__)
word_manager = WordManager()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manage")
def manage():
    words = word_manager.get_words()
    return render_template("manage.html", words=words)

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/api/add", methods=["POST"])
def api_add():
    word_manager.add_word({
        "word": request.form["word"],
        "def": request.form["def"]
    })
    return redirect("/manage")

if __name__ == "__main__":
    app.run(debug=True)