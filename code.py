import pandas as pd
import os

data = {
    "name": ["John", "Jane", "Jim", "Jill"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)


new_row = {
    "name": " vardhan",
    "age": 20,
    "city": "Hyderabad"
}


second_row = {
    "name": "Eswar",
    "age": 20,
    "city": "Hyderabad"
}

df.loc[len(df)] = new_row
df.loc[len(df)] = second_row

dir = "data"

os.makedirs(dir, exist_ok=True)

file_path = os.path.join(dir, "data.csv")

 


df.to_csv(file_path, index=False)   
# below code will read the data from the csv file and print it
df = pd.read_csv(file_path)
print(df)

