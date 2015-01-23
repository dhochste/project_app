from flask import render_template, request
from project_app import app
import pymysql as mdb
import json
from doc2vec_model import model_music
# from a_Model import ModelIt #This willbe my model

with open('doc2vec_music_project2/credentials.json') as credentials_file:
    credentials = json.load(credentials_file)
passwd = credentials['mysql']['password']

db = mdb.connect(user="root", host="localhost", passwd=passwd,
	db="world_innodb", charset='utf8')

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/output')
def output():
    #pull 'ID' from input field and store it
    input_string = request.args.get('ID')

    #Hard coding
    results = model_music('',app.model)


    # parse the string

    # use it in the model

    return render_template("output.html", results_list = results)

@app.route('/about')
def about():
    return render_template("about.html")

