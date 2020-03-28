import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import urllib.request

pd.set_option('display.expand_frame_repr', False)
# get data from website and save to local location (datapath)
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-27.xlsx'
datapath = r'C:\Users\paul\Dropbox\Paul\COVID19\covid19Data.xlsx'
file = urllib.request.urlretrieve(url,datapath)

# Get data from local file
getData = pd.read_excel(datapath)

# Set up a dataFrame and filter the data by country
data = pd.DataFrame(getData)
data.index = getData['geoId']
uk = data.filter(like='UK', axis = 0)
us = data.filter(like='US', axis = 0)
it = data.filter(like='IT', axis = 0)
cn = data.filter(like='CN', axis = 0)
es = data.filter(like='ES', axis = 0)
fr = data.filter(like='FR', axis = 0)

# Make numpy arrays of the data
# UK Data
ukx = np.array(uk['dateRep'])
uky = np.array(uk['cases'])
ukz = np.array(uk['deaths'])
ukp = np.array(uk['popData2018'])

# US Data
usx = np.array(us['dateRep'])
usy = np.array(us['cases'])
usz = np.array(us['deaths'])
usp = np.array(us['popData2018'])

# Italian data
itx = np.array(it['dateRep'])
ity = np.array(it['cases'])
itz = np.array(it['deaths'])
itp = np.array(it['popData2018'])

# China Data
cnx = np.array(cn['dateRep'])
cny = np.array(cn['cases'])
cnz = np.array(cn['deaths'])
cnp = np.array(cn['popData2018'])

# Spanish Data
esx = np.array(es['dateRep'])
esy = np.array(es['cases'])
esz = np.array(es['deaths'])
esp = np.array(es['popData2018'])

# French Data
frx = np.array(fr['dateRep'])
fry = np.array(fr['cases'])
frz = np.array(fr['deaths'])
frp = np.array(fr['popData2018'])

# plot the data
plt.figure(figsize=[5,5])
# Deaths normalised by population
plt.subplot(1,2,1)
plt.plot(ukx,100*ukz/ukp, label = 'UK')
plt.plot(usx,100* usz/usp, label = 'US')
plt.plot(itx, 100*itz/itp, label = 'IT')
plt.plot(cnx,100*cnz/cnp, label = 'CN')
plt.plot(esx,100*esz/esp, label = 'ES')
plt.plot(frx,100*frz/frp, label = 'FR')
plt.xticks(rotation=20)
plt.grid()
plt.xlabel('Date')
plt.ylabel('% of population per day')
plt.legend()
plt.title('Deaths from COVID 19 normalised by population')

# Cases normalised by population
plt.subplot(1,2,2)
plt.plot(ukx,100*uky/ukp, label = 'UK')
plt.plot(usx, 100*usy/usp, label = 'US')
plt.plot(itx, 100*ity/itp, label = 'IT')
plt.plot(cnx,100*cny/cnp, label = 'CN')
plt.plot(esx,100*esy/esp, label = 'ES')
plt.plot(frx,100*fry/frp, label = 'FR')
plt.xticks(rotation=20)
plt.grid()
plt.xlabel('Date')
plt.ylabel('% of population per day')
plt.legend()
plt.title('Cases of COVID 19 normalised by population')
plt.show()
