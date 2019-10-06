# %% Importamos las librerías correspondientes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Cargamos los datos del archivo CSV
electricity_prices = pd.read_csv("electricity_prices_household.csv", delimiter=";")

electricity_prices.shape

es_electricity = electricity_prices.loc[(electricity_prices['geo\\time'] == 'ES') & (electricity_prices['tax'] == 'X_TAX') & (electricity_prices['currency'] == 'EUR')]
es_electricity

# %% Generamos los valores para reproducirlos
x = np.flip(es_electricity.columns[6:].to_numpy())

nparray = es_electricity.to_numpy()
y1 = np.flip(nparray[0, 6:])
y2 = np.flip(nparray[1, 6:])
y3 = np.flip(nparray[2, 6:])
y4 = np.flip(nparray[3, 6:])
y5 = np.flip(nparray[4, 6:])



# %% Reproducimos con puntos para poder comparar mejor
plt.figure(figsize=(20,20))
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)

plt.ylabel('Cost')
plt.xlabel('Time')
plt.show()
