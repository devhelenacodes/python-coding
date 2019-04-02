# Decode a Web Page

import requests
from bs4 import BeautifulSoup

def main():
	url = "https://twitter.com/linustech"
	web_request = requests.get(url)
	web_request_html = web_request.text

	soup = BeautifulSoup(web_request_html, "html.parser")
	title = soup.find_all(class_="TweetTextSize")
	list_href = []

	for link in title:
		list_href.append(link.get_text())

	print(list_href)

main()