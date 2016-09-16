import webbrowser


class Movie():
	"""This class stores basic movie information and shows the movie trailer.

	Attributes:
        title: The movies title.
        storyline: The movies storyline (preferably from wikipedia).
        poster_image_url: URL of movie poster (preferably from wikipedia).
        trailer_youtube_url: URL of the movies trailer on youtube.

    Methods:
    	show_trailer(): open webbrowser and show movie trailer

	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""Inits Movie with title, storyline, poster image and trailer url."""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		"""Open Webbrowser and show youtube movie trailer."""
		webbrowser.open(self.trailer_youtube_url)
