from nltk.stem.porter import PorterStemmer

def frequency(words):
	words=[str.upper(word) for word in words]
	words = stemmer(words)

	return {word:words.count(words) for word in words}

def stemmer(words):
	#Stemming the words using Porter's algorithm
	stemmer = PorterStemmer()
	return list([stemmer.stem(word) for word in words])

def word_count_sort(words)		


