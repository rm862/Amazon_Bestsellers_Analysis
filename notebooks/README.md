# Notebooks
This folder contains Jupyter notebook for the main data analysis project - Amazon Books Analysis (amazon_books_analysis.ipynb)

### The project contains the following analysis: 
- Book ratings and reviews by genre
- Author publication patterns
- Genre distribution trends
- Top-performing authors

### Data Cleaning Steps

- Removed duplicate entries
- Renamed columns for clarity (Name → Title, Year → Publication Year, User Rating → Rating)
- Converted Price column to float data type

### Key Findings

- Fiction books: Higher ratings (4.65 avg) and more reviews (15,684 avg)
- Non Fiction books: Larger volume (310 vs 240 titles)
- Top author: Jeff Kinney (12 publications)

### Analysis Insights
This analysis reveals that while Fiction books tend to receive higher ratings and significantly more reviews, Non Fiction books dominate the bestseller lists by volume. The data also shows a concentration of bestselling titles among a relatively small group of prolific authors, particularly in children's and young adult fiction genres.

### Outputs:
- Analysis CSVs saved to the the results repository
- Visualizations: genre distribution pie chart, top authors bar chart

### Requirements
```bash
pip install pandas matplotlib
