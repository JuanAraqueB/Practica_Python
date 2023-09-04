import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV
data = pd.read_csv('Emergencias_UNGRD_Original.xlsx.csv')

# Punto 1
cantidad_eventos = data['DEPARTAMENTO'].value_counts()
print(cantidad_eventos.head(5))

# Punto 2
data['FECHA'] = pd.to_datetime(data['FECHA'])
eventos = data['FECHA'].dt.year.value_counts()
print(eventos)

# Punto 3
e_2019 = data[data['FECHA'].dt.year == 2019]
n_categorias = e_2019['EVENTO'].nunique()
print('Cantidad de categorias:')
print(n_categorias)

categorias = e_2019['EVENTO'].value_counts().head(5)
print("Las 5 categorias mas frecuentes son:")
print(categorias)


# Punto 4.1
evento_fallecidos = e_2019.groupby('EVENTO')['FALLECIDOS'].sum().idxmax()
cantidad_fallecidos = e_2019.groupby('EVENTO')['FALLECIDOS'].sum().max()
print('Evento con más fallecidos: ', evento_fallecidos)
print('Cantidad: ', cantidad_eventos)

# Punto 4.2
evento_heridos = e_2019.groupby('EVENTO')['HERIDOS'].sum().idxmax()
cantidad_heridos = e_2019.groupby('EVENTO')['HERIDOS'].sum().max()
print('Evento con más heridos: ', evento_heridos)
print('Cantidad: ', cantidad_heridos)

# Punto 4.3
e_2019['HECTAREAS'] = e_2019['HECTAREAS'].str.replace(',', '.').astype(float)
evento_hectareas = e_2019.groupby('EVENTO')['HECTAREAS'].sum().idxmax()
cantidad_hectareas = e_2019.groupby('EVENTO')['HECTAREAS'].sum().max()
print('Evento con más hectareas perdidas: ', evento_hectareas)
print('Cantidad: ', cantidad_hectareas)

# Punto 5
movimientos_2019 = e_2019.groupby('DEPARTAMENTO')['FAMILIAS'].sum().idxmax()
cantidad_movimientos_2019 = e_2019.groupby('DEPARTAMENTO')['FAMILIAS'].sum().max()
print('Departamendo con mas movimientos 2019: ', movimientos_2019)
print('Cantidad: ', cantidad_movimientos_2019)

e_2020 = data[data['FECHA'].dt.year == 2020]
movimientos_2020 = e_2020.groupby('DEPARTAMENTO')['FAMILIAS'].sum().idxmax()
cantidad_movimientos_2020 = e_2020.groupby('DEPARTAMENTO')['FAMILIAS'].sum().max()
print('Departamendo con mas movimientos 2020: ', movimientos_2020)
print('Cantidad: ', cantidad_movimientos_2020)

e_2021 = data[data['FECHA'].dt.year == 2021]
movimientos_2021 = e_2021.groupby('DEPARTAMENTO')['FAMILIAS'].sum().idxmax()
cantidad_movimientos_2021 = e_2021.groupby('DEPARTAMENTO')['FAMILIAS'].sum().max()
print('Departamendo con mas movimientos 2021: ', movimientos_2021)
print('Cantidad: ', cantidad_movimientos_2021)

# Punto 6
e_2019 = data[data['FECHA'].astype(str).str.contains('2019')]
e_2019[['VALOR KIT DE ALIMENTO', 'VALOR MATERIALES DE CONSTRUCCION', 'RECURSOS EJECUTADOS']] = e_2019[['VALOR KIT DE ALIMENTO', 'VALOR MATERIALES DE CONSTRUCCION', 'RECURSOS EJECUTADOS']].apply(lambda x: x.str.replace('[^\d.]', '', regex=True)).astype(float)
kits_2019 = e_2019['VALOR KIT DE ALIMENTO'].sum()
materiales_construccion_2019 = e_2019['VALOR MATERIALES DE CONSTRUCCION'].sum()
total_recursos_2019 = e_2019['RECURSOS EJECUTADOS'].sum()
porcentaje_kits = (kits_2019 / total_recursos_2019) * 100
porcentaje_materiales_construccion = (materiales_construccion_2019 / total_recursos_2019) * 100
print(f"Porcentaje para kits de alimentos año 2019: {porcentaje_kits:.2f}%")
print(f"Porcentaje para materiales de construcción año 2019: {porcentaje_materiales_construccion:.2f}%")


# Punto 7
recursos = e_2019.groupby('EVENTO')['RECURSOS EJECUTADOS'].sum()
recursos_max = recursos.idxmax()
monto_max_recursos = recursos.max()
print(f"El evento en el que la UNGRD ejecutó más recursos en el año 2019 fue: {recursos_max}")
print(f"Valor: {monto_max_recursos}")

# Punto 8
eventos_2019_2021 = data[(data['FECHA'].dt.year >= 2019) & (data['FECHA'].dt.year <= 2021)]
eventos_2019_2021['MES'] = eventos_2019_2021['FECHA'].dt.month
eventos_por_mes = eventos_2019_2021['MES'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
eventos_por_mes.plot(kind='bar', color='r')
plt.title('Cantidad total de eventos por mes (2019-2021)')
plt.xlabel('Mes')
plt.ylabel('Cantidad de eventos')
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()

# Punto 9
data['FECHA'] = pd.to_datetime(data['FECHA'])
e_2019 = data[data['FECHA'].dt.year == 2019]
familias_max = e_2019['FAMILIAS'].idxmax()
municipio_max_familias = e_2019.loc[familias_max, 'MUNICIPIO']
print(f"En 2019, el evento que afectó a la mayor cantidad de familias ocurrió en el municipio: {municipio_max_familias}")

# Punto 10
eventos_años = data['FECHA'].dt.year.value_counts()
plt.figure(figsize=(10, 6))
eventos_años.plot(kind='bar', color='g')
plt.title('Porcentaje de Eventos por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Eventos')
plt.show()

