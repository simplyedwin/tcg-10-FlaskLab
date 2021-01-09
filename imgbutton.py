from flask import Flask

app = Flask(__name__)

@app.route('/')
def img():
    return '<img src="/workspace/tcg-10-FlaskLab/AlightLiaoLah_Busstop.svg" width="50" height="50">'






if __name__=='__main__':

    app.run(host='localhost',port=8080,debug=True)