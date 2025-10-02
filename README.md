# Amazon Bestseller Data Analysis

A comprehensive data analysis project exploring Amazon bestsellers dataset to uncover insights about book ratings, reviews, author productivity, and genre trends.

## Overview

This project analyzes a dataset of 550 Amazon bestselling books, examining patterns in ratings, reviews, pricing, and publication trends across Fiction and Non-Fiction genres.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-pandas%20%7C%20matplotlib%20%7C%20numpy%20%7C%20jupyter-orange)

## Key Findings

- **Fiction books** receive 73% more reviews than Non-Fiction (15,684 vs 9,065 average)
- **Non-Fiction books** dominate the bestseller list (56.4% of titles)
- **Jeff Kinney** leads with 12 bestselling publications
- Average ratings are similar across genres (Fiction: 4.65, Non-Fiction: 4.60)

## Repository Structure

```
├── data/                             # Dataset files
├── notebooks/                        # Jupyter notebook analysis
    └── amazon_books_analysis.ipynb
├── src/                              # Python scripts
    └── amazon_books_analysis.py
├── results/                          # Generated outputs
    ├── *.csv                         # Analysis results
    └── images/                       # Visualizations
          └── *.png                    
├── requirements.txt                  # Dependencies
└── README.md                         # This file
```

## Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Usage Options

**Option 1: Jupyter Notebook (Recommended)**

```bash
jupyter notebook notebooks/amazon_books_analysis.ipynb
```

**Option 2: Python Script**

```bash
python src/amazon_books_analysis.py
```

## Dataset

- **File**: `bestsellers with categories.csv`
- **Records**: 550 books
- **Columns**: Title, Author, Rating, Reviews, Price, Publication Year, Genre

## Outputs

### Analysis Files
- Genre-wise ratings and review statistics
- Author publication counts
- Top 20 most prolific authors

### Visualizations
- Genre distribution pie chart
- Top authors bar chart

## Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Jupyter Notebook** - Interactive analysis environment

## License

This project is licensed under the MIT License - see the LICENSE file for details.
