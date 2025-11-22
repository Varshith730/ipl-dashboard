import streamlit as st
from src.data_loader import load_lifetime, load_deliveries
from src.features import combined_player_profile


def app():
    st.title("👥 Player Comparison")

    # Load data
    lifetime_df = load_lifetime()
    deliveries = load_deliveries()

    # FIXED: Use correct column name: "Player"
    players = sorted(lifetime_df["Player"].unique())

    col1, col2 = st.columns(2)
    with col1:
        player1 = st.selectbox("Player 1", players)
    with col2:
        player2 = st.selectbox("Player 2", players)

    # Profiles
    p1 = combined_player_profile(player1)
    p2 = combined_player_profile(player2)

    # FIXED: Round all values to 2 decimals
    def r(v):
        return round(v, 2) if isinstance(v, (int, float)) else v

    stats = {
        "Total Runs": (r(p1["total_runs"]), r(p2["total_runs"])),
        "Average": (r(p1["batting_avg"]), r(p2["batting_avg"])),
        "Strike Rate": (r(p1["strike_rate"]), r(p2["strike_rate"])),
        "IPL Runs": (r(p1["ipl_runs"]), r(p2["ipl_runs"])),
        "IPL 4s": (r(p1["ipl_4s"]), r(p2["ipl_4s"])),
        "IPL 6s": (r(p1["ipl_6s"]), r(p2["ipl_6s"])),

        # Bowling stats added
        "IPL Wickets": (r(p1["ipl_wkts"]), r(p2["ipl_wkts"])),
        "Economy Rate": (r(p1["eco_rate"]), r(p2["eco_rate"])),
        "Bowling Average": (r(p1["bowl_avg"]), r(p2["bowl_avg"])),
        "Bowling Strike Rate": (r(p1["bowl_sr"]), r(p2["bowl_sr"])),
    }

    st.write("### Comparison Table")
    st.table(
        {
            "Stat": list(stats.keys()),
            player1: [v[0] for v in stats.values()],
            player2: [v[1] for v in stats.values()],
        }
    )
