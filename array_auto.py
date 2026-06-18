import pandas as pd

# Read Excel
df = pd.read_excel("matrices.xlsx")

# Extract arrays from excel
array1 = df.iloc[:, 0:2]
array2 = df.iloc[:, 2:4]

# Add arrays
result = array1 + array2

print(result)