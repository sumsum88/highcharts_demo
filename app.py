#!/usr/bin/env python # coding: utf-8
import sys

from flask import Flask, render_template
from flask import request, jsonify, url_for, redirect
from process import format_for_highcharts

app = Flask(__name__)
app.config['DEBUG'] = True

import pandas as pd


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/graph", methods=['GET'])
def graph():
    df = pd.read_csv('sample.csv', index_col=0)
    return jsonify(format_for_highcharts(df))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)