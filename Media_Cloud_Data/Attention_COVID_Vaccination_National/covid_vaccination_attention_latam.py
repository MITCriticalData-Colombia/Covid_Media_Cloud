import glob
import pandas as pd

df_to_concat = []
res = None

for filename in glob.glob("*.csv"):
    df = pd.read_csv(filename)
    # rename columns
    columns = list(df.columns)
    for i, c in enumerate(columns):
        if c != "date":
            country_name = filename[:-4]
            columns[i] = columns[i] + f"_{country_name}"
    df.columns = columns
    if res is None:
        res = df.copy(deep=True)
    else:
        res = res.merge(df, left_on="date", right_on="date")

res.to_csv("covid_vaccination_attention_latam.csv")
