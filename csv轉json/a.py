import pandas as pd
a = pd.read_csv("data.csv")
b = a.to_json("data.json", orient="records", force_ascii=False)
