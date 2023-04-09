from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("login.html")

@app.route("/loginapi", methods=["POST", "GET"])
def loginapi(): 
  return render_template("predict_form.html")


@app.route("/predict", methods=["GET", "POST"])
def predict(): 
  # size= request.form['size']
  # location = request.form['location']
  # email = request.form['email']
  return render_template("result.html")
  

if __name__ == "__main__":
  app.run()
