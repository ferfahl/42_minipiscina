import requests
import sys
from bs4 import BeautifulSoup

def request_info(subject, roads):
    response = requests.get("https://en.wikipedia.org/wiki/" + subject)
    if response.status_code != 200:
        if response.status_code == 404:
            sys.exit("It leads to a dead end !")
        else:
            sys.exit('HTTP error ', str(response.status_code))
    soup = BeautifulSoup(response.text, 'html.parser')
    title = str(soup.title.string)
    title = title.replace(' - Wikipedia', '')
    roads.append(title)
    tables = soup.find_all('table')
    for item in tables:
        item.clear()

    content = soup.find(id="mw-content-text").select("p > a")
    for link in content:
        if link.get('href') != None and link['href'].startswith('/wiki/') \
                and not link['href'].startswith('/wiki/wikipedia:') \
                and not link['href'].startswith('/wiki/Help:'):
            return (link['href'].split('/')[2].replace('_', ' '))
    sys.exit("It leads to a dead end !")

def request(subject):
    roads = []
    first = subject
    while str(subject.lower()) != 'philosophy':
        subject = request_info(subject, roads)
        print(subject)
        if subject in roads:
            sys.exit("It leads to an infinite loop !")
    print(f"{len(roads)} roads from {first} to philosophy !")
    

def roads_to_philosophy():
    if len(sys.argv) != 2:
        sys.exit("Error: Wrong number of arguments. The program needs a argument: 'Subject'.")
    try:
        search_name = sys.argv[1].replace(' ', '_')
        request(search_name)

    except Exception as msg:
        sys.exit(msg)



if __name__ == '__main__':
    roads_to_philosophy()

