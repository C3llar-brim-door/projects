from capturing_video import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")



cds = ColumnDataSource(df)

f = figure(x_axis_type = "datetime" , height = 200 , width = 500 , title = "Movement within frame")
f.yaxis.minor_tick_line_color = None
f.ygrid[0].ticker = None

hover = HoverTool(tooltips = [("Start: " , "@Start_string"), ("End: " , "@End_string")])
f.add_tools(hover)

q = f.quad(left = "Start_string", right = "End_string" , bottom = 0 , top = 1 , color = "red", source = cds)

output_file("Graph.html")
show(f)
