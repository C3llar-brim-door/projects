# projects

Projects contains 5 apps built using python and related frameworks. 

App 1 (volcano-man): creates a web app that uses google maps to supply detail and information on the whereabouts of volcanoes in Continental USA. This is run from the map1.py script, and utilizes the volcanoes.txt file for information. Volcano man uses folium, pandas and Json. 

App 2 (motion-man): a motion tracking app using your computers camera to document any motion discovered in the frame, using the cv2 library. This app compiles that information into a graph using pandas. This script requires both the capturing_video.py script and the Plotting.py script, and is run from Plotting.py. motion man uses cv2, time, pandas and datetime.

App 3 (Data-man): this app displays data retrieved from a CSV file (using pandas) as a series of graphs. This app then creates a locally hosted website using Justpy, and displays the graphs there. This is run from the Data_man.py script, and recieves data from reviews.csv. Data-man uses justpy pandas datetime pytz and matplotlib

App 4 (Web-man): This is a basic website, available at nattypaczek.pythonanywhere.com. This was built using the flask web-framework. The code is available to review in Flask_app.py, home.html, layout.html, about.html and main.css.

App 5 (Book-man): Book man runs on SQLite3 and Tkinter and uses a GUI with assigned functions to create a database of books (books.db). Book man then can search and update these entries as required. Book man requires backend.py and book_app.py and runs from book_app.py. Book man uses Tkinter and SQLite3
