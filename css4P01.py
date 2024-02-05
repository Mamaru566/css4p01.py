#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:16:40 2024

@author: mamaru
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df.info())

df.columns = df.columns.str.replace(' ', '_')
df['Revenue_(Millions)'].fillna(df['Revenue_(Millions)'].mean(), inplace=True)
df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)


df_sorted = df.sort_values('Rating', ascending=False)
print(df_sorted.iloc[0]['Title'])

# Calculate the average revenue
average_revenue = df['Revenue_(Millions)'].mean()
print(average_revenue)

# Filter the data for the specified years (2015 to 2017) and calculate the average revenue
average_revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue_(Millions)'].mean()
print(average_revenue_2015_2017)

# Count the number of movies released in 2016
num_movies_2016 = df[df['Year'] == 2016].shape[0]
print(num_movies_2016)

#Count the number of movies directed by Christopher Nolan
num_movies_nolan = df[df['Director'] == 'Christopher Nolan'].shape[0]
print(num_movies_nolan)

# Count the number of movies with a rating of at least 8.0
num_movies_rating_8 = df[df['Rating'] >= 8.0].shape[0]
print(num_movies_rating_8)


#Filter the data for movies directed by Christopher Nolan and calculate the median rating
nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan = nolan_movies['Rating'].median()
print(median_rating_nolan)

# Calculate the average rating for each year and find the year with the highest average rating
yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highest_rating = yearly_average_rating.idxmax()
print(year_with_highest_rating)

#Filter the data for the years 2006 and 2016 and count the number of movies
num_movies_2006 = df[df['Year'] == 2006].shape[0]
num_movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase in the number of movies made between 2006 and 2016
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print(percentage_increase)

# Create a list of all actors in the dataset
all_actors = []
for actors in df['Actors']:
    all_actors.extend(actors.split(', '))
    
# Count the number of occurrences of each actor
actor_counts = pd.Series(all_actors).value_counts()

#Create a list of all actors in the dataset
all_actors = df['Actors'].str.split(', ').explode()

# Count the number of occurrences of each actor
actor_counts = all_actors.value_counts()

# Find the most common actor
most_common_actor = actor_counts.index[0]
print(most_common_actor)

# Find the most common actor
most_common_actor = actor_counts.index[0]
print(most_common_actor)

# Split the genres and create a list of all unique genres
unique_genres = set(df['Genre'].str.split(', ').explode())

# Count the number of unique genres
num_unique_genres = len(unique_genres)
print(num_unique_genres)

# Convert the "Revenue (Millions)" column to numeric, replacing non-numeric values with NaN
correlation = df.drop(columns=["Title", "Genre", "Description", "Director", "Actors" ]).corr()
print(correlation)