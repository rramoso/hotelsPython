import requests
from requests.auth import HTTPDigestAuth
import json

PUJ = "http://terminal2.expedia.com/x/mhotels/search?city={}&checkInDate=2016-08-16&checkOutDate=2016-08-19&room1=2&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
STI = "http://terminal2.expedia.com/x/mhotels/search?city=STI&checkInDate=2016-12-01&checkOutDate=2016-12-03&room1=2&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
SDQ = "http://terminal2.expedia.com/x/mhotels/search?city=SDQ&checkInDate=2016-12-01&checkOutDate=2016-12-03&room1=2&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
SFO = "http://terminal2.expedia.com/x/mhotels/search?city=SFO&checkInDate=2016-12-01&checkOutDate=2016-12-03&room1=2&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"

cities = [PUJ,STI,SDQ,SFO]
hotelList = []
hotelNames = []
for city_code in cities: 
	r = requests.get(city_code)
	city =  json.loads(r.content)
	for num,i in enumerate(city['hotelList']):
		name = i['name']
		city = i['city']
		idHotel = i['hotelId']
		try:
			hotelList.append(idHotel)
			hotelNames.append(name)
		except Exception as e:
			hotelNames.append(name.encode('utf-8'))

hotelByID = "http://terminal2.expedia.com/x/mhotels/info?hotelId=%s&apikey=3oFyYOgQptyxEzCRjV81Bhzy0FR7pb6d"
aux = {}
result = {}
for hId in hotelList:
	r = requests.get(hotelByID%hId)
	try:
		content = json.loads(r.content)
	except Exception as e:
		print hId
		continue
	hotelInfo = {}
	hotelInfo['hName'] = content['hotelName']
	hotelInfo['hPhoneNumber'] = content['telesalesNumber']
	hotelInfo['hAddress'] = content['hotelAddress']	
	hotelInfo['hCity'] = content['hotelCity']
	hotelInfo['hCountry'] = content['hotelCountry']
	hotelInfo['hRating'] = content['hotelStarRating']
	aux[content['hotelId']] = hotelInfo
result["tblHotels"] = aux
print json.dumps(result)

