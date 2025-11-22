import streamlit as st
from src.data_loader import load_lifetime

st.set_page_config(page_title="IPL Dashboard", layout="wide")

st.sidebar.title("IPL Dashboard Navigation")

st.sidebar.write("Use the sidebar to navigate to pages:")

st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/1_home.py", label="🔥 Home Page")
st.sidebar.page_link("pages/2_player_stats.py", label="👤 Player Stats")
st.sidebar.page_link("pages/3_team_stats.py", label="🏏 Team Stats")
st.sidebar.page_link("pages/4_season_analysis.py", label="📅 Season Analysis")
st.sidebar.page_link("pages/5_player_compare.py", label="⚔ Player Comparison")

lifetime = load_lifetime()
st.sidebar.metric("Players in dataset", lifetime['player'].nunique())

st.title("Welcome to the IPL Analytics Dashboard")
st.write("Select a page from the sidebar to continue.")
