from flask import Flask
from flask import render_template, request, jsonify
from euroMarkov import EuroMarkov
import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/')
#@app.route('/hello/<name>')
def root():
    countryList = request.values.getlist("country")
    euroMarkov = EuroMarkov()
    countries = euroMarkov.generateCountryList()
    return render_template('index.html',countryList=countries)


@app.route('/generate', methods=["POST"])
def generate():
    startYear = int(request.form.get("startYear"))
    endYear = int(request.form.get("endYear"))
    countryList = request.values.getlist("country")
    euroMarkov = EuroMarkov()
    model = euroMarkov.loadFiles(startYear,endYear,countryList)
    euroMarkov.runMarkov(model)
    songTitle = euroMarkov.generateString()
    songLyrics = "<p>"
    for i in range(16):
        songLyrics += euroMarkov.generateString() +"<br />"
        if i%4==3:
            songLyrics += "</p><p>"
    songLyrics += "</p>"
    return jsonify(songTitle= songTitle, songLyrics=songLyrics)
	

if __name__ == '__main__':
    app.debug=True
    app.run()

