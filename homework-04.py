import numpy as np
import pandas as pd



# 1. Разобраться как использовать мультииндексные ключи в данном примере
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]
pop = pd.Series(population, index = index)
pop.index = pd.MultiIndex.from_tuples(pop.index) # Необходимо преобразовать индексы в мультииндекс, чтобы можно было обращаться к ним по отдельности
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)

print (pop_df)

pop_df_1 = pop_df.loc['city_1', 'something']
print (pop_df_1)

pop_df_2 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print (pop_df_2)

pop_df_3 = pop_df.loc[['city_1', 'city_3'], 'something']
print (pop_df_3)



# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2 

data = {
    ('city_1', 2010): 100,
    ('city_1', 2020): 200,
    ('city_2', 2010): 1001,
    ('city_2', 2020): 2001,   
}

s = pd.Series(data)
print (s)

s.index.names = ['city', 'year']
print (s)

index = pd.MultiIndex.from_product(
      [
          ['city_1', 'city_2'],
          [2010, 2020]
      ],
      names=['city', 'year']
)
print (index)

columns = pd.MultiIndex.from_product(
      [
          ['person_1', 'person_2', 'person_3'],
          ['job_1', 'job_2']
      ],
      names=['worker', 'job']
)

rng = np.random.default_rng(1)

data = rng.random((4, 6))
print (data)

data_df = pd.DataFrame(data, index=index, columns=columns)
print (data_df)

print (data_df.loc[(slice(None), 2020), :]) # данные по 2020 году (для всех столбцов)

print (data_df.loc[:, (slice(None), 'job_1')]) # данные по job_1 (для всех строк)

print(data_df.loc[('city_1', slice(None)), (slice(None), 'job_2')]) # данные для city_1 и job_2  



# 3. Взять за основу DataFrame со следующей структурой
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)
# 
# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использованием срезов)

print (data_df.loc[:, (['person_1','person_3'], slice(None))]) # все данные по person_1 и person_3

print (data_df.loc[('city_1', slice(None)), (slice('person_1','person_2'), slice(None))]) # все данные по первому городу и первым двум person-ам (с использованием срезов)

# Приведите пример (самостоятельно) с использованием pd.IndexSlice

idx = pd.IndexSlice
print (data_df.loc[idx[:, 2020], idx['person_1':'person_2', :]]) # все данные по 2020 году и первым двум person-ам (с использованием pd.IndexSlice)



#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)

ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['b', 'c', 'f'], index=[3,4,5])
print (ser1)
print (ser2)

print (pd.concat([ser1, ser2], axis=1, join='outer')) # производит объединение по всем индексам
print (pd.concat([ser1, ser2], axis=1, join='inner')) # производит объединение только по общим индексам 