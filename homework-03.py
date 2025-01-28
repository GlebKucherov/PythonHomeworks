import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значения
# - словари


Series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']) # список Python
print (Series1)


Series2 = pd.Series(np.array([1, 2, 3, 4]), index=['a', 'b', 'c', 'd']) # массив Python
print (Series2)


Series3 = pd.Series(10, index=['a', 'b', 'c', 'd']) # скалярное значение
print (Series3)


dict = {
        'Liverpool': 'England',
        'Los Angeles': 'USA',
        'Melbourne': 'Australia',
        'Saint Petersburg': 'Russia',
        }
Series4 = pd.Series(dict) # словарь
print (Series4)


# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy


series1 = pd.Series([1, 2, 3, 4])
series2 = pd.Series([5, 6, 7])
DataFrame1 = pd.DataFrame([series1, series2])
print (DataFrame1) # Через объекты Series


dict1 = {
        'Liverpool': 'England',
        'Los Angeles': 'USA',
        'Melbourne': 'Australia',
        'Saint Petersburg': 'Russia',
        }
dict2 = {
        'Liverpool': 'Europe',
        'Los Angeles': 'North America',
        'Melbourne': 'Australia',
        'Saint Petersburg': 'Europe',
    }
DataFrame2 = pd.DataFrame([dict1, dict2]) # Через список словарей
print (DataFrame2)


Series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], name='Column1')
Series2 = pd.Series([5, 6, 7, 8], index=['a', 'b', 'c', 'd'], name='Column2')
DataFrame3 = pd.DataFrame({Series1.name: Series1, Series2.name: Series2}) # Через словари объектов Series
print (DataFrame3)


a = np.array([[0,1,2], [3,4,5]])
DataFrame4 = pd.DataFrame(a) # Через двумерный массив NumPy
print (DataFrame4)


data = np.zeros(4, dtype = {
    'names':(
        'name', 'age'
    ),
    'formats':(
        'U10', 'i4'
    )
})
name = ['name1', 'name2', 'name3', 'name4']
age = [10,20,30,40]
data['name'] = name
data['age'] = age
DataFrame5 = pd.DataFrame(data) # Через структурированный массив NumPy
print (DataFrame5)


# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1


pop = pd.Series(
    {
        'city_1': 1001,
        'city_2': 1002,
        'city_3': 1003,
        'city_41': 1004,
        'city_51': 1005,
    })

area = pd.Series(
    {
        'city_1': 9991,
        'city_2': 9992,
        'city_3': 9993,
        'city_42': 9994,
        'city_52': 9995,
    })

data = pd.DataFrame({'area1':area, 'pop1':pop, 'pop':pop})

print (data.fillna(1))


# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ


rng = np.random.default_rng(1)
A = rng.integers(0, 10, (3,4))
print (A)
df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print (df)
print (df.iloc[:,0])
print (df.subtract(df.iloc[:,0], axis=0))

print (df.iloc[::2, 0])
print (df.subtract(df.iloc[::2, 0], axis=0))


# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()


series = pd.Series([np.nan, None, 3, 4, pd.NA, 6])
print (series)
print (series.ffill()) # ffill заполняет NA-значения ближайшими предыдущими численными значениями (если они есть)
print (series.bfill()) # bfill заполняет NA-значения ближайшими следующими численными значениями (если они есть)

df = pd.DataFrame(
    [
      [1,2,3,np.nan,None,pd.NA],
      [1,2,3,None,5,6],
      [1,np.nan,3,None,np.nan,6],
      ]
    )
print (df)
print (df.ffill()) # по умолчанию заполнение идёт по столбцам
print (df.bfill()) # по умолчанию заполнение идёт по столбцам
print (df.ffill(axis=1)) # заполнение идёт по строкам
print (df.bfill(axis=1)) # заполнение идёт по строкам