import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")

# Load data
@st.cache_data
def load_data():
    try:
        df_anthro = pd.read_csv("NBA_Combine_Anthro (2000-21).csv", encoding='latin1')
        df_physical = pd.read_csv("NBA_Combine_Physical (2000-21).csv", encoding='latin1')
        df_history = pd.read_csv("NBA_History (1947-2020).csv", encoding='latin1')
        return df_anthro, df_physical, df_history
    except Exception as e:
        st.error(f"Data loading error: {e}")
        return None, None, None

df_anthro, df_physical, df_history = load_data()

# Set initial state
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Page map
page_labels = {
    "welcome": "🏠 Welcome",
    "menu": "📋 Main Menu",
    "section1": "🧑‍💼 Player Profiling",
    "section2": "📚 History & Trend",
    "section3": "🔬 Research",
    "section4": "🏆 Player Career"
}
page_reverse_map = {v: k for k, v in page_labels.items()}

# Sidebar
with st.sidebar:
    st.title("Navigation")
    selected_label = st.selectbox("Go to:", list(page_labels.values()), index=list(page_labels.keys()).index(st.session_state.page))
    selected_page = page_reverse_map[selected_label]
    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.rerun()

# Global style
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #f45208;
            --secondary-color: #2f6974;
            --text-color: white;
        }
        .title-custom {
            font-family: 'Orbitron', sans-serif;
            font-weight: 800;
            font-size: 5rem;
            color: var(--primary-color);
            -webkit-text-stroke: 3px var(--text-color);
            text-shadow: 5px 5px 10px rgba(0,0,0,0.3);
            text-align: center;
            margin-bottom: 2rem;
        }
        .subtitle-effect {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            color: white;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
            transition: transform 0.3s ease;
            margin-bottom: 3rem;
        }
        .subtitle-effect:hover {
            transform: scale(1.08);
            color: #f45208;
            text-shadow: 0 0 10px rgba(244,82,8,0.7);
        }
        .back-arrow {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 18px;
            color: white;
            font-weight: bold;
            text-decoration: none;
            background-color: transparent;
            border: 2px solid white;
            padding: 6px 12px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .back-arrow:hover {
            background-color: white;
            color: #2f6974;
            text-decoration: none;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .stApp {
            background-color: #2f6974;
        }
    </style>
""", unsafe_allow_html=True)

# Show back to menu only in sections
if st.session_state.page.startswith("section"):
    if st.button("⬅️ Back to Menu"):
        st.session_state.page = "menu"
        st.rerun()

# Pages
def welcome_page():
    st.markdown("""
        <div style='display: flex; flex-direction: column; justify-content: center; 
                    align-items: center; height: 80vh; padding: 2rem;'>
            <div class="title-custom">NEXT GEN<br>DRAFT</div>
            <div class="subtitle-effect">
                Where talent meets destiny and every pick could shape the future of the game
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Start"):
        st.session_state.page = "menu"
        st.rerun()

def main_menu():
    st.title("📋 Main Menu")
    st.write("Choose a section below:")
    if st.button("🧑‍💼 Player Profiling"):
        st.session_state.page = "section1"
        st.rerun()
    if st.button("📚 History & Trend"):
        st.session_state.page = "section2"
        st.rerun()
    if st.button("🔬 Research"):
        st.session_state.page = "section3"
        st.rerun()
    if st.button("🏆 Player Career"):
        st.session_state.page = "section4"
        st.rerun()

def section1():
    st.title("🧑‍💼 Player Profiling")
    if df_anthro is not None:
        player = st.selectbox("Select player", df_anthro['Player'].unique())
        st.dataframe(df_anthro[df_anthro['Player'] == player])

def section2():
    st.title("📚 History & Trend")
    st.write("Historical trends and performance across NBA history.")

def section3():
    st.title("🔬 Research")
    st.write("Explore stats, correlations, and predictive insights.")

def section4():
    st.title("🏆 Player Career")
    st.write("Detailed career paths and draft outcomes of players.")

# Router
pages = {
    "welcome": welcome_page,
    "menu": main_menu,
    "section1": section1,
    "section2": section2,
    "section3": section3,
    "section4": section4
}
pages[st.session_state.page]()