from flask import Flask,render_template,request
import requests 

app=Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    weather_data=None

    if request.method=='POST':
        city=request.form[city]
        api_key='34266ddf1b406ce8e61696389f83c987'
        url=f'https://api.openweathermap.org/2.5/weather?g={city}&appid={api_key}&units=metric'

        response=request.get(url)

    if response.status_code==200:
        data=response.json()
        weather_data={
            'city':city,
            'temperature':data['main']['temp'],
            'description':data['weather'][0]['description']
        }
    else:
        weather_data=['error: City not found or Api error']

    return render_template('index.html', weather=weather_data)

