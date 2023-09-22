from bs4 import BeautifulSoup

import requests
import pickle

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
          'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9',
          'Connection': 'keep-alive', 
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'}
url = 'https://www.jellycat.com/us/bartholomew-bear-barm3br/'
resp = requests.get(url, headers=header)
html = resp.text
soup = BeautifulSoup(html, "html.parser")
print(soup.body.get_text().strip())
with open('html.pkl', 'wb') as f:
    pickle.dump(resp, f)