from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename
from Geo import FelGeo
import pandas as pd

geomethod = FelGeo()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        file=request.files["file"]
        geomethod.encode(file)
        df = pd.read_csv("geocodedfile.csv")
        return render_template("success.html", text = df.to_html(), btn = "download.html")
    return render_template("index.html")

@app.route("/download")
def download():
    return send_file("geocodedfile.csv", as_attachment = True)


if __name__ == "__main__":
    app.debug=True
    app.run()
