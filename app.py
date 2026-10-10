# File: app.py
import streamlit as st # type: ignore
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="PromoMind AI Dashboard", layout="wide", page_icon="🤖")

st.title("🤖 PromoMind AI — Autonomous Promotion Planner")
st.subheader("Multi-Agent Omnichannel Indian Retail Optimization Engine")

# --- SIDEBAR: HARD ENTERPRISE CONSTRAINTS ---
st.sidebar.header("🛡️ Corporate Constraint Guardrails")
min_margin_floor = st.sidebar.slider("Minimum Net Margin Floor (%)", min_value=5, max_value=30, value=15, step=1)
# Configured in INR (₹) with typical Indian enterprise budget parameters
marketing_budget = st.sidebar.number_input("Available Marketing Budget (₹)", min_value=50000, max_value=5000000, value=500000, step=50000, format="%d")

# --- SECTION 1: SIMULATED INGESTION INPUTS ---
st.header("📥 Real-Time Market Data Ingestion")
col1, col2, col3 = st.columns(3)

with col1:
    inventory_volume = st.slider("Current Inventory Volume (Units)", min_value=100, max_value=5000, value=1500, step=100)
    baseline_margin = st.slider("Product Baseline Margin (%)", min_value=20, max_value=60, value=40, step=5)

with col2:
    competitor_discount = st.slider("Competitor Discount Threat (%)", min_value=0, max_value=50, value=15, step=5)
    # Seasonal events updated to major festive and shopping periods in India
    holiday_season = st.selectbox("Upcoming Seasonal Event", ["None", "Ganesh Chaturthi", "Diwali / Festive Sale", "Dussehra", "End of Season Sale (EOSS)"])

with col3:
    # Target segments aligned with common Indian consumer behavioral profiling
    target_segment = st.selectbox("Target Customer Segment", ["Festive Value Hunters", "Brand Loyalists", "Tier-2/Tier-3 Aspirant Buyers"])

# --- SECTION 2: THE AGENTIC ENGINE LOGIC ---
st.header("🧠 Multi-Agent Negotiation Logs")

# Autonomous logic simulation
proposed_discount = competitor_discount + 2.0  # Scout agent logic
net_margin_after_promo = baseline_margin - proposed_discount

# Initialize Agent Logs Text Box
agent_logs = []
agent_logs.append(f"🔍 [Market Scout]: Detected competitor slashing prices by {competitor_discount}%. Holiday threat status: {holiday_season}.")

if inventory_volume > 1000:
    agent_logs.append(f"📦 [Inventory Guardian]: Alert! High surplus stock detected ({inventory_volume} units). Clearance strategy recommended to free up warehouse space.")
else:
    agent_logs.append("📦 [Inventory Guardian]: Stock levels nominal. Heavy clearance discounts are unnecessary.")

# Financial Constraint Shield Intervention
if net_margin_after_promo < min_margin_floor:
    final_discount = baseline_margin - min_margin_floor
    status = "⚠️ Capped by Financial Overseer"
    agent_logs.append(f"🚨 [Financial Overseer]: BLOCKED! The proposed {proposed_discount}% discount drops net margin to {net_margin_after_promo}%, breaching the required {min_margin_floor}% floor.")
    agent_logs.append(f"⚖️ [Financial Overseer]: Recalculating... Safe promotional cap applied at exactly {final_discount}% discount to protect gross margins.")
else:
    final_discount = proposed_discount
    status = "✅ Approved by All Agents"
    agent_logs.append(f"💰 [Financial Overseer]: Safe parameters verified. Projected net promo margin ({net_margin_after_promo}%) clears the {min_margin_floor}% corporate floor.")

# Display Logs nicely in a code block
st.code("\n".join(agent_logs), language="text")

# --- SECTION 3: DECISION OUTPUTS ---
st.header("📊 Optimized Strategic Output")
out_col1, out_col2, out_col3 = st.columns(3)

with out_col1:
    st.metric(label="Recommended Discount Amount", value=f"{final_discount}%", delta=status)
with out_col2:
    st.metric(label="Promotion Duration", value="4 Days" if holiday_season != "None" else "10 Days")
with out_col3:
    st.metric(label="Target Routing Audience", value=target_segment)

st.success(f"Strategy calculated successfully for Budget: ₹{marketing_budget:,}. Ready for production export.")
