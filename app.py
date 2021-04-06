from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)

   return redirect("http://localhost:5000/", code=302)
   
<<<<<<< HEAD
if __name__ == "__main__":
      app.run(debug=True)
=======
   if __name__ == "__main__":
<<<<<<< HEAD
      app.run(debug=True)
=======
      app.run()
>>>>>>> 48fd4b821637c063f23052f057212b5760d5512d
>>>>>>> c7c3598eac35f3d5931e711a33cf88ed91f758e6
