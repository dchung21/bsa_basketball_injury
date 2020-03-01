import requests
import csv
from bs4 import BeautifulSoup as bs

class InjuryScraper(object):
    SCRAPE_URL = 'https://www.prosportstransactions.com/basketball/Search/SearchResults.php?Player=&Team=&BeginDate=1990-01-01&EndDate=2020-02-29&ILChkBx=yes&Submit=Search&start=0'

    HEADERS = {
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
	    'charset': 'charset=utf-8'}

    BASE_URL = 'https://www.prosportstransactions.com/basketball/Search/'

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
    def nextPage(self, parse):
        url = parse.find("a", text='Next')
        if url is None:
            url = ''
            return ''

        return self.BASE_URL + url['href']

    """
    Scrapes the data from the webpage
    
    Args:
        url: url of the webpage to parse

    Return:
        void function, should record data in auxilary data structure...?
    """
    def scrapeData(self, parsed):
        parse = parsed.find("table", {"class": "datatable center"})
        parse = parsed.find_all("tr", {"align": "left"})
        return parse
 
   

    def getPage(self, url):
        resp = self.session.get(url, headers=self.HEADERS)
        parse = bs(resp.text, features="lxml")
        return parse

 
    def main(self):
        rows = ['date', 'team', 'name', 'status']
        data = []
        nextPage = self.SCRAPE_URL
        open("data.csv", "x")    

        filename = "data.csv"

        #while True:
        for k in range(0, 500):
            resp = self.getPage(nextPage)
            page_data = self.scrapeData(resp)
            nextPage = self.nextPage(resp)

            filt = self.scrapeData(resp)


            for td in filt:
                subData = td.text.split('\n')
                subData.remove('')
                subData.remove(' ')
                subData.remove('')
                dictData = {'date': subData[0], 'team':subData[1], 'name':subData[2], 'status': subData[3]}
                print(dictData)
                data.append(dictData)

            print("Moving onto: " + nextPage)

            
            if (nextPage == ''):
                break;

        with open(filename, 'w') as csvfile:
            #creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames = rows) 


            # writing headers (field names) 
            writer.writeheader() 

            #writing data rows
            writer.writerows(data)

        #a = self.scrapeData(self.SCRAPE_URL)          
        
        #for td in a:
        #    print(td.text)
    """
       rows = ['date', 'team', 'name', 'status']
       
       for i in ran
       open("data.csv", "x")    
       
       filename = "data.csv"

       with open(filename, 'w') as csvfile:
            #creating a csv writer object
            csvwriter = csv.writer(csvfile)

            #writing the fields
          """  
    """
    Writes data to csv file per year
    
    Args:
        date, name, injury, year

    Return:
        void function, write csv
    """
#    def dataCSV(self, parsed):
       

scraper = InjuryScraper()
scraper.main()
