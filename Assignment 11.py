
import pandas as pd
import numpy as np

numbers = np.random.randint(1, 100, 10)
ser = pd.Series(numbers)

print("1. Pandas Series with 10 Random Numbers:")
print(ser)


ser_custom = pd.Series(
    [10, 20, 30, 40, 50],
    index=['a', 'b', 'c', 'd', 'e']
)

print("\n2. Series with Custom Index:")
print(ser_custom)


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
}

df = pd.DataFrame(data)

print("\n3. DataFrame:")
print(df)


data = [
    {'Name': 'Alice', 'Age': 24, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 27, 'City': 'Los Angeles'}
]

df = pd.DataFrame(data)

print("\n4. DataFrame from List of Dictionaries:")
print(df)


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston']
}

df = pd.DataFrame(data)

print("\n5. Single Column:")
print(df['Name'])

print("\nMultiple Columns:")
print(df[['Name', 'City']])

print("\nFirst Row:")
print(df.iloc[0])

print("\nSecond and Third Rows:")
print(df.iloc[1:3])

print("\nRow by Label:")
print(df.loc[0])

print("\nRows by Label:")
print(df.loc[1:3])


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, None, 22, 25],
    'City': ['New York', 'Los Angeles', None, 'Boston']
}

df = pd.DataFrame(data)

print("\n6. Missing Values:")
print(df.isnull())

print("\nAfter Dropping Missing Values:")
print(df.dropna())

print("\nAfter Filling Missing Values:")
print(df.fillna({
    'Age': df['Age'].mean(),
    'City': 'Unknown'
}))


data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'Age': [24, 27, 24, 22]
}

df = pd.DataFrame(data)

print("\n7. Original DataFrame:")
print(df)

print("\nAfter Removing Duplicates:")
print(df.drop_duplicates())


df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5],
    'Age': [24, 27, 22]
})

print("\n8. Inner Join:")
print(pd.merge(df1, df2, on='ID', how='inner'))

print("\nLeft Join:")
print(pd.merge(df1, df2, on='ID', how='left'))

print("\nRight Join:")
print(pd.merge(df1, df2, on='ID', how='right'))

print("\nOuter Join:")
print(pd.merge(df1, df2, on='ID', how='outer'))


# 9. Aggregation and Grouping
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 52000, 58000]
}

df = pd.DataFrame(data)

grouped = df.groupby('Department')

print("\n9. Average Salary:")
print(grouped['Salary'].mean())

print("\nMultiple Aggregations:")
print(grouped['Salary'].agg(['mean', 'sum', 'max']))

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'],
    'Age': [24, 27, None, 30, 24],
    'Department': ['HR', 'IT', 'HR', 'IT', 'HR'],
    'Salary': [50000, 60000, 52000, 58000, 50000]
}

df = pd.DataFrame(data)

print("\n10. Original Employee Data:")
print(df)

df_cleaned = df.drop_duplicates()

df_cleaned = df_cleaned.copy()

df_cleaned['Age'] = df_cleaned['Age'].fillna(
    df_cleaned['Age'].mean()
)

print("\nCleaned Employee Data:")
print(df_cleaned)

print("\nAverage Salary by Department:")
avg_salary = df_cleaned.groupby('Department')['Salary'].mean()
print(avg_salary)

print("\nOldest and Youngest Employee in Each Department:")
age_stats = df_cleaned.groupby('Department')['Age'].agg(['max', 'min'])
print(age_stats)
