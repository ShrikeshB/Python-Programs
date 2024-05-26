from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def home():
    items = ['a','b','c','d']
    return render_template('index_1.html', items = items)

app.run(port = 5001)