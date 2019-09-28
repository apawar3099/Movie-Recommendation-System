from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

texts=["london paris london","paris paris london"]
cv = CountVectorizer()
cv_fit = cv.fit_transform(texts)

print(cv.get_feature_names())
print(cv_fit.toarray())


similarity_scores =cosine_similarity(cv_fit,dense_output="True")
print(similarity_scores)