import pandas as pd


# --- Exercise 1 ---
df = pd.read_csv("data/retail_sales.csv")

print("Exercise 1:")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# --- Exercise 2 ---
south = df[df["region"] == "South"]

print("\nExercise 2:")
print(len(south))
print(south.head())
