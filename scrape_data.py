#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:01:19 2017

@author: tianyunan
"""

import requests
from bs4 import BeautifulSoup
import json
import omdb

MOVIE = ["zoolander_2",
         "moonlight_2016",
         "the_finest_hours",
         "florence_foster_jenkins_2016",
         "hell_or_high_water",
         "the_forest_2016",
         "ben_hur_2016",
         "bridget_joness_baby_2016",
         "kevin_hart_what_now"
         ]
MOVIE_NAME = ["Zoolander 2",
              "Moonlight",
              "The Finest Hours",
              "Florence Foster Jenkins",
              "Hell or High Water",
              "The Forest",
              "Ben-Hur",
              "Bridget Jones's Baby",
              "Kevin Hart: What Now?"
              ]

file = open ('91-100.json','w')

for movie in MOVIE:
    index = MOVIE.index(movie)
    movie_name = omdb.title(MOVIE_NAME[index])
    
    for index in range(1,52):
        resp = requests.get('https://www.rottentomatoes.com/m/' + movie + '/reviews/?page='+ str(index)+'&type=user&sort=')
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.title.string
        mydiv = soup.findAll("div",{"class":"user_review"})
        for res in mydiv:
            individual = str(res.text.encode('utf-8'))
            data = {
            "Title": movie_name.title,
            "Year": movie_name.year,
            "Rated": movie_name.rated,
            "Released": movie_name.released,
            "Runtime": movie_name.runtime,
            "Genre": movie_name.genre,
            "Director": movie_name.director,
            "Actors": movie_name.actors,
            "Country": movie_name.country,
            "Poster": movie_name.poster,
            "Ratings": movie_name.imdb_rating,
            "ReviewText": individual }
            json_str = json.dumps(data)
            file.write(json_str)
            file.write('\n')
    file.write('\n')

file.close()
