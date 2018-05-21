#!/usr/bin/env python
import media
import fresh_tomatoes

# movie, image urls

premam = media.Movie("Pramam", "Love",
                     "https://bit.ly/2IuNNTb",
                     "https://www.youtube.com/watch?v=RZKq166U1pw")

lucy = media.Movie("Lucy", "Scifi",
                   "https://bit.ly/2KHpCxn",
                   "https://www.youtube.com/watch?v=MVt32qoyhi0")

vikramvedha = media.Movie("Vikram vedha", "Crime",
                          "https://bit.ly/2kcWNhf",
                          "https://www.youtube.com/watch?v=1sVr-uWZPjE")

rabnebanadijodi = media.Movie("Rab ne bana di jodi", "Love",
                              "https://bit.ly/2IPVsuy",
                              "https://www.youtube.com/watch?v=eBi8syxPd14")

wrongturn = media.Movie("Wrongturn", "crime mystery",
                        "https://bit.ly/2IC61C7",
                        "https://www.youtube.com/watch?v=NnoaCE1VPgc")

sorcerersapp = media.Movie("Sorcerers apprentice", "physics mystery",
                                  "https://bit.ly/2IBomQ0",
                                  "https://www.youtube.com/watch?v=v2uV0_1C4UM")

movies = [premam, lucy, vikramvedha,
          rabnebanadijodi, wrongturn, sorcerersapp]
fresh_tomatoes.open_movies_page(movies)
