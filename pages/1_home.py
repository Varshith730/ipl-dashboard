import streamlit as st
from src.data_loader import load_lifetime
from src.features import combined_player_profile

st.title("🔥Most Active Players in IPL🔥")

# Load lifetime dataset
lifetime = load_lifetime()

# Best batter (based on total runs)
best_batter = lifetime.sort_values("total_runs", ascending=False).iloc[0]

st.subheader(f"🔥 Most Active Batter: {best_batter['player']}")
st.metric("Total Runs", best_batter["total_runs"])

# Best bowler based on wickets
if "wickets" in lifetime.columns:
    best_bowler = lifetime.sort_values("wickets", ascending=False).iloc[0]
    st.subheader(f"🎯 Best Bowler: {best_bowler['player']}")
    st.metric("Wickets", best_bowler["wickets"])
