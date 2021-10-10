import requests                                                  # for first task and third task
import os                                                        # for prforming second task
from pprint import pprint                                        # for third task 
import time                                                      # for forth task
import random                                                    # for fifth task
import qrcode                                                    # for sixth task



# first task -- to get github profile picture 

import requests    
from bs4 import BeautifulSoup as bs                               # for ease bs --BeautifulSoup 

github_user = input("Input Github User: ")
                                                                  # url = 'https://github.com/Dipti-22'      ** link for my profile      
url = 'https://github.com/'+github_user                           # to make it dynamic 
r = requests.get(url)
soup = bs(r.content, 'html.parser')                               # we have saved whole html content of that page in soup
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image) 




# second task -- to rename files in bulk  

import os  

def main():
    i = 0
    path = "C:/Users/hp/Downloads/python/Summer Projects/PHOTOS for project/"      # last / is imp
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"                                  # bulk rename 
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1 

if __name__ == '__main__':
    main()




# third task -- getting weather information

import requests  
from pprint import pprint   

API_Key = '323cb235d92a6514b3b32526ba6af465'
city = input("Enter a City: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key+"&q=" + city
weather_data = requests.get(base_url).json()
pprint(weather_data)






# forth task -- Countdown Timer 

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{: 02d}:{: 02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1 
    print('Time Over..')
t = input('Enter the time in seconds: ')
countdown(int(t))







# fifth task -- Password Generator 

import random

print('WELCOME TO YOUR PASSWORD GENERATOR')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input("How many password needed to be generated: "))
lenght = int(input("Your password lenght: "))

print('\n here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)  







# sixth task -- QR Code with Python ( encoding and decoding )

# Encoding the QR Code 
import qrcode
data = 'Hey my name is Dipti KK Sharma this is my first QR Code'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)


img = qr.make_image(fill_color = 'blue', back_color = 'white')                             # creating qr code 

img.save('C:/Users/hp/Downloads/python/Summer Projects/PHOTOS for project/myqrcode.png')




# for barcode encoding

from barcode import EAN13
from barcode.writer import ImageWriter

with open('C:/Users/hp/Downloads/python/Summer Projects/PHOTOS for project/myqrcode1.png', 'wb') as f:
    EAN13('982923393997', writer=ImageWriter()).write(f)

