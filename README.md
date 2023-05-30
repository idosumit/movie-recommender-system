# Content-Based Recommender App for Movies: An End-To-End Project

> Objective: To build a recommender app that can recommend 5 similar movies when a user selects a movie from the library.

## Table of Contents
(Details in the [notebook](https://github.com/psumitcode/movie-recommender-system/blob/main/recommender-system_notebook.ipynb))

1. Preprocessing
        
2. Text Vectorization

3. Creating the Main Function

4. Streamlit and Deployment

#

Dataset used: [**`tmdb-movie-dataset`**](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), taken from Kaggle.

I deployed the cloud-based application via Git. I had originally used the [`Heroku`](https://heroku.com) platform for hosting; however, since it doesn't have free services anymore, I migrated the app to [`Render`](https://render.com/).

The link to the recommender app developed with these codes can be accessed [**`HERE`**](https://cine-recs.com/). It's a custom domain that I've made use of via `Route 53`, the DNS provider by AWS (`A` and `CNAME` records in use).
