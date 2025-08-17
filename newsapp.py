import requests

query = input("What type of news are you interested in today?")
api = "016646891c42487a9bb9f1c259ace806"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-08&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]

for index, article in  enumerate(articles):
    print(index+1,article["title"])
    print(article["url"])
    print("\n****************\n")
