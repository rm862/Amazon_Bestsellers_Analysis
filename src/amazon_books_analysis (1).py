# -*- coding: utf-8 -*-
"""amazon_books_analysis.ipynb

Amazon Books Data Analysis
Data analysis of Amazon bestsellers dataset

"""

import pandas as pd
import matplotlib.pyplot as plt

#if you save the data to your google drive,use this
#from google.colab import drive
#drive.mount('linktoyourdrive')

#loadspreadsheet
df = pd.read_csv('data/bestsellers with categories.csv')

#dataexploration
display(df.head())

print(df.shape)

print(df.columns)

print(df.describe())

print(df.dtypes)

#datacleaning
df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

df["Price"] = df["Price"].astype(float)

#checking the changes made
print(df.dtypes)

#data analysis
#average rating per genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")

#number of reviews per genre
reviews_per_genre = df.groupby("Genre")["Reviews"].mean()
print(reviews_per_genre)
reviews_per_genre.to_csv("reviews_per_genre.csv")

#number of books per genre
books_per_genre = df['Genre'].value_counts()
print(books_per_genre)
books_per_genre.to_csv("books_per_genre.csv")

#Pie chart showing genre distribution
plt.figure(figsize=(8, 8))
books_per_genre.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Genres', fontsize=14, fontweight='bold')
plt.ylabel('') # Remove default y-label for pie chart
plt.tight_layout()

#Save the plot
plt.savefig("genre_distribution.png", bbox_inches='tight')

plt.show()

#number of books by each author
books_per_author = df['Author'].value_counts()
display(books_per_author)
books_per_author.to_csv("books_per_author.csv")

#list of top 20 authors
top_20_authors = books_per_author.head(20)
display(top_20_authors)
top_20_authors.to_csv("top_20_authors.csv")

# Horizontal bar plot
plt.figure(figsize=(10, 8))
top_20_authors.plot(kind='barh')
plt.title('Top 20 Authors by Number of Publications', fontsize=14, fontweight='bold')
plt.xlabel('Number of Publications', fontsize=12)
plt.ylabel('Author', fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()

# Save the plot
plt.savefig("top_20_authors.png", bbox_inches='tight')

plt.show()