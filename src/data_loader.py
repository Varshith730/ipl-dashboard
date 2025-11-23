# src/data_loader.py
import pandas as pd
import zipfile
import os
from functools import lru_cache

DATA_DIR = "data"
DELIVERY_CSV = os.path.join(DATA_DIR, "deliveries.csv")
DELIVERY_ZIP = os.path.join(DATA_DIR, "deliveries.csv.zip")
MATCHES_CSV = os.path.join(DATA_DIR, "matches.csv")
LIFETIME_CSV = os.path.join(DATA_DIR, "cricket_full_ipl_lifetime.csv")

@lru_cache(maxsize=1)
def load_matches(path=MATCHES_CSV):
    if not os.path.exists(path):
        raise FileNotFoundError(f"matches file not found at {path}")
    df = pd.read_csv(path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]
    return df

@lru_cache(maxsize=1)
def load_lifetime(path=LIFETIME_CSV):
    if not os.path.exists(path):
        raise FileNotFoundError(f"lifetime file not found at {path}")
    df = pd.read_csv(path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]
    return df

@lru_cache(maxsize=1)
def load_deliveries():
    # If csv is present use it, else try to extract from zip
    if os.path.exists(DELIVERY_CSV):
        df = pd.read_csv(DELIVERY_CSV, low_memory=False)
        df.columns = [c.strip() for c in df.columns]
        return df

    if os.path.exists(DELIVERY_ZIP):
        try:
            with zipfile.ZipFile(DELIVERY_ZIP, "r") as z:
                # extract only deliveries.csv to data dir
                members = z.namelist()
                target_name = None
                for m in members:
                    if os.path.basename(m).lower() == "deliveries.csv":
                        target_name = m
                        break
                if target_name is None:
                    # fallback: extract first csv
                    for m in members:
                        if m.lower().endswith(".csv"):
                            target_name = m
                            break
                if target_name is None:
                    raise FileNotFoundError("No CSV found inside deliveries.zip")

                z.extract(target_name, DATA_DIR)
                extracted_path = os.path.join(DATA_DIR, target_name)
                # If nested path, move/rename to deliveries.csv at DATA_DIR root
                if os.path.basename(extracted_path).lower() != "deliveries.csv":
                    final_path = DELIVERY_CSV
                    os.replace(extracted_path, final_path)
                else:
                    final_path = extracted_path

            df = pd.read_csv(final_path, low_memory=False)
            df.columns = [c.strip() for c in df.columns]
            return df
        except Exception as e:
            raise RuntimeError(f"Failed to extract deliveries.zip: {e}")

    # Neither CSV nor ZIP found
    raise FileNotFoundError(f"Neither {DELIVERY_CSV} nor {DELIVERY_ZIP} found in data folder")
