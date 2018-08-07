def writeDictToFile(filename, words):
	f = open(filename, 'a')
	for item in words.keys():
		text = str(item)+'#'+str(words[item])+'\n'
		f.write(text)
	f.close()
