import pandas as pd 
import requests
latitude = float(input())
longitude = float(input())
api_key = input()
response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}&exclude=['current','minutely,'daily','alerts']&units=metric")
d = response.json()["hourly"]            
meta_cols = ["wind_gust","wind_deg","wind_speed","visibility","clouds","uvi","dew_point","humidity","pressure","feels_like","temp","dt"]
df = pd.json_normalize(d,record_path=["weather"],meta=meta_cols)
df['datetime'] = pd.to_datetime(df['dt'], unit='s')
df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
df.drop(["datetime","dt"],inplace=True,axis=1)
df["longitude"]=longitude
df["latitude"]=latitude
df.apply(lambda x: print(x.values), axis=1)
