import json
import os
from unicodedata import category
from unicodedata import category
from urllib import response
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen
from dotenv import load_dotenv

load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")

query = "Kenya"
max_articles = 10

if not news_api_key:
    print("NEWS_API_KEY is not set in the .env file.")
    raise SystemExit(1)

params = urlencode({"q": query, "language": "en", "sortBy": "publishedAt", "pageSize": max_articles})
url = f"https://newsapi.org/v2/everything?{params}&apiKey={news_api_key}"

try:
    with urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
except HTTPError as error:
    status_code = error.code
    if status_code == 401:
        print("API KEY is invalid or not yet active. Check your .env file.")
    elif status_code == 404:
        print(f"News not found for query: {query}.")
    elif status_code == 429:
        print("Too many requests. Wait before trying again.")
    else:
        print(f"Unexpected error: {status_code}")
        print(error.read().decode("utf-8", errors="replace"))
else:
    articles = data.get("articles", [])
    if not articles:
        print(f"No news articles found for query: {query}.")
    else:
        for article in articles:
            title = article.get("title", "No title")
            description = article.get("description", "No description")
            article_url = article.get("url", "No URL")
            print(f"Title: {title}\nDescription: {description}\nURL: {article_url}\n")