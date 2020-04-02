# analysis of just UK Cases
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import pandas as pd
import os
import datetime as dt
from matplotlib import style


# make the directory current
# os.chdir(r'C:\Users\paul\Dropbox\Paul\COVID19')

# get the data from a downloaded excel file
data = pd.read_excel(r'C:\Users\paul\Dropbox\Paul\COVID19\covid19Data.xlsx')

# change the index to the territory code
data.index = data['geoId']

# filter UK data
uk_data = data.loc['UK', :]

# plot the Cases
x=dt.datetime.strptime('2020/03/23', '%Y/%m/%d').date()
y = dt.datetime.strptime('2020/04/06','%Y/%m/%d').date()
ax1 = plt.subplot2grid((1,2), (0,0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((1,2), (0,1), rowspan=1, colspan=1)
ax1.plot(uk_data['dateRep'], uk_data['cases'], 'red')
plt.sca(ax1)
plt.axvline(x,0,2000)
plt.axvline(y,0,2000)
plt.grid()
plt.xlabel('Date')
plt.ylabel('Number per day')
plt.title('COVID19 Cases')
plt.xticks(rotation=45)
ax2.plot(uk_data['dateRep'], uk_data['deaths'], 'red')
plt.sca(ax2)
plt.axvline(x,0,2000)
plt.axvline(y,0,2000)
plt.grid()
plt.xlabel('Date')
plt.ylabel('Number per day')
plt.title('COVID19 Deaths')
plt.xticks(rotation=45)
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.tight_layout()
plt.show()
