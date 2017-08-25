import media               #medial file is imported which we hav created earlier
import fresh_tomatoes      #file name as fresh_tomatoes has been imported so that all the data here can be stored in that file so we can view it on a webpage

toy_story = media.Movie("Toy story","A story of boy","1.jpeg","https://www.youtube.com/watch?v=KYz2wyBy3kc")    #toy_story instance of class named media is created


avatar = media.Movie("Avatar","A marine on alien planet","new2.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")  #avatar instance of class named media is created


American_pie = media.Movie("American Pie","stroty of 4 friends","3.jpg","https://www.youtube.com/watch?v=Sithad108Og")   #American_pie instance of class named media is created


inception = media.Movie("Inception","stroty of 4 friends","4.jpg","https://www.youtube.com/watch?v=YoHD9XEInc0")     #inception instance of class named media is created


hello_bro = media.Movie("Hello brother","stroty of 4 friends","6.jpg","https://www.youtube.com/watch?v=KWueu0lz5TM")#hello_brother instance of class named media is created

 
dhoni = media.Movie("M.S Dhoni","stroty of 4 friends","5.jpg","https://www.youtube.com/watch?v=6L6XqWoS8tw")   #dhoni instance of class named media is created

 
movies = [toy_story,avatar,American_pie,inception,hello_bro,dhoni]   #arrays of movies is created
fresh_tomatoes.open_movies_page(movies)           #file named fesh tomatoes called and open the array nameda as movies


