import webbrowser    #webbrowser file is imported

class Movie():        #i have created a class named as Movie so to access my instances
    """ this is a class named Movie """
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):   #i have called init function which is inside the class ,here self is the default value
        self.title = movie_title                                                      #self.title stores the movie title
        self.storyline = movie_storyline                                              #self.storyline stores the story about movie
        self.poster_image_url = poster_image                                          #self.poster_iamge_url stores the omage of the movie 
        self.trailer_youtube_url = trailer_youtube                                    #self.trailer_youtube_url stores the movie trailer directly linked from youtube.

    def show_trailer(self):                                                           # a function defined to show the trailer of the particular movie selected
        webbrowser.open(self.trailer_youtube_url)                                      #it opne the movie trailer.
        
