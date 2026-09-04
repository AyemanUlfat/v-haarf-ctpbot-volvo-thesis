# 🚗 Evaluation of Tailor-Made Generative AI Solutions for Efficient Test Vehicle Allocation at Volvo Cars

> A case study on feasibility, effort, and implementation practices for agentic AI in industrial test planning — developed at University West in collaboration with Volvo Cars.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-V--HAARF-0A66C2)
![Case study](https://img.shields.io/badge/Case%20study-CTPBot-orange)
![Evaluation](https://img.shields.io/badge/Effectiveness-73%2F100-green)
![Status](https://img.shields.io/badge/Thesis-Completed-success)

---

## 📌 Overview

This thesis tackles a real industrial decision problem: **when should Volvo Cars use agentic generative AI** for test vehicle allocation — and when are simpler automation or human-led processes the better choice?

The work was carried out with Volvo Cars’ **Product Test and Certification** department. It evaluates **CTPBot**, an agentic AI tool built to support the Compatible Test Plan (CTP) workflow, and delivers reusable frameworks so future AI projects can be assessed in a consistent way.

The project covers the full adoption lifecycle: **feasibility and business value**, **effort to reach domain-specific performance**, and **implementation practices** after a system is already in use.

---

## 🎯 Project goals

- Decide where agentic AI adds value, where RPA/rules are enough, and where humans should stay in control
- Estimate the real time and effort needed to reach acceptable domain performance
- Capture methods and best practices for later AI projects at Volvo Cars

---

## 🧩 Frameworks

### V-HAARF
**Volvo Hybrid AI Adoption & Readiness Framework** — a three-layer decision tool:

1. **Strategic evolution** — is this the right kind of problem for AI at company level?
2. **Process readiness** — is the workflow, data, and organisation ready?
3. **Task suitability** — which tasks should be agentic, automated, or human-led?

### Post-implementation evaluation
A separate three-layer framework for systems already in use. It combines quantitative metrics and qualitative analysis (including Template Analysis) into one **AI System Effectiveness Score (0–100)**.

---

## 📁 Repository structure

```text
v-haarf-ctpbot-thesis/
├── README.md
├── requirements.txt
├── config/
│   └── default.yaml
├── data/
│   └── results/
├── src/
├── notebooks/
├── templates/
└── docs/
