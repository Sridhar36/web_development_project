# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16283278#notes

from flask import Flask, render_template

# render_template - allows to send the html files
app = Flask(__name__)  # we are creating an object of Flask and __name__ here is file name i.e main file in this script

'''app.route is decorator. / represents whatever until the first slash i.e., http://127.0.0.1:5000/ in our case.
 When this module is run then this hello world method runs when '''


@app.route("/")
def hello_world():
    return "<p>Welcome to Sridhar's web portfolio -->  HELLOOO there !</p>"


@app.route("/blog")
def blog():
    return 'these are my thoughts on blogs!'


'''http://127.0.0.1:5000/blog now this works'''


@app.route("/blog/2022/dogs")
def blog2():
    return 'this is my dog!'


# in order to send the html files
@app.route("/web")
def htmlsample():
    return render_template('index.html')

# note: render_template by default looks for files in templates folder
# we have to store the files under template folder only in order for this method to work

@app.route("/about.html")
def htmlsample2():
    return render_template('about.html')

'''to add CSS and Javascript:
static files - these are files that will never change..
like CSS and JS files once we send them out usually wont change.
we have to have these static files under static folder
note - make sure you update html file with the correct path,.
'''

'''favicon: can be used to have icon on tab
should be added using link text in html, under head tags
'''
