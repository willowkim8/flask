from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, Willow\'s World!'

@app.route('/user')
def user():
    return 'Helle, User!'

if __name__ == '__main__':
    app.run(debug=True)