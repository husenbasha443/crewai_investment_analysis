# 📊 Investment Analysis System using CrewAI

## 📌 Project Overview

This project implements an **AI-powered Investment Analysis System** using **CrewAI**, where multiple intelligent agents collaborate to analyze an investment opportunity and provide a final recommendation.

The system uses a **multi-agent architecture** backed by a **Large Language Model (LLM)** to perform:

* Investment research
* Financial analysis
* Final investment advice

Each agent is responsible for a specific task, and together they generate a **comprehensive investment analysis report**.

---

## 🎯 Problem Statement

Investors often struggle to:

* Understand complex investment instruments
* Evaluate risks and volatility
* Make informed long-term investment decisions

This project solves the problem by simulating a **team of financial experts** using AI agents that work together to analyze an investment topic provided by the user.

---

## 🧠 Solution Architecture (Multi-Agent Workflow)

```
Research Analyst Agent
        ↓
Financial Analyst Agent
        ↓
Investment Advisor Agent
        ↓
Final Investment Analysis Report
```

---

## 👥 Agents Description

### 1️⃣ Research Analyst Agent

* Researches the investment topic provided by the user
* Identifies asset type, market trends, and key drivers
* Produces an initial research summary

### 2️⃣ Financial Analyst Agent

* Analyzes volatility, returns, and financial characteristics
* Evaluates risks and long-term suitability
* Builds upon the research agent’s output

### 3️⃣ Investment Advisor Agent

* Combines research and financial analysis
* Considers risk appetite and investment horizon
* Produces the final **Buy / Hold / Avoid** recommendation

---

## 📂 Project Structure

```
crewai_investment_analysis/
│
├── .venv/                          # Virtual environment
│
├── knowledge/                      # (Optional) RAG documents
│
├── src/
│   └── crewai_investment_analysis/
│       ├── __init__.py
│       ├── crew.py                 # Agent & task orchestration
│       ├── main.py                 # Entry point (inputs & kickoff)
│       │
│       ├── config/
│       │   ├── agents.yaml         # Agent definitions
│       │   └── tasks.yaml          # Task definitions
│       │
│       └── tools/                  # (Optional) custom tools
│
├── tests/                          # (Optional) tests
│
├── .env                            # API keys (Groq / OpenAI / etc.)
├── .gitignore
├── pyproject.toml                  # Project dependencies
├── README.md                       # Project documentation
└── report.md                       # Final generated report (optional)
```

---

## 📄 Configuration Files

### 🔹 agents.yaml

Defines:

* Agent roles
* Goals
* Background expertise

Each agent represents a real-world financial role.

---

### 🔹 tasks.yaml

Defines:

* Task descriptions
* Expected outputs
* Agent-task mapping
* Dynamic input binding using `{{ topic }}`

Example:

```yaml
description: >
  Conduct detailed research on {{ topic }}.
```

---

## 📝 User Input

The user provides an **investment topic** at runtime.

Example input:

```python
inputs = {
  "topic": "Nippon India Silver ETF (FoF) for long-term investment considering a very high risk appetite"
}
```

This input is dynamically injected into all tasks and guides agent reasoning.

---

## ⚙️ Technologies Used

* **Python 3.11**
* **CrewAI**
* **LiteLLM**
* **Groq LLM (LLaMA 3.1)**
* **YAML (for configuration)**

---

## 🔐 Environment Variables (`.env`)

```env
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=your_groq_api_key
```

> ⚠️ Never commit API keys to GitHub.

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment (using uv)

```bash
uv venv --python 3.11
```

### 2️⃣ Activate Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
uv pip install crewai crewai-tools
```

or

```bash
uv pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create a `.env` file and add your API keys.

### 5️⃣ Run the Crew

```bash
crewai run
```

---

## ✅ Output

The system generates a **detailed investment analysis report**, including:

* Research summary
* Financial analysis
* Risk assessment
* Final investment recommendation
* Target price outlook (if applicable)

---

## 🧪 How to Verify LLM & Multi-Agent Execution

* Change the input topic → output changes
* Each agent produces its own reasoning
* Output is not hardcoded
* Confirms real LLM usage

---

## 🎓 Learning Outcomes

* Understanding of multi-agent AI systems
* Practical usage of CrewAI
* LLM-driven decision making
* Prompt engineering using dynamic inputs
* Real-world AI system design

---


