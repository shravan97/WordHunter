from nltk.stem.porter import PorterStemmer as ps
import re , csv

def frequency(words):
	words=[str.upper(word) for word in words]
	words = stemmer(words)

	return {word:words.count(word) for word in words}

def stemmer(words):
	#Stemming the words using Porter's algorithm
	stemmer = ps()
	return [stemmer.stem(word) for word in words]

def word_diff(words):
	#This function preserves the ending of each word since it gets destroyed after stemming
	stmr = ps()
	word_dict = {stmr.stem(word):[] for word in words}

	for word in words:
		stemmed = stmr.stem(word)
		st_temp = stmr.stem(word)
		while word.startswith(st_temp)==False and len(st_temp)!=0:
			splitted_str = list(st_temp)
			splitted_str.pop()
			st_temp = ''.join(splitted_str)

		word_dict[stemmed].append(re.sub(st_temp , '' , word))
	print word_dict

	# !!--- Don't forget to fix words like 'very' , 'angrily' ..., which are stemmed to 'veri','angrili' ---!!

def preposition_filter(words):
	
	file = open('prepositions.csv' , 'r+')
 	#prepositions in file scrapped from https://www.englishclub.com/grammar/prepositions-list.htm
	rows = csv.reader(file)
	prepositions=[row[0] for row in rows]
 	
 	#As of now , there are 57 prepositions in the file . You can add more prepositions to the 'prepositions.csv' file
 	
 	for k in range(0,len(words)-1):
 		if str.upper(str(words[k])) in prepositions:
 			words.pop(k)

 	return words