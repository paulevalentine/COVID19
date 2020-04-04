"""Plot the COVID19 data for countries by population."""
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})


def get_covid_data(date):
    """Get data and save to a local excel file."""
    url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-{}.xlsx'.format(
        date)
    datapath = r'C:\Users\paul\Dropbox\Paul\COVID19\covid19Data.xlsx'
    urllib.request.urlretrieve(url, datapath)
    print('Data retrieved')


def plot_world_data():
    """Plot a selectoin fo world data for deaths and cases."""
    # Get data from local file
    datapath = r'C:\Users\paul\Dropbox\Paul\COVID19\covid19Data.xlsx'
    getData = pd.read_excel(datapath)
    # Set up a dataFrame and filter the data by country
    data = pd.DataFrame(getData)
    data.index = data['geoId']
    uk = data.filter(like='UK', axis=0)
    us = data.filter(like='US', axis=0)
    it = data.filter(like='IT', axis=0)
    cn = data.filter(like='CN', axis=0)
    es = data.filter(like='ES', axis=0)
    fr = data.filter(like='FR', axis=0)

    # Make numpy arrays of the data
    # UK Data
    ukx = np.array(uk['dateRep'])
    uky = np.array(uk['cases'])
    ukz = np.array(uk['deaths'])
    ukp = np.array(uk['popData2018'])
    cumDeath = uk['deaths'][::-1].cumsum()[::-1]
    cumCase = uk['cases'][::-1].cumsum()[::-1]
    ukdr = 100 * cumDeath / cumCase

    # US Data
    usx = np.array(us['dateRep'])
    usy = np.array(us['cases'])
    usz = np.array(us['deaths'])
    usp = np.array(us['popData2018'])
    cumDeath = us['deaths'][::-1].cumsum()[::-1]
    cumCase = us['cases'][::-1].cumsum()[::-1]
    usdr = 100 * cumDeath / cumCase
    # Italian data
    itx = np.array(it['dateRep'])
    ity = np.array(it['cases'])
    itz = np.array(it['deaths'])
    itp = np.array(it['popData2018'])
    cumDeath = it['deaths'][::-1].cumsum()[::-1]
    cumCase = it['cases'][::-1].cumsum()[::-1]
    itdr = 100 * cumDeath / cumCase
    # China Data
    cnx = np.array(cn['dateRep'])
    cny = np.array(cn['cases'])
    cnz = np.array(cn['deaths'])
    cnp = np.array(cn['popData2018'])
    cumDeath = cn['deaths'][::-1].cumsum()[::-1]
    cumCase = cn['cases'][::-1].cumsum()[::-1]
    cndr = 100 * cumDeath / cumCase
    # Spanish Data
    esx = np.array(es['dateRep'])
    esy = np.array(es['cases'])
    esz = np.array(es['deaths'])
    esp = np.array(es['popData2018'])
    cumDeath = es['deaths'][::-1].cumsum()[::-1]
    cumCase = es['cases'][::-1].cumsum()[::-1]
    esdr = 100 * cumDeath / cumCase
    # French Data
    frx = np.array(fr['dateRep'])
    fry = np.array(fr['cases'])
    frz = np.array(fr['deaths'])
    frp = np.array(fr['popData2018'])
    cumDeath = fr['deaths'][::-1].cumsum()[::-1]
    cumCase = fr['cases'][::-1].cumsum()[::-1]
    frdr = 100 * cumDeath / cumCase
    # plot the data
    plt.figure(figsize=[12, 12])

    # Deaths normalised by population
    plt.subplot(2, 2, 1)
    plt.plot(ukx, 100*ukz/ukp, label='UK {}'.format(np.sum(ukz)))
    plt.plot(usx, 100 * usz/usp, label='US {}'.format(np.sum(usz)))
    plt.plot(itx, 100*itz/itp, label='IT {}'.format(np.sum(itz)))
    plt.plot(cnx, 100*cnz/cnp, label='CN {}'.format(np.sum(cnz)))
    plt.plot(esx, 100*esz/esp, label='ES {}'.format(np.sum(esz)))
    plt.plot(frx, 100*frz/frp, label='FR {}'.format(np.sum(frz)))
    plt.xticks(rotation=45)
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('% of population per day')
    plt.legend()
    plt.title('Deaths from COVID 19 normalised by population')

    # Cases normalised by population
    plt.subplot(2, 2, 2)
    plt.plot(ukx, 100*uky/ukp, label='UK {}'.format(np.sum(uky)))
    plt.plot(usx, 100*usy/usp, label='US {}'.format(np.sum(usy)))
    plt.plot(itx, 100*ity/itp, label='IT {}'.format(np.sum(ity)))
    plt.plot(cnx, 100*cny/cnp, label='CN {}'.format(np.sum(cny)))
    plt.plot(esx, 100*esy/esp, label='ES {}'.format(np.sum(esy)))
    plt.plot(frx, 100*fry/frp, label='FR {}'.format(np.sum(fry)))
    plt.xticks(rotation=45)
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('% of population per day')
    plt.legend()
    plt.title('Cases of COVID 19 normalised by population')

    # Death Rates
    plt.subplot(2, 2, 3)
    plt.plot(ukx, ukdr, label='UK: {:.2f}%'.format(100 * np.sum(ukz)/np.sum(uky)))
    plt.plot(usx, usdr, label='US: {:.2f}%'.format(100 * np.sum(usz)/np.sum(usy)))
    plt.plot(itx, itdr, label='IT: {:.2f}%'.format(100 * np.sum(itz)/np.sum(ity)))
    plt.plot(cnx, cndr, label='CN: {:.2f}%'.format(100 * np.sum(cnz)/np.sum(cny)))
    plt.plot(esx, esdr, label='ES: {:.2f}%'.format(100 * np.sum(esz)/np.sum(esy)))
    plt.plot(frx, frdr, label='FR: {:.2f}%'.format(100 * np.sum(frz)/np.sum(fry)))
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Death Rate %')
    plt.title('COVID 19 Death Rates')
    plt.legend()
    plt.grid()

    plt.show()


