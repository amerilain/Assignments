from flask import Flask, requests

app = Flask(__name__)
@app.route('/prime')
def prime():