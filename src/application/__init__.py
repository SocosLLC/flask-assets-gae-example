#!./env/bin/python

import os
import sys
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))

from flask import Flask, render_template

import assets

app = Flask('application')
# app.config['ASSETS_DEBUG'] = True  # uncomment to not minify assets
app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

assets.init(app)


@app.route('/')
def home():
    return render_template('index.html')

