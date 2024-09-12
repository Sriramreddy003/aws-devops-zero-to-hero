from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'big black monkey boy (guna)!'

if __name__ == '__main__':
    app.run()

