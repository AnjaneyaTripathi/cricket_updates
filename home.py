from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import time

from details import *
from stats import *
from whatsapp import *
    
browser = webdriver.Chrome('/Users/anjaneyatripathi/downloads/chromedriver') 
URL = 'https://web.whatsapp.com/'
browser.get(URL)
time.sleep(20)

batter = False

while(1):
    det, scores = overview()
    table = fetch_details('https://www.cricbuzz.com' + det)
    for row in table:
        if(row[0]=='Batsman' or row[0]=='Bowler'):
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'cyan', attrs=['bold']))
            batter = not batter
        else:
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'white'))
            if(batter):
                send_message('Papa', row[0]+' '+row[1]+'('+row[2]+')')
    print('\n')
    send_message('Papa', scores)
    sleep(200)


    
    
    