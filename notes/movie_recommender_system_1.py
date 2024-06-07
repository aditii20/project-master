import streamlit as st
import pickle
import pandas as pd
import requests



movies_dict = pickle.load(open("movie_dict.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[0:20]
    recommended_movies = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
# flask can also be used here

st.title("Movie Recommender system")
selected_movie_name = st.selectbox("Which Movie would you like to watch!?",movies["title"].values) 
if st.button("Recommend"):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
# streamlit run python_file.py
