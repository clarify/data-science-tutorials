from pyclarify.client import APIClient
from pyclarify.models.data import DataFrame, Signal
import requests
from datetime import datetime
import os
import time
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

SIGNAL_ID_LIST = ["signal_id", "enum_id"]
API_KEY = ""
LOCATION_NAME = "Trondheim"

def get_data():
   
    client = APIClient("./clarify-credentials.json")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={LOCATION_NAME}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    # Get local time in ISO 8601
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%Z")
    current_time += "Z" # ADD UTC time offset

    # extract data from API
    temperature = response["main"]["temp"]
    weather_condition_enum = response["weather"][0]["main"]
    weather_condition_enum_number = int(str(response["weather"][0]["id"])[0])
    values = [temperature, weather_condition_enum_number]

    # create a data frame model
    series = {}
    for signal_id, value in zip(SIGNAL_ID_LIST, values):
        series[signal_id] = [value]

    df = DataFrame(times=[current_time], series=series)


    # write signal data to Clarify
    insert_response = client.insert(data=df)
    # print for logs in Google Cloud
    print(insert_response)

    # add metadata for enums
    enum_signal = Signal(
        name=SIGNAL_ID_LIST[1], 
        type="enum", 
        enumValues={weather_condition_enum_number: weather_condition_enum}
    )

    save_signals_response = client.save_signals(
        inputs={weather_condition_enum_number: enum_signal}, 
        created_only=False
    )
    
    # print for logs in Google Cloud
    print(save_signals_response)

# start background scheduler
sched = BackgroundScheduler(daemon=True)
sched.add_job(get_data,'interval',minutes=1)
sched.start()

# Use flask app to get persistent docker image
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))