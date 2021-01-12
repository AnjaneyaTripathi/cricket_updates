from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from termcolor import colored
import time

from detail import *
from overview import *
from send import send_message

# replace this with the location of your driver
browser = webdriver.Chrome('/path/to/your/driver')

URL = 'https://web.whatsapp.com/'
browser.get(URL)
time.sleep(10)

batter = False

while(1):
    message = ''
    det, scores = overview()
    message += scores
    table = fetch_details('https://www.cricbuzz.com' + det)
    for row in table:
        if(row[0]=='Batsman' or row[0]=='Bowler'):
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'cyan', attrs=['bold']))
            batter = not batter
        else:
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'white'))
            if(batter):
                msg = '\n'+row[0]+':  '+row[1]+'('+row[2]+')'+'  '+'S.R. '+row[5]
                message += msg
            else:
                msg = '\n'+row[0]+':  '+row[1]+'-'+row[2]+'-'+row[3]+'-'+row[4]
                message += msg            
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    message += ('\nThis is the latest score updated at: ' + current_time)
    print('\n')
    
    # replace this with the name of the contact you want to send the scorecard to
    send_message('name-of-contact', message, browser)

    time.sleep(300)