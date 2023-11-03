import pandas as pd

films = pd.read_csv("imdb-1000.csv")
print(films.columns)

films = films.drop("content_rating", axis = 1)
films = films.drop("actors_list", axis = 1)

films = films.drop(2, axis = 0)
rowsToDrop = [0,1,2,4,6,8,9,10]
films = films.drop(rowsToDrop, axis = 0)
print(films.mean())