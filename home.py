from whatsapp import *
from details import *
from stats import *

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import time

import requests 
from bs4 import BeautifulSoup 
import csv 
from termcolor import colored
from time import sleep

while(1):
    det, scores = overview()
    table = fetch_details('https://www.cricbuzz.com' + det)
    for row in table:
        if(row[0]=='Batsman' or row[0]=='Bowler'):
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'cyan', attrs=['bold']))
        else:
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'white'))
    print('\n')
    send_message('Papa', scores)
    sleep(10)
    
