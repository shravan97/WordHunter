from nltk.stem.porter import PorterStemmer as ps
import re , csv , os

class WordAnalyze:
	def __init__(self , words_list):
		self.words = words_list

	def frequency(self):
		words=[str.upper(word.encode('utf8')) for word in self.words]

		print "calculating frequencies ......"	
		return {word:words.count(word) for word in words}

	def stemmer(self):
		#Stems a list of words using Porter's algorithm
		stmr = ps()
		return [stmr.stem(word) for word in self.words]

	# !!--- Don't forget that words like 'very' , 'angrily' ..., are stemmed to 'veri','angrili' ---!!

	def words_filter(self , path_to_prepositions):
		#filter prepositions first
		file = open(path_to_prepositions+'prepositions.csv' , 'r+')
	 	#prepositions in file scrapped from https://www.englishclub.com/grammar/prepositions-list.htm
		rows = csv.reader(file)
		prepositions=[row[0] for row in rows]
	 	
	 	print "Filtering out words ........."

	 	#As of now , there are about 60 prepositions in the file . You can add more prepositions to the 'prepositions.csv' file
	 	w = self.words
	 	w_temp = list(w)
	 	curr_index=0

	 	for k in w_temp:
	 		if str.upper(k.encode('utf8')) in prepositions:
	 			w.pop(curr_index)
	 			curr_index-=1
	 		curr_index+=1

	 	# !!-- Add more filters here --!!		
	
	 	return w