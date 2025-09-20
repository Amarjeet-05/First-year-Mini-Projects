import requests
import json
from datetime import datetime, timedelta
api = input("Enter your Newsapi's Api key : ")
n = input("Enter the topic : ")
no = int(input("Enter the no. of headings : "))
date = datetime.today().date() - timedelta(hours=1)
date_str = date.strftime("%Y-%m-%d") 
urls = f"https://newsapi.org/v2/everything?q={n}&from={date_str}&sortBy=publishedAt&apiKey={api}"
response = requests.get(urls)#this can get the html data of the url
key = response.json()#it converts api data or url data in python dictionary
# print(json.dumps(key, indent=4))
articles = key['articles'] #articles is the key in the api so it it used as dictionary key to access the value of other keys
i = 1                      #basically article is a nested dictionary in which title, description,url,etc keys are availabe.
for article in articles[:no]:
    print(f"\n{i}.{article['publishedAt']}")
    print(f"Title :- {article['title']}\n")
    print(f"Description :- {article['description']}")
    print(f"For more info visit :- {article['url']}\n\n")
    i += 1


    