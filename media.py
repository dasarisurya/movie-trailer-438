#!/usr/bin/env python
print("Content-type:text/html \n")

import webbrowser

class Movie():

    def __init__(self,movieName,
                 movieStoryline, posterImage,trailerYoutube):
        self.title = movieName
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
