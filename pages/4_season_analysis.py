import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_loader import load_deliveries, load_matches
import pandas as pd

st.title("📅 Season Analysis")

deliveries = load_deliveries()
matches = load_matches()

# Merge matches to deliveries to bring season
merged = deliveries.merge(
    matches[['id', 'season']],
    left_on='match_id',
    right_on='id',
    how='left'
)

# ---- BATTING SECTION ----
st.subheader("🏏 Top Run Scorers (Season-wise)")

season_list = sorted(merged['season'].unique())
season = st.selectbox("Select Season", season_list)

season_batting = (
    merged[merged['season'] == season]
    .groupby('batter')['batsman_runs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

st.write(season_batting)

fig, ax = plt.subplots()
sns.barplot(data=season_batting, x='batsman_runs', y='batter', ax=ax)
ax.set_title(f"Top Run Scorers - {season}")
st.pyplot(fig)



# ---- BOWLING SECTION ----
st.subheader("🎯 Top Wicket Takers (Season-wise)")

# Filter valid bowler wickets
valid_wickets = merged[
    (merged['is_wicket'] == 1) &
    (~merged['dismissal_kind'].isin(["run out", "retired hurt", "obstructing the field"]))
]

season_wickets = (
    valid_wickets[valid_wickets['season'] == season]
    .groupby('bowler')['is_wicket']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

st.write(season_wickets)

fig2, ax2 = plt.subplots()
sns.barplot(data=season_wickets, x='is_wicket', y='bowler', ax=ax2)
ax2.set_title(f"Top Wicket Takers - {season}")
st.pyplot(fig2)
