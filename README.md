# 📬 Investment Newsletter A/B Testing Dashboard

This project simulates and visualizes A/B testing outcomes for a hypothetical investment research newsletter, helping evaluate how subject lines, content topics, and send times impact user engagement (CTR). Built as an interactive Streamlit dashboard, it showcases basic experimentation logic, modeling, and UI-driven insight delivery — ideal for marketing or product teams experimenting with communication strategies.

## 🎯 Project Objective

- Simulate A/B test variants on **subject lines**, **content types** (Macro, Equities, Crypto), and **send times**
- Generate **synthetic user interaction data** (opens, clicks) for 30,000 newsletter recipients
- Train models to predict **click-through probability**
- Visualize results with **interactive dashboards** for rapid marketing insight

---

## 🧪 A/B Test Setup

- **Variants** tested:
  - Subject Lines: A vs. B
  - Content Types: Macro, Equities, Crypto
  - Send Times: 8 AM, 9 AM, 12 PM

- **Synthetic User Data**:
  - 30,000 simulated users with open and click probabilities
  - Generated using `numpy`, `pandas`, and logic assumptions

---

## 📈 Key Features

### ✅ Modeled Insights
- **Logistic Regression** and **Gradient Boosting (XGBoost)** used to predict CTR
- AUC scores shown on the dashboard for quick model evaluation

### 📊 Streamlit Dashboard
- View engagement by **content type** and **send time**
- Monitor model AUC for predictive performance
- Explore real-time charts (bar graphs, metrics) to simulate insights for a marketing team
