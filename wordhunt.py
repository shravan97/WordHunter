from Web import web
from ImageSearch import GoogleImageSearch
from WordsAnalyzer import WordAnalyze

def process():
    
    #Input API credentials
    my_api_key = raw_input(
        "Please enter in your API key for google custom search engine : ")

    my_cse_id = raw_input(
        "Please enter in your CSE id for google custom search engine : ")
    
    #Input Topic of Interest
    topic = raw_input("Please enter your topic of interest : ")
    
    #Google search using google-api-client
    w = web()
    urls = w.get_results(my_api_key, my_cse_id , topic)
    words = w.get_words_from_urls(urls)
    
    """
    Perform various operations and filter out the words found using 
    search engine
    
    """

    wa = WordAnalyze(words)
    words = wa.words_filter()
    
    #Frequency of words found using search engine
    freq_words = wa.frequency()
    
    #Sort the dictionary based on its frequency and get a sorted list
    sorted_freq = sorted(freq_words.items() , key=lambda x:x[1])
    
    #Suggested words from the sorted frequency distribution 
    suggested_words = sorted_freq[:]
    
    """
    The code for suggestion of words needs improvement since its currently 
    just an approximation

    """
    
    print "Here are the suggested words : "
    for k in suggested_words:
        print k[0]
    
    #Image search using one of the suggested words
    # For now , I'm taking in the word as input
    im_word = raw_input(
    "Enter a word (from list of suggested words) to search for its image :")
    im_search = GoogleImageSearch(my_api_key,my_cse_id)
    im_urls = im_search.get_image_links(im_word)

    print "Here is a list of image URLs : "
    for k in im_urls:
        print k

def main():
    #When arguments are added in the future , its code goes here
    process()

if __name__=="__main__":
    main()