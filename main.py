
from colorama import Fore
import requests
from bs4 import BeautifulSoup

city = input("Enter city name: ")

url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

data_split = time_sky.split('\n')
time = data_split[0]
sky = data_split[1]

print(Fore.BLUE + city.capitalize(),":")
print("Temperature is", temp)
print("Today the sky is:", sky)
print("Today is", time)

#issue was here -> 
print(temp)
temp_digit = temp[:-1]
temp_digit = int(temp_digit[:-1])

if 41 <= temp_digit <= 59:
    print(Fore.RED + "You're going to need a jacket today!")

elif temp_digit < 41:
    print("Maybe you should wear a winter coat instead!")

else:
    print(Fore.YELLOW + "You don't need a jacket today. Enjoy the weather!")
#Fix the F to C conversion 