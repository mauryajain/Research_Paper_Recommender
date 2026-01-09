import streamlit as st
import pandas as pd
import numpy as np
import pickle
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Contextual Research Paper Discovery",
    layout="centered"
)

st.title("Contextual Discovery of Research Papers")
st.write("Enter research keywords or a short description to find relevant papers")

# -------------------- Load Data --------------------
@st.cache_data
def load_data():
    final = pd.read_pickle("final.pkl")
    vectors = pickle.load(open("vectors.pkl", "rb"))
    final["published_date"] = pd.to_datetime(
        final["published_date"], errors="coerce"
    )
    return final, vectors

final, vectors = load_data()

# Compute year range once
min_year = final["published_date"].dt.year.min()
max_year = final["published_date"].dt.year.max()

# -------------------- Recommendation Function --------------------
def recommend_from_text(query_text, year_range, top_k, sort_desc):
    # Filter dataframe by year
    filtered_final = final[
        (final["published_date"].dt.year >= year_range[0]) &
        (final["published_date"].dt.year <= year_range[1])
    ].copy()

    if filtered_final.empty:
        return [], [], []

    # Fit TF-IDF on corpus + query
    tfidf = TfidfVectorizer(
        stop_words="english",
        max_features=15000,
        min_df=3,
        max_df=0.85,
        ngram_range=(1, 2),
        sublinear_tf=True
    )

    tfidf_matrix = tfidf.fit_transform(filtered_final["summary"].fillna(""))
    query_vec = tfidf.transform([query_text])

    scores = cosine_similarity(query_vec, tfidf_matrix)[0]

    # Cap top_k safely
    top_k = min(top_k, len(scores))

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for idx in top_indices:
        results.append({
            "title": filtered_final.iloc[idx]["title"],
            "date": filtered_final.iloc[idx]["published_date"],
            "summary": filtered_final.iloc[idx]["summary"],
            "similarity_score": scores[idx]
        })

    # Sort by date
    results = sorted(
        results,
        key=lambda x: x["date"],
        reverse=sort_desc
    )

    titles = [re.sub(r'\s+', ' ', r["title"]) for r in results]
    raw_titles = [r["title"] for r in results]
    sim_scores = [r["similarity_score"] for r in results]

    return titles, raw_titles, sim_scores, results

# -------------------- UI --------------------
user_text = st.text_input(
    "Describe the paper you want",
    placeholder="e.g. Machine Learning, Dark Matter, Quantum Computing"
)

with st.expander("Filters"):
    year_range = st.slider(
        "Publication Year",
        int(min_year),
        int(max_year),
        (int(min_year), int(max_year))
    )

    top_k = st.slider(
        "Number of recommendations",
        min_value=2,
        max_value=10,
        value=8
    )

    sort_desc = st.toggle(
        "Sort by Date (Newest first)",
        value=True
    )

# -------------------- Results --------------------
if st.button("Search") and user_text.strip():
    with st.spinner("Finding relevant papers..."):
        titles, raw_titles, sim_scores, results = recommend_from_text(
            user_text, year_range, top_k, sort_desc
        )

    st.subheader("Recommended Papers")

    if not results or max(sim_scores) == 0:
        st.info(
            "Sorry! We couldn’t find closely related papers in our dataset.\n\n"
            "Try:\n"
            "- using broader keywords\n"
            "- removing very specific terms\n"
            "- expanding the year range"
        )
    else:
        for i in range(len(results)):
            st.markdown(f"**{results[i]['title']}**")
            st.caption(f"Similarity score: {sim_scores[i]:.2f}")

            date_only = results[i]["date"].strftime("%Y-%m-%d")
            st.write("📅 Published:", date_only)

            st.markdown("**Summary:**")
            st.markdown(results[i]["summary"])

            st.markdown("---")




