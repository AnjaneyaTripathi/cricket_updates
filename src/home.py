from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

from detail import *
from overview import *
from send import send_message

browser = webdriver.Chrome('/Users/anjaneyatripathi/downloads/chromedriver') 
URL = 'https://web.whatsapp.com/'
browser.get(URL)
time.sleep(10)

batter = False

while(1):
    message = ''
    det, scores = overview()
    message += scores
    '''
    table = fetch_details('https://www.cricbuzz.com' + det)
    for row in table:
        if(row[0]=='Batsman' or row[0]=='Bowler'):
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'cyan', attrs=['bold']))
            batter = not batter
        else:
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'white'))
            if(batter):
                msg = (Keys.SHIFT + Keys.ENTER)+row[0]+'{:<4}'+row[1]+'('+row[2]+')'+'{:<4}'+'S.R. '+row[5]
                message += msg
                # send_message('Papa', row[0]+'{:<4}'+row[1]+'('+row[2]+')'+'{:<4}'+'S.R. '+row[5])
            else:
                msg = (Keys.SHIFT + Keys.ENTER)+row[0]+'{:<4}'+row[1]+'-'+row[2]+'-'+row[3]+'-'+row[4]
                message += msg
                # send_message('Papa', row[0]+'{:<4}'+row[1]+'-'+row[2]+'-'+row[3]+'-'+row[4])
    '''
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    message += ('\nThis is the latest score updated at: ' + current_time)
    print('\n')
    print(message)
    send_message('Ajitesh', message, browser)
    time.sleep(10)


    
    
    