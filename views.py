from flask import render_template, request
from project_app import app
# import pymysql as mdb
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from doc2vec_model_methods import model_app_results
from doc2vec_model_methods import populate_artist_genres
from doc2vec_model_methods import most_similar_artists
from doc2vec_model_methods import most_similar_artists_w_genre
from api_query import do_en_imgurl_query

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
    # results = model_music([input_add_string, input_subtract_string],app.model)
    results = model_app_results([input_add_string, input_subtract_string],
        app.artist_list,app.genre_lookup,app.model,list_len=8,lower=False)

    # results2 = (results[2][0].decode('utf-8'), results[2][1])
    top_artists = [tup[0] for tup in results] # List of results

    #Query for images
    # img_src_list = do_list_query(top_artists)

    #Query both images and url
    img_url_list = do_en_imgurl_query(top_artists)

    results2 = [[artist.replace('_',' '), imgurl[0], imgurl[1]] for artist, imgurl in zip(top_artists, img_url_list)]

    return render_template("output.html", add_list = input_add_string,
        subtract_list = input_subtract_string, results_list = results2) #, img_src_list = img_src_list)

@app.route('/about')
def about():
    return render_template("about.html")

