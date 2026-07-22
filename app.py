import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="NEURO-STEER AI", page_icon="🧠", layout="wide")

st.title("🧠 NEURO-STEER AI: Magnetic Nanoparticle Steering Dashboard")
st.caption("Brain-Computer Interface & Directed Electromagnetic Clot Targeted System")

# Sidebar Controls
st.sidebar.header("🕹️ Operator & System Controls")
focus_level = st.sidebar.slider("Brain Focus Level (%)", 0, 100, 75)
steering_angle = st.sidebar.slider("Steering Angle (°)", -90, 90, 0)
injection_status = st.sidebar.button("💉 Inject Nanoparticles")

# Magnetic Coils Control Panel
st.sidebar.subheader("🧲 Helmet Coil Intensity (mT)")
coil_1 = st.sidebar.slider("Coil 1 (North)", 0, 100, 40)
coil_2 = st.sidebar.slider("Coil 2 (East)", 0, 100, 80 if steering_angle > 0 else 20)
coil_3 = st.sidebar.slider("Coil 3 (South)", 0, 100, 10)
coil_4 = st.sidebar.slider("Coil 4 (West)", 0, 100, 80 if steering_angle < 0 else 20)

col1, col2 = st.columns(2)

# --- PANEL 1: EEG BRAIN WAVE GRAPH ---
with col1:
    st.subheader("🧠 Live EEG Signal Monitoring")
    time_series = np.linspace(0, 2, 200)
    alpha_wave = np.sin(2 * np.pi * 10 * time_series) * (focus_level / 100)
    beta_wave = np.sin(2 * np.pi * 20 * time_series) * (1 - focus_level / 100)
    combined_eeg = alpha_wave + beta_wave + np.random.normal(0, 0.1, 200)

    fig_eeg = go.Figure()
    fig_eeg.add_trace(go.Scatter(y=combined_eeg, mode='lines', name='EEG Signal', line=dict(color='#00FFCC')))
    fig_eeg.update_layout(title="Real-Time Brain Intent (Alpha/Beta Waves)", xaxis_title="Time", yaxis_title="Amplitude (uV)", template="plotly_dark", height=350)
    st.plotly_chart(fig_eeg, use_container_width=True)

# --- PANEL 2: NANOPARTICLE BLOOD VESSEL VISUALIZER ---
with col2:
    st.subheader("🩸 Blood Vessel Nanoparticle Simulation")
    
    fig_vessel = go.Figure()
    
    # Vessel borders
    fig_vessel.add_trace(go.Scatter(x=[0, 10], y=[2, 2], mode='lines', line=dict(color='red', width=4), name='Vessel Wall'))
    fig_vessel.add_trace(go.Scatter(x=[0, 10], y=[-2, -2], mode='lines', line=dict(color='red', width=4), name='Vessel Wall'))
    
    # Blood Clot Target Location
    fig_vessel.add_trace(go.Scatter(x=[8], y=[0], mode='markers', marker=dict(size=35, color='darkred', symbol='square'), name='Blood Clot'))

    # Nanoparticle Swarm Positions based on Steering Angle & Focus
    np_x = np.linspace(1, 7, 30) if injection_status else np.ones(30) * 1
    np_y = (steering_angle / 90) * 1.5 + np.random.normal(0, 0.2, 30) if injection_status else np.random.normal(0, 0.2, 30)

    fig_vessel.add_trace(go.Scatter(x=np_x, y=np_y, mode='markers', marker=dict(size=10, color='gold', symbol='circle'), name='Nanoparticles'))

    fig_vessel.update_layout(title=f"Magnetic Path Angle: {steering_angle}° | Target Status: {'TARGETING CLOT 🎯' if injection_status else 'READY'}", xaxis=dict(range=[0, 10]), yaxis=dict(range=[-3, 3]), template="plotly_dark", height=350)
    st.plotly_chart(fig_vessel, use_container_width=True)

# Status Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Target Focus", f"{focus_level}%")
m2.metric("Active Magnetic Field", f"{max(coil_1, coil_2, coil_3, coil_4)} mT")
m3.metric("Clot Disruption Efficiency", f"{int(focus_level * 0.95)}%")
m4.metric("Nanoparticle Delivery", "ACTIVE" if injection_status else "STANDBY")
