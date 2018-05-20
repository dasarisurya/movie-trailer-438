#!/usr/bin/env python
import webbrowser
print("Content-type:text/html \n")


class Movie():
    '''
      movie class is defined
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
