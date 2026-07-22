import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="NEURO-STEER AI", page_icon="🧠", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Title Header
st.title("🧠 NEURO-STEER AI — Autonomous Micro-Vascular Steering System")
st.caption("Painless & Non-Invasive Targeted Nano-Swarm Navigation for Brain Stroke Treatment")

st.divider()

# Patient & Diagnostic Section
st.header("📋 Patient & Diagnostic Scanning")

col1, col2 = st.columns(2)

with col1:
    patient_id = st.text_input("Patient ID", "HACK-2026-NEURO-01")
    protocol = st.selectbox(
        "Scanning Protocol",
        ["Photoacoustic Laser + Ultrasound Hybrid", "Real-Time Micro-MRI Triangulation", "CT Angiography Fusion"]
    )

with col2:
    st.write("### Target Vascular Parameters")
    if st.button("🔍 SCAN & TRIANGULATE CLOT"):
        with st.spinner("Analyzing micro-vascular pathways..."):
            time.sleep(1.5)
            st.success("Target Clot Locked Successfully!")
            st.metric("Clot Coordinates (X, Y, Z)", "12.4mm, -4.2mm, 8.1mm")
            st.metric("Vessel Diameter", "180 µm (Micro-Capillary Zone)")
            st.metric("Estimated Swarm Size Required", "250,000 Nano-Bots")

st.divider()

# --- OPERATOR & STEERING CONTROLS ---
st.sidebar.header("🕹️ Operator & Steering Controls")
focus_level = st.sidebar.slider("Brain Focus Level (%)", 0, 100, 75)
steering_angle = st.sidebar.slider("Steering Path Angle (°)", -90, 90, 0)
injection_status = st.sidebar.button("🚀 INITIATE AUTONOMOUS INJECTION & STEERING")

# Magnetic Coils Control Panel
st.sidebar.subheader("🧲 Helmet Coil Intensity (mT)")
coil_1 = st.sidebar.slider("Coil 1 (North)", 0, 100, 40)
coil_2 = st.sidebar.slider("Coil 2 (East)", 0, 100, 80 if steering_angle > 0 else 20)
coil_3 = st.sidebar.slider("Coil 3 (South)", 0, 100, 10)
coil_4 = st.sidebar.slider("Coil 4 (West)", 0, 100, 80 if steering_angle < 0 else 20)

# --- VISUALIZATION PANELS ---
v_col1, v_col2 = st.columns(2)

# PANEL 1: EEG Signal Graph
with v_col1:
    st.subheader("🧠 Live EEG Signal Monitoring")
    time_series = np.linspace(0, 2, 200)
    alpha_wave = np.sin(2 * np.pi * 10 * time_series) * (focus_level / 100)
    beta_wave = np.sin(2 * np.pi * 20 * time_series) * (1 - focus_level / 100)
    combined_eeg = alpha_wave + beta_wave + np.random.normal(0, 0.1, 200)

    fig_eeg = go.Figure()
    fig_eeg.add_trace(go.Scatter(y=combined_eeg, mode='lines', name='EEG Signal', line=dict(color='#00FFCC')))
    fig_eeg.update_layout(
        title="Real-Time Brain Intent (Alpha/Beta Waves)",
        xaxis_title="Time",
        yaxis_title="Amplitude (uV)",
        template="plotly_dark",
        height=350
    )
    st.plotly_chart(fig_eeg, use_container_width=True)

# PANEL 2: Blood Vessel Simulation
with v_col2:
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

    fig_vessel.update_layout(
        title=f"Magnetic Path Angle: {steering_angle}° | Target Status: {'TARGETING CLOT 🎯' if injection_status else 'READY'}",
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[-3, 3]),
        template="plotly_dark",
        height=350
    )
    st.plotly_chart(fig_vessel, use_container_width=True)

# System Status Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Target Focus", f"{focus_level}%")
m2.metric("Active Field Strength", f"{max(coil_1, coil_2, coil_3, coil_4)} mT")
m3.metric("Clot Disruption Efficiency", f"{int(focus_level * 0.95)}%")
m4.metric("Nanoparticle Delivery", "ACTIVE" if injection_status else "STANDBY")
