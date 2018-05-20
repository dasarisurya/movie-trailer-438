#!/usr/bin/env python
print("Content-type:text/html \n")

import surya
import fresh_capeta


premam = surya.Movie("Pramam", "Love",
                     "https://sharestills.com/posters/telugu/"
                     "premam-telugu-movie-posters/premam-telugu-movie-posters-1.jpg",
                     "https://www.youtube.com/watch?v=RZKq166U1pw")
lucy = surya.Movie("Lucy", "Scifi",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9HBSR7mUyg6CJDOu-SHUhVb0h8_iEUWDqop3ipYLeuQJGOeJm",
                     "https://www.youtube.com/watch?v=MVt32qoyhi0")
vikramvedha = surya.Movie("Vikram vedha", "Crime",
                     "https://timesofindia.indiatimes.com/thumb/61203195.cms?width=219&height=317&imgsize=48878",
                     "https://www.youtube.com/watch?v=1sVr-uWZPjE")
rabnebanadijodi = surya.Movie("Rab ne bana di jodi", "Love",
                     "https://alchetron.com/cdn/Rab-Ne-Bana-Di-Jodi-images-1d3ca203-b3a8-4fbe-b275-7303a77bfdd.jpg",
                     "https://www.youtube.com/watch?v=eBi8syxPd14")
wrongturn = surya.Movie("Wrongturn", "crime mystery",
                     "https://media-cache.cinematerial.com/p/500x/lmv2kd7w/wrong-turn-3-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=NnoaCE1VPgc")
sorcerersapprentice = surya.Movie("Sorcerers apprentice", "physics mystery",
                     "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-qtxkpo_f075f6b3.jpeg?region=0%2C0%2C1578%2C2213",
                     "https://www.youtube.com/watch?v=v2uV0_1C4UM")
movies=[premam,lucy,vikramvedha,rabnebanadijodi,wrongturn,sorcerersapprentice]
fresh_capeta.open_movies_page(movies)

