from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home_template.html')


@app.route('/say-hi')
def greetings():
    firstname = "Edwin"
    lastname = "Ng"
    today = datetime.now()
    return render_template('greetings.template.html', f=firstname, l=lastname, dt=today)


@app.route('/say-hi/<username>/<sur>')
def wishing(username, sur):
    return render_template('greetings.template.html', f=username, l=sur, dt=datetime.now())


@app.route('/add/<n1>/<n2>')
def sumall(n1, n2):
    return render_template('sum.template.html', tsum=int(n1)+int(n2))


if __name__ == '__main__':

    app.run(host='localhost', port=8080, debug=True)
