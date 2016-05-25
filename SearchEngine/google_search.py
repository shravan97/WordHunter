from googleapiclient.discovery import build
import pprint , urllib2 ,re
from bs4 import BeautifulSoup as bs

''' You may notice here that a few functions can be merged and made into a single function .
But I'm preserving every small function to enhance modularity '''

class GoogleSearch:

	def __init__(self , api_key , cse_id):
		self.my_api_key = api_key
		self.my_cse_id = cse_id

	def search(self , search_term, **kwargs):    
	    google_service = build("customsearch", "v1", developerKey=self.my_api_key)
	    result = google_service.cse().list(q=search_term, cx=self.my_cse_id, **kwargs).execute()
	    return result['items']

	def get_results(self,search_term):
		urls=[]
		print "Querying Google ......"
		for k in range(0,7):
			res = self.search(search_term , start=k*10+1 , num=10)
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
		for k in url_list:
			scr = GoogleSearch.scrape_site(str(k))
			if scr!=-1:
				words.append(scr)
		
		return words


	@staticmethod
	def scrape_site(url):
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(url , headers=hdr)
		try:
			print 'Scraping '+url+' ......'
			page = urllib2.urlopen(req)
			soup = bs(page)
			[s.extract() for s in soup('script')]
			[s.extract() for s in soup('style')]
			phrases=[]
			words=[]
	
			for k in soup.strings:
				phrases.append(re.split('[\n\t ]+' , k))
	
			for k in phrases:
				for z in k:
					if z!='':
						words.append(z)
	
			return words
		except :
			return -1
		