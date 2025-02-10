# Netflix Movie Data Analysis

## Overview
This Python script analyzes Netflix movie data to extract insights about movies released in the 1990s, short movies, and the most common movie durations. It also visualizes key trends using **matplotlib** and **seaborn**.

## Features
- Loads and explores the dataset.
- Filters movies released in the 1990s.
- Identifies the most frequent movie duration in the 1990s.
- Analyzes short movies (**< 90 minutes**) and short action movies.
- Generates various visualizations:
  1. **Distribution of Movie Durations in the 1990s**
  2. **Genre-wise Distribution of Short Movies**
  3. **Yearly Count of Short Action Movies**
  4. **Overall Movie Duration Distribution**
  5. **Top 10 Directors with the Most Short Action Movies**

## Dataset
The script expects a CSV file named **`netflix_data.csv`** containing at least the following columns:
- `type`: Specifies whether the entry is a "Movie" or a "TV Show".
- `release_year`: The year the movie was released.
- `duration`: Movie duration in minutes.
- `genre`: The movie's genre.
- `director`: The movie's director (if available).

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install pandas matplotlib seaborn
```

## Usage
Run the script using:
```bash
python script.py
```
Make sure the dataset **`netflix_data.csv`** is in the same directory as the script.

## Visualizations
The script generates multiple plots to help understand movie trends. These include histograms, count plots, and bar charts.

## License
This project is for educational purposes only.

