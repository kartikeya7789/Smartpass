import streamlit as st
from database import SessionLocal
from models import Leave
from qr_utils import generate_qr
import os

def student_dashboard(user, menu):

    db = SessionLocal()
    my = db.query(Leave).filter_by(student=user["username"]).all()

    if menu == "Dashboard":
        st.markdown('<div class="card glow"><h2>🎓 Student Control Center</h2></div>', unsafe_allow_html=True)

    elif menu == "Apply Leave":
        st.markdown('<div class="card glow">', unsafe_allow_html=True)

        reason = st.text_input("Reason")
        if st.button("Generate SmartPass"):
            new = Leave(student=user["username"], reason=reason, status="pending")
            db.add(new)
            db.commit()
            st.success("Request Sent 🚀")
            st.snow()
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    elif menu == "My SmartPass":

        approved = [l for l in my if l.status == "approved"]

        if approved:
            latest = approved[-1]
            file = f"qr_{latest.id}.png"

            if not os.path.exists(file):
                generate_qr(f"{latest.student}-{latest.reason}", file)

            st.markdown('<div class="card glow">', unsafe_allow_html=True)
            st.subheader("🎫 LIVE SMARTPASS ID")
            st.image(file, width=250)
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.info("No Active SmartPass")

    elif menu == "History":
        for l in my:
            st.write(l.reason, l.status)
