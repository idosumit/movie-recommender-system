import streamlit as st
import pickle
import pandas as pd
import requests

def get_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=849f1680a50ddf85941e336db926b570".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x : x[1])[1:6]

    recommended_movies = []
    recommended_mov_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id;
        #we'll get posters here via API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_mov_posters.append(get_poster(movie_id))
    return recommended_movies, recommended_mov_posters;

movie_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

movie_picked = st.selectbox(
'Pick a movie. We will recommend 5 movies from our library that are the most similar to it.', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(movie_picked)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
