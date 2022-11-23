from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<username>')
def hello_world(username=None):
    return render_template('index.html', name=username)

# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


@app.route("/blog")
def blog():
    return 'these are my thoughts on blogs!'


@app.route("/blog/2022/dogs")
def blog2():
    return 'this is my dog!'


@app.route("/web")
def htmlsample():
    return render_template('index.html')


@app.route("/about.html")
def htmlsample2():
    return render_template('about.html')
