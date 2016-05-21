from googleapiclient.discovery import build
import pprint , urllib2 ,re
from bs4 import BeautifulSoup as bs

def search(search_term, api_key, cse_id, **kwargs):    
    google_service = build("customsearch", "v1", developerKey=api_key)
    result = google_service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return result['items']

def get_results(search_term,my_api_key , my_cse_id):
	urls=[]
	print "Querying Google ......"
	for k in range(0,7):
		res = search(search_term , my_api_key , my_cse_id , start=k*10+1 , num=10)
		for z in res:
			if re.match('https' , z['formattedUrl'])!=None:
				z['formattedUrl']=re.sub('https','http',z['formattedUrl'])
			elif re.match('http' , z['formattedUrl'])==None:
				z['formattedUrl'] = 'http://'+z['formattedUrl']
			urls.append(str(z['formattedUrl']))
	return urls				

def get_words_from_urls(url_list):
	#Gets all the words from a list of urls
	words = []
	for k in url_list:
		scr = scrape_site(str(k))
		if scr!=-1:
			words.append(scr)
	
	return words	

def scrape_site(url):
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(url , headers=hdr)
	try:
		print 'Scraping '+url+' ......'
		page = urllib2.urlopen(req)
		soup = bs(page)
		[s.extract() for s in soup('script')]
		[s.extract() for s in soup('style')]
		words=[]
	
		for k in soup.strings:
			words.append(re.split('[\n\t]+' , k))

		return words
	except :
		return -1
