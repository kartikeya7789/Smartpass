import streamlit as st
from database import SessionLocal
from models import Leave

def security_dashboard(menu):

    db = SessionLocal()

    if menu == "Scan Pass":
        st.markdown('<div class="card glow"><h2>📷 Live SmartPass Scanner</h2></div>', unsafe_allow_html=True)

        img = st.camera_input("Scan QR Gatepass")

        if img:
            st.success("QR Captured ✔️ (Demo Mode)")

    elif menu == "Active Passes":
        approved = db.query(Leave).filter_by(status="approved").all()
        for l in approved:
            st.success(l.student)

    elif menu == "Logs":
        st.info("Enterprise logs coming soon")
