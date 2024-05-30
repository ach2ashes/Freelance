import requests
import pandas as pd
latitude = float(input())
longitude = float(input())
start_date = input("start date in format : yyyy-MM-DD")
end_date = input("start date in format : yyyy-MM-DD")
df  = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,rain,windspeed_10m,winddirection_10m,direct_radiation&start_date={start_date}&end_date={end_date}")
response = df.json()
time = response["hourly"]["time"]
temperature_2m= response["hourly"]['temperature_2m']
precipitation_probability= response["hourly"]['precipitation_probability']
rain = response["hourly"]['rain']
windspeed_10m= response["hourly"]['windspeed_10m']
winddirection_10m = response["hourly"]['winddirection_10m']
direct_radiation= response["hourly"]['direct_radiation']
dict = {'time':time,'temperature':temperature_2m,'sun':direct_radiation,'% change of rain':precipitation_probability,'rain':rain,'winddirection':winddirection_10m,'windspeed':windspeed_10m}
dff = pd.DataFrame(dict)
dff[['date','time']]=dff["time"].str.split("T",expand=True)
dff['longitude'] = longitude
dff['latitude'] = latitude
dff.apply(lambda x: print(x.values), axis=1)