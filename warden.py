import streamlit as st
from database import SessionLocal
from models import Leave

def warden_dashboard(menu):

    db = SessionLocal()
    leaves = db.query(Leave).all()

    if menu == "Pending Requests":
        pending = db.query(Leave).filter_by(status="pending").all()

        for l in pending:
            st.markdown('<div class="card glow">', unsafe_allow_html=True)
            st.write(l.student, l.reason)

            if st.button("Approve", key=f"a{l.id}"):
                l.status = "approved"
                db.commit()
                st.rerun()

            if st.button("Reject", key=f"r{l.id}"):
                l.status = "rejected"
                db.commit()
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    elif menu == "Approved Leaves":
        approved = db.query(Leave).filter_by(status="approved").all()
        for l in approved:
            st.success(l.student)

    elif menu == "Analytics":
        total = len(leaves)
        approved = len([l for l in leaves if l.status == "approved"])
        pending = len([l for l in leaves if l.status == "pending"])

        st.bar_chart({
            "Approved":[approved],
            "Pending":[pending]
        })
