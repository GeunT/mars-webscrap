from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars
from splinter import Browser
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.mars_db

@app.route("/")
def index():
    mars = db.mars_table.find_one()
    return render_template("index.html", mars = mars)


@app.route("/scrape")
def scraper():

    return redirect("/", code=302)
    #return "success"

if __name__ == "__main__":
    app.run(debug=True)
