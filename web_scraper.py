import urllib.request 							#built-in python module for working with URLs
from bs4 import BeautifulSoup 					#module for analyzing information

												#class is an outline for objects defined inside of it
class Scraper: 									#scraper class is for building the tools(objects) to extract data from websites
	def __init__(self, site): 					#__inti__ is a constructor that is a special method that is automatically called when this object of the class is created. 
		self.site = site 						#self refers to itself (object) which has called the method, site refers to website being used. 
	def scrape(self): 							#scrape is an object for collecting information from website.
		r = urllib.request.urlopen(self.site)	#urlopen() function sends a request to the website and returns a response object in which its HTML code is stored, along with additional data.
		html = r.read()							#the response of the function .read() returns the HTML of the response object. all the HTML for the website is in the html variable.
		parser = "html.parser"					#html variable parameter
		sp = BeautifulSoup(html,parser)			#BeautifulSoup object parses the HTML
		for tag in sp.find_all("a"):			#runs loop to find all the urls in the website
			url = tag.get("href")				#href is the url placement in html 
			if url is None:						#if statement to skip over non-url info
				continue						#loop control statement to force next iteration
			if "articles" in url:				#if statement to confirm data is external article
				print("\n" + url)				#print url

news = "https://news.google.com/" 				#website url for scraping
Scraper(news).scrape()							#Running the web scraper program 

