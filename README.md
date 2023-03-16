# projects

Projects contains 10 apps built using python and related frameworks. 

App 1 (volcano-man): creates a web app that uses google maps to supply detail and information on the whereabouts of volcanoes in Continental USA. This is run from the map1.py script, and utilizes the volcanoes.txt file for information. Volcano man uses folium, pandas and Json. 

App 2 (motion-man): a motion tracking app using your computers camera to document any motion discovered in the frame, using the cv2 library. This app compiles that information into a graph using pandas. This script requires both the capturing_video.py script and the Plotting.py script, and is run from Plotting.py. motion man uses cv2, time, pandas and datetime.

App 3 (Data-man): this app displays data retrieved from a CSV file (using pandas) as a series of graphs. This app then creates a locally hosted website using Justpy, and displays the graphs there. This is run from the Data_man.py script, and recieves data from reviews.csv. Data-man uses justpy pandas datetime pytz and matplotlib

App 4 (Web-man): This is a basic website. This was built using the flask web-framework. The code is available to review in Flask_app.py, home.html, layout.html, about.html and main.css.

App 5 (Book-man): Book man runs on SQLite3 and Tkinter and uses a GUI with assigned functions to create a database of books (books.db). Book man then can search and update these entries as required. Book man requires backend.py and book_app.py and runs from book_app.py. Book man uses Tkinter and SQLite3

App 6 (mobile-man): This app runs from main.py within the mobile_app folder. This is a kivy design linked to an object-oriented python file. When run signed up users can see quotes that relate to their mood. This app uses kivy, hoverable and random.

App 7 (webscraper-man): This is a web scraping app relating to a specific website, which reports on the data found on that website. It is run from web_scrape_app.py

App 8 (Data-flask-man): This is a website built using flask which collects data from visitors, and emails them the results of the survey. The related code can be found in the flask_and_databases folder. The app is run from app.py.

App 9 (The novel): This is a django website available on http://nattypaczek.pythonanywhere.com/. It contains the entirety of my first novel, the prince of the ancient forest. The code is available to review in the Django_app folder.

App 10 (independence-man): This app was created independently and is a geocoding website built in flask. Visitors can upload csv files containing addresses, and they will be geocoded, the geocoded addresses will be available to download from the success page on the website.
