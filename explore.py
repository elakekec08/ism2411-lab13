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

# --- Exercise 3 ---
top_five = df.sort_values("revenue", ascending=False).head(5)

print("\nExercise 3:")
print(top_five)


# --- Exercise 4 ---
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print("\nExercise 4:")
print(len(big_south))
print(big_south.head())

# --- Exercise 5 ---
df["per_unit"] = df["revenue"] / df["quantity"]

print("\nExercise 5:")
print(df.head())
print(df["per_unit"].mean())


# --- Exercise 6 ---
print("\nExercise 6:")
print(df["region"].unique())
print(df["region"].value_counts())
