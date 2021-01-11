import requests 
from bs4 import BeautifulSoup 
import csv 
from termcolor import colored
from time import sleep

def fetch_details(link):
    URL = link
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    
    players = soup.find_all('div', attrs = {'class': 'cb-col cb-col-50'})
    stats = soup.find('div', attrs = {'class': 'cb-col-67 cb-col'})
    scores = stats.find_all('div')
    
    table = []
    cnt = 0
    row = {}
    
    for s in scores:
        if(cnt%6==0 and len(row)):
            table.append(row)
            row = {}
        if(len(s.find_all('div'))==0):
            cnt+=1
            row[(cnt-1)%6]=s.text.strip()
    table.append(row)
    
    return table

    
    
    
    
    
    
    