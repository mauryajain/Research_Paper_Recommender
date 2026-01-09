import streamlit as st
st.markdown("""
<style>
div[data-testid="column"] {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="ScholarSphere", layout="wide")

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- HOME PAGE ----------
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center;'>ScholarSphere</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size:18px;'>"
        "Explore papers with recommendations and trend insights"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Paper Recommender")
        st.write("Get research paper recommendations based on similarity.")
        if st.button("Go →", key="rec"):
            st.switch_page("pages/recommender.py")

    with col2:
        st.markdown("### Publication Timeline & Trend Analyzer")
        st.write("Analyze research trends by genre and year.")
        if st.button("Go →", key="trend"):
            st.switch_page("pages/Trend_Analyser.py")

    with col3:
        st.markdown("### Paper Search")
        st.write("Find papers using a short description or keywords.")
        if st.button("Go →", key="search"):
            st.switch_page("pages/Searcher.py")
