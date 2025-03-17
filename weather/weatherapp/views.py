from django.shortcuts import render
import requests
import datetime


# Create your views here.
def index(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'London'
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f2a770be0d56cca953c1b9c5e9ca0ede'
    PARAMS = {'units':'metric'}
    
    data = requests.get(url,PARAMS).json()
    day = datetime.date.today()
    image_url = get_city_image(city)
    print(image_url)
    return render(request, 'index.html', {'data':data, 'city':city, 'day':day, 'image':image_url})
    
    
def get_city_image(city):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": city,
        "cx": '25835f330b1b845d0',
        "key": 'AIzaSyA54ZnzoWkcJ_xksLJ5UugxWVOyiMTQwvo',
        "searchType": "image",
        "num": 1
    }
    response = requests.get(search_url, params=params).json()
    if "items" in response:
        return response["items"][0]["link"]
    return None