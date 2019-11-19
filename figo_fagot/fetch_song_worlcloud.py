#-*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup
import re
import pandas as pd


URLS = ['https://www.tekstowo.pl/piosenki_artysty,bracia_figo_fagot.html', 
'https://www.tekstowo.pl/piosenki_artysty,bracia_figo_fagot,alfabetycznie,strona,2.html']


class figo_fagot:
	def __init__(self, URL):
		self.URL = URL

	def dane(self):
		page = urllib2.urlopen(self.URL)
		soup = BeautifulSoup(page)
		temp = soup.body.findAll('div', attrs={'class' : 'box-przeboje'})
		return temp

	def get_song_name(self):
		names = []
		page = urllib2.urlopen(self.URL)
		soup = BeautifulSoup(page)
		temp = soup.body.findAll('div', attrs={'class' : 'box-przeboje'})
		for song in temp:
			x = song.text.split(" - ")[1][:-4].strip("(")
			names.append(x)
		return names

	def text_song_url(self):
		text_url = []
		page = urllib2.urlopen(self.URL)
		soup = BeautifulSoup(page)
		temp = soup.body.findAll('div', attrs={'class' : 'box-przeboje'})
		for song in temp:
			url = "https://www.tekstowo.pl"+song.a.get('href')
			text_url.append(url)
		return text_url
	
	def text_song(self):
		text = []
		URLS = self.text_song_url()
		for URL in URLS:
			page = urllib2.urlopen(URL)
			soup = BeautifulSoup(page)
			temp = soup.body.findAll('div', attrs={'class' : 'song-text'})
			song_text = temp[0].text


			text.append(song_text)
		return text




A = figo_fagot(URLS[0])
B = figo_fagot(URLS[1])

C = A.text_song()+B.text_song()


song_all_text = ""
for text in C:
	text = text.replace("Tekst piosenki:","")
	text = text.replace("nbsp","")
	song_all_text+=text+" "






