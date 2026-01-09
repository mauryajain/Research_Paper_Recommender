import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import pickle
import os
st.title("""Temporal Distribution of Research Papers
Analyzing year-over-year volume to determine field maturity and momentum.""")
# -------------------- Load Data --------------------
@st.cache_data
def load_data():
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    final = pd.read_pickle(os.path.join(ROOT_DIR, "final.pkl"))
    vectors = pickle.load(open(os.path.join(ROOT_DIR, "vectors.pkl"), "rb"))
    final["published_date"] = pd.to_datetime(
        final["published_date"], errors="coerce"
    )
    return final, vectors


final, vectors = load_data()
category = st.selectbox(
    "Select the research category",
    np.unique(final["category"].values)
)
submit = st.button("Submit")

if submit:
    final['published_date'] = pd.to_datetime(final['published_date'], errors='coerce')
    final['year']=final['published_date'].dt.year
    filtered = final[final['category'] == category]
    year_counts = (filtered.groupby('year')
                   .size()
                   .reset_index(name='papers')
                   .sort_values('year'))
    year_counts1= (filtered.groupby('year')
                   .size()
                   .reset_index(name='papers')
                   .sort_values('year',ascending=False))
    chart = alt.Chart(year_counts1).mark_bar().encode(
        x=alt.X('papers:Q', title='Number of Papers'),
        y=alt.Y('year:O',sort=alt.SortField(field='year', order='descending'),title='Year'),
        tooltip=['year', 'papers'],color = alt.Color('papers:Q', scale=alt.Scale(scheme='blues')))
    st.altair_chart(chart, use_container_width=True)
    row_count=len(year_counts)
    if row_count==1:
        with st.container(border=True):
            st.markdown("###   Quick Insight")
            st.markdown("""
            * **Data Insight:** This search returned a singular, specific match within the current dataset.
            * **Trend:** Insufficient data points to establish a chronological trend or growth pattern.
            * **User Advice:** Review this paper for unique relevance, or try broader categories for more context.
            """)
    elif row_count>1 and row_count<4:
        with st.container(border=True):
            if int(year_counts['papers'][row_count-1])==int(year_counts['papers'][0]):
                st.markdown("###   Consistent Pulse (Steady in 2-3 years)")
                st.markdown("""
                            * **Data Insight:** The number of publications has remained almost identical year-over-year.
                            * **Activity:** This represents a "Niche Stability," where a specific community provides a steady, reliable output.
                            * **User Advice:** Both the older and newer papers in this set likely carry equal weight and relevance to your query.
                            """)
            elif int(year_counts['papers'][row_count-1])>int(year_counts['papers'][0]):
                st.markdown("###   Rising Momentum (Growth in 2-3 years)")
                st.markdown("""
                                            * **Data Insight:** Research volume has shown a sharp increase within the available short-term window.
                                            * **Activity:** This indicates a "Hot Topic" where new papers are being added to the database at an accelerating rate.
                                            * **User Advice:** Prioritize the most recent entries, as the increase suggests rapidly evolving techniques or new discoveries.
                                            """)
            else:
                st.markdown("###   Cooling Activity (Decline in 2-3 years)")
                st.markdown("""
                            * **Data Insight:** Publication density was higher at the start of the timeframe than in the most recent entries.
                            * **Activity:** This suggests the specific sub-topic might be maturing or the research focus is shifting elsewhere.
                            * **User Advice:** Look toward the earlier papers in this set for the most comprehensive data and foundational methodologies.
                            """)
    else:
        with st.container(border=True):
            power=1/row_count
            cagr=((year_counts['papers'][row_count-1]//year_counts['papers'][0])**power)-1
            if cagr>5:
                st.markdown("###   Consistent Growth (Strong Uptrend)")
                st.markdown(f"""
                            * **Data Insight:** This field shows a steady Compound Annual Growth Rate (CAGR) of {cagr:.1f}% across the last {row_count} years.
                            * **Trend:** The data confirms a long-term 'Expansion Phase,' indicating that {category} is becoming a permanent fixture in the landscape.
                            * **User Advice:** This is a high-impact area; look for 'Survey' papers from {int(year_counts['year'][row_count-1])} to understand the latest developments.
                            """)
            elif cagr<=5 and cagr>=-5:
                st.markdown("###   Mature/Foundational (Stable over 4+ years)")
                st.markdown(f"""
                            * **Data Insight:** Publication volume has remained stable with a marginal Compound Annual Growth Rate (CAGR) of {cagr:.1f}% since {int(year_counts['year'][0])}.
                            * **Trend:** This signifies a 'Foundational' field with established core principles and periodic bursts of high-volume research activity.
                            * **User Advice:** These results are highly reliable; focus on 'Gap Analysis' papers to find unsolved niches in this established area.
                            """)
            else:
                st.markdown("###   Paradigm Shift (Long-term Decline)")
                st.markdown(f"""
                            * **Data Insight:** There has been a gradual multi-year decrease in publications, showing a negative CAGR of {cagr:.1f}%.
                            * **Trend:** This often indicates a 'Paradigm Shift,' where research focus has moved from {category} toward newer successor technologies.
                            * **User Advice:** Treat these as 'Classic Works' that provide necessary context, but search for newer terminology for current debates.
                            """)

