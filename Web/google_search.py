from googleapiclient.discovery import build
import pprint , urllib2 ,re
from bs4 import BeautifulSoup as bs

''' You may notice here that a few functions can be merged and made into a single function .
But I'm preserving every small function to enhance modularity '''

class web:

	def __init__(self):
		pass

	def search(self , api_key , cse_id , search_term, **kwargs):    
	    google_service = build("customsearch", "v1", developerKey=api_key)
	    result = google_service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	    return result['items']

	def get_results(self, api_key , cse_id , search_term):
		urls=[]
		print "Querying ......"
		for k in range(0,7):
			res = self.search(api_key , cse_id , search_term , start=k*10+1 , num=10)
			for z in res:
				if re.match('https' , z['formattedUrl'])!=None:
					z['formattedUrl']=re.sub('https','http',z['formattedUrl'])
				elif re.match('http' , z['formattedUrl'])==None:
					z['formattedUrl'] = 'http://'+z['formattedUrl']
				urls.append(str(z['formattedUrl']))
		return urls


	@staticmethod	
	def get_words_from_urls(url_list):
		#Gets all the words from a list of urls
		words = []
		print "Scraping and fetching words ......."
		for k in url_list:
			scr = web.scrape_site(str(k))
			if scr!=-1:
				for word in scr:
					words.append(word)
		
		return words


	@staticmethod
	def scrape_site(url):
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(url , headers=hdr)
		try:
			page = urllib2.urlopen(req)
			soup = bs(page)
			[s.extract() for s in soup('script')] #remove content from script tags
			[s.extract() for s in soup('style')] # remove content from style tags
			phrases=[]
			words=[]
	
			for k in soup.strings:
				phrases.append(re.split('[\n\t.,\"\'()!;= ]+' , k))
	
			for k in phrases:
				for z in k:
					flag=1
					for ch in z:
						if re.match('[a-zA-z]',ch)== None: #Filter out words by checking each character
							flag=0
							break
					if z!='' and flag==1:
						words.append(z)
	
			return words
		except :
			return -1
		