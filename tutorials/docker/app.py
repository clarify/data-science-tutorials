from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask
from pyclarify.client import APIClient
from pyclarify.models.data import DataFrame
import requests


SIGNAL_ID = ["temperature_value", "weather_condition"]
API_KEY = "<your-API-key>"
CITY_NAME = "Trondheim"

def main():
   
    client = APIClient("./clarify-credentials.json")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
    response_json = requests.get(url).json()

    # Get local time in ISO 8601
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%Z")
    current_time += "Z" # ADD UTC time offset

    # extract data from API
    temperature = response_json["main"]["temp"]
    weather_condition_enum_number = int(str(response_json["weather"][0]["id"])[0])
    values = [temperature, weather_condition_enum_number]

    # create a data frame model
    series = {}
    for signal_id_, data_ in zip(SIGNAL_ID, values):
        series[signal_id_] = [data_]

    df = DataFrame(times=[current_time], series=series)

    # write signal data to Clarify
    response = client.insert(data=df)
    print(response)


app = Flask(__name__)

sched = BackgroundScheduler(daemon=True)
sched.add_job(main, 'interval', minutes=1)
sched.start()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
