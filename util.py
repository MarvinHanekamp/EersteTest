#bestand maken in notepad en opslaan als @@.py.
#dan bestand openen in anaconda prompt als volgt; python @@.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(txt, title):

	wc = WordCloud().generate(txt)

	plt.figure(figsize=(18, 14))
	plt.imshow(wc)

	plt.savefig(title+".png")

if __name__== "__main__":

	create_wordcloud("Test text met woorden")
