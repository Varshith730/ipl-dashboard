import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_loader import load_lifetime
from src.features import combined_player_profile

st.title("🏏 Player Statistics")

lifetime = load_lifetime()
players = sorted(lifetime['player'].unique())

player = st.selectbox("Select Player", players)

profile = combined_player_profile(player)

# ------------------- Lifetime Stats -------------------
life = profile["lifetime"]

if life:
    st.subheader("🎖 Lifetime Stats")
    col1, col2, col3, col4 = st.columns(4)

    with col1: st.metric("Runs", life["total_runs"])
    with col2: st.metric("Average", life["batting_average"])
    with col3: st.metric("Strike Rate", life["strike_rate"])
    with col4: st.metric("Centuries", life["centuries"])
else:
    st.warning("⚠ Lifetime stats not available for this player.")

# ------------------- IPL REAL STATS -------------------
st.write("---")
st.subheader("📊 IPL Real Stats")

col1, col2, col3, col4 = st.columns(4)

with col1: st.metric("IPL Runs", profile["runs"])
with col2: st.metric("Balls", profile["balls"])
with col3: st.metric("4s", profile["fours"])
with col4: st.metric("6s", profile["sixes"])

# ------------------- Season-wise Graph -------------------
if not profile["season_runs"].empty:
    st.subheader("📈 Season-wise IPL Runs")
    fig, ax = plt.subplots()
    sns.lineplot(data=profile["season_runs"], x='season', y='batsman_runs', marker='o')
    st.pyplot(fig)
else:
    st.info("No season-wise data available.")
