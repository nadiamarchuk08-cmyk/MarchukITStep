import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    book_blocks = soup.find_all("h3")
    book_titles = []
    for book in book_blocks:
        title_tag = book.find("a")
        if title_tag and "title" in title_tag.attrs:
            book_titles.append(title_tag["title"])

    for title in book_titles:
        print(title)
else:
    print("Не вдалося завантажити сторінку")