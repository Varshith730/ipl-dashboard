from rapidfuzz import process
import pandas as pd
from src.data_loader import load_lifetime, load_deliveries, load_matches

def best_match(name, candidates):
    """Return the closest matching player name using fuzzy matching."""
    match, score, index = process.extractOne(name, candidates)
    return match if score >= 70 else None

def combined_player_profile(player_name):
    deliveries = load_deliveries()
    matches = load_matches()
    lifetime = load_lifetime()

    # ------------------- LIFETIME MATCH -------------------
    life_names = lifetime['player'].tolist()
    matched_life = best_match(player_name, life_names)

    life = None
    if matched_life:
        life = lifetime[lifetime['player'] == matched_life].iloc[0].to_dict()

    # ------------------- IPL MATCH (deliveries) -------------------
    deliv_names = deliveries['batter'].unique().tolist()
    matched_deliv = best_match(player_name, deliv_names)

    if not matched_deliv:
        return {
            "lifetime": life,
            "runs": 0,
            "balls": 0,
            "fours": 0,
            "sixes": 0,
            "season_runs": pd.DataFrame(columns=['season', 'batsman_runs'])
        }

    player_del = deliveries[deliveries['batter'] == matched_deliv]

    runs = player_del['batsman_runs'].sum()
    balls = len(player_del)
    fours = (player_del['batsman_runs'] == 4).sum()
    sixes = (player_del['batsman_runs'] == 6).sum()

    merged = player_del.merge(
        matches[['id', 'season']],
        left_on='match_id',
        right_on='id',
        how='left'
    )
    season_runs = merged.groupby('season')['batsman_runs'].sum().reset_index()

    return {
        "lifetime": life,
        "runs": runs,
        "balls": balls,
        "fours": fours,
        "sixes": sixes,
        "season_runs": season_runs
    }
