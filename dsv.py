import pandas as pd

df11 = pd.read_csv("worldsData/2011.csv")
df12 = pd.read_csv("worldsData/2012.csv")
df13 = pd.read_csv("worldsData/2013.csv")
df14 = pd.read_csv("worldsData/2014.csv")
df15 = pd.read_csv("worldsData/2015.csv")
df16 = pd.read_csv("worldsData/2016.csv")
df17 = pd.read_csv("worldsData/2017.csv")
df18 = pd.read_csv("worldsData/2018.csv")
df19 = pd.read_csv("worldsData/2019.csv")
df20 = pd.read_csv("worldsData/2020.csv")
df21 = pd.read_csv("worldsData/2021.csv")

dfs = [df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21]


# we want
filters = ["Champion", "Pos", "GP", "P%", "B%", "P+B%", "W%"]

for i in range(len(dfs)):
	dfs[i] = dfs[i].filter(filters)

baseYear = 2011
for i in range(len(dfs)):
	dfs[i]["Year"] = baseYear
	baseYear += 1

df = pd.concat(dfs)


# print(df.loc[df["GP"].idxmax()])

# print(len(df))

df["P%"] = df['P%'].str.rstrip('%').astype(float)
df["B%"] = df['B%'].str.rstrip('%').astype(float)
df["P+B%"] = df['P+B%'].str.rstrip('%').astype(float)
df["W%"] = df['W%'].str.rstrip('%').astype(float)

# print(len(df))

# for col in df.columns:
#     print(col)
# print(data[0])
df.to_csv('worlds2.csv', index=False)




