import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.features import combined_player_profile
from src.data_loader import load_lifetime, load_deliveries, load_matches


st.title("🏆 Team Performance Analysis")

matches = load_matches()

teams = sorted(matches['team1'].unique())
team = st.selectbox("Select a Team", teams)

# Team matches
team_matches = matches[(matches['team1'] == team) | (matches['team2'] == team)]

wins = (team_matches['winner'] == team).sum()
losses = team_matches.shape[0] - wins

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Matches Played", team_matches.shape[0])
with col2:
    st.metric("Wins", wins)
with col3:
    st.metric("Losses", losses)

# Wins by season
st.subheader("📅 Wins by Season")

wins_season = team_matches[team_matches['winner'] == team].groupby('season').size()

fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(x=wins_season.index, y=wins_season.values, ax=ax)
plt.title(f"Wins by Season - {team}")
st.pyplot(fig)

# Venue performance
st.subheader("🏟️ Venue Performance")

venue_wins = team_matches[team_matches['winner'] == team]['venue'].value_counts().head(10)

st.bar_chart(venue_wins)
