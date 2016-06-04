from nltk.stem.porter import PorterStemmer as ps
import re , csv , os , inspect

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

	def word_diff(self):
		#This function preserves the ending of each word since it gets destroyed after stemming
		stmr = ps()
		word_dict = {stmr.stem(word):[] for word in self.words}

		for word in self.words:
			stemmed = stmr.stem(word)
			st_temp = stmr.stem(word)
			while word.startswith(st_temp)==False and len(st_temp)!=0:
				splitted_str = list(st_temp)
				splitted_str.pop()
				st_temp = ''.join(splitted_str)

			word_dict[stemmed].append(re.sub(st_temp , '' , word))
		return word_dict	

	# !!--- Don't forget that words like 'very' , 'angrily' ..., are stemmed to 'veri','angrili' ---!!

	def words_filter(self):
		#filter prepositions first
		filename = inspect.getframeinfo(inspect.currentframe()).filename
		path_to_prepositions = os.path.dirname(os.path.abspath(filename))
		file = open(path_to_prepositions+'/prepositions.csv' , 'r+')
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