#!/usr/bin/env python
# encoding: utf-8
"""
IMDB250TallyDirectors.py

Created by Jin Budelmann on 2012-08-03.
"""

import sys
import os

import json
import urllib2

import operator

from bs4 import BeautifulSoup

def main():
	html = BeautifulSoup(urllib2.urlopen('http://www.imdb.com/chart/top'))
	table = html.find('table')
	print 'Found table'
		
	ids = []
	for link in table.find_all('a'):
		url = link.get('href')
		ids.append( url.split('/')[2] )
	
	print 'Collected ids'
	
	count = 1
	directors = {}
	for id in ids:
		data = json.load(urllib2.urlopen('http://www.imdbapi.com/?i=' + id))
		director = data['Director']
		if (director in directors):
			directors[director] += 1
		else:
			directors[director] = 1
		print 'Collected ' + str(count) + ' directors'
		count += 1
	
	print 'Done\n'
	
	for w in sorted(directors, key=directors.get, reverse=True):
		if (directors[w] > 2):
	  		print w, directors[w]
		else:
			break
	
if __name__ == '__main__':
	main()