                                                📄 Research Paper Recommender System
Live Demo Link: https://researchpaperrecommender.streamlit.app/

A content-based recommender system that suggests research papers similar to a selected paper using **TF-IDF vectorization** and **cosine similarity**.

1.Overview

This project helps users discover semantically similar research papers based on textual similarity between paper titles and summary of the respective research papers. It is designed as a lightweight, interactive web application.

2.Methodology
- Text preprocessing using regex-based cleaning
- Feature extraction using **TF-IDF**
- Similarity computation using **cosine similarity**
- Ranking of papers based on semantic relevance
- Interactive UI built with **Streamlit**

The dataset of research papers used in this project was taken from Kaggle and analyzed to build a research paper recommender system. The goal of the system is to recommend papers that are similar based on the titles and summaries of the research papers.

To do this, the TF-IDF (Term Frequency–Inverse Document Frequency) technique was used. The title and summary of each paper were combined and converted into numerical form. Around 15,000 unique words were selected, and each research paper was represented as a vector of numbers. Each number (TF-IDF weight) shows how important a word is in that paper compared to all other papers in the dataset.

These vectors were then compared using cosine similarity, which measures how close two papers are in terms of their content. A higher cosine similarity value means the papers are more similar.

For faster performance, the processed data was saved into pickle files. The vectors.pkl file stores the TF-IDF vectors of all research papers, and the final.pkl file stores the paper details such as titles and publication dates. Using these saved files, the system can quickly find and display the top 15 most similar research papers for a given input paper.

Dataset Link: https://www.kaggle.com/datasets/sumitm004/arxiv-scientific-research-papers-dataset

3.Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

4.Features
- Select a paper and get top similar recommendations
- Displays paper title and publication date
- Scrollable and clean UI
- Cached data loading for faster performance
- Clear separation between preprocessing and inference


5.How to Run Locally
```bash
python -m streamlit run app.py
