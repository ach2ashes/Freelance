import requests
import pandas as pd
from datetime import datetime, timedelta
import mysql.connector
import time

# Initialize the array for the first run
data_array = []

while True:
    start_date = datetime.today().strftime('%Y-%m-%d')
    end_date = (datetime.today()+timedelta(days=3)).strftime('%Y-%m-%d')

    latitude = 52.63
    longitude = 4.75

    df = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,rain,windspeed_10m,winddirection_10m,direct_radiation&start_date={start_date}&end_date={end_date}")

    response = df.json()

    tijd = response["hourly"]["time"]
    temperature_2m = response["hourly"]['temperature_2m']
    precipitation_probability = response["hourly"]['precipitation_probability']
    rain = response["hourly"]['rain']
    windspeed_10m = response["hourly"]['windspeed_10m']
    winddirection_10m = response["hourly"]['winddirection_10m']
    direct_radiation = response["hourly"]['direct_radiation']
    
    # Create a new dataframe for the current data
    dict = {'tijd': tijd, 'temperature': temperature_2m, 'sun': direct_radiation, '% change of rain': precipitation_probability, 'rain': rain, 'winddirection': winddirection_10m, 'windspeed': windspeed_10m}
    dff = pd.DataFrame(dict)
    dff[['date', 'tijd']] = dff["tijd"].str.split("T", expand=True)
    dff['longitude'] = longitude
    dff['latitude'] = latitude

    # Check if there are changes in the rows compared to the previous run
    for index, row in dff.iterrows():
        # Search for the row in the array
        row_found = False
        for prev_row in data_array:
            if prev_row['date'] == row['date'] and prev_row['tijd'] == row['tijd']:
                row_found = True
                # Check if the values have changed
                if prev_row['temperature'] != row['temperature'] or prev_row['sun'] != row['sun'] or prev_row['% change of rain'] != row['% change of rain'] or prev_row['rain'] != row['rain'] or prev_row['winddirection'] != row['winddirection'] or prev_row['windspeed'] != row['windspeed']:
                    # Update the row in the array with the new values
                    prev_row.update(row)
                    # Print the changed row
                    print(prev_row['longitude'], prev_row['date'], prev_row['tijd'], prev_row['temperature'], prev_row['sun'], prev_row['% change of rain'], prev_row['rain'], prev_row['winddirection'], prev_row['windspeed'])
                break

        # If the row is not found in the array, add it to the array and print it
        if not row_found:
            data_array.append(row.to_dict())
            print(row['longitude'], row['date'], row['tijd'], row['temperature'], row['sun'], row['% change of rain'], row['rain'], row['winddirection'], row['windspeed'])

    time.sleep(100)
