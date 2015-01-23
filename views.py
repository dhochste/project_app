from flask import render_template, request
from project_app import app
# import pymysql as mdb
import json
from doc2vec_model import model_music
# from a_Model import ModelIt #This willbe my model

""" NOT USING MYSQL
with open('doc2vec_music_project2/credentials.json') as credentials_file:
    credentials = json.load(credentials_file)
passwd = credentials['mysql']['password']

db = mdb.connect(user="root", host="localhost", passwd=passwd,
	db="world_innodb", charset='utf8')
"""

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/cont_input')
def cont_input():
    add_string = request.args.get

@app.route('/output')
def output():
    #pull 'ID' from input field and store it
    input_add_string = request.args.get('inputAdd')
    input_subtract_string = request.args.get('inputSubtract')

    #Hard coding
    results = model_music([input_add_string, input_subtract_string],app.model)


    # parse the string

    # use it in the model

    return render_template("output.html", add_list = input_add_string,
        subtract_list = input_subtract_string, results_list = results)

@app.route('/about')
def about():
    return render_template("about.html")

