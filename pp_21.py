# Write to a File

import requests
from bs4 import BeautifulSoup

def main():
	url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
	web_request = requests.get(url)
	web_request_html = web_request.text

	soup = BeautifulSoup(web_request_html, "html.parser")
	title = soup.find_all(class_="content-section")
	list_href = []

	for link in title:
		list_href.append(link.get_text())

	with open('file_to_save.text', 'w') as open_file:
		open_file.write(str(list_href))
		open_file.close()

	print(list_href)

if __name__=="__main__":
	main()