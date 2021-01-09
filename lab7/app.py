from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/about-us')
def aboutus():
    return render_template('aboutus.template.html')


@app.route('/our-product')
def ourproduct():
    return render_template('product.template.html')


if __name__ == '__main__':

    app.run(host='localhost', port=8080, debug=True)
