import pandas as pd


data = {
    'Name': ['girija', 'anu', 'abhi', 'varsha'],
    'Age': [22, 22, 27, 18],
    'place': ['bangalore', 'moodalapalya', 'XYZ', 'jayanagar']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nAges:\n", df['Age'])

print("\nPeople older than 25:\n", df[df['Age'] > 25])

df['Salary'] = [70000, 80000, 65000, 90000]
print("\nDataFrame with Salary column:\n", df)

print("\nAverage Age:", df['Age'].mean())

