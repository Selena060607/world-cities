import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="Home - World Cities",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and welcome section
st.title("🌍 World Cities")

st.markdown("""
    ## Welcome to the World Cities App!
    
    This application helps you explore and discover information about cities around the world.
    Whether you're looking for travel inspiration, city statistics, or geographic insights,
    you've come to the right place.
    
    ### Features:
    - 🗺️ Explore cities by region
    - 📊 View city statistics and demographics
    - 🌐 Discover interesting facts about world cities
    - 🔍 Search and filter by your interests
""")

# Navigation button to app.py
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Go to App", use_container_width=True, key="nav_to_app"):
        st.switch_page("pages/app.py")

st.markdown("---")

# Footer section
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px; margin-top: 50px;'>
        <p>Explore the world, one city at a time 🌟</p>
    </div>
""", unsafe_allow_html=True)
