import requests
import os
from twilio.rest import Client
from datetime import datetime, timedelta

CRYPTO = "BTC"
MARKET = "EUR"
api_key = "Alpha Advantage API"
twilio_api = 'Twilio API'
twilio_num = 'Twilio Number'
account_sid = "Twilio account SID"

url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey=YourApiKey"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=url)
data = response.json()
last_day = data["Meta Data"]["6. Last Refreshed"]
last_day_date = datetime.strptime(last_day, "%Y-%m-%d %H:%M:%S").date()
last_day_date_str = last_day_date.isoformat()
num_days_to_substract = 1

prev_day = last_day_date - timedelta(num_days_to_substract)
two_days_before = prev_day - timedelta(num_days_to_substract)
prev_day_str = prev_day.isoformat()
two_days_before_str = two_days_before.isoformat()

t_s = "Time Series (Digital Currency Daily)"
prev_date_num = float(data[t_s][prev_day_str]["4a. close (EUR)"])
p_date_num = int(prev_date_num)
t_d_before = float(data[t_s][two_days_before_str]["4a. close (EUR)"])
t_d_before_num = int(t_d_before)
print(p_date_num)
print(t_d_before_num)

def count_percent_diff():
    p_diff = float(t_d_before_num / p_date_num)
    org_percent = 1.0
    count_diff = org_percent - p_diff
    if -5 >= count_diff:
        print("The price fell by over 5 %")
        client = Client(account_sid, twilio_api)
        message = client.messages \
            .create(
            body=f"The price of BTC rose by {round(count_diff, 2)}\n{titles_list[1]}\n{text_list[1]}",
            from_=twilio_num,
            to='Your Phone Number')
    elif count_diff >= 5:
        print("The price rose by 5 %")
        client = Client(account_sid, twilio_api)
        message = client.messages \
            .create(
            body=f"The price of BTC fell by {round(count_diff, 2)}\n{titles_list[0]}\n{text_list[0]}",
            from_=twilio_num,
            to='Your Phone Number')
    else:
        print(f"There is {round(count_diff, 3)} % difference")
        client = Client(account_sid, twilio_api)
        message = client.messages \
            .create(
            body=f"The price of BTC changed by {round(count_diff, 3)}\n{titles_list[2]}\n{text_list[2]}",
            from_=twilio_num,
            to='Your Phone Number')

# print(time_diff)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
url_news = 'https://newsapi.org/v2/everything'
params_news = {
    "q": "+bitcoin%",
    'from': f'{prev_day_str}&',
    'apiKey': 'Alpha Vantage API',
}
response_news = requests.get(url_news, params=params_news)
data_news = response_news.json()

news_list = data_news["articles"][:3]
titles_list = []
text_list = []
for article in news_list:
    titles_list.append(article['title'])
    text_list.append(article['description'])
# print(text_list)
count_percent_diff()




