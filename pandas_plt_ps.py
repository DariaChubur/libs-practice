import kagglehub
import pandas as pd

# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
# df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# depression=df[['depression_pct', "country"]]
# europe_depression=df[df["region"]=="Europe"]
# print(europe_depression[["country", "suicide_rate_per100k"]])

# mask = (df["region"]=="Europe") & (df["depression_pct"]>5)
# europe_depression=df[mask]
# print(europe_depression[["country", "depression_pct"]])

# new_dataframe=df["suicide_rate_per100k"] * df["population_millions"]
# print(new_dataframe)



