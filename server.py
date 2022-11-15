# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16283278#notes

from flask import Flask

app = Flask(__name__)  # we are creating an object of Flask and __name__ here is file name i.e main file in this script

'''app.route is decorator. / represents whatever until the first slash i.e., http://127.0.0.1:5000/ in our case.
 When this module is run then this hello world method runs when '''
@app.route("/")
def hello_world():
    return "<p>Welcome to Sridhar's web portfolio -->  HELLOOO there !</p>"
