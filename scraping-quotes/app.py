from selenium import webdriver

from Pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    chrome = webdriver.Chrome(executable_path="C:/Users/muatif/Downloads/PycharmProjects/scraping-quotes/chromedriver.exe")
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)
    
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")
    print(page.search_for_quotes(author, tag))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred")
