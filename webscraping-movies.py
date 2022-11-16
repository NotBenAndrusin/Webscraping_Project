
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

movie_rows = soup.findAll("tr")


# skip 0 because first tr has nothing in it
for row in rows[1:6]:
    td = row.findAll('td')
    if td:
        try:
            total_gross = td[7].text.lstrip('$')
            total_gross_1 = total_gross.replace(',','')
            theaters = td[6].text.replace(',','')
            avg_gross = float(total_gross_1)/float(theaters)
        except:
            avg_gross = 'N/A'
        print('Rank:',td[0].text)
        print('Movie Name',td[1].text)
        print('Total Gross',td[7].text)
        print('Distributor:',td[9].text)
        print('Avg Gross/Theater:',"${:,.2f}".format(avg_gross))
        print()
        print()

