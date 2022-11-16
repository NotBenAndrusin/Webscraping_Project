import keys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = keys.accountSID
auth_token = keys.authToken
my_number = '+15129481143'
twilio_number = '+18179935622'
client = Client(account_sid, auth_token)

url = "https://crypto.com/price"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

crypto_info = soup.find('tbody').find_all('tr')
names = []
curr_price = []
percent_change = []
corr_price = []

for i in range(5):
    this_crypto = crypto_info[i].find_all('td')
    newName = this_crypto[2].text
    for i in range(31-len(newName)):
        newName += ' '
    names.append(newName)

    price = float(this_crypto[3].text.split('$')[1].replace(',',''))
    newCurrPrice = '$' + this_crypto[3].text.split('$')[1]
    for i in range(23-len(newCurrPrice)):
        newCurrPrice += ' '
    curr_price.append(newCurrPrice)
    if '+' in this_crypto[3].text:
        percent = float(this_crypto[3].text.split('+')[1].replace('%',''))
        percent_change.append('+' + this_crypto[3].text.split('+')[1])
        corr_price.append(f'${(1 - percent/100) * price:,.2f}')
    else:
        percent = float(this_crypto[3].text.split('-')[1].replace('%',''))
        percent_change.append('-' + this_crypto[3].text.split('-')[1])
        corr_price.append(f'${(1 - percent/100) * price:,.2f}')

print('Name\t\t\t\tCurrent Price\t\tPercent Change\t\t Corresponding Price')
for i in range(5):
    print(names[i], curr_price[i], percent_change[i], '\t\t\t', corr_price[i])
    print('-----------------------------------------------------------------------------------------------------------------')

for i in range(5):
    b = ""; sendText = False
    if "Bitcoin" in names[i] and float(curr_price[i].strip('$').replace(',', '')) < 40000:
        b += f"Bitcoin is currently {curr_price[i]}\n"
        sendText = True
    if "Ethereum" in names[i] and float(curr_price[i].strip('$').replace(',', '')) < 3000:
        b += f"Ethereum is currently {curr_price[i]}\n"
        sendText = True
    if sendText:
        # print(b)
        message = client.messages.create(
                 body=b,
                 from_=twilio_number,
                 to=my_number
             )
    