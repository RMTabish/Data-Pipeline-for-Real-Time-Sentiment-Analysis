import requests
city = "Berlin"
country = "DE"
weather = requests.get(f'http://api.openweathermap.org/data/2.5/forecast/?q={city},{country}&appid={OWM_key}&units=metric&lang=en')
#get yout own key 
