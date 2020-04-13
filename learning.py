import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv(r'C:\Users\paul\Dropbox\Paul\Market Analysis\DCC.L.csv')

data = df['close']

y = data.values
x = np.arange(len(y))

poly = PolynomialFeatures(degree=8)
x_poly = poly.fit_transform(x.reshape(-1, 1))
model = LinearRegression()
model.fit(x_poly, y.reshape(-1, 1))
y_pred = model.predict(x_poly)


plt.scatter(x, y, s=2)
plt.plot(x, y_pred, color='red')
plt.show()
