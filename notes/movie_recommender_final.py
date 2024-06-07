import pickle
import pandas as pd
import numpy as np
import re
from chatbot_stella import mood
import random
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

def clean_genres(genres):
    return re.sub("[^a-zA-Z ]", " ", genres)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ngram_range=(1,5))
tfidf = vectorizer.fit_transform(movies["clean_genres"])
from sklearn.metrics.pairwise import cosine_similarity

if mood == "happy":
    genres = ["comedy", "children", "animation","fantasy"]
    genre = random.choice(genres)
elif mood == "sad":
    genres = ["mystry","musical","war"]
    genre = random.choice(genres)
elif mood == "party":
    genres = ["adventure", "drama", "action", "sci fi"]
    genre = random.choice(genres)


# if user_input == "recommend":
#     print("STELLA: " + "so what would you like to do? -- listen to a song or a movie")

# elif user_input == "songs":
#     print("STELLA: " + "Song it is then!")
#     print("STELLA: umm..any specific genre?")

# elif user_input == "yes":
#     print("STELLA: and what will that be?")
#     mood = user_input

# elif user_input == "no":
#     print("STELLA: then you are at my mercy *evil laugh*")
#     mood = mood

# elif user_input == "movie":
#     print("STELLA: " + " your wish is my command so moives it is then")
#     print("STELLA: umm..any specific genre?")

# elif user_input == "yes":
#     print("STELLA: and what will that be?")
#     mood = user_input
#     #search(genre)
# elif user_input == "no":
#     print("STELLA: then you are at my mercy *evil laugh*")
#     mood = mood

# elif user_input == "you decide":
#     print("STELLA: " + "well if it's upto me then i'll recommned a movie")
#     print("STELLA: umm..any specific genre?")

# elif user_input == "yes":
#     print("STELLA: and what will that be?")
#     mood = user_input

# elif user_input == "no":
#     print("STELLA: then you are at my mercy *evil laugh*")
#     mood = mood

def search(genre):
    genre = clean_genres(genre)         
    query_vec = vectorizer.transform([genre])           
    similarity = cosine_similarity(query_vec,tfidf).flatten()           
    indices = np.argpartition(similarity, -10)[-10:]   
    results = movies.iloc[indices][::-1]          
    return results
    print("The recommended movies: \n", results)
# print(search(genre))