#bestand maken in notepad en opslaan als @@.py.
#dan bestand openen in anaconda prompt als volgt; python @@.py

import feedparser
import util

url = 'http://feeds.nos.nl/nosnieuwseconomie'
feed = feedparser.parse(url)

for entry in feed["entries"]:
	util.create_wordcloud(entry.summary, entry.title)
