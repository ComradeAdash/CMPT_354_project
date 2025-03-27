# ----------------------------
# Query logic & Requests
# ----------------------------
from flask import Flask, render_template, url_for

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html', template_folder='../templates')