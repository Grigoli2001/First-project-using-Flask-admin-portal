# First-project-using-Flask-admin-portal

In the beginning of the assignment, I had no Idea how to do it. I did many research and almost every source were suggesting either Django or Flask. Since, some of my classmates were using flask I decided to use flask, because I thought if I get lost, I would ask them to help me. 
The reasons I decided to use flask were:
1.	Learning a new framework, which can be very useful in the real world.
2.	In my opinion, it is way more efficient than writing html pages using python. 
I watched many tutorials about flask but one of the most useful was this -  https://www.youtube.com/watch?v=dam0GPOAvVI&t=6653s 
First thing I did was writing queries, which seemed easy but the database given is not correct, so it made writing queries harder.
I wrote 5 queries in different python files because that was the requirement. I used string formatting to change the values of queries. For example, changing an intake and so on. For connecting database, I used given template using Jaydebeapi. I did not have to set up java environment variable because my h2 file is placed in the same folder as java files. So if you’ll have problem connecting the database that might be an issue. 

Now, I am going to explain my code in details.
1.	Main.py
 
I strictly followed the tutorial I watched; this is typical flask application that creates a flask app. It uses create_app function from the website module. Flask has its debugging application and debug=true enables that. if __name__ == '__main__' statement is used to start the Flask development server when the script is run as the main program.

2.	__init__.py
 

This file defines the create_app () function which creates and configures a Flask app. 
Again, this is flask default code so it is essential for flask. This code is from the same tutorial.

Secret key, is for security. In my case create app registers a blueprint named “root”. 

So, to sum up this __init__.py file is a basic setup for flask.



3.	Root.py
 

This is the main file that I had to write by myself. This is where I connect my database files to html files. Figuring out this part was the hardest thing in this project to me. 
This code looked much more better until I implemented charts. Because of charts I had to create course list with a list of lists. And some for loops in the home function.
Apart from that again, I followed instructions given in tutorials and I managed to connect my database functions to html.

This root.py file is used to pass python functions to html which you can use with jinja. In my case I have 3 routes registered, Home, population and grades.
In the home route I have passed two functions pop and “att” to get the populations and attendance data for each course. And after it renders the home.html template.

In the population route I pass students function as pops (I should have changed the names to make the code more readable but because of time I could not) and courses function as stud.
And I render populations template.

And the last route is grades, where I pass “student grades” function as data and render grades.html template.

If you take a look, you’ll notice that my functions each has 3 parameters, so I am passing parameters from Html to the queries.

4.	Here I am going to explain only 1 database because all of them are same.

 

This is my attendance.py file as you can see it is basically the same as you provided but my query is in a function because to me it seemed easier to pass the values using function and its parameters. 
In general, I know that in a function return should be the last code but for some reason my close functions only works in that position.
As I already explained I used string formatting to change values of queries.

5.	In the html files I used jinja to get values from python files. Jinja is very good tool because it allows you to even use python functions such as loops in html files, which was very useful in my case. 

Since, html files are too big I’ll provide 1 example of each flask element I used.

 

This is how I linked my home page to populations page. I had to manually specify the programs and pass the values. Now that I’m thinking I could have used lists and then loops to do that but since programs are few it still is a good approach.

 

This is how I used my “att” function in html. I just had to pass the arguments and that was it.

To finish my home page, I used chart.js for charts. Which was pretty simple cause codes were given in website.


 

That is where I used pythons for loop to create a table rows. I knew from my queries that I was passing 4 values for each student. So, I just used indexing to get the value.

The other tables work same as this so there is no point of explaining each of them.

Finally, I used CSS to make the pages look good. I wanted to use bootstrap and I know how to use it but in the end I decided to use CSS. My website is not responsive at all, I just did not focus on that because usually I use bootstrap and it takes care of it by itself.

 
Also, I was thinking of adding one more feature to my website which was REGISTER A STUDENT.
But I did not have a time for that. We had so many assignments I hardly had any personal time. 
But this “register a student” would enable admin to add a user in database. I would have created register page and then in the form I would ask admin to input some information, then create a query with insert values and pass the inputted values to that query.

In conclusion this assignment helped me develop new skills such as using flask and jinja helped me understand how does the back-end work and in general it has been very beneficial to me.
I wish to have more assignments like this because in my opinion this is how we study the most efficiently.

 Thank you.
