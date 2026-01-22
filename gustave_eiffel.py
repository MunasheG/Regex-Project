import re
import urllib.request
from urllib.request import Request, urlopen
import matplotlib.pyplot as plt
import numpy as np

url = 'https://en.wikipedia.org/wiki/Gustave_Eiffel'

req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
hand = urllib.request.urlopen(req)

html = hand.read().decode('utf-8')
hand = urlopen(req)
# counts
list_dates = []
final_dates =[]

for line in hand:
    line = line.decode().strip()
    if re.search('Registres', line):
        break
    list_date = re.findall('[12][089][0-9][0-9]', line)
    if list_date != []:
        list_dates = list_dates + list_date
    for year in list_date:
        if int(year) >= 1800 and int(year) <= 2011:
            final_dates.append(year)
final_dates=[int(d) for d in final_dates]
print(final_dates)

#Histogram
plt.hist(final_dates, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Dates')
plt.ylabel('Frequency')
plt.title('Dates in Gustave Eiffle Bio')

ticks = np.linspace(min(final_dates), max(final_dates), 12)
#plt.xticks(ticks, rotation=45)
plt.savefig('dates.png', dpi=200)
plt.show()
        
        
