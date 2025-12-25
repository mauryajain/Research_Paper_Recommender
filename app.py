import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Research Paper Recommender",
    layout="centered"
)

st.title("📄 Research Paper Recommender")
st.write("Find research papers similar to a selected paper")

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
def recommend(paper,year_range, top_k,sort_desc):
    # index of selected paper
    paper_idx = final.index[final['title'] == paper][0]

    # filter dataframe by year
    filtered_final = final[
        (final["published_date"].dt.year >= year_range[0]) &
        (final["published_date"].dt.year <= year_range[1])
        ].copy()

    if len(filtered_final) <= 1:
        return [], []

    # cap top_k safely
    top_k = min(top_k, len(filtered_final) - 1)

    # get filtered vectors
    filtered_indices = filtered_final.index
    filtered_vectors = vectors[filtered_indices]

    # compute similarity ONLY on filtered vectors
    scores = cosine_similarity(
        vectors[paper_idx],
        filtered_vectors
    )[0]

    # rank results
    top = sorted(
        list(enumerate(scores)),
        reverse=True,
        key=lambda x: x[1]
    )[1:top_k + 1]

    results = []

    for i in top:
        idx = filtered_indices[i[0]]
        results.append({
            "title": final.loc[idx, "title"],
            "date": final.loc[idx, "published_date"]
        })

    # sort by date
    results = sorted(
        results,
        key=lambda x: x["date"],
        reverse=sort_desc
    )

    titles_clean = [re.sub(r'\s+', ' ', r["title"]) for r in results]
    titles_raw = [r["title"] for r in results]
    return titles_clean, titles_raw


# -------------------- UI --------------------
paper = st.selectbox(
    "Select a research paper",
    final["title"].values
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

if st.button("Recommend"):
    results,results2 = recommend(paper, year_range, top_k,sort_desc)
    st.subheader("Recommended Papers")

    # Scrollable container
    html = "<div style='max-height: 450px; overflow-y: auto;'>"
    for i in range(0,len(results)):
        st.markdown(f"**{results[i]}**")
        published_date = final.loc[final['title'] == results2[i], 'published_date'].iloc[0]
        date_only = published_date.strftime('%Y-%m-%d')
        print(date_only)
        st.write("📅 Published:", date_only)
        st.markdown("---")

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
