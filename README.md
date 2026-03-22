# 🚀 Invisible Credit Score (ICS)

> **AI-powered Behavioral Credit Scoring for the Credit-Invisible**

[![Node.js](https://img.shields.io/badge/Node.js-18%2B-339933?logo=node.js&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-ML%20Service-009688?logo=fastapi&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)
[![Status](https://img.shields.io/badge/Status-Phase%203%20Production--Ready-blue)](#)

---

## 💼 Investor Pitch (Executive Summary)

**Problem:**  
Over 300M+ individuals in emerging markets lack formal credit history, making them invisible to traditional bureaus (CIBIL/Experian). Lenders, in turn, face high default risk and low approval rates.

**Solution:**  
ICS is a **Behavioral Risk Scoring Engine** that converts real-world financial behavior (transactions, savings discipline, payment patterns) into a **real-time, explainable credit score (0–1000)**.

**Why Now:**  
- Explosion of UPI/digital payments → rich behavioral data
- AI/ML maturity for risk modeling
- Regulatory push for financial inclusion

**Product:**  
- B2B API for lenders/NBFCs
- Real-time scoring + explainability
- Modular ML pipeline (feature engineering → inference → retraining)

**Traction Plan:**
- Pilot with small NBFCs (improve approvals by 20–30%)
- Expand to BNPL, neobanks, and salary platforms

**Moat:**
- Proprietary feature engineering on behavioral signals
- Model + data flywheel (better predictions over time)
- Explainability layer for compliance and trust

**Business Model:**
- API pricing (₹5–₹20 per score)
- SaaS dashboard for risk teams
- Enterprise customization

---

## ✨ GitHub “Wow Factor” Overview

- 🧠 ML-first architecture (FastAPI microservice)
- ⚡ Real-time scoring API (Node.js gateway)
- 🧩 Feature engineering pipeline
- 🔍 Explainable AI outputs (reasons + risk)
- 🐳 Docker-ready infra
- 📈 Phase 3: retraining pipeline scaffold

---

## 🏗️ Architecture Diagram

```
                ┌──────────────────────┐
                │   Client / NBFC App  │
                └──────────┬───────────┘
                           │ HTTP
                    ┌──────▼──────┐
                    │ API Gateway │  (Node.js)
                    └──────┬──────┘
                           │
        ┌──────────────────▼──────────────────┐
        │          ML Service (FastAPI)        │
        │ ┌──────────────┐  ┌──────────────┐  │
        │ │  Features    │  │   Model      │  │
        │ │ Engineering  │→ │ Inference    │  │
        │ └──────┬───────┘  └──────┬───────┘  │
        │        │                 │          │
        │  ┌─────▼─────┐    ┌─────▼─────┐    │
        │  │  Pipeline  │    │ Explain AI│    │
        │  │ Retraining │    │  Reasons  │    │
        │  └────────────┘    └───────────┘    │
        └─────────────────────────────────────┘
```

---

## 📁 Project Structure

```
ics-phase3-repo/
├── api-gateway/          # Node.js API Gateway
├── ml-service/           # FastAPI ML microservice
│   ├── features/         # Feature engineering
│   ├── models/           # Model loader + artifacts
│   ├── services/         # Scoring logic
│   └── pipeline/         # Retraining scaffold
├── dashboard/            # (Starter) UI placeholder
├── infra/                # Docker compose
├── database/             # SQL schema
└── README.md
```

---

## ⚙️ Quick Start (Local Setup)

### 1) ML Service

```bash
cd ml-service
pip install -r requirements.txt
python train.py
uvicorn app.main:app --reload
```

- URL: http://localhost:8000

### 2) API Gateway

```bash
cd api-gateway
npm install
node src/app.js
```

- URL: http://localhost:3000

---

## 🧪 Test the API

```bash
curl -X POST http://localhost:3000/api/score \
-H "Content-Type: application/json" \
-d '{
  "income": 50000,
  "expenses": 20000,
  "savings": 10000,
  "late_payments": 0
}'
```

**Response**

```json
{
  "credit_score": 750,
  "risk": "LOW",
  "reasons": ["Good savings"]
}
```

---

## 🧠 Feature Engineering (Core IP)

Derived features:
- Income level & stability (proxy)
- Expense-to-income ratio
- Savings rate
- Late payment frequency

These capture:
- Financial discipline
- Volatility and risk
- Liquidity buffer

---

## 🤖 ML Model

**Current:** RandomForest (baseline)  
**Upgrade Path:** XGBoost / LightGBM → Ensemble → Deep models

**Scoring:**
```
score = P(default=0) * 1000
```

**Risk Bands:**
- 700+ → LOW
- 500–700 → MEDIUM
- <500 → HIGH

---

## 🔍 Explainability (Why it matters)

Lenders require transparency. ICS returns:

```json
{
  "score": 720,
  "reasons": [
    "High savings rate",
    "Low late payments"
  ]
}
```

---

## 🔐 Production Hardening (Checklist)

- [ ] API keys + JWT auth
- [ ] Rate limiting
- [ ] Input validation (schema)
- [ ] Logging + tracing
- [ ] Redis cache (score caching)
- [ ] Queue (Kafka/RabbitMQ) for async ingestion

---

## 🐳 Docker (Optional)

```bash
cd infra
docker-compose up --build
```

---

## ☁️ Deployment Blueprint

- API: AWS EC2 / ECS
- ML: Dockerized FastAPI (autoscaled)
- DB: PostgreSQL (RDS)
- Models: S3 (versioned)
- CI/CD: GitHub Actions

---

## 📈 Phase 3 Capabilities

- Modular ML pipeline
- Explainable scoring
- Service-oriented architecture
- Retraining scaffold (ready for automation)

---

## 🔮 Phase 4 Roadmap

- Real-time ingestion (Kafka)
- Feature store (Feast-like)
- Continuous training + A/B models
- Full React dashboard for lenders
- Usage billing + API monetization

---

## 🏆 Why ICS Wins

- Works without traditional credit history
- Real-time + explainable
- Built for emerging markets
- Strong data/ML moat over time

---

## 🤝 Contributing

1. Fork
2. Create branch (`feature/xyz`)
3. Commit
4. PR

---

## 📜 License

MIT License

---

## 🧑‍💻 Author

Built as a production-grade fintech system to bridge the credit inclusion gap using AI.

---

> ⭐ If this project helped you, star the repo and share it!

