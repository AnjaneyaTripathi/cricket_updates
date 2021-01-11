from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import time

from details import *
from stats import *

def send_message(rec, mes):
    try:
        time.sleep(5)
        search_bar = browser.find_elements_by_xpath('//div[@contenteditable = "true"]')[0]          
        search_bar.send_keys(rec)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        msg_bar = browser.find_elements_by_xpath('//div[@contenteditable = "true"]')[1]
        msg_bar.send_keys(mes)
        msg_bar.send_keys(Keys.ENTER)
        time.sleep(5)
        return 'Sent Successfully'
    except Exception as e:
        print('Error encountered: ', e)
        return 'Error Encountered'
    
browser = webdriver.Chrome('/Users/anjaneyatripathi/downloads/chromedriver') 
URL = 'https://web.whatsapp.com/'
browser.get(URL)
time.sleep(20)

while(1):
    det, scores = overview()
    table = fetch_details('https://www.cricbuzz.com' + det)
    for row in table:
        if(row[0]=='Batsman' or row[0]=='Bowler'):
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'cyan', attrs=['bold']))
        else:
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'white'))
    print('\n')
    send_message('#intern_boys scam', scores)
    sleep(100)


    
    
    