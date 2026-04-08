import kagglehub
import pandas as pd
from matplotlib import pyplot as plt

# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# depression=df[['depression_pct', "country"]]
# europe_depression=df[df["region"]=="Europe"]
# print(europe_depression[["country", "suicide_rate_per100k"]])

# mask = (df["region"]=="Europe") & (df["depression_pct"]>5)
# europe_depression=df[mask]
# print(europe_depression[["country", "depression_pct"]])

# new_dataframe=df["suicide_rate_per100k"] * df["population_millions"]
# print(new_dataframe)

# df["millions_mult_rate"]= df["suicide_rate_per100k"] * df["population_millions"] * 10
# print(df[["country", "millions_mult_rate"]])

#guided_practise1
# mask= (df["gdp_per_capita_usd"]<=10000) & (df["mh_system_score"]<5)
# rich_contry=df[mask]
#
# rich_contry["lack_of_care_mln"]=(rich_contry["population_millions"] *rich_contry["treatment_gap_pct"])/100
# print(rich_contry[["country", "mh_system_score", "lack_of_care_mln"]])

# top_5 = df.nlargest(5, "depression_pct")
# plt.figure(figsize = (8,4))
# plt.plot(top_5["country"], top_5["depression_pct"], marker = "o", label = "depression")
# plt.plot(top_5["country"], top_5["anxiety_pct"], marker = "s", label = "anxiety")
# plt.title("Anxiety vs Depression (%)")
# plt.xlabel("Countries")
# plt.ylabel("Percent")
# plt.legend()
# plt.show()

#guided practise2
# plt.figure(figsize=(8, 4))
# plt.scatter(df["social_media_hours_daily"] ,df["youth_mh_crisis_score"],color='red', s=50, alpha=0.4) #
# plt.xlabel("social_media_hours_daily")
# plt.ylabel("youth_mh_crisis_score")
# plt.grid(True)
# plt.show()
