# Bitcoin-Price-and-News_Notifications-App
This app allows for a user to receive daily messages about the change in the price of Bitcoin.  In the text message 
to the user there's also a single, most recent article on Bitcoin. The app uses Alphavantage API, NewsAPI, and Twilio API.  

When the price changes by 5% or more from the day before yesterday to yesterday. The script will retrieve the top 
three news articles about Bitcoin from the NewsAPI, using the same API key. It will then use the Twilio API to send 
a message with the percentage change in price and the titles and descriptions of the news articles.

Technical:
This script is written in Python and requires the requests, os, twilio, and datetime modules to be installed. 
It uses the Alpha Advantage and NewsAPIs to retrieve price and news data, and the Twilio API to send SMS messages. 
The script calculates the percentage difference in price between the day before yesterday and yesterday and sends a message via 
Twilio with news article titles and descriptions if the difference is 5% or more.

Usage:
To use this script, you need to have API keys for Alpha Advantage, NewsAPI, and Twilio. 
You also need to have Python installed, along with the requests, os, twilio, and datetime modules. 
Once you have set up your API keys, you can run the script in a Python environment or execute it on a scheduled basis using a tool like cron.

Features:
This script features price monitoring of Bitcoin in Euros, automated news article retrieval using the NewsAPI, 
and SMS messaging using the Twilio API. It also calculates percentage difference in price and sends a message if the difference is 5% or more. 
This script can be modified to monitor other cryptocurrencies or assets by changing the parameters in the Alpha Advantage API URL.
