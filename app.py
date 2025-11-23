# app.py
import streamlit as st
from src.data_loader import load_lifetime

st.set_page_config(page_title="IPL Analytics Dashboard", layout="wide")
st.title("🏏 IPL Analytics Dashboard")

st.sidebar.title("Navigation")
st.sidebar.write("Use the pages listed below (Streamlit auto-detects files in /pages):")
st.sidebar.markdown("- Home\n- Player Stats\n- Team Stats\n- Season Analysis\n- Player Compare")

# small metric
try:
    lifetime = load_lifetime()
    st.sidebar.metric("Players in dataset", int(lifetime['player'].nunique()))
except Exception as e:
    st.sidebar.warning(f"Lifetime dataset not loaded: {e}")

st.write("Open the sidebar or the pages menu to navigate. If pages do not show, make sure files exist under the `pages/` folder.")
