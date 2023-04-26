from flask import Flask
from flask import render_template, request, redirect, url_for
import folium
import time 
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("login.html")

@app.route("/loginapi", methods=["POST", "GET"])
def loginapi(): 
  return render_template("predict_form.html")

@app.route("/map_form")
def map_form(): 
    time.sleep(3)
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=13)
    folium.Marker(location=[12.9716, 77.5946], popup='Bangalore').add_to(m)
    m.add_child(folium.LatLngPopup())
    # def on_click(e):
    # lat, lon = e.latlng
    # return redirect(url_for('new_page', lat=lat, lon=lon))
    m.add_child(folium.ClickForMarker())
    map_html = m.get_root().render()
    return render_template("map_form.html", map_html=map_html)

@app.route("/map")
def map(): 
   time.sleep(5)
   return render_template("map.html")


@app.route("/predict", methods=["GET", "POST"])
def predict(): 

  # size= request.form['size']
  # location = request.form['location']
  # bedrooms = request.form['bedrooms']
  # bathrooms = request.form['bathrooms']
  # age = request.form['age']
  # amenities = request.form['amenities']
  # school = request.form['school']
  # data={size: "size", location: "location", bedrooms: "bedrooms", age: "age", amenities: "amenities", school: "school"}
  time.sleep(4)
  return render_template("result.html")

@app.route('/new_page/<float:lat>/<float:lon>')
def new_page(lat, lon):
    # Do something with the lat and lon values
    return render_template('new_page.html')


# @app.route("/predict2", methods=["GET", "POST"])
# def predict2(): 
#   size= request.form['size']
#   location = request.form['location']
#   email = request.form['email']
#   return render_template("result copy.html")
  

if __name__ == "__main__":
  app.run()
