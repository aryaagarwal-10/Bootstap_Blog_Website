from flask import Flask, render_template
import requests

posts = requests.get(url="https://api.npoint.io/979ba7c812b305d0a884").json()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/index.html')
def index():
    return render_template("index.html", all_posts=posts)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/bye")
def bye():
    return "bye"


if __name__ == "__main__":
    app.run(debug=True)
