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
from bs4 import BeautifulSoup

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

@app.route('/output')
def output():
    #pull from input field name the value
    input_add_string = request.args.get('inputAdd')
    input_subtract_string = request.args.get('inputSubtract')
    radio_option = request.args.get('optionsRadios')

    #check if any inputs
    if not input_add_string and not input_subtract_string:
        key_error = 2
        results2 = []
    else:
        results, key_error = model_app_results(radio_option,app.df_artist_title,
            [input_add_string, input_subtract_string],app.artist_list,
            app.title_list,app.genre_lookup,app.model,list_len=6,lower=False)

    if key_error == 1:
        results2 = results
    elif key_error == 0:
        top_artists = [tup[0] for tup in results] # List of results
        img_url = [app.df_artist_img_txt[app.df_artist_img_txt['artist']==name]['image'].iloc[0] for name in top_artists]
        txt_url = [app.df_artist_img_txt[app.df_artist_img_txt['artist']==name]['text_summary'].iloc[0] for name in top_artists]
        max_text_length = 400
        for i in range(len(txt_url)):
            # Use BeautifulSoup to remove html
            txt_url[i] = BeautifulSoup(txt_url[i]).get_text()
            if len(txt_url[i])> max_text_length:
                txt_url[i] = txt_url[i][:max_text_length] + '...'

        if radio_option == 'optionArtist':
            # Get artist into presentable form:
            results2 = [[artist.replace('_',' ').replace('&amp;','&'), imgurl, txturl] for artist, imgurl, 
                txturl in zip(top_artists, img_url, txt_url)]
        elif radio_option == 'optionAlbum':
            # Get artist into presentable form:
            top_titles = [tup[1] for tup in results] # List of results
            results2 = [[artist.replace('_',' ').replace('&amp;','&'), title.replace('_',' ').replace('&amp;','&'),
                imgurl, txturl] for artist, title, imgurl, txturl in zip(top_artists, top_titles, img_url, txt_url)]

    return render_template("output.html", add_list = input_add_string,
        subtract_list = input_subtract_string, radio_type = radio_option, key_error = key_error, results_list = results2)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/slides')
def slides():
    return render_template("about.html")

