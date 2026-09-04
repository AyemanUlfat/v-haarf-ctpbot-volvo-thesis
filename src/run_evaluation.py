"""Recompute the published CTPBot effectiveness score from config + CSVs."""

from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.io_utils import load_config
from src.issues import load_issues, summarize_issues
from src.scoring import effectiveness_score_100, score_band


def main():
    cfg = load_config()
    pi = cfg["post_implementation"]
    scores = pi["ctpbot_scores"]
    overall = effectiveness_score_100(scores["L1"], scores["L2"], scores["L3"], pi["weights"])
    print(f"AI System Effectiveness Score: {overall}/100 ({score_band(overall)})")
    print(f"Published thesis score:        {scores['overall']}/100")

    issues = load_issues(ROOT / cfg["paths"]["issue_log"])
    print("\nIssue categories (template log, not the full confidential 42):")
    print(summarize_issues(issues).to_string(index=False))

    effort = pd.read_csv(ROOT / cfg["paths"]["effort_log"])
    print("\nEffort log:")
    print(effort.to_string(index=False))


if __name__ == "__main__":
    main()
