import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# pronalazenje jednog elementa
# quote_1 = soup.find("div", class_ = "quote")
# print(quote_1)

# tekst = quote_1.find("span", class_ = "text").text
# autor = quote_1.find("small", class_ = "author").text

# print(tekst)
# print(autor)

# pronalazenje svih quote elemenata

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_ = "text").text
    author = quote.find("small", class_ = "author").text

    assert text is not None
    assert author is not None