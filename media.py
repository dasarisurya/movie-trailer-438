#!/usr/bin/env python
import webbrowser


class Movie():
    '''
      class Movie():
A class movie takes the contents of the movie

Attributes:
    movieName (str): movie name is taken.
    movieStoryline (str): movie Storyline is described.
    posterImage (str): movie posterimage is taken.
    trailerYoutube (str): youtube url is taken.
    '''

    def __init__(self, movieName,
                 movieStoryline, posterImage, trailerYoutube):
        '''movie content'''
        self.title = movieName
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube

    def show_trailer(self):
        '''trailer opens in default browser in the same window'''
        webbrowser.open(self.trailer_youtube_url)
