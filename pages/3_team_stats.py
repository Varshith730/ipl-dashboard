# pages/3_team_stats.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_loader import load_matches

st.title("🏏 Team Statistics")

matches = load_matches()
teams = sorted(pd.unique(matches[['team1','team2']].values.ravel('K')))
team = st.selectbox("Select Team", teams)

team_matches = matches[(matches['team1'] == team) | (matches['team2'] == team)]
wins = team_matches['winner'].value_counts().get(team, 0)
st.metric("Matches Played", int(team_matches.shape[0]))
st.metric("Wins", int(wins))

# Wins by season
wins_season = team_matches[team_matches['winner'] == team].groupby('season').size().reset_index(name='wins')
if not wins_season.empty:
    fig, ax = plt.subplots()
    sns.barplot(data=wins_season, x='season', y='wins', ax=ax)
    ax.set_title(f"Wins by season - {team}")
    st.pyplot(fig)
else:
    st.info("No wins data for this team in dataset.")
