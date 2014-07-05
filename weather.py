import json
import urllib.request as url
import math

#pushes time and temperature once a second.
#Queries the weather database once every three minutes
#Waits for certain flag bytes from the Arduino



API_KEY = '' #Aqcuire from weather.com by signing up for free account

def make_request(key,features,query,_format = '.json'):

    '''Sends the http get request to the server.  Key is the API key,
that is defined above.  Features is an iterable of strings.
query, and optionally format are just strings.
matching the API's description. '''

    feature_string = '/'.join(features)

    full_string = r'http://api.wunderground.com/api/' + \
                  API_KEY + '/' + \
                  feature_string + '/' + \
                  'q/' + \
                  query + \
                  _format

    #later I should double check that the weather api isn't giving
    #me an error regarding too many calls.
    #For now, its enough to call it at most every 3 mins,
    
    result = url.urlopen(full_string)
    return result

def weather_now():

    result = make_request(API_KEY,['conditions'],'11727')

    result = result.read().decode()
    result = json.loads(result)

    stuff = result['current_observation']

    temperature = str(math.floor(stuff['temp_f']))
    weather = str(stuff['weather'])
    

    return temperature,weather

if __name__ == '__main__':
    #for debugging
    a,b = weather_now()
    print(a)
    print(b)
