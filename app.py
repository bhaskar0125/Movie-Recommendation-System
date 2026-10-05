import streamlit as st
import pickle
import joblib
st.write('Movies Recommendation System')

with open('movies.pickle','rb') as file:
       movies = pickle.load(file)
       movies_title= movies['title'].values
similarities = joblib.load('similarities.joblib')
movie = st.selectbox("Enter the movie name:",movies_title)
def recommend(movie):
       movies_list =[]
       movie_index = movies[movies['title']==movie].index[0]
       recomendation = similarities[movie_index]
       sorted_similarities = sorted(enumerate(recomendation),reverse=True, key=lambda x: x[1])[1:6]
       for index, similar in sorted_similarities:
              movies_list.append(movies.iloc[index]['title'])
       return movies_list

if st.button('Recommended'):
       movies_recc = recommend(movie)
       st.write('The recommended movies are: ')
       for movie in movies_recc:
              st.write(movie)


       
       