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
'''
while(1):
    table = fetch_details('https://www.cricbuzz.com/live-cricket-scores/31647/aus-vs-ind-3rd-test-india-tour-of-australia-2020-21')
    for row in table:
        if(row[0]=='Batsman' or row[0]=='Bowler'):
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'cyan', attrs=['bold']))
        else:
            print(colored("{:<24} {:<8} {:<8} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5]), 'white'))
    print('\n')
    sleep(300)
'''
    
    
    
    
    
    
    