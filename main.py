import sqlite3
from datetime import datetime
from weather_api import get_weather
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    weather_data = True
    a = 5
    if request.method == "POST":
        city = request.form['city']
        if city:
            weather_data = get_weather(city)
    return render_template('asdasasds.html', weather_data=weather_data)





if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)

