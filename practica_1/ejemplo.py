import pandas as pd
import matplotlib.pyplot as plt

#df_emp = pd.read_csv('employees.csv', sep = ';')
#print(df_emp.DEPARTMENT_ID)


file_id = '17dJ5NaxghaGWrDCEtbFtRjfb7gqDXe-H'
# Construir la URL de descarga directa
url = f'https://drive.google.com/uc?id={file_id}'

# Lee el archivo CSV 
df_emp = pd.read_csv(url, sep=";")


#Listar los Empleados cuyo salario es mayor a 1500 0 dolares.
print(df_emp[df_emp.SALARY > 15000])

# Realizando proyección de Columnas
print(df_emp[df_emp.SALARY > 15000][["FIRST_NAME","SALARY"]])

# Listar los Empleados que ganan mas de 9000 dolares y menos de 14000 dolares
print(df_emp[(df_emp.SALARY >= 9000) & (df_emp.SALARY <= 10000)][['FIRST_NAME','LAST_NAME','SALARY']])

# Listar los empleados que pertenecen al departamento 50
print(df_emp[df_emp.DEPARTMENT_ID == 50][['FIRST_NAME','LAST_NAME','SALARY', 'DEPARTMENT_ID']])
print(df_emp[(df_emp.DEPARTMENT_ID == 50) & (df_emp.SALARY >= 6000)][['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']])

# Empleados que tienen salario superior a 15000 dolares y
# además pertenecen a los departamentos con codigosuperior a 50.
# Utilizando la funcion query()
# Primero mostrar todas las columnas
print(df_emp.query('SALARY>15000 and DEPARTMENT_ID>50'))
# Algunas columnas
print(df_emp.query('SALARY>15000 and DEPARTMENT_ID>50')[['FIRST_NAME','LAST_NAME']])

# Solucion ejercicio 1
print(df_emp[(df_emp.DEPARTMENT_ID == 50) & (df_emp.SALARY >= 4000)][['FIRST_NAME','LAST_NAME','SALARY','DEPARTMENT_ID']])
print(df_emp.query('SALARY>15000 and DEPARTMENT_ID>50')[['FIRST_NAME','LAST_NAME']])

# Solución ejercicio 2
print(df_emp[(df_emp.FIRST_NAME == "Alexander")][['FIRST_NAME','LAST_NAME','SALARY','EMPLOYEE_ID']])
print(df_emp.query('FIRST_NAME == "Alexander"')[['FIRST_NAME','LAST_NAME','SALARY','EMPLOYEE_ID']])

#-------------------------------------------------------------------------------------------
# Tipo de clase groupby
groupby_department = df_emp.groupby('DEPARTMENT_ID')
print(groupby_department)
print(type(groupby_department))
# Consultar el promedio del salario de cada departamento. (Agrupar por departamento)
print(groupby_department[['SALARY']].mean())

# Solución ejercicio 3
# Consultar la cantidad de empleados que pertenecen a cada departamento.
groupby_department[['EMPLOYEE_ID']].count()
# Es posible ordenar los datos
# ordenar de forma ascendente la cantidad de empleados por departamento
groupby_department[['EMPLOYEE_ID']].count().sort_values(by='EMPLOYEE_ID')
groupby_department[['EMPLOYEE_ID']].count().sort_values(by='EMPLOYEE_ID',ascending=True)
# Es posible ordenar los datos
# ordenar de forma descendente la cantidad de empleados por departamento
groupby_department[['EMPLOYEE_ID']].count().sort_values(by='EMPLOYEE_ID',ascending=False)

#Solución ejercicio 4
# Determinar para cada departamento cual es el minímo salario.
groupby_department[['SALARY']].min()

#Solución ejercicio 5
#Determinar para cada departamento cual es el máximo salario.
groupby_department[['SALARY']].max()


# Of distinct values in a column
# Para determinar los valores distintos en una serie o columna
print(df_emp['SALARY'].nunique())
print(df_emp['DEPARTMENT_ID'].nunique())
print(df_emp['COMMISSION_PCT'].nunique())

