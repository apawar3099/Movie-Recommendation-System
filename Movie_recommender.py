import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
def get_title_from_index(index):

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv("movie_dataset.csv")
print(df.head())

for feature in features:
	df[feature] = df[feature].fillna('')
def combine_features(row):
	return row['keywords'] +" "+ row['cast']+ " "+ row['genres'] + " " + row['director']
	# try:
	# 	return row['keywords'] +" "+ row['cast']+ " "+ row['genres'] + " " + row['director']
	# except:
	# 	print("Error : ",row)

df["combined_features"]=df.apply(combine_features,axis=1)
print(df["combined_features"].head())  	

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
print(count_matrix.toarray())

cosine_sim =cosine_similarity(count_matrix,dense_output="True")

movie_tile_likes = "Insidious"

movie_index = get_index_from_title(movie_tile_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies, key = lambda x: x[1] , reverse = True)

i=0
for m in sorted_similar_movies:
	print(get_title_from_index(m[0]))
	i+=1
	if i>10:
		break
