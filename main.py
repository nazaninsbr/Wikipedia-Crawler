from sys import argv
import singlePageCrawler
import databaseStuff
import general

MAX_COUNT = 10
MAIN_URL = 'https://en.wikipedia.org'

def crawlTheLinks(link, text):
	links = []
	texts = []
	links.extend(link)
	texts.extend(text)
	count = 0
	for webpageLink in links:
		count += 1
		if webpageLink[0]=='/':
			webpageLink = MAIN_URL+webpageLink
		print('Crawling: ', webpageLink)
		text, link = singlePageCrawler.mainFunc(webpageLink)
		if not text==-1:
			texts.append(text)
			links.append(link)
			databaseStuff.insert({'url': webpageLink, 'value': text}, 'wiki_text')
			databaseStuff.insert({'url': webpageLink, 'value': link}, 'wiki_links')
		if count == MAX_COUNT:
			break
	return texts, links
		
	
def getTheData():
	databaseStuff.createTables()
	URL = 'https://en.wikipedia.org/wiki/Main_Page'
	text, link = singlePageCrawler.mainFunc(URL)
	if not text==-1:
		texts, links = crawlTheLinks(link, text)
	return texts, links

def countEachWord(texts):
	words = {}
	for text in texts:
		seperated = text.split(' ') 
		for word in seperated:
			if word in words:
				words[word] += 1
			else:
				words[word] = 1
	return words

def useTheWebsite():
	text, links = getTheData()
	words = countEachWord(text)
	general.writeDictToFile('wordCount.txt', words)


def countWordsDB(textTable):
	words = {}
	for text in textTable:
		seperated = text['value'].split(' ') 
		for word in seperated:
			if word in words:
				words[word] += 1
			else:
				words[word] = 1
	return words

def useTheDatabase():
	textTable = databaseStuff.readTable('wiki_text')
	words = countWordsDB(textTable)
	general.writeDictToFile('wordCount.txt', words)
	
if __name__ == '__main__':
	if '--website' in argv:
		useTheWebsite()
	elif '--db' in argv:
		useTheDatabase()



