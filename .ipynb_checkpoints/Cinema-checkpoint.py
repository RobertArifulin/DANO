import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

from visualize_coefficients import visualize_coefficients

df = pd.read_csv(r'data/cinema_csv.csv', on_bad_lines="skip", encoding="utf_8", sep=";", index_col="order_id", parse_dates=["creation_date", "session_date"], dayfirst=True)


ages = ["0+", "12+", "16+", "18+", "6+"]
for i in ages:
  df["movie_age_restriction"] = df["movie_age_restriction"].replace(i, i[:-1])
df['movie_duration'] = df['movie_duration'].str.replace(' мин.','')
df['movie_duration'] = df['movie_duration'].str.replace('т','')
df['movie_duration'] = df['movie_duration'].str.replace('-','1')
df['ticket_price_in_cu'] = df['ticket_price_in_cu'].str.replace(',','.')
df['movie_age_restriction'] = df['movie_age_restriction'].str.replace(',','.')
df['sales_in_cu'] = df['sales_in_cu'].str.replace(',','.')
df['movie_rating'] = df['movie_rating'].str.replace(',','.')
except_1 = ['creation_date', 'session_date', 'movie_name', "movie_id", "cinema_name", "cinema_address", "client_id", "places"]
except_2 = ["number_of_tickets"]
for i in except_1:
   df = df.drop(i, axis=1)
for i in except_2:
  df = df.drop(i, axis=1)
df = df.astype({"movie_duration": np.float64, "movie_age_restriction": np.float64, "movie_rating" : np.float64, "sales_in_cu": np.float64, "ticket_price_in_cu": np.float64})

# dum = pd.get_dummies(df["cinema_city"])
# dum.head()
# df = df.merge(dum, left_index=True, right_index=True)
df = df.drop("cinema_city", axis=1)
df = df.dropna()

print(df.head())
