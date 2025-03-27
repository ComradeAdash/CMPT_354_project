from flask import Flask, render_template, url_for
from modules.db import * 
from modules.routes import *  

app = Flask(__name__) 
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)