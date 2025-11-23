# pages/1_home.py
import streamlit as st
from src.data_loader import load_lifetime, load_deliveries, load_matches

st.title("🏠 Home — IPL Dashboard")

# Load
lifetime = load_lifetime()
deliveries = load_deliveries()
matches = load_matches()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Players (lifetime)", lifetime['player'].nunique())
with col2:
    st.metric("Total Matches", int(matches.shape[0]))
with col3:
    st.metric("Total Deliveries (approx)", int(deliveries.shape[0]))

st.write("---")
st.subheader("Top performers (overall IPL lifetime file)")

top_batter = lifetime.sort_values("total_runs", ascending=False).head(5)[['player', 'total_runs']]
st.write("Top batters (by total runs)")
st.table(top_batter)

if 'wickets' in lifetime.columns:
    top_bowler = lifetime.sort_values("wickets", ascending=False).head(5)[['player', 'wickets']]
    st.write("Top bowlers (by wickets)")
    st.table(top_bowler)
