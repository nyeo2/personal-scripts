#! python3
import requests, sys, webbrowser, bs4, time

# display text while downloading the Google page
subredd = input('Whaddya wanna scrape: ')
print('Scrapin...')

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://old.reddit.com/r/' + subredd
res = requests.get(url, headers=headers)

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
start = time.time()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.thing')

for i in range(len(linkElems)):
    if linkElems[i].get('data-domain')[:5] == 'self.':
        print('https://www.reddit.com' + linkElems[i].get('data-url'))
    else:
        print(linkElems[i].get('data-url'))

print("Total time taken: %s" % (time.time() - start))
input('Thanks! (Enter to exit)')
