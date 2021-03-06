import requests 
from bs4 import BeautifulSoup
from termcolor import colored

def overview():
    URL = "https://www.cricbuzz.com"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.find_all('li', attrs = {'class': 'cb-col cb-col-25 cb-mtch-blk cb-vid-sml-card-api videos-carousal-item cb-carousal-item-large cb-view-all-ga'}) 
    
    # replace this with the team initials eg. IND for India
    pref = 'team-initials'
    
    for li in table:
        match = li.text.strip()
        if(match.count(pref)>0):
            print(colored(match, 'magenta'))
            link = li.find('a', attrs = {'class': 'cb-font-12'})
            print('\n')
            return link['href'], match