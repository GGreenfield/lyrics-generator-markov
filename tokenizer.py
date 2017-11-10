#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2, random, re

def buildTextData():
	baseUrl = "https://www.azlyrics.com"
	artist = "/d/deathgrips.html"
        page = urllib2.urlopen(baseUrl+artist)
	soup = BeautifulSoup(page)

	songLinks = [link.get('href') for link in soup.find_all('a', href=re.compile('../lyrics/'))]

	for link in songLinks:
		page = urllib2.urlopen(baseUrl+link.replace('..',''))
		soup = BeautifulSoup(page)

		lyrics = str(soup)
		startFlag = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
		lyrics = lyrics.split(startFlag)[1]
		lyrics = lyrics.split('</div>')[0]
		##now replace the html tags and strip
		##for each line add a START and END tag
		##write each line to a file locally
		print(lyrics)

	
#this script only needs to be run once(or whenever the artist releases new music)
#in order to build the body of text from which a frequency table will be built
#and then a markov chain will be implemented
#main
buildTextData()

