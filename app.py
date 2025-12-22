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

# -------------------- Recommendation Function --------------------
def recommend(paper):
    paper_idx = final.index[final['title'] == paper][0]
    scores = cosine_similarity(vectors[paper_idx], vectors)[0]
    #scores is a 1d array with cosine values between entered paper and rest others
    top=sorted(list(enumerate(scores)),reverse=True, key=lambda x:x[1])[1:9]
    #enumerate creates tuples with (index,cosine values)
    #top_dates=sorted(top,reverse=True, key=lambda x:final['published_date'].iloc[x[0]])
    stack=[]
    stack2=[]
    for i in top:
        stack2.append(final['title'].iloc[i[0]])
    for i in top:
        stack.append(re.sub(r'\s+', ' ',final['title'].iloc[i[0]]))
    return stack,stack2


# -------------------- UI --------------------
paper = st.selectbox(
    "Select a research paper",
    final["title"].values
)

if st.button("Recommend"):
    results,results2 = recommend(paper)

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
