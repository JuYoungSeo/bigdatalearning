from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 이 객체를 만든다는건 ORM을 사용한다는 의미


@app.route('/')
def homepage():
    return render_template('mainhome.html')

@app.route('/11')
def testpage():
    return render_template('test.html')




if __name__ == '__main__':
    app.run()
