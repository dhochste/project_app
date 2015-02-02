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
from doc2vec_model_methods import parse_list
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

    results, key_error = model_app_results(app.df_artist_title,
        [input_add_string, input_subtract_string],app.artist_list,
        app.title_list,app.genre_lookup,app.model,list_len=6,lower=False)

    if key_error:
        results2 = results
    else:
        top_artists = [tup[0] for tup in results] # List of results
        img_url = [app.df_artist_img_txt[app.df_artist_img_txt['artist']==name]['image'].iloc[0] for name in top_artists]
        txt_url = [app.df_artist_img_txt[app.df_artist_img_txt['artist']==name]['text_summary'].iloc[0] for name in top_artists]
        max_text_length = 430
        for i in range(len(txt_url)):
            if len(txt_url[i])> max_text_length:
                txt_url[i] = txt_url[i][:max_text_length] + '...'
        # Get artist into presentable form:
        results2 = [[artist.replace('_',' ').replace('&amp;','&'), imgurl, txturl] for artist, imgurl, txturl in zip(top_artists, img_url, txt_url)]


    # Get the images and text
    # #Query for images
    # # img_src_list = do_list_query(top_artists)

    # #Query both images and url
    # img_url_list = do_en_imgurl_query(top_artists)

    # results2 = [[artist.replace('_',' '), imgurl[0], imgurl[1]] for artist, imgurl in zip(top_artists, img_url_list)]
    # add_terms, sub_terms = parse_list([input_add_string, input_subtract_string])

    return render_template("output.html", add_list = input_add_string,
        subtract_list = input_subtract_string, results_list = results2) #, img_src_list = img_src_list)

@app.route('/about')
def about():
    return render_template("about.html")

