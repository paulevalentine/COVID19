import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import os
plt.style.use('dark_background')


os.chdir(r'C:\Users\paul\Dropbox\Paul\COVID19')


df = pd.read_excel('road_accident_data.xlsx', index_col='Accident year')
plt.plot(df)
plt.grid('grey', linestyle='dotted')
plt.xlabel('Year')
plt.ylabel('No of Accidents')
plt.show()
