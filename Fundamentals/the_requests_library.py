import requests

def getWeather(query):
    key = "&appid=90624cc9255f43fb0afc02b5a0ca2d75";
    api = "http://api.openweathermap.org/data/2.5/weather?q="
    url = api+query+key
    res = requests.get(url)

    def kelToFahr(kel):
        return 9/5*(kel-273)+32

    curStr = ""
    for i in res:
        for j in i:
            curStr += j
    curStr = curStr.split(',')

    state    = curStr[25]
    stateStr = ""
    for i in range(8,16):
        stateStr += state[i]

    temp  = list(curStr[7])
    fahr = ""
    for i in range(15,21):
        fahr += temp[i]
    fahr = kelToFahr(float(fahr))
    
    print "Location:",stateStr," | ","Temperature:",fahr
getWeather("Maryland")