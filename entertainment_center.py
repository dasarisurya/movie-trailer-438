#!/usr/bin/env python
import media
import fresh_tomatoes

print("Content-type:text/html \n")

# movie, image urls

premam = media.Movie("Pramam", "Love",
                     "https://bit.ly/2IuNNTb",
                     "https://www.youtube.com/watch?v=RZKq166U1pw")

lucy = media.Movie("Lucy", "Scifi",
                   "https://bit.ly/2KHpCxn",
                   "https://www.youtube.com/watch?v=MVt32qoyhi0")

vikramvedha = media.Movie("Vikram vedha", "Crime",
                          "https://bit.ly/2rURLdg",
                          "https://www.youtube.com/watch?v=1sVr-uWZPjE")

rabnebanadijodi = media.Movie("Rab ne bana di jodi", "Love",
                              "https://bit.ly/2IPVsuy",
                              "https://www.youtube.com/watch?v=eBi8syxPd14")

wrongturn = media.Movie("Wrongturn", "crime mystery",
                        "https://bit.ly/2KD8qcq",
                        "https://www.youtube.com/watch?v=NnoaCE1VPgc")

sorcerersapprentice = media.Movie("Sorcerers apprentice", "physics mystery",
                                  "https://bit.ly/2IBomQ0",
                                  "https://www.youtube.com/watch?v=v2uV0_1C4UM")

movies = [premam, lucy, vikramvedha,
          rabnebanadijodi, wrongturn, sorcerersapprentice]
fresh_tomatoes.open_movies_page(movies)
