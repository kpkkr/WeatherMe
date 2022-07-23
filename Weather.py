# import Flask
from flask import Flask, render_template, request
import requests

# create object of flask
app = Flask(__name__)

# create a homepage using @app.route decorator
@app.route('/')
def home():
    return render_template('input.html')
    return render_template('style.css')

# create submit page and accept the data using request
@app.route('/submit', methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        result = request.form 

        # call to the weather api
        params = {'q': result['city'],'units':'metric','appid':''}
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        response = requests.get(url = url, params = params)
        data = response.json()
        # data to be passed - city, temp, feels like, weather, windspeed
        d_result = {'city': result['city'], 'temp': data['main']['temp'], 'feels_like': data['main']['feels_like'], 'weather': data['weather'][0]['description'], 'wind': data['wind']['speed'],'icon' : data['weather'][0]['icon']}
        return render_template('display.html',result=d_result)
        return render_template('styles.css')
    else:
        return 'Invalid request'

# run the web application
if __name__ == '__main__':
    app.run(debug=True)