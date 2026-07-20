import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="NEURO-STEER AI",
    page_icon="🧠",
    layout="wide"
)

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
    if st.button("📡 SCAN & TRIANGULATE CLOT"):
        with st.spinner("Analyzing micro-vascular pathways..."):
            time.sleep(1.5)
            st.success("Target Clot Locked Successfully!")
            st.metric("Clot Coordinates (X, Y, Z)", "12.4mm, -4.2mm, 8.1mm")
            st.metric("Vessel Diameter", "180 µm (Micro-Capillary Zone)")
            st.metric("Estimated Swarm Size Required", "250,000 Nano-Bots")

st.divider()

# Autonomous Steering Control Section
st.header("🚀 Live Swarm Auto-Pilot & Vessel Safety Monitor")

if st.button("▶ INITIATE AUTONOMOUS INJECTION & STEERING", type="primary"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    alert_box = st.empty()
    
    stages = [
        (10, "Injecting Magneto-Plasmonic Swarm into Femoral Artery..."),
        (35, "Navigating Swarm via Dynamic External Magnetic Field..."),
        (60, "Approaching Bifurcation: Redirecting Field Gradient..."),
        (75, "⚠️ CRITICAL CAPILLARY DETECTED: Scaling magnetic force down to prevent vessel wall puncture!"),
        (90, "Swarm Anchored at Clot Site. Activating Localized Thrombolysis..."),
        (100, "Clot Dissolved Successfully! Safety Integrity 100%.")
    ]
    
    for prog, msg in stages:
        time.sleep(1.2)
        progress_bar.progress(prog)
        status_text.subheader(f"Status: {msg}")
        
        if prog == 75:
            alert_box.error("⚠️ Vessel Protection Alert: Micro-capillary shear stress limit reached. Autonomous Auto-Tuning Engaged.")
        elif prog == 100:
            alert_box.success("✅ Procedure Completed Safely with Zero Extravasation Risk!")
            st.balloons()

st.sidebar.title("🎮 Manual Override Controls")
st.sidebar.slider("Magnetic Field Strength (Tesla)", 0.0, 3.0, 1.2)
st.sidebar.slider("Swarm Velocity (mm/s)", 0.0, 10.0, 2.5)
st.sidebar.selectbox("Safety Limit Mode", ["Strict Autonomous Shielding", "Semi-Auto Emergency Hold"])
