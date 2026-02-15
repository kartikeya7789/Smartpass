import streamlit as st
from database import SessionLocal
from models import Leave
from qr_utils import generate_qr
import os


def student_dashboard(user, menu):

    db = SessionLocal()
    my = db.query(Leave).filter_by(student=user["username"]).all()

    st.markdown(f"""
    <div class="card glow">
        <h2>👋 Welcome, {user["username"]}</h2>
        <p style="color:#94a3b8;">SmartPass Elite Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    # ================= DASHBOARD =================
    if menu == "Dashboard":

        approved = len([l for l in my if l.status == "approved"])
        pending = len([l for l in my if l.status == "pending"])
        rejected = len([l for l in my if l.status == "rejected"])

        c1, c2, c3 = st.columns(3)

        c1.markdown(f'<div class="stat">✅ Approved<h2>{approved}</h2></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="stat">⏳ Pending<h2>{pending}</h2></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="stat">❌ Rejected<h2>{rejected}</h2></div>', unsafe_allow_html=True)

    # ================= APPLY LEAVE =================
    elif menu == "Apply Leave":

        reason = st.text_input("Leave Reason")

        if st.button("🎫 Generate SmartPass Request"):
            new = Leave(
                student=user["username"],
                reason=reason,
                status="pending"
            )
            db.add(new)
            db.commit()
            st.success("Request Sent 🚀")
            st.rerun()

    # ================= SMARTPASS =================
    elif menu == "My SmartPass":

        approved_leaves = [l for l in my if l.status == "approved"]

        if approved_leaves:

            latest = approved_leaves[-1]
            file = f"qr_{latest.id}.png"

            # ⭐ NEW REAL QR GENERATION
            if not os.path.exists(file):
                generate_qr(
                    latest.id,
                    latest.student,
                    latest.reason,
                    file
                )

            st.markdown(f"""
            <div class="card glow">
                <h3>🎫 DIGITAL SMARTPASS</h3>
                <p><b>Name:</b> {latest.student}</p>
                <p><b>Reason:</b> {latest.reason}</p>
                <p style="color:#22c55e;"><b>Status:</b> ACTIVE</p>
            </div>
            """, unsafe_allow_html=True)

            st.image(file, width=260)

        else:
            st.info("No Active SmartPass")

    # ================= HISTORY =================
    elif menu == "History":

        if not my:
            st.info("No history yet.")
        else:
            for l in reversed(my):

                col1, col2 = st.columns([3,1])

                col1.markdown(f'<div class="card">📌 {l.reason}</div>', unsafe_allow_html=True)

                if l.status == "approved":
                    col2.success("APPROVED")
                elif l.status == "rejected":
                    col2.error("REJECTED")
                else:
                    col2.warning("PENDING")

