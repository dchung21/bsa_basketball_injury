import requests
import csv
from bs4 import BeautifulSoup as bs

class InjuryScraper(object):
    SCRAPE_URL = 'https://www.prosportstransactions.com/basketball/Search/SearchResults.php?Player=&Team=&BeginDate=1990-01-01&EndDate=2020-02-29&ILChkBx=yes&Submit=Search'

    HEADERS = {
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	    'charset': 'charset=utf-8'}

    BASE_URL = 'prosportstransactions.com/basketball/Search/'

    onPage = False
 
    """
    Constructor opens a new session
    """
    def __init__(self):
        self.session = requests.Session()
    
    """
    Goes to the next page if currently on the page
    
    Args:
        resp: the parsed webpage

    Returns:
        string link to the next page
    """
    def nextPage(self, resp):
        parse = bs(resp.text, features="lxml")
        url = parse.find("a", text='Next');
        print(self.BASE_URL + url['href'])

    """
    Scrapes the data from the webpage
    
    Args:
        url: url of the webpage to parse

    Return:
        void function, should record data in auxilary data structure...?
    """
    def scrapeData(self, url):
        #Load new page
        resp = self.session.get(url, headers=self.HEADERS)
        
        #Get all of the rows containg data
        parse = bs(resp.text, features="lxml")
        parse = parse.find("table", {"class": "datatable center"})
        parse = parse.find_all("tr", {"align": "left"})
        return parse
 
    
    def main(self):
        self.scrapeData(self.SCRAPE_URL)          


    """
    Writes data to csv file per year
    
    Args:
        date, name, injury, year

    Return:
        void function, write csv
    """
    def dataCSV(self, parsed):
       

 
scraper = InjuryScraper()
scraper.main()
