from flask import Flask
app = Flask('test')


@app.route('/')
def index():
    return "<h1>Hello World!</h1>"
