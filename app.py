import streamlit as st
from auth import login_or_register
from pages.student import student_dashboard
from pages.warden import warden_dashboard
from pages.security import security_dashboard
from ui_theme import apply_enterprise_theme

st.set_page_config(page_title="SmartPass Enterprise", layout="wide")

if "user" not in st.session_state:
    st.session_state.user=None


# LOGIN
if st.session_state.user is None:

    apply_enterprise_theme("student")

    st.title("🎫 SmartPass Enterprise")

    name=st.text_input("Full Name")
    email=st.text_input("NITJ Email")
    password=st.text_input("Password",type="password")

    if st.button("Continue"):
        user,msg=login_or_register(name,email,password)

        if user:
            st.session_state.user=user
            st.success(msg)
            st.rerun()
        else:
            st.error(msg)

# DASHBOARD
else:

    user=st.session_state.user
    apply_enterprise_theme(user["role"])

    st.sidebar.write(f"👤 {user['username']}")
    st.sidebar.write(f"🔐 {user['role']}")

    if user["role"]=="student":
        menu=st.sidebar.radio("Menu",
        ["Dashboard","Apply Leave","My SmartPass","History"])

    elif user["role"]=="warden":
        menu=st.sidebar.radio("Menu",
        ["Pending Requests","Approved Leaves","Analytics"])

    elif user["role"]=="security":
        menu=st.sidebar.radio("Menu",
        ["Scan Pass","Active Passes","Logs"])

    if st.sidebar.button("Logout"):
        st.session_state.user=None
        st.rerun()

    if user["role"]=="student":
        student_dashboard(user,menu)

    elif user["role"]=="warden":
        warden_dashboard(menu)

    elif user["role"]=="security":
        security_dashboard(menu)
