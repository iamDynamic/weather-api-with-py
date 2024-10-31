from flask import Flask,render_template
import requests
headers = {
    'x-rapidapi-key': "7626dd03femsh15b00c89eeed8cbp185012jsnfa57c8cbd6fe",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com"
}

def ApiFetch():
    
    ApiUrl = "https://open-weather13.p.rapidapi.com/city/italy/EN"
    ApiRes = requests.get(ApiUrl,headers=headers)
    code = ApiRes.json()['cod']
    timezone = ApiRes.json()['timezone']
    name = ApiRes.json()['name']
    temp = ApiRes.json()['main']['temp']
    see_level = ApiRes.json()['main']['sea_level']
    humidity = ApiRes.json()['main']['humidity']
    contry = ApiRes.json()['sys']['country']
    wind_speed = ApiRes.json()['wind']['speed']
    wind_deg = ApiRes.json()['wind']['deg']
    sunsrise = ApiRes.json()['sys']['sunrise']
    sunset = ApiRes.json()['sys']['sunset']
    
    print(code)
    print(timezone)
    print(name)
    print(temp)
    print(see_level)
    print(humidity)
    print(contry)
    print(wind_speed)
    print(wind_deg)
    print(sunsrise)
    print(sunset)
    
ApiFetch()