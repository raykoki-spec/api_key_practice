# File: README.md

# News API Practice 


## What It Does


## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python

for article in articles:
            title = article.get("title", "No title")
            description = article.get("description", "No description")
            article_url = article.get("url", "No URL")
            print(f"Title: {title}\nDescription: {description}\nURL: {article_url}\n")

```

## Sample Output

```
Title: Kenya Records Second Ebola-Related Death - سانا
Description: Nairobi, Oct. 24 (SANA) Kenya recorded its second Ebola-relateddeath on Friday, following an outbreak of the virus in the Democratic Republic of the Congo
URL: https://sana.sy/en/health/2353212/

```

## Stack

Python

Built-in Module: `JSON`
