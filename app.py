import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="NEURO-STEER AI", page_icon="🧠", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.title("🧠 NEURO-STEER AI — Digital Twin & 3D Micro-Vascular Steering Platform")
st.caption("Painless & Non-Invasive Targeted Nano-Swarm Navigation for Brain Stroke Intervention")

st.divider()

# --- SECTION 1: DIAGNOSTICS & SCANNING ---
st.header("📋 Patient Diagnostic & 3D Clot Triangulation")

col1, col2 = st.columns(2)

with col1:
    patient_id = st.text_input("Patient ID", "HACK-2026-NEURO-01")
    protocol = st.selectbox(
        "Scanning Protocol",
        ["Photoacoustic Laser + Ultrasound Hybrid", "Real-Time Micro-MRI Triangulation", "CT Angiography Fusion"]
    )

with col2:
    st.write("### Target Vascular Parameters")
    if st.button("🔍 SCAN & TRIANGULATE 3D CLOT"):
        with st.spinner("Processing 3D micro-vascular point cloud..."):
            time.sleep(1.2)
            st.success("Target Clot Locked Successfully!")
            c1, c2, c3 = st.columns(3)
            c1.metric("Coordinates (X,Y,Z)", "12.4, -4.2, 8.1 mm")
            c2.metric("Vessel Radius", "180 µm")
            c3.metric("Required Swarm", "250,000 Bots")

st.divider()

# --- SIDEBAR: OPERATOR & AI CONTROLS ---
st.sidebar.header("🕹️ Operator & System Controls")

# Mode Switch
ai_mode = st.sidebar.toggle("🤖 Enable AI Autonomous Steering Mode", value=False)

if ai_mode:
    st.sidebar.info("AI Pathfinding Active: Auto-calculating optimal magnetic vectors.")
    focus_level = 88
    steering_angle = 15
else:
    focus_level = st.sidebar.slider("Brain Focus Level (%)", 0, 100, 75)
    steering_angle = st.sidebar.slider("Steering Path Angle (°)", -90, 90, 0)

injection_status = st.sidebar.button("🚀 INITIATE NANO-SWARM NAVIGATION")

# Helmet Coils Control
st.sidebar.subheader("🧲 Helmet Coil Intensity (mT)")
coil_1 = st.sidebar.slider("Coil 1 (North)", 0, 100, 45 if ai_mode else 40)
coil_2 = st.sidebar.slider("Coil 2 (East)", 0, 100, 85 if ai_mode or steering_angle > 0 else 20)
coil_3 = st.sidebar.slider("Coil 3 (South)", 0, 100, 15 if ai_mode else 10)
coil_4 = st.sidebar.slider("Coil 4 (West)", 0, 100, 85 if ai_mode or steering_angle < 0 else 20)

# --- SECTION 2: 3D SIMULATION PANELS ---
v_col1, v_col2 = st.columns(2)

# PANEL 1: 3D Brain Wave Signal Surface / Line
with v_col1:
    st.subheader("🧠 Live BCI Brain Signal Waveform")
    time_series = np.linspace(0, 2, 200)
    alpha_wave = np.sin(2 * np.pi * 10 * time_series) * (focus_level / 100)
    beta_wave = np.sin(2 * np.pi * 20 * time_series) * (1 - focus_level / 100)
    eeg_signal = alpha_wave + beta_wave + np.random.normal(0, 0.08, 200)

    fig_eeg = go.Figure()
    fig_eeg.add_trace(go.Scatter(y=eeg_signal, mode='lines', name='Live Signal', line=dict(color='#00FFCC', width=2)))
    fig_eeg.update_layout(
        title=f"BCI Focus Signal ({focus_level}%)",
        xaxis_title="Time Frame",
        yaxis_title="Amplitude (µV)",
        template="plotly_dark",
        height=380
    )
    st.plotly_chart(fig_eeg, use_container_width=True)

# PANEL 2: True 3D Blood Vessel & Nanoparticle Swarm Visualizer
with v_col2:
    st.subheader("🩸 3D Vascular Nanoparticle Swarm Visualizer")

    # 3D Cylinder / Vessel Geometry
    z_vessel = np.linspace(0, 10, 30)
    theta = np.linspace(0, 2 * np.pi, 20)
    theta_grid, z_grid = np.meshgrid(theta, z_vessel)
    r = 2.0  # Vessel radius
    x_vessel = r * np.cos(theta_grid)
    y_vessel = r * np.sin(theta_grid)

    fig_3d = go.Figure()

    # Render Vessel Mesh Wall
    fig_3d.add_trace(go.Surface(
        x=x_vessel, y=y_vessel, z=z_grid,
        opacity=0.15,
        colorscale='Reds',
        showscale=False,
        name='Vessel Wall'
    ))

    # Render 3D Blood Clot (Thrombus Target)
    fig_3d.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[8.5],
        mode='markers',
        marker=dict(size=18, color='darkred', symbol='diamond'),
        name='Blood Clot Target'
    ))

    # Render 3D Nanoparticle Swarm Positions
    num_particles = 40
    if injection_status:
        np_z = np.linspace(0.5, 8.0, num_particles)
        np_x = (steering_angle / 90.0) * 1.2 + np.random.normal(0, 0.25, num_particles)
        np_y = np.random.normal(0, 0.25, num_particles)
    else:
        np_z = np.full(num_particles, 0.5)
        np_x = np.random.normal(0, 0.2, num_particles)
        np_y = np.random.normal(0, 0.2, num_particles)

    fig_3d.add_trace(go.Scatter3d(
        x=np_x, y=np_y, z=np_z,
        mode='markers',
        marker=dict(size=6, color='gold', symbol='circle'),
        name='Nanoparticle Swarm'
    ))

    fig_3d.update_layout(
        title=f"3D Path Angle: {steering_angle}° | Mode: {'AI AUTONOMOUS 🤖' if ai_mode else 'MANUAL 🕹️'}",
        scene=dict(
            xaxis=dict(range=[-3, 3], title='X (mm)'),
            yaxis=dict(range=[-3, 3], title='Y (mm)'),
            zaxis=dict(range=[0, 10], title='Vessel Length (mm)'),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=2)
        ),
        template="plotly_dark",
        height=380
    )
    st.plotly_chart(fig_3d, use_container_width=True)

st.divider()

# --- SECTION 3: SAFETY MONITORING & CLINICAL REPORT ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Intracranial Pressure (ICP)", "11.2 mmHg", delta="Normal", delta_color="normal")
m2.metric("Peak Field Strength", f"{max(coil_1, coil_2, coil_3, coil_4)} mT")
m3.metric("Wall Shear Stress Risk", "LOW (0.12 Pa)", delta="Safe", delta_color="normal")
m4.metric("Clot Disruption Efficiency", f"{int(focus_level * 0.96)}%")

st.subheader("📑 Surgical Summary & Report")
if st.button("📄 GENERATE SURGICAL SUMMARY REPORT"):
    st.write("---")
    st.success("✅ Procedure Summary Generated!")
    st.json({
        "Patient ID": patient_id,
        "Target Location": "Middle Cerebral Artery (MCA) Branch 2",
        "Mode Used": "AI Autonomous Steering" if ai_mode else "Manual BCI Steering",
        "Average Focus Score": f"{focus_level}%",
        "Peak Magnetic Field": f"{max(coil_1, coil_2, coil_3, coil_4)} mT",
        "Clot Clearance Status": "98.7% Target Clearance Achieved",
        "Safety Check": "No vessel shear stress threshold breached."
    })
