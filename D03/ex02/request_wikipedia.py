import requests
import sys
from dewiki import from_string

def request(subject):
    r = requests.get("https://en.wikipedia.org/w/api.php",
        params={'action': 'parse',
                'page': subject,
                'prop': 'wikitext',
                'format': 'json',
                'redirects': True}).json()
    if r.get("error") is not None:
        raise Exception(r["error"]["info"])
    temp = r['parse']['wikitext']['*']
    return dewiki.from_string(temp).strip()


def wikipedia_request():
    if len(sys.argv) != 2:
        sys.exit("Error: Wrong number of arguments. The program needs a argument: 'Subject'.")
    try:
        name = sys.argv[1].title().replace(' ', '_')
        data = request(name)
        file = open(f"{name}.wiki", "w")
        file.write(data)
    except Exception as e:
        sys.exit(e)

if __name__ == '__main__':
    wikipedia_request()