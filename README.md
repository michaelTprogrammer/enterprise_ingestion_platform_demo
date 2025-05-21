
# Enterprise Ingestion Demo

This project simulates an enterprise-grade ingestion pipeline from SharePoint exports to Redshift (mocked via PostgreSQL), transforming the data with dbt, and orchestrated via GitHub Actions.

## 💡 Project Purpose

To showcase engineering capabilities in:
- Config-driven ingestion with Python
- Schema validation and error handling
- dbt semantic modeling (staging → marts)
- CI/CD automation using GitHub Actions
- Modular, scalable data platform design

## 🔧 Stack

- Python (pandas, openpyxl, pyyaml)
- dbt-core
- PostgreSQL (mock Redshift)
- GitHub Actions
- YAML (for config)
- pytest (validation)
- Power BI (optional downstream use)

## 📂 Structure

```
enterprise_ingestion_demo/
├── data/                 ← Mock Excel data from "SharePoint"
├── ingestion/            ← Python scripts to load and validate
├── dbt_project/          ← dbt models
│   └── models/
│       ├── staging/
│       ├── intermediate/
│       └── marts/
├── tests/                ← Pytest schema tests
├── .github/workflows/    ← CI/CD YAML
└── README.md             ← You're reading it
```

## ✅ Goals

- Show modular data engineering thinking
- Demonstrate practical dbt usage
- Make engineering ability visible for hiring manager

## 🚀 Next Steps

1. Generate mock Excel files in `/data`
2. Write `ingestion/main.py` to parse config and upload to Postgres
3. Define `config.yml` for source definitions
4. Create dbt project, models, and tests
5. Push with GitHub Actions to validate CI pipeline
