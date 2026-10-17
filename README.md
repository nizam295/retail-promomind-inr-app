# PromoMind AI: Autonomous Multi-Agent Indian Retail Promotion Engine

PromoMind AI is an enterprise-grade, agentic promotion planning dashboard built specifically for the high-velocity Indian retail economy. It autonomously optimizes the "What, How Much, How Long, and to Whom" of product promotions during intense festive surges (like Diwali, Dussehra, and Ganesh Chaturthi) while keeping the strategies strictly bounded by corporate financial guardrails.

## 🚀 System Architecture & Multi-Agent Network
The application orchestrates a multi-agent framework built on a concurrent state machine:
1. **📦 Inventory Guardian:** Scans warehouse stock levels, alerting the engine to overstock scenarios and prioritizing clearance to optimize storage costs.
2. **🔍 Market Scout:** Monitored competitor price cuts and matches local Indian festive buying surges.
3. **🛡️ Financial Overseer:** Intercepts agent recommendations, passing variables through a deterministic optimization engine (`scipy.optimize`) to enforce strict non-negotiable boundaries.

## ⚙️ Corporate Constraints Bounded in INR (₹)
* **Minimum Net Margin Floor (%):** Prevents aggressive pricing models from eroding margins below safety caps.
* **Available Marketing Budget (₹):** Dynamically scales from ₹50,000 to ₹5,00,00,000 to insulate macro enterprise finances.

## 🔄 Automated Production DevOps Pipeline
The repository features an enterprise-grade **Azure DevOps CI/CD pipeline** configured via `azure-pipelines.yml`. Every single code modification triggers automated quality test gates running `pytest`. If an LLM prompt attempt or code modification threatens to bypass the baseline financial constraints, the pipeline automatically fails the build, preventing faulty deployment configurations.

---

## 🛠️ Step-by-Step Installation & Local Execution

### Prerequisites
- Python 3.10 or 3.11 installed on your computer.

### Step 1: Clone the Repository
```bash
git clone https://github.com
cd retail-promomind-inr-app
```

### Step 2: Establish a Virtual Environment
```bash
python -m venv venv
# On Windows Command Prompt:
venv\Scripts\activate
# On Mac/Linux/Git Bash:
source venv/bin/activate
```

### Step 3: Install Platform Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Execute the Guardrail Test Matrix
Run the automated testing matrix to verify constraint safety bounds:
```bash
pytest test_agents.py
```

### Step 5: Boot the Live Dashboard UI
```bash
streamlit run app.py
```
Once initialized, the interactive control environment will automatically launch inside your local browser at `http://localhost:8501`.

---

### 📋 Technical Components Map
- **Frontend Dashboard Engine:** Streamlit
- **Computational Math Optimizer:** SciPy (Optimize Core Module)
- **Automated Validation Core:** PyTest & PyTest-Cov
- **CI/CD Cloud Automation:** Azure DevOps Pipelines (`azure-pipelines.yml`)