def plot_uk_data():
    """Plot the UK data."""
    data = pd.read_excel(r'C:\Users\paul\Dropbox\Paul\COVID19\covid19Data.xlsx')
    # change the index to the territory code
    data.index = data['geoId']
    # filter UK data
    uk_data = data.loc['UK', :]
    # plot the Cases
    plt.figure(figsize=[12, 12])
    x = dt.datetime.strptime('2020/03/23', '%Y/%m/%d').date()
    y = dt.datetime.strptime('2020/04/06', '%Y/%m/%d').date()
    ax1 = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=2)
    ax1.plot(uk_data['dateRep'], uk_data['cases'], 'red')
    plt.sca(ax1)
    plt.axvline(x, 0, 2000)
    plt.axvline(y, 0, 2000)
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Number per day')
    plt.title('COVID19 Cases')
    plt.xticks(rotation=45)
    ax2.plot(uk_data['dateRep'], uk_data['deaths'], 'red')
    plt.sca(ax2)
    plt.axvline(x, 0, 2000)
    plt.axvline(y, 0, 2000)
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Number per day')
    plt.title('COVID19 Deaths')
    plt.xticks(rotation=45)
    cumDeath = uk_data['deaths'][::-1].cumsum()[::-1]
    cumCase = uk_data['cases'][::-1].cumsum()[::-1]
    ukdr = 100 * cumDeath / cumCase
    ax3.plot(uk_data['dateRep'], ukdr, 'red')
    plt.sca(ax3)
    plt.axvline(x, 0, 2000)
    plt.axvline(y, 0, 2000)
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Rate %')
    plt.title('COVID19 Death Rate')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
