from webbrowser import Error

import requests

from send_email import send_email

api_key="fc9817d7f8a44264ad7c974099fb8d43"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-10-06&sortBy="
       "publishedAt&apiKey=fc9817d7f8a44264ad7c974099fb8d43")

# Make a request
req=requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article titles and description
body = ""
for article in content['articles']:

    if article['title'] is not None :
        body=body+article['title']+article['description'] +2*'\n'

body=body.encode("utf-8")
send_email(body)