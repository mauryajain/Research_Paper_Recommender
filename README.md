# Research Paper Exploration Dashboard

An interactive web-based application built using Streamlit for discovering, analyzing, and exploring research papers through recommendations, publication trend analysis, and description-based search.

---

## 1. Overview

This project is designed to help users explore academic research papers more effectively. Instead of functioning only as a research paper recommender, the application provides a unified dashboard with multiple features that support discovery, analysis, and trend understanding.

Users can:
- Get recommendations for research papers similar to a selected paper
- Analyze year-wise publication trends across different research categories
- Search for relevant research papers using a short textual description

The application is lightweight, interactive, and suitable for academic exploration.

---

## 2. Methodology

The system follows a content-based approach using textual information from research papers such as titles and summaries.

### Common Preprocessing Steps
- Text cleaning using regular expression-based preprocessing
- Removal of noise and irrelevant characters
- Combining paper titles and summaries for better semantic representation

The processed data is then utilized differently across the three main features described below.

---

## 3. Features and Implementation

### 3.1 Research Paper Recommender

This feature suggests research papers that are semantically similar to a selected paper.

**Techniques Used:**
- TF-IDF (Term Frequency–Inverse Document Frequency) vectorization
- Cosine similarity for measuring similarity

The title and summary of each research paper are combined and transformed into TF-IDF vectors. Around 15,000 unique terms are used to represent the corpus. Cosine similarity is then computed between papers to identify the most relevant recommendations.

For efficient performance:
- `vectors.pkl` stores the precomputed TF-IDF vectors
- `final.pkl` stores metadata such as paper titles, categories, and publication dates

The system displays the top most similar research papers for a selected input paper.

---

### 3.2 Publication Trend Analysis

This feature analyzes how research output changes over time across different categories.

**Techniques Used:**
- Temporal analysis of publication dates
- Year-wise aggregation of research papers
- Bar chart visualization using Altair

For a selected research category, the system:
- Displays a bar graph showing the number of papers published each year
- Identifies trends such as growth, stability, or decline in research activity
- Provides qualitative insights to help understand field maturity and momentum

This feature helps users understand long-term research trends and emerging or declining areas.

---

### 3.3 Description-Based Paper Search

This feature allows users to search for research papers using a short textual description instead of selecting an existing paper.

**Techniques Used:**
- TF-IDF vectorization of the user’s input description
- Cosine similarity with existing paper vectors

The input description is converted into a TF-IDF vector using the same vocabulary as the dataset. Similarity scores are computed between the input vector and all stored research paper vectors, and the most relevant papers are returned.

This feature is particularly useful when users do not know exact paper titles or are exploring a new topic.

---

## 4. Dataset

The dataset used in this project was obtained from Kaggle:

**Dataset:** ArXiv Scientific Research Papers  
**Link:** https://www.kaggle.com/datasets/sumitm004/arxiv-scientific-research-papers-dataset

The dataset contains paper titles, summaries, categories, and publication dates, which are essential for recommendation and trend analysis.

---

## 5. Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Altair  

---

## 6. Key Highlights

- Content-based research paper recommendation system
- Publication trend analysis with visual insights
- Description-based semantic search
- Cached data loading for improved performance
- Modular multipage Streamlit architecture
- Clear separation between preprocessing and inference

---

