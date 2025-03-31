import streamlit as st
import pandas as pd

# Assuming df is already saved or loaded from CSV
df = pd.read_csv("your_data.csv")  # Or wherever your df comes from

st.title("Investment Newsletter A/B Testing Insights")

st.write("### Engagement by Content Type")
st.bar_chart(df.groupby("content_type")["clicked"].mean())

st.write("### Send Time Effect on CTR")
st.bar_chart(df.groupby("send_time")["clicked"].mean())

st.write("### Model AUC Scores")
st.metric("XGBoost AUC", "0.83")
