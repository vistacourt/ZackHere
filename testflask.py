from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    test1='test1'
    test2='test2'
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run()
#hello_world()
