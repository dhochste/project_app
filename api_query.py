"""
Querying Google's Freebase API

David L. Hochestetler
1/26/15

"""

import json
import requests
import sys
import time

with open('doc2vec_music_project2/credentials.json') as credentials_file:
    credentials = json.load(credentials_file)
api_key = credentials['echonest_api']['api_key']

service_url = 'http://developer.echonest.com/api/v4/artist/images?'

def do_list_query(artist_list, service_url=service_url, api_key=api_key, limit = 1):

	img_src_list = []

	for name in artist_list:

		# Covert artist name to format for echonest
		name = name.replace(' ','+')
		full_url = service_url+'api_key='+api_key+'&name='+name+'&results=1'
		r = requests.get(full_url)
		response = r.json()

		#Get the image
		try:
			img_src = str(response[u'response'][u'images'][0][u'url'])
			img_src.encode('ascii','ignore')
		except:
			img_src = 'http://cdns2.freepik.com/free-photo/cool-music-theme-vector--3_15-13638.jpg'

		img_src_list.append(img_src)

	return img_src_list
