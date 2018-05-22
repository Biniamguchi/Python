import requests 

>>> r=requests.get('http://api.fixer.io/latest?base=USD')

>>> print(r.json)
<bound method Response.json of <Response [200]>>

>>> print(r.text)
{"__deprecation_message__":"This API endpoint is deprecated and will stop working on June 1st, 2018. For more information please vis
it: https://github.com/fixerAPI/fixer#readme","base":"USD","date": "2018-05-18","rates":{"AUD":1.3304,"BGN":1.6601,"BRL":3.7205,"CAD"
:1.2795,"CHF":0.99932,"CNY":6.3787,"CZK":21.721,"DKK":6.3223,"EUR":0.84882,"GBP":0.74124,"HKD":7.8499,"HRK":6.2677,"HUF":269.65,"IDR
":14147.0,"ILS":3.5916,"INR":68.001,"ISK":104.74,"JPY":110.93,"KRW ":1080.9,"MXN":19.776,"MYR":3.972,"NOK":8.1294,"NZD":1.4472,"PHP":
52.408,"PLN":3.6457,"RON":3.932,"RUB":62.147,"SEK":8.7488,"SGD":1.3435,"THB":32.195,"TRY":4.4745,"ZAR":12.684}}

>>> print(r.status_code)
200

>>> print(r.history)
[]

# import requests

# def getWeather(query):
#     key = "&appid=90624cc9255f43fb0afc02b5a0ca2d75";
#     api = "http://api.openweathermap.org/data/2.5/weather?q="
#     url = api+query+key
#     res = requests.get(url)

#     def kelToFahr(kel):
#         return 9/5*(kel-273)+32

#     curStr = ""
#     for i in res:
#         for j in i:
#             curStr += j
#     curStr = curStr.split(',')

#     state    = curStr[25]
#     stateStr = ""
#     for i in range(8,16):
#         stateStr += state[i]

#     temp  = list(curStr[7])
#     fahr = ""
#     for i in range(15,21):
#         fahr += temp[i]
#     fahr = kelToFahr(float(fahr))
    
#     print "Location:",stateStr," | ","Temperature:",fahr
# getWeather("Maryland")
