>>> import numpy as np
... import pandas as pd
... import difflib
... from sklearn.feature_extraction.text import TfidfVectorizer
... from sklearn.metrics.pairwise import cosine_similarity
... 
... 
... df= pd.read_csv('movies.csv')
... print(df.head())
... print(df.columns)
... print(df.describe())
... print(df.shape)
... print(df.isnull().sum())
... 
... 
... selected_features=['genres','keywords','tagline','cast','director']
... print(selected_features)
... for feature in selected_features:
...   df[feature] = df[feature].fillna('')
... # combining all the 5 selected features
... 
... combined_features = df['genres']+' '+df['keywords']+' '+df['tagline']+' '+df['cast']+' '+df['director']
... print(combined_features)
... 
... vectorizer = TfidfVectorizer()
... feature_vectors = vectorizer.fit_transform(combined_features)
... print(feature_vectors)
... 
... similarity = cosine_similarity(feature_vectors)
... print(similarity)
... print(similarity.shape)
... movie_name = input('Enter the Movie Name: ')
... list_of_all_title=df['title'].tolist()
... print(list_of_all_title)
... find_close_match = difflib.get_close_matches(movie_name,list_of_all_title)
... print(find_close_match)
close_match = find_close_match[0]
print(close_match)
index= df[df.title == close_match]['index'].values[0]
print(index)

similarity_score = list(enumerate(similarity[index]))
print(similarity_score)
#
#
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)
#
print('Movies suggested for you : \n')
#
i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<31):
    print(i, '.',title_from_index)
    i+=1
