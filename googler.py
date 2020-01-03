#! python3
import requests, sys, webbrowser, bs4, pyperclip,time

start = time.time()
print('Googling...') # display text while downloading the Google page
address = pyperclip.paste()

res = requests.get('http://google.com/search?q=' + ' '+ address)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(3, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

print("Total time taken: %s" % (time.time() - start))
input('Thanks! (Enter to exit)')
