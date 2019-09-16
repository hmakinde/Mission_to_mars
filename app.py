    # Flask application
# Create a route called /scrape that will import your scrape_mars.py script and call your  scrape function

# Dependencies
import pymongo
import scrape_mars
from flask import Flask, render_template, redirect

# Create flask app
app = Flask(__name__)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_facts


# Create root/index route to query mongoDB and pass mars data to HTML template to display data

@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars.scrape()
    print("\n\n\n")

    db.mars_facts.insert_one(mars)
    return "Some scrapped data"

@app.route("/")
def home():
    mars = list(db.mars_facts.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)

    
    
