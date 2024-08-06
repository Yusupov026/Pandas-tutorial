import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')

#type(df)
#print(df)

#df2 = pd.DataFrame.from_dict({'a':[1,2], 'b':[3,4]})
#print(df2)

#df.info()
print(df.tail(3))

########### Первичный анализ DataFrame функции
1) df.info() - Общая информация
2) print(df.shape) - размер
3) print(df.columns) - Возвращает колонки
4) print(df.head(3)) - Первые 3 элементы
5) print(df.tail(3)) Последние 3 элемента  