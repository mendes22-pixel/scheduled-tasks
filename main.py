#Get API Key and latitude and longitude coordinates
API_KEY = os.getenv("api_key")
MY_LAT = 41.402360   #39.768450
MY_LONG = -8.501508  #-86.156212

#Define the "extracting" parameters according to the API
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
#print("Status: ",response.status_code)
weather_data = response.json()

#Check if it will rain based on the id --> If<700 = rain
will_rain = False
for id_condition in weather_data["list"]:
    weather_condition = id_condition["weather"][0]["id"]
    if int(weather_condition) < 700:
        weather_description = weather_data["list"][0]["weather"][0]["description"].title()
        weather_temperature = int(weather_data["list"][0]["main"]["temp_kf"])
        weather_temperature_celsius = (weather_temperature-32)/1.8

        will_rain = True

if will_rain:
    #Set up email adress
    MY_EMAIL = "conta1.python@gmail.com"
    FINAL_EMAIL = "conta2.python@yahoo.com"
    MY_PASSWORD = os.getenv("my_password")

    #Send email
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        msg = EmailMessage()
        msg["From"] = MY_EMAIL
        msg["To"] = FINAL_EMAIL
        msg["Subject"] = "WEATHER CONDITIONS"
        msg.set_content(f'It is going to rain today🌧️\n\nDescription: {weather_description}\nTemperature: {weather_temperature_celsius:.2f}ºC')

        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)
else:
    messagebox.showinfo(title="WEATHER CONDITION 🌤️", message=f'Description: {weather_description}\nTemperature: {weather_temperature:.2f}ºC')
    