#---------------------------------------------------------------------------------
#groupby_salary = df_emp.groupby('SALARY')
#print('verificar')
#print(groupby_salary)
#print(type(groupby_salary))

# Solucion ejercicio 6.
# Seleccionar los empleados cuyo salario es igual al mínimo salario de la compañia.
minimo_salario = df_emp['SALARY'].min()
print('salario minimo')
print(minimo_salario)

print(df_emp[df_emp.SALARY == minimo_salario])
print(df_emp.query('SALARY == @minimo_salario'))


# Solucion ejercicio 7.
#Seleccionar los empleados cuyo salario es mayor al salario promedio de la compañia.
promedio_salario = df_emp['SALARY'].mean()
print('salario promedio')
print(promedio_salario)

print(df_emp[df_emp.SALARY > promedio_salario])
print(df_emp.query('SALARY > @promedio_salario'))

# Solucion ejercicio 8.
#Listar el empleado con el salario mas alto de la compañia
#Realizarlos tanto accediendo por el nombre de la serie, como utilizando la función query
maximo_salario = df_emp['SALARY'].max()
print('salario mas alto')
print(maximo_salario)

print(df_emp[df_emp.SALARY == maximo_salario])
print(df_emp.query('SALARY == @maximo_salario'))

# -----------------------------------------------------------------------------------------

#Solución ejercicio 9 Otra forma de hacer agrupamientos de datos utilizando el método value_counts().
# Se utiliza la serie JOB_ID o código de cargos para conocer la cantidad de empleados
# asignados en cada uno de los cargos.
df_emp['JOB_ID'].value_counts()

# Solución ejercicio 9
# Cuales son los 5 cargos más comunes. Utilizar el metodo value_counts()
# Se utiliza el metodo extendido nlargest() para filtrar del agrupamiento solo aquellos cargos con la mayor cantidad de empleados.
df_emp['JOB_ID'].value_counts().nlargest(5)

# Solución ejercicio 10
# Cuales son los 5 departamentos con más empleados (más comunes)
# Otra forma de hacer agrupamientos de datos utilizando el método value_counts().
# Se utiliza la codigo del departamento o DEPARTMENT_ID para conocer la cantidad de empleados que tiene cada departamento.
df_emp['DEPARTMENT_ID'].value_counts()

#Solución ejercicio 10
# Se utiliza el metodo extendido nlargest() para filtrar del agrupamiento solo aquellos departamentos con la mayor cantidad de empleados.
df_emp['DEPARTMENT_ID'].value_counts().nlargest(5)

# Otra forma de dar solución al ejercicio 9
#count number of rows with each unique value of variable
s_JOB_ID=df_emp['JOB_ID'].value_counts()
s_JOB_ID.head(n=5)
s_JOB_ID

# Otra forma de dar solución al ejercicio 10
s_department_id=df_emp['DEPARTMENT_ID'].value_counts()
s_department_id.head(n=5)
s_department_id

# Solución ejercicio 11
# Lista de empleados que el apellido contenga las letras "man". Posiblemente es necesario utilizar funciones como: contains, lower y upper.
# Gestión de strings
df_emp[df_emp.LAST_NAME.str.contains('man')] # convertir en mayuscula o minuscula --
df_emp[df_emp.LAST_NAME.str.lower().str.contains('man')] # convertir en mayuscula o minuscula --
df_emp[df_emp.LAST_NAME.str.upper().str.contains('MAN')] # convertir en mayuscula o minuscula --

# Solucion ejercicio 12
# Otro filtro sobre el DataFrame Empelados. Listar Empleados donde el apellido inicia por la vocal A
# Empleados cuyo apellido inicia por la vocal A
df_emp[df_emp.LAST_NAME.str.contains('^A', regex=True)]


#13. Listar los Empleados, que tengan en el apellido una letra H o la letra k.
print(df_emp[df_emp.LAST_NAME.str.contains('H|k')])

#14. Mostrar los Empleados, que tengan en el apellido una letra h, enseguida 2 caracteres cualquiera y luego la letra o.
print(df_emp[df_emp.LAST_NAME.str.contains('h..o', case=False, regex=True)])
print(df_emp[df_emp.LAST_NAME.str.contains('H..o', regex=True)])

