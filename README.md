# 🚗 Evaluation of Tailor-Made Generative AI Solutions for Efficient Test Vehicle Allocation at Volvo Cars

> A case study on feasibility, effort, and implementation practices for agentic AI in industrial test planning — developed at University West in collaboration with Volvo Cars.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-V--HAARF-0A66C2)
![Case study](https://img.shields.io/badge/Case%20study-CTPBot-orange)
![Evaluation](https://img.shields.io/badge/Effectiveness-73%2F100-green)
![Status](https://img.shields.io/badge/Thesis-Completed-success)

---

📌 Overview
This project tackles a real industrial decision problem: where agentic generative AI can improve test vehicle allocation, where simpler automation is enough, and where the process should stay human-led.
The work was carried out with Volvo Cars’ Product Test and Certification department. It evaluates CTPBot, an agentic AI tool for the Compatible Test Plan (CTP) workflow, and delivers reusable frameworks so future AI initiatives can be assessed in a consistent way.
The study was designed end-to-end — from process analysis and scenario-based testing to scoring models, issue logs, and implementation recommendations — as a 30-credit master’s thesis at University West.

🎯 Key Results
text| Item                           | Result                                              |
| ------------------------------ | --------------------------------------------------- |
| AI System Effectiveness Score  | 73 / 100                                            |
| Layer 1 Lifecycle/Governance   | 4.0 / 5  (weight 30%)                               |
| Layer 2 Capability             | 3.2 / 5  (weight 40%)                               |
| Layer 3 Real-world performance | 3.9 / 5  (weight 30%)                               |
| Issues logged                  | 42 technical and usability issues                   |
| Effort tracked                 | ~395 hours (validation + refinement + analysis)     |
| Method                         | Scenario testing + Template Analysis                |
✅ Promising and partly ready for wider use — needs work on latency, governance, edge cases, and knowledge transfer.

🏗️ System Architecture
textVolvo business process
        │
        ▼
┌─────────────────────────────────┐
│  V-HAARF (pre-adoption)         │
│  L1 Strategic evolution         │
│  L2 Process readiness           │
│  L3 Task suitability            │
│  → human / RPA / agentic pilot  │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  CTPBot (agentic CTP support)   │
│  • prompt + context management  │
│  • multimodal process data      │
│  • allocation recommendations   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│  Post-implementation evaluation │
│  L1 Lifecycle & governance      │
│  L2 Capability                  │
│  L3 Real-world performance      │
│  → Effectiveness Score 0–100    │
└──────────────┬──────────────────┘
               │
               ▼
     Issue log (42)
     Effort log (~395 h)
     Recommendations & checklists

🧠 Technical Approach
Framework 1 — V-HAARF (pre-adoption)
Problem: Volvo needed a reusable way to judge any process before building agentic AI.
Solution:

Three-layer model: strategy, process readiness, task suitability
1–5 scoring per layer
Recommendation bands: human-led, traditional automation, agentic AI pilot
Effort estimation at each layer

Framework 2 — Post-implementation evaluation (CTPBot)
Problem: CTPBot was already under implementation and needed an evidence-based review.
Solution:

Three weighted layers combined into one 0–100 score
Formula: Score = 20 × (0.30·L1 + 0.40·L2 + 0.30·L3)
Scenario-based testing of allocation queries and edge cases
42 issues categorised (latency, governance, edge cases, usability, knowledge transfer)
Template Analysis for qualitative themes and critical success factors

Tools produced

Evaluation templates and scoring model
Effort estimation template
Checklists for the next Volvo process


📁 Repository Structure
textv-haarf-ctpbot-thesis/
├── notebooks/
│   └── ctpbot_effectiveness_score.ipynb
├── src/
│   ├── run_evaluation.py
│   ├── scoring.py
│   ├── vhaarf.py
│   ├── issues.py
│   └── io_utils.py
├── config/
│   └── default.yaml
├── data/
│   └── results/
├── templates/
│   └── vhaarf_checklist.md
├── docs/
│   ├── Masters_Thesis_Paper.pdf
│   └── Master_Thesis_Description.pdf
├── requirements.txt
└── README.md

🚀 Getting Started
Prerequisites
Bashpip install -r requirements.txt
Run the evaluation scripts
Bashpython src/run_evaluation.py
Run the notebook

Open notebooks/ctpbot_effectiveness_score.ipynb in Jupyter or VS Code
Run cells from the repository root
The notebook loads config/default.yaml and the CSV files under data/results/

Quick score check
Pythonfrom src.io_utils import load_config
from src.scoring import effectiveness_score_100, score_band

cfg = load_config("config/default.yaml")
s = cfg["post_implementation"]["ctpbot_scores"]
w = cfg["post_implementation"]["weights"]
score = effectiveness_score_100(s["L1"], s["L2"], s["L3"], w)
print(score, score_band(score))

📦 Dataset
This is an evaluation study, not a public vehicle dataset.
What is in the repo:

published layer scores that produce 73/100
aggregated effort (~395 h)
an anonymised issue-log template

Real CTP allocations, vehicle identifiers, and internal Volvo documents stay inside the company.

🛠️ Tech Stack
text| Component              | Tool                                   |
| ---------------------- | -------------------------------------- |
| Agentic system (case)  | CTPBot (Volvo internal)                |
| Decision framework     | V-HAARF                                |
| Post-go-live scoring   | 3-layer weighted effectiveness model   |
| Qualitative analysis   | Template Analysis                      |
| Config                 | YAML                                   |
| Analysis / notebooks   | Python, pandas, Jupyter                |
| Documentation          | Markdown, thesis PDF                   |
| Industrial context     | Test vehicle allocation / CTP workflow |

📊 Evaluation Details

Score range: 0–100 (layers scored 1–5, then weighted)
Weights: Lifecycle & governance 30%, Capability 40%, Real-world performance 30%
CTPBot outcome: 73/100
Evidence: scenario tests, 42 logged issues, ~395 hours of effort
Follow-up focus: response latency, governance / audit trail, edge-case handling, knowledge transfer


🔭 Future Work

Apply V-HAARF to more Volvo processes
Re-score CTPBot after latency and governance fixes
Empirically validate V-HAARF beyond the single CTPBot case
Stronger edge-case tests and a formal risk review before a wider pilot
Knowledge-transfer mechanisms so domain rules are not locked in one expert


👤 Author
Ayeman Ulfat

MSc AI & Automation · University West, Trollhättan, Sweden

Advisor: Fredrik Ahrenberg, Volvo Cars

Examiner: Morgan Nilsen

Email: ayul0001@student.hv.se

📄 License
This repository is for thesis, portfolio, and research documentation.

Framework descriptions and code in this repo may be reused with attribution.

CTPBot, internal process data, and Volvo confidential material remain the property of Volvo Cars and must not be published.
