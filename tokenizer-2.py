#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from keys import *

def getJSON(path, params):
	base_url = "http://api.genius.com"
	headers = {"Authorization" : "Bearer " + geniusAccessKey}
	url = base_url + path
	response = requests.get(url=url, params=params, headers=headers)
	return response.json()

def getArtistId():
	artist_name = raw_input("Enter an artist to search: ")

	params = {"q" : artist_name}
	path = "/search"
	json = getJSON(path=path, params=params)

	return json["response"]["hits"][0]["result"]["primary_artist"]["id"]
	

def getSongs():
	page = 1
	a_id = getArtistId()

	

	song_list = []
	while(1):
		
		params = {"page" : page}
		path = "/artists/{}/songs".format(a_id)
		json = getJSON(path=path, params=params)

		for i in range(len(json["response"]["songs"])):
			song_list.append(json["response"]["songs"][i]["url"])

		if not (json["response"]["next_page"]): 
			break
		page+=1
		

	return song_list

#in progress
def getLyrics():
	songs = getSongs()
	f = open("body-of-text", "a")

	songs = [str(song) for song in songs]

	for song in songs:
		page = requests.get(song)
		soup = BeautifulSoup(page.text, "html.parser")
		lyrics = soup.find_all("div", class_= "lyrics")
		#... parse parse parse
		
		print(lyrics)
		#f.write(lyrics)
	f.close()


getLyrics()



