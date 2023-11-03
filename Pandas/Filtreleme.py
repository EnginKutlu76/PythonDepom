import pandas as pd
films = pd.read_csv("imdb-1000.csv")

print(films)
print(films.columns)
print(films.head())
print(films.tail())
print(films['title']. head())
print(films[:9][['title', 'star_rating']].head())
print(films[films['star_rating']>=8.5][['title', 'star_rating']])

print(films.query('star_rating>=9.0 & star_rating <= 9.3')
                                  [['title', 'star_rating']])