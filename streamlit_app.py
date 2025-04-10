import streamlit as st
from PIL import Image
import pandas as pd

# Sidebar with current page indicator
st.sidebar.markdown(f"📍 Current page: ⁠ {st.session_state.page if 'page' in st.session_state else 'welcome'} ⁠")

# CSV uploader - always available
st.sidebar.write("### Upload a CSV file")
uploaded_file = st.sidebar.file_uploader("Upload your data", type="csv")
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')  # o encoding='ISO-8859-1'
    st.sidebar.success("CSV uploaded successfully!")


# Load images (replace with actual image URLs or local file paths)
player_img = "https://via.placeholder.com/150?text=Player+Profiling"
history_img = "https://via.placeholder.com/150?text=History+%26+Trend"
research_img = "https://via.placeholder.com/150?text=Research"
career_img = "https://via.placeholder.com/150?text=Player+Career"

# Welcome Page
def welcome_page():
    st.title("🏀 NBA Combine Draft")
    st.image("https://cdn.nba.com/logos/nba.png", width=100)  # Optional logo
    st.write("Welcome to the official NBA Combine Draft site!")
    if st.button("🚀 Start"):
        st.session_state.page = "menu"

# Main Menu with clickable image cards
def main_menu():
    st.title("📋 Main Menu")
    st.write("Choose one of the sections:")

    col1, col2 = st.columns(2)
    with col1:
        if st.image(player_img, caption="🧑‍💼 Player Profiling", use_column_width=True):
            if st.button("Select Player Profiling"):
                st.session_state.page = "section1"
        if st.image(history_img, caption="📚 History & Trend", use_column_width=True):
            if st.button("Select History & Trend"):
                st.session_state.page = "section2"

    with col2:
        if st.image(research_img, caption="🔬 Research", use_column_width=True):
            if st.button("Select Research"):
                st.session_state.page = "section3"
        if st.image(career_img, caption="🏆 Player Career", use_column_width=True):
            if st.button("Select Player Career"):
                st.session_state.page = "section4"

    if st.button("🔙 Back to Home"):
        st.session_state.page = "welcome"

# Section placeholders
def section1():
    st.title("🧑‍💼 Player Profiling")
    st.write("Content for Player Profiling goes here.")
    if st.button("⬅ Back to Menu"):
        st.session_state.page = "menu"

def section2():
    st.title("📚 History & Trend")
    st.write("Content for History & Trend goes here.")
    if st.button("⬅ Back to Menu"):
        st.session_state.page = "menu"

def section3():
    st.title("🔬 Research")
    st.write("Content for Research goes here.")
    if st.button("⬅ Back to Menu"):
        st.session_state.page = "menu"

def section4():
    st.title("🏆 Player Career")
    st.write("Content for Player Career goes here.")
    if st.button("⬅ Back to Menu"):
        st.session_state.page = "menu"

# Initialize current page
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Page routing
if st.session_state.page == "welcome":
    welcome_page()
elif st.session_state.page == "menu":
    main_menu()
elif st.session_state.page == "section1":
    section1()
elif st.session_state.page == "section2":
    section2()
elif st.session_state.page == "section3":
    section3()
elif st.session_state.page == "section4":
    section4()