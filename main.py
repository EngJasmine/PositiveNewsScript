import os

import requests
from textblob import TextBlob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from send_email import send_email  # Assuming this is a custom function

api_key = "fc9817d7f8a44264ad7c974099fb8d43"
topic = 'google'
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2025-01-06&"
       "sortBy="
       "publishedAt&"
       "apiKey=fc9817d7f8a44264ad7c974099fb8d43&"
       "language=en")

# Make a request
req = requests.get(url)

# Get a dictionary with data
content = req.json()
print(content)
# Initialize the email body
body = ""

# Loop through the articles and filter based on sentiment
for article in content['articles'][0:20]:
    if article['title'] is not None:
        # Combine title and description for sentiment analysis
        text = article['title'] + " " + article['description']

        # Perform sentiment analysis
        sentiment = TextBlob(text).sentiment.polarity

        # If the sentiment is positive, add to the body
        if sentiment > 0:
            body += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

# If there are positive articles, send an email
if body:
    send_email(body)
else:
    print("No positive articles found.")
