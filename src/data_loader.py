import pandas as pd
from functools import lru_cache

@lru_cache(maxsize=1)
def load_matches(path="data/matches.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df

@lru_cache(maxsize=1)
def load_deliveries(path="data/deliveries.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df

@lru_cache(maxsize=1)
def load_lifetime(path="data/cricket_full_ipl_lifetime.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df
