# A simple module to get the links of first 10 images displayed on google image search
from googleapiclient.discovery import build

class GoogleImageSearch:
	def __init__(self,api_key,cse_id):
		self.my_api_key = api_key
		self.my_cse_id= cse_id

	def search(self,search_term,**kwargs):
		google_service = build("customsearch", "v1", developerKey=self.my_api_key)
		result = google_service.cse().list(q=search_term, cx=self.my_cse_id, **kwargs).execute()
		return result['items']	

	def get_image_links(self , search_term):
		results = self.search(search_term , searchType='image')
		links = [result['link'] for result in results]
		return links