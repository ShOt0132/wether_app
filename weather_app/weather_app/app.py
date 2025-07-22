import os
import requests
from flask import Flask, render_template, request
from datetime import datetime
from models import db, WeatherQuery

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/weather_db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

API_KEY = os.getenv("API_KEY", "your_openweathermap_api_key")

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("main"):
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            weather = {"city": city, "temp": temp, "desc": description}
            #noqa
            query = WeatherQuery(
                city_name=city,
                temperature=temp,
                description=description,
                timestamp=datetime.utcnow()
            )
            db.session.add(query)
            db.session.commit()
    return render_template("index.html", weather=weather)

@app.route("/history")
def history():
    queries = WeatherQuery.query.order_by(WeatherQuery.timestamp.desc()).all()
    return render_template("history.html", queries=queries)

if __name__ == "__main__":
    app.run(debug=True)
