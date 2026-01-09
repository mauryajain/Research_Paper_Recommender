                                                Research Paper Recommender System
Live Demo Link: https://researchpaperrecommender.streamlit.app/

Research Paper Exploration Dashboard

A multi-feature, content-based research paper exploration system that enables recommendation, publication trend analysis, and description-based paper search using natural language processing and data visualization techniques.

1. Overview

This project is an interactive web-based application designed to assist users in exploring academic research papers more effectively. Instead of functioning solely as a recommender system, the application provides a unified dashboard with multiple analytical and discovery-oriented features.

Users can:
Discover research papers similar to a selected paper
Analyze publication trends across years and research categories
Search for relevant papers using a short textual description
The application is implemented using Streamlit, making it lightweight, interactive, and easy to use.

2. Methodology

The project follows a content-based approach using textual information from research papers such as titles and summaries.

Common Preprocessing Steps
Text cleaning using regular expressions
Removal of noise and irrelevant characters
Combination of paper titles and summaries for richer context

The processed data is then used differently across the three features described below.

3. Features and Implementation
3.1 Research Paper Recommender

This feature recommends research papers that are semantically similar to a selected paper.

Approach Used:

TF-IDF (Term Frequency–Inverse Document Frequency) vectorization
Cosine similarity for similarity measurement

The combined text (title + summary) of each paper is converted into a TF-IDF vector representation, capturing the importance of words relative to the entire dataset. Approximately 15,000 unique terms are used to represent the corpus.

Cosine similarity is then applied to measure the closeness between papers in vector space. Papers with higher similarity scores are considered more relevant.

For performance optimization:

vectors.pkl stores the precomputed TF-IDF vectors
final.pkl stores metadata such as paper titles and publication dates

The system retrieves and displays the top 15 most similar papers for a selected input paper.

3.2 Publication Trend Analysis

This feature analyzes how research activity evolves over time for different research categories.

Approach Used:
Temporal analysis of publication dates
Year-wise aggregation of papers
Interactive bar chart visualization using Altair

The publication date of each paper is extracted and grouped by year. For a selected research category, the system:
Displays a bar graph showing the number of papers published each year
Analyzes growth, stability, or decline in publication volume
Provides qualitative insights such as emerging trends, mature fields, or declining research interest

This helps users understand the maturity and momentum of a research field over time.

3.3 Description-Based Paper Search

This feature allows users to find relevant research papers using a short textual description instead of selecting an existing paper.

Approach Used:
TF-IDF vectorization of the input description
Cosine similarity with existing paper vectors

The user’s input text is transformed into a TF-IDF vector using the same vocabulary as the dataset. Cosine similarity is then computed between the input vector and all stored paper vectors.

Papers with the highest similarity scores are returned as recommendations, making this feature useful when users:
Do not know exact paper titles
Are exploring a new topic
Want suggestions based on an abstract idea

4. Dataset

The dataset used in this project was sourced from Kaggle:
Dataset: ArXiv Scientific Research Papers
Link: https://www.kaggle.com/datasets/sumitm004/arxiv-scientific-research-papers-dataset

It contains metadata including paper titles, summaries, categories, and publication dates, which are essential for both recommendation and trend analysis.

5. Tech Stack

Python
Pandas – Data manipulation and preprocessing
NumPy – Numerical operations
Scikit-learn – TF-IDF vectorization and cosine similarity
Streamlit – Interactive web interface
Altair – Data visualization

6. Key Highlights

Content-based recommendation system
Publication trend analysis with visual insights
Description-based semantic search
Cached data loading for faster performance
Modular Streamlit multipage architecture
Clear separation between preprocessing and inference

