from bs4 import BeautifulSoup
from urllib import request


# Get text data from BBC website and save it in a file
def url_text(page_url, file_url):
    soup = BeautifulSoup(request.urlopen(page_url).read().decode("utf-8"), "html.parser")
    paragraphs = soup.find_all("p")
    text = ""
    for tag in paragraphs:
        if tag is not None:
            text += tag.text

    split_lines = text.splitlines()
    file = open(file_url, "w")

    for each_line in split_lines:
        file.write(each_line)

    file.close()
