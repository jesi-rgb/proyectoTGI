# %% IMPORTAMOS LAS LIBRERÍAS CORRESPONDIENTES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% CARGAMOS LOS DATOS DEL ARCHIVO CSV
electricity_prices = pd.read_csv("electricity_prices_household.csv", delimiter=";")

electricity_prices.shape

#tomamos solo las filas que contengan lo que nos interesa: datos de españa, precios sin tasas añadidas y el precio representado en euros
es_electricity = electricity_prices.loc[(electricity_prices['geo\\time'] == 'ES') & (electricity_prices['tax'] == 'X_TAX') & (electricity_prices['currency'] == 'EUR')]


# %% GENERAMOS LOS VALORES PARA REPRODUCIRLOS

# eliminamos la columna correspondiente al primer semestre de 2007,
# ya que no hay datos de esa época
es_electricity = es_electricity.drop(columns="2007S1")

# le damos la vuelta porque los años están dispuestos del revés
# generamos la x que pondremos abajo en nuestra gráfica
x = np.flip(es_electricity.columns[6:].to_numpy())

# convertimos el DataFrame de pandas a un numpy array para manipularlo más fácilmente
nparray = es_electricity.to_numpy()

# hacemos lo mismo que con la x, pero con la y
y1 = np.flip(nparray[0, 6:])
y2 = np.flip(nparray[1, 6:])
y3 = np.flip(nparray[2, 6:])
y4 = np.flip(nparray[3, 6:])
y5 = np.flip(nparray[4, 6:])

# el siguiente paso es castearlos a un tipo flotante,
# así que nos aseguramos de que los valores no numéricos
# no existan

y1[y1 == ': '] = -1
y2[y2 == ': '] = -1
y3[y3 == ': '] = -1
y4[y4 == ': '] = -1
y5[y5 == ': '] = -1

# convertimos el array a float, ya que hasta ahora era
# un array de strings
y1 = y1.astype(float)
y2 = y2.astype(float)
y3 = y3.astype(float)
y4 = y4.astype(float)
y5 = y5.astype(float)



# %% REPRODUCIMOS CON PUNTOS PARA PODER COMPARAR MEJOR
plt.figure(figsize=(20,10))
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
legend = ["< 1000 kWh", "1000 kWh < Consumption < 2500 kWh","2500 kWh < Consumption < 5000 kWh","5000 kWh < Consumption < 15000 kWh",]
plt.legend(legend)
plt.ylabel('Cost')
plt.xlabel('Time')
plt.title("Cost of energy per year per consumption category, no taxes applied")
plt.show()
