import requests
from bs4 import BeautifulSoup
from keys import *

class GeniusAPIClient:

    def __init__(self):
        pass

    def getJSON(self, path, params):
        base_url = "http://api.genius.com"
        headers = {"Authorization" : "Bearer " + geniusAccessKey}
        url = base_url + path
        response = requests.get(url=url, params=params, headers=headers)
        print("got response")
        return response.json()	
    
    # Execute a search from an artist_name
    def getArtistId(self, artist_name):
        params = {"q" : artist_name}
        path = "/search"
        json = self.getJSON(path=path, params=params)
        return json["response"]["hits"][0]["result"]["primary_artist"]["id"]

    def getSongs(self, artist_name):
            page = 1
            a_id = self.getArtistId(artist_name)

            song_list = []
            while(1):
                
                params = {"page" : page}
                path = "/artists/{}/songs".format(a_id)
                json = self.getJSON(path=path, params=params)

                for i in range(len(json["response"]["songs"])):
                    song_list.append(json["response"]["songs"][i]["url"])

                if not (json["response"]["next_page"]): 
                    break
                page+=1
                

            return song_list

    #refactor to get lyrics from ONE song
    """  def getLyrics(self):
        songs = self.getSongs()
        f = open("body-of-text", "a")

        songs = [str(song) for song in songs]

        for song in songs:
            page = requests.get(song)
            soup = BeautifulSoup(page.text, "html.parser")
            lyrics = soup.find_all("div", class_= "lyrics")
            #... parse parse parse
            
            print(lyrics)
            #f.write(lyrics)
        f.close() """
