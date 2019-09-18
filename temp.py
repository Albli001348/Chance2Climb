import requests
from bs4 import BeautifulSoup

brickyard = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.498&lon=-119.861')	#'https://www.wunderground.com/weather/us/ca/santa-barbara/93105')

brickyard_data = (brickyard.text)

brickyard_soup = BeautifulSoup(brickyard_data, 'html.parser')

brickyard_day = brickyard_soup.find("li", class_="forecast-tombstone")

brickyard_high = brickyard_day.find("p", class_="temp temp-high").text

brickyard_day = brickyard_day.next_sibling
brickyard_low = brickyard_day.find("p", class_="temp temp-low").text

print(brickyard_low)

#brickyard_high = brickyard_soup.find("span", "_ngcontent-app-root-c5", class_="hi").text
#brickyard_low = brickyard_soup.find("span", "_ngcontent-app-root-c5", class_="lo").text
#brickyard_weather = brickyard_soup.find("div", "_ngcontent-app-root-c5", class_="condition-icon small-6 medium-12 columns").p.text

#print(brickyard_high)
#print(brickyard_low)
#print(brickyard_weather)
#schedule.every().day.at("8:00").do(post())
#https://forecast.weather.gov/MapClick.php?textField1=34.4694&textField2=-119.6825
#https://forecast.weather.gov/MapClick.php?lat=34.498&lon=-119.861
