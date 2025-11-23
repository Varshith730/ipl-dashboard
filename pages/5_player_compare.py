# pages/5_player_compare.py
import streamlit as st
import pandas as pd
from src.data_loader import load_lifetime, load_deliveries
from src.features import combined_player_profile

st.title("👥 Player Comparison")

lifetime = load_lifetime()
players = sorted(lifetime['player'].unique())

col1, col2 = st.columns(2)
p1 = col1.selectbox("Player 1", players, index=0)
p2 = col2.selectbox("Player 2", players, index=1)

prof1 = combined_player_profile(p1)
prof2 = combined_player_profile(p2)

def safe(v):
    try:
        if v is None:
            return 0
        return round(float(v), 2)
    except:
        return v

# Build comparison table rows
rows = [
    ("Total Runs (lifetime)", safe(prof1.get("lifetime", {}).get("total_runs") if prof1.get("lifetime") else None),
                             safe(prof2.get("lifetime", {}).get("total_runs") if prof2.get("lifetime") else None)),
    ("Average (lifetime)", safe(prof1.get("lifetime", {}).get("batting_average") if prof1.get("lifetime") else None),
                             safe(prof2.get("lifetime", {}).get("batting_average") if prof2.get("lifetime") else None)),
    ("Strike Rate (lifetime)", safe(prof1.get("lifetime", {}).get("strike_rate") if prof1.get("lifetime") else None),
                                 safe(prof2.get("lifetime", {}).get("strike_rate") if prof2.get("lifetime") else None)),
    ("IPL Runs", safe(prof1.get("runs", 0)), safe(prof2.get("runs", 0))),
    ("IPL 4s", safe(prof1.get("fours", 0)), safe(prof2.get("fours", 0))),
    ("IPL 6s", safe(prof1.get("sixes", 0)), safe(prof2.get("sixes", 0))),
    ("IPL Wickets (lifetime)", safe(prof1.get("lifetime", {}).get("wickets") if prof1.get("lifetime") else None),
                              safe(prof2.get("lifetime", {}).get("wickets") if prof2.get("lifetime") else None)),
    ("Economy (lifetime)", safe(prof1.get("lifetime", {}).get("economy") if prof1.get("lifetime") else None),
                           safe(prof2.get("lifetime", {}).get("economy") if prof2.get("lifetime") else None)),
    ("Bowling Average (lifetime)", safe(prof1.get("lifetime", {}).get("bowling_average") if prof1.get("lifetime") else None),
                                   safe(prof2.get("lifetime", {}).get("bowling_average") if prof2.get("lifetime") else None)),
    ("Bowling SR (lifetime)", safe(prof1.get("lifetime", {}).get("bowling_strike_rate") if prof1.get("lifetime") else None),
                               safe(prof2.get("lifetime", {}).get("bowling_strike_rate") if prof2.get("lifetime") else None)),
]

df = pd.DataFrame({
    "Stat": [r[0] for r in rows],
    p1: [r[1] for r in rows],
    p2: [r[2] for r in rows]
})

st.dataframe(df, use_container_width=True)
