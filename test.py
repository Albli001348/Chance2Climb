import weather
import schedule
import time




climbing_spots = {
	'brickyard' : ['34.498','-119.861'],
	'gibraltar'	: ['34.4694', '-119.6825']
}
climbing_weather = dict()


for spots in climbing_spots:
	url = weather.get_location_url(climbing_spots[spots])
	climbing_weather.setdefault(spots, weather.get_weather(url))

print(climbing_weather['brickyard'])
print(climbing_weather['gibraltar'])

#brickyard_url = weather.get_location_url('ca','santa-barbara', '93105')
#brickyard = weather.get_weather(brickyard_url)
#print (brickyard)