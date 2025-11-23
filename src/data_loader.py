import pandas as pd
import zipfile
from functools import lru_cache

@lru_cache(maxsize=1)
def load_deliveries(path="data/deliveries.csv.zip"):
    """Loads deliveries data from ZIP (Streamlit Cloud compatible)"""
    try:
        with zipfile.ZipFile(path, 'r') as z:
            # auto-detect first file inside the ZIP
            inner_file = z.namelist()[0]
            df = pd.read_csv(z.open(inner_file))
            df.columns = [c.strip().lower() for c in df.columns]
            return df
    except Exception as e:
        raise FileNotFoundError(f"Deliveries ZIP not found or unreadable: {e}")


ROOT = Path(__file__).resolve().parents[1]  # project root

@lru_cache(maxsize=1)
def load_matches(path:str = str(ROOT / "data" / "matches.csv")):
    """
    Load matches.csv (small CSV)
    """
    df = pd.read_csv(path)
    # normalize column names
    df.columns = [c.strip() for c in df.columns]
    return df


@lru_cache(maxsize=1)
def load_lifetime(path:str = str(ROOT / "data" / "cricket_full_ipl_lifetime.csv")):
    """
    Load lifetime/player dataset (cricket_full_ipl_lifetime.csv).
    """
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df