#15. Listar los empleados, que finalicen con la letra g en el apellido.
print(df_emp[df_emp.LAST_NAME.str.endswith('g')])


#16. Nombre del empleado con mayor salario de la organización
maximo_salario = df_emp['SALARY'].max()
print('salario mas alto')
print(maximo_salario)

print(df_emp[df_emp.SALARY == maximo_salario])
print(df_emp.query('SALARY == @maximo_salario'))

#17. Ordene los salarios de los empleados de forma descendente. Utilice función sort_values
print(df_emp.sort_values(by='SALARY', ascending=False))

#18. Empleados cuyo salario es mayor o igual a 13500 y menor o igual a 17000. Mostrar las columnas FIRST_NAME, LAST_NAME, JOB_ID,SALARY.
print(df_emp[(df_emp.SALARY >= 13500) & (df_emp.SALARY <= 17000)][['FIRST_NAME','LAST_NAME', 'JOB_ID','SALARY']])

#19. Empleados que pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas DEPARTMENT_ID,FIRST_NAME. Utilice la función isin
departamentos_interes = [10, 20, 40, 70]
empleados_interes = df_emp[df_emp['DEPARTMENT_ID'].isin(departamentos_interes)][['DEPARTMENT_ID', 'FIRST_NAME']]
print('empleados que pertenecen')
print(empleados_interes)

#20. Empleados que NO pertenecen a los departamentos: 10, 20, 40 y 70. Mostrar solamente las columnas DEPARTMENT_ID,FIRST_NAME.Utilice la negación~
empleados_no_interes = df_emp[~df_emp['DEPARTMENT_ID'].isin(departamentos_interes)][['DEPARTMENT_ID', 'FIRST_NAME']]
print('empleados que no pertenecen')
print(empleados_no_interes)


# ------------- graficacion ------------

# Tipo de clase groupby
groupby_department = df_emp.groupby('DEPARTMENT_ID')

new_df_para_graficar=groupby_department[['EMPLOYEE_ID']].count()
print(new_df_para_graficar)

# Crear un DataFrame de ejemplo
df = pd.DataFrame(new_df_para_graficar)
 
# Exportar el DataFrame a CSV
df.to_csv('cant_emp_por_dep.csv', index=True)

df_cant_emp_por_dep = pd.read_csv('cant_emp_por_dep.csv', sep = ',')

plt.plot(df_cant_emp_por_dep.DEPARTMENT_ID,df_cant_emp_por_dep.EMPLOYEE_ID)

plt.title("Relacion de Empleados por Departamento")
plt.ylabel("Cantidad de Empleados")
plt.xlabel("Numero de Departamento")
plt.show()

# FIGURA 2

plt.figure()
#Figura
x_values1 = df_cant_emp_por_dep.DEPARTMENT_ID
y_values1 = df_cant_emp_por_dep.EMPLOYEE_ID
plt.bar(x_values1, y_values1)
plt.title("Relacion de Empleados por Departamento")
plt.ylabel("Cantidad de Empleados")
plt.xlabel("Numero de Departamento")
plt.show()


# FIGURA 3
# Datos
x_values1 = df_cant_emp_por_dep.DEPARTMENT_ID
y_values1 = df_cant_emp_por_dep.EMPLOYEE_ID
# Gráfico de barras
fig, ax = plt.subplots()
plt.grid()
ax.bar(x = x_values1, height = y_values1)
plt.show()

# FIGURA 4
plt.figure()
#Figura
x_values1 = df_cant_emp_por_dep.DEPARTMENT_ID
y_values1 = df_cant_emp_por_dep.EMPLOYEE_ID
ax = plt.subplot(1,1,1)
#Axis
plt.bar(x_values1, y_values1)
#El gráfico
plt.title('Relacion de Empleados por Departamento')
#El título
ax.set_xticks(x_values1)
plt.grid()
#Eje x
ax.set_xticklabels(x_values1, rotation=60)
#Etiquetas del eje x
ax.set_xlabel('Numero de Departamento')
#Nombre del eje x
ax.set_ylabel('Cantidad de Empleados')
#Nombre del eje y
plt.show()

