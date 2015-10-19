import media
import fresh_tomatoes

interstellar = media.Movie("Intersteller", "The End of Earth Will Not Be the End of Us","http://www.cinemablend.com/images/news/67232/_1410876434.jpg", "https://www.youtube.com/watch?v=0vxOhd4qlnA")
watchmen = media.Movie("Watchmen", "Who Watches the Watchmen?", "http://www.watchmencomicmovie.com/posters/watchmen-theatrical-poster-big.jpg", "https://www.youtube.com/watch?v=R3orQKBxiEg")
knight = media.Movie("The Dark Knight", "Welcome to a World Without Rules", "https://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [interstellar, watchmen, knight]
fresh_tomatoes.open_movies_page(movies)
