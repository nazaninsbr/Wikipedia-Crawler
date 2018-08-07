import requests
from bs4 import BeautifulSoup 
from bs4.element import Comment
import copy 
import re

def tag_visible(element):
	if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
		return False
	if isinstance(element, Comment):
		return False
	return True

def getPageContent(url):
	try:
		r = requests.get(url)
		if not r.status_code==200:
			print("Problem accessing page data.")
			return -1
		return r.text
	except:
		print("Bad URL")
		return -1

def getText(content):
	contentCopy = copy.deepcopy(content)
	soup = BeautifulSoup(contentCopy, 'html.parser')
	texts = soup.findAll(text=True)
	visible_texts = filter(tag_visible, texts)  
	result =  u" ".join(t.strip() for t in visible_texts)
	return result

def getLinks(content):
	contentCopy = copy.deepcopy(content)
	soup = BeautifulSoup(contentCopy, 'html.parser')
	links = []
	for a in soup.find_all('a', href=True):
		links.append(a['href'])
 
	return links 

def mainFunc(url):
	content = getPageContent(url)
	if not content==-1:
		text = getText(content)
		links = getLinks(content)
		return text, links
	return -1, -1




