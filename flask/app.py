from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/flask-health-check')
def flask_health_check():
	return "success"
