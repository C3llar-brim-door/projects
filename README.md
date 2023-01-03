# projects

Projects contains 4 apps built using python and related frameworks. 

App 1 (volcano-man): creates a web app that uses google maps to supply detail and information on the whereabouts of volcanoes in Continental USA. This is run from the map1.py script, and utilizes the volcanoes.txt file for information.

App 2 (motion-man): a motion tracking app using your computers camera to document any motion discovered in the frame, using the cv2 library. This app compiles that information into a graph using pandas. This script requires both the capturing_video.py script and the Plotting.py script, and is run from Plotting.py.

App 3 (Data-man): this app displays data retrieved from a CSV file (using pandas) as a series of graphs. This app then creates a locally hosted website using Justpy, and displays the graphs there. This is run from the Data_man.py script, and recieves data from reviews.csv. 

App 4 (Web-man): This is a basic website, available at nattypaczek.pythonanywhere.com. This was built using the flask web-framework. The code is available to review in Flask_app.py, home.html, layout.html, about.html and main.css.
