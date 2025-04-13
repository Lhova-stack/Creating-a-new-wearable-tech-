import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Athlete Dashboard", layout="wide")

st.title("🏋️‍♂️ AI Wearable Athlete Dashboard")
st.markdown("Monitor your performance, fatigue, and stats in real-time.")

# Sidebar filters
sport = st.sidebar.selectbox("Select Sport", ["Soccer", "Rugby", "Cricket"])
player = st.sidebar.selectbox("Player", ["Player 1", "Player 2", "Player 3"])

# Simulated performance data
st.subheader(f"Performance Metrics - {player} ({sport})")
data = pd.DataFrame({
    "Session": [f"S{i}" for i in range(1, 11)],
    "Speed (km/h)": np.random.uniform(18, 30, 10),
    "Fatigue Level": np.random.uniform(0.1, 0.9, 10),
    "Heart Rate (bpm)": np.random.uniform(80, 170, 10)
})

chart = alt.Chart(data).transform_fold(
    ["Speed (km/h)", "Fatigue Level", "Heart Rate (bpm)"]
).mark_line(point=True).encode(
    x='Session',
    y='value:Q',
    color='key:N'
).properties(width=800, height=400)

st.altair_chart(chart)

# Summary stats
st.subheader("🧠 AI Insights")
st.success("Player is performing optimally. No signs of critical fatigue.")
