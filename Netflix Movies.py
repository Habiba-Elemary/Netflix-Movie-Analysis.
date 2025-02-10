import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#getting basic info about the data
df= pd.read_csv("netflix_data.csv")
print(df)
df.info()

# Filter movies released in the 1990s
movies_1990s = df[(df['type'] == 'Movie') & (df['release_year'] >= 1990) & (df['release_year'] <= 1999)]

# Find the most frequent movie duration in the 1990s
most_frequent_duration = movies_1990s['duration'].mode().iloc[0]

# Save the approximate answer as an integer
duration = int(most_frequent_duration)

# Print the result
print(f"The most frequent movie duration in the 1990s was approximately {duration} minutes.")

#dissecting movies
movies= df[df['type']=='Movie']
print(movies)

#finding short movies (in this case less than 90 minutes) & finding short action movies
short_movie= df[df['duration']<90]
print(short_movie)
short_movie_count = short_movie[
    (short_movie['genre'] == 'Action') &
    (short_movie['release_year'] >= 1990) &
    (short_movie['release_year'] <= 1999)
].shape[0]
print(short_movie_count)

#Graph1: Distribution of Movie Durations in the 1990s
plt.figure(figsize=(10, 6))
sns.histplot(movies_1990s['duration'], bins=30, kde=True, color='green')
plt.axvline(x=duration, color='red', linestyle='--', label=f'Most Frequent Duration: {duration} minutes')
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.legend()
plt.show()


#Graph2: Count/distribution of short movies
plt.figure(figsize=(12,6))
sns.countplot(data=short_movie, x= 'genre', order=short_movie['genre'].value_counts().index, palette='viridis')
plt.title('Short Movies by Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

#Graph3: Count of short action movies
short_movie_count_df= short_movie[short_movie['genre']== 'Action']
short_movie_count_df['release_year']= pd.to_datetime(short_movie_count_df['release_year'], format='%Y')
short_movie_count_df['year']= short_movie_count_df['release_year'].dt.year
plt.figure(figsize=(10,6))
sns.countplot(data=short_movie_count_df, x='year', palette='magma')
plt.title('Count of Short Action Movies')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

#Graph4: Distribution of movie duration
plt.figure(figsize=(10,6))
sns.histplot(movies['duration'], bins=30, kde=True, color='blue')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration in Minutes')
plt.ylabel('Frequency')
plt.axvline(x=90, color='red', linestyle='--', label='90 Minutes')
plt.legend()
plt.show()

#Graph5: Top 10 directors with the shortest action movies
TopDirectors= short_movie_count_df['director'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=TopDirectors.values, y=TopDirectors.index, palette='rocket')
plt.title('Top 10 Directors with the Shortest Action Movies')
plt.xlabel('Number of Movies')
plt.ylabel('Director')
plt.show()
