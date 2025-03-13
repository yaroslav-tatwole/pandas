import pandas as pd
df_excel = pd.read_excel('data.xlsx')
print(df_excel.head())
num_rows, num_columns = df.shape
data_types = df.dtypes

print("\nТипы данных каждого столбца:")
print(data_types)
E=Age
filtered_df = df[(df['E'] > 18)]
print("\nВыбранные строки (возраст > 18 :" )
print(filtered_df)
missing_values = df.isnull().sum()

print("\nСтолбцы с пропущенными значениями:")
print(missing_values[missing_values > 0])





