#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2, random, re

#Obtain list of links
#Iterate through each link and save lyrics line by link with START and END tokens
def buildTextData():
	baseUrl = "https://www.azlyrics.com"
	artist = "/d/deathgrips.html"
        page = urllib2.urlopen(baseUrl+artist)
	soup = BeautifulSoup(page)

	songLinks = [link.get('href') for link in soup.find_all('a', href=re.compile('../lyrics/'))]

	for link in songLinks:
		page = urllib2.urlopen(baseUrl+link.replace('..',''))
		soup = BeautifulSoup(page)
		lyrics = [lyric for lyric in soup.find_all('div')]
		print(lyrics[21])

#main
buildTextData()

