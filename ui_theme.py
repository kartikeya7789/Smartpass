import streamlit as st

def apply_enterprise_theme(role):

    color = {
        "student": "#22d3ee",
        "warden": "#facc15",
        "security": "#ef4444"
    }.get(role, "#22d3ee")

    st.markdown(f"""
    <style>

    .stApp {{
        background: radial-gradient(circle at top,#020617,#020617);
        color:white;
    }}

    section[data-testid="stSidebar"] {{
        background:#020617;
    }}

    .card {{
        background: rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.1);
        border-radius:20px;
        padding:20px;
        margin-bottom:20px;
    }}

    .glow {{
        border:1px solid {color};
        box-shadow:0 0 20px {color};
    }}

    .stButton>button {{
        background: linear-gradient(90deg,{color},#6366f1);
        border-radius:12px;
        color:white;
    }}

    .main .block-container {{
        padding-top:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }}

    </style>
    """, unsafe_allow_html=True)
