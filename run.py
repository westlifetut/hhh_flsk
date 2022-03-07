from flask import Flask, Blueprint, render_template

app = Flask(__name__)

blueprint = Blueprint('hhh_blueprint', __name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login')
def login():
    """
    学生登录页面
    :return:
    """
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
