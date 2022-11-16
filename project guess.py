import keys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = keys.accountSID
auth_token = keys.authToken
my_number = '+15129481143'
twilio_number = '+18179935622'
client = Client(account_sid, auth_token)

url = "https://coinmarketcap.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

