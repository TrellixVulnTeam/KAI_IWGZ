from flask import Flask, render_template
from flask_assets import Environment, Bundle


app = Flask(__name__)

assets = Environment()
assets.init_app(app)

css = Bundle('src/css/*.css', filters='postcss', output='static/css/style.css')
assets.register('css', css)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/stream')
def stream():
    return render_template('stream.html')
