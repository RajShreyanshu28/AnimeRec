
import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.stem.porter import PorterStemmer


movies = pd.read_csv('Anime_dataset.csv')
movies = movies[['title','genre','type', 'episodes', 'rating']]

def operate(text):
  L = []
  for i in ast.literal_eval(text):
    L.append()
  return L

movies['genre'].fillna('', inplace=True)                 #problem
movies['genre'] = movies['genre'].apply(lambda x:x.split())

movies.dropna(inplace=True)

def convert_genre(text):
    L = []
    for i in ast.literal_eval(text):
            L.append(i)
    return L

movies['genre'] = movies['genre'].apply(lambda x: ' '.join(x) if isinstance(x, list) else '')

# Concatenate 'title', 'genre', and 'type' columns
movies['tags'] = movies['title'] + ', ' + movies['genre'] + ', ' + movies['type']

new_df = movies[['title', 'genre', 'type', 'tags']]
# new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))



cv = CountVectorizer(max_features = 5000)

v = cv.fit_transform(new_df['tags']).toarray()


ps = PorterStemmer()                            #Converting loving loved love to love love love

def stem(text):
  y = []
  #same
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(v)

sorted(list(enumerate(similarity[0])), reverse = True, key = lambda x : x[1])[1:10]

def recommend(movie):
  if movie not in new_df['title'].values:
        print(f"Movie '{movie}' not found in the dataset.")
        return []
  movie_index = new_df[new_df['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1:11]

  # for i in movies_list:
  #   print(new_df.iloc[i[0]].title)
  recommended_movies = []

  for i in movies_list:
        movie_name = new_df.iloc[i[0]]['title']
        recommended_movies.append(movie_name)

  return recommended_movies


