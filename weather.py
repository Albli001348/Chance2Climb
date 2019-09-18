import requests
from bs4 import BeautifulSoup

#brickyard = requests.get('https://www.wunderground.com/weather/us/ca/santa-barbara/93105')

#brickyard_data = (brickyard.text)

#brickyard_soup = BeautifulSoup(brickyard_data, 'html.parser')

#brickyard_high = brickyard_soup.find("span", "_ngcontent-app-root-c5", class_="hi").text
#brickyard_low = brickyard_soup.find("span", "_ngcontent-app-root-c5", class_="lo").text
#brickyard_weather = brickyard_soup.find("div", "_ngcontent-app-root-c5", class_="condition-icon small-6 medium-12 columns").p.text

#print(brickyard_high)
#print(brickyard_low)
#print(brickyard_weather)
#schedule.every().day.at("8:00").do(post())
#https://forecast.weather.gov/MapClick.php?textField1=34.4694&textField2=-119.6825
#https://forecast.weather.gov/MapClick.php?lat=34.498&lon=-119.861

def get_location_url(spots):
	return ('https://forecast.weather.gov/MapClick.php?lat=' + spots[0] + '&lon=' + spots[1])
	#return ('https://www.wunderground.com/weather/us/' + spots[0] + '/' + spots[1] + '/' + spots[2])

def get_weather(location):
	website = requests.get(location)
	data = (website.text)
	soup = BeautifulSoup(data, 'html.parser')

	day = soup.find("li", class_="forecast-tombstone")
	high = day.find("p", class_="temp temp-high").text
	day = day.next_sibling
	low = day.find("p", class_="temp temp-low").text
	weather = soup.find("p", class_="short-desc").text

	#high = soup.find("span", "_ngcontent-app-root-c5", class_="hi").text
	#low = soup.find("span", "_ngcontent-app-root-c5", class_="lo").text
	#weather = soup.find("div", "_ngcontent-app-root-c5", class_="condition-icon small-6 medium-12 columns").p.text
	weather_dict = [high,low,weather]
	return weather_dict


#high = soup.find("p", class_="temp temp-high").text						#soup.find("span", "_ngcontent-app-root-c5", class_="hi").text
#low = soup.find("p", class_="temp temp-low").text	

