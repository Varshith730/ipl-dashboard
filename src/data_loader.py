import pandas as pd
import zipfile
import os
from functools import lru_cache


DATA_DIR = "data"
DELIVERY_CSV = f"{DATA_DIR}/deliveries.csv"
DELIVERY_ZIP = f"{DATA_DIR}/deliveries.csv.zip"


# -------------------------------
# Load Matches
# -------------------------------
@lru_cache(maxsize=1)
def load_matches(path=f"{DATA_DIR}/matches.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df


# -------------------------------
# Load Lifetime Dataset
# -------------------------------
@lru_cache(maxsize=1)
def load_lifetime(path=f"{DATA_DIR}/cricket_data.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df


# -------------------------------------
# LOAD DELIVERIES (Auto-unzip supported)
# -------------------------------------
@lru_cache(maxsize=1)
def load_deliveries():

    # If CSV already extracted → just load it
    if os.path.exists(DELIVERY_CSV):
        df = pd.read_csv(DELIVERY_CSV)
        df.columns = [c.strip() for c in df.columns]
        return df

    # If CSV missing → but ZIP exists → extract it
    elif os.path.exists(DELIVERY_ZIP):
        try:
            with zipfile.ZipFile(DELIVERY_ZIP, "r") as z:
                z.extractall(DATA_DIR)
            print("✔ Extracted deliveries.csv from ZIP")

            df = pd.read_csv(DELIVERY_CSV)
            df.columns = [c.strip() for c in df.columns]
            return df

        except Exception as e:
            raise FileNotFoundError(f"Error extracting deliveries.csv.zip → {e}")

    else:
        raise FileNotFoundError(
            "❌ deliveries.csv NOT found and deliveries.csv.zip NOT found in /data folder"
        )
