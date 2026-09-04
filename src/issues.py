from pathlib import Path
import pandas as pd


def load_issues(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path, comment="#")


def summarize_issues(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["category", "severity"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )
