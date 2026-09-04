# Evaluation of Tailor-Made Generative AI Solutions for Efficient Test Vehicle Allocation at Volvo Cars

Master’s thesis (30 hp), University West, June 2026  
**Ayeman Ulfat** — Advisor: Fredrik Ahrenberg, Volvo Cars — Examiner: Morgan Nilsen

Case study of **CTPBot**, an agentic AI assistant for the Compatible Test Plan (test vehicle allocation) workflow.

## What this repository contains

1. **V-HAARF** — Volvo Hybrid AI Adoption & Readiness Framework (strategic / process / task).
2. **Post-implementation evaluation** — three-layer score that produced **73/100** for CTPBot.
3. Templates and scripts for issue logging (~42 issues), effort tracking (~395 h), and scoring.

Volvo operational data is **not** included.

## Layout

```text
config/       scoring weights and published CTPBot layer scores
data/         anonymised / template CSV results
src/          scoring and evaluation scripts
notebooks/    walkthrough of the 73/100 score
docs/         thesis PDF and one-page description
templates/    empty checklists for the next Volvo process
requirements.txt
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_evaluation.py
```

Then open `notebooks/ctpbot_effectiveness_score.ipynb`.

## Published CTPBot result

| Layer | Name | Score (1–5) | Weight |
|-------|------|-------------|--------|
| L1 | Lifecycle and Governance | 4.0 | 30% |
| L2 | Capability | 3.2 | 40% |
| L3 | Real-world performance | 3.9 | 30% |
| **Overall** | **AI System Effectiveness Score** | | **73 / 100** |

Band: promising, needs work on latency, governance, edge cases, and knowledge transfer.


