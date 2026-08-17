import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="NEURO-STEER AI Dashboard", layout="wide", page_icon="🧠")

st.title("🧠 NEURO-STEER AI : Dual-Mode Clinical Intervention Platform")
st.caption("Photoacoustic-Guided & BCI Closed-Loop Magnetic Swarm Steering for Ischemic Stroke")

# Sidebar Controls
st.sidebar.header("🕹️ Operator & Telemetry Panel")
patient_id = st.sidebar.selectbox("Select Patient Profile", ["PAT-2026-MCA-01 (Acute)", "PAT-2026-ACA-04 (Distal)"])
laser_toggle = st.sidebar.toggle("Activate 808nm NIR Pulsed Laser", value=True)
bci_focus = st.sidebar.slider("Operator Cognitive Focus (EEG Beta/Alpha Ratio %)", 0, 100, 78)
auto_pilot = st.sidebar.checkbox("Enable AI Co-Pilot Shared Autonomy", value=True)

# Gating Logic
if bci_focus >= 70:
    control_status = "🟢 MANUAL BCI ACTIVE"
    status_color = "success"
    steering_authority = "Operator Direct Control"
else:
    if auto_pilot:
        control_status = "🟡 AI CO-PILOT ENGAGED (Fatigue Fallback)"
        status_color = "warning"
        steering_authority = "Reinforcement Learning Autonomous Agent"
    else:
        control_status = "🔴 STANDBY (Focus Below Threshold)"
        status_color = "error"
        steering_authority = "Thrusters Locked"

st.sidebar.markdown(f"**Current State:** :{status_color}[{control_status}]")
st.sidebar.caption(f"Authority: {steering_authority}")

# Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Acoustic Target Depth", "32.4 mm", "±0.2 mm")
col2.metric("Targeting Efficiency", f"{min(92.4, 60 + (bci_focus*0.32)):.1f}%", "+4.2%")
clot_dissolution = min(100, int((bci_focus / 100) * 88))
col3.metric("Clot Dissolution Rate", f"{clot_dissolution}%", "Active" if laser_toggle else "Paused")
col4.metric("Off-Target Exposure Risk", "< 12%", "-68% vs Systemic")

st.divider()

# Main Layout: 3D Twin & Diagnostic Waves
left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.subheader("🌐 3D Vascular Digital Twin (Target Bifurcation)")
    
    # Generate Synthetic 3D Vessel Geometry
    z_main = np.linspace(0, 10, 40)
    x_main = np.zeros_like(z_main)
    y_main = np.zeros_like(z_main)

    z_branch = np.linspace(10, 18, 30)
    x_branch = (z_branch - 10) * 0.5
    y_branch = (z_branch - 10) * 0.2

    # Particle Swarm Positioning based on focus
    t_factor = bci_focus / 100.0
    px = np.random.normal(x_branch[-1] * t_factor, 0.4, 60)
    py = np.random.normal(y_branch[-1] * t_factor, 0.4, 60)
    pz = np.random.normal(10 + (8 * t_factor), 0.5, 60)

    fig_3d = go.Figure()
    
    # Parent Vessel
    fig_3d.add_trace(go.Scatter3d(x=x_main, y=y_main, z=z_main, mode='lines',
                                 line=dict(color='crimson', width=12), name='Main MCA Vessel'))
    # Occluded Branch
    fig_3d.add_trace(go.Scatter3d(x=x_branch, y=y_branch, z=z_branch, mode='lines',
                                 line=dict(color='darkred', width=8), name='Occluded Branch'))
    # Clot Location
    fig_3d.add_trace(go.Scatter3d(x=[x_branch[-1]], y=[y_branch[-1]], z=[z_branch[-1]], mode='markers',
                                 marker=dict(size=14, color='purple', opacity=0.8), name='Thrombus (Clot)'))
    # Ferrofluid Swarm
    fig_3d.add_trace(go.Scatter3d(x=px, y=py, z=pz, mode='markers',
                                 marker=dict(size=4, color='cyan', opacity=0.9), name='SPION Swarm'))

    fig_3d.update_layout(scene=dict(xaxis_title='X (mm)', yaxis_title='Y (mm)', zaxis_title='Z (Depth mm)',
                                    bgcolor='#0E1117'),
                         margin=dict(l=0, r=0, b=0, t=0), height=420, template="plotly_dark")
    st.plotly_chart(fig_3d, use_container_width=True)

with right_col:
    st.subheader("📡 Photoacoustic & Coil Telemetry")
    
    # Photoacoustic Response Waveform
    time_pts = np.linspace(0, 20, 200)
    acoustic_wave = np.exp(-(time_pts - 8)**2 / 2) * np.sin(4 * np.pi * time_pts) if laser_toggle else np.random.normal(0, 0.05, 200)
    
    fig_pa = go.Figure()
    fig_pa.add_trace(go.Scatter(x=time_pts, y=acoustic_wave, mode='lines', line=dict(color='#00D2FF', width=2), name="808nm Acoustic Pulse"))
    fig_pa.update_layout(title="Transducer Time-of-Flight Acoustic Waveform", xaxis_title="Time (μs)", yaxis_title="Amplitude (mV)",
                         height=210, margin=dict(l=20, r=20, t=30, b=20), template="plotly_dark")
    st.plotly_chart(fig_pa, use_container_width=True)

    # Coil Vector Actuation Progress
    st.markdown("**Electromagnetic Coil Array Duty Cycle (PWM)**")
    c1, c2 = st.columns(2)
    c1.progress(int(bci_focus * 0.9), text=f"Coil 1 (Anterior): {int(bci_focus*0.9)}%")
    c1.progress(int(bci_focus * 0.75), text=f"Coil 2 (Posterior): {int(bci_focus*0.75)}%")
    c2.progress(int(bci_focus * 0.6), text=f"Coil 3 (Lateral Left): {int(bci_focus*0.6)}%")
    c2.progress(int(bci_focus * 0.85), text=f"Coil 4 (Lateral Right): {int(bci_focus*0.85)}%")

st.success("System operational: Dual-mode bio-telemetry synchronized with digital twin.")
    
