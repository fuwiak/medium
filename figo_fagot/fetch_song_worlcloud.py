#-*- coding: utf-8 -*-
#python2.7
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import pandas as pd


URLS = ['https://www.tekstowo.pl/piosenki_artysty,bracia_figo_fagot.html', 
'https://www.tekstowo.pl/piosenki_artysty,bracia_figo_fagot,alfabetycznie,strona,2.html',
'https://www.tekstowo.pl/piosenki_artysty,bracia_figo_fagot,alfabetycznie,strona,3.html']


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
		from BeautifulSoup import BeautifulSoup, NavigableString, Tag
		TXT = []

		URLS = self.text_song_url()

		ind=0
		for URL in URLS:

			

			page = urllib2.urlopen(URL)
			soup = BeautifulSoup(page)
			temp = soup.body.findAll('div', attrs={'class' : 'song-text'})

			
			br_text = temp[0].findAll('br')

			song_text = []
			for br in br_text:
				next_s = br.nextSibling

				if not (next_s and isinstance(next_s,NavigableString)):
					continue
				next2_s = next_s.nextSibling
			   	if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
			   		text = str(next_s).strip()
			   		text_line = text.split("\n")
			   		for line in text_line:
			   			song_text.append(line)

			# print(ss)
			# print(song_text)
			# ind+=1
			TXT.append(song_text)
		return TXT





A = figo_fagot(URLS[0])
B = figo_fagot(URLS[1])
C = figo_fagot(URLS[2])

D = A.text_song()+B.text_song()+C.text_song()

names = A.get_song_name()+B.get_song_name()+C.get_song_name()

df = pd.DataFrame()
df['names']=names
df['text'] = D
df.to_csv("df.csv", encoding = 'utf-8')

# song_all_text = ""
# for text in C:
# 	text = text.replace("Tekst piosenki:","")
# 	text = text.replace("nbsp","")
# 	song_all_text+=text+" "






