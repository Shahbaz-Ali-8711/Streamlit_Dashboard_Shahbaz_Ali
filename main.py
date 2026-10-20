"""
================================================================================
  CYAN.GLASS ANALYTICS | WARM IVORY, EMERALD GREEN & VERMILION PALETTE
================================================================================
  Color System:
  - Tone 1: Warm Ivory (#FBF8F2, #FAF6EE, #F5EFE0)
  - Tone 2: Emerald Green (#043A2B, #065F46, #047857, #10B981)
  - Tone 3: Vermilion (#E34234, #FF4633, #C83224)
  
  Features:
  - Dual Aesthetic Engine:
      1. Warm Ivory Editorial Canvas (Default Luxury Light)
      2. Emerald Velvet Studio (Executive Dark)
  - Non-wrapping, Tabular Numerics for All Currencies, Metrics & Percentages
  - Overridden Streamlit Components (Vermilion/Emerald Sliders & Chips, Glass Tabs)
  - 5 Full-Featured Visualization & Telemetry Labs
================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & METADATA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Heritage Analytics | Ivory, Emerald & Vermilion",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. SIDEBAR THEME SWITCHER & CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 11px; margin-bottom: 4px;">
            <div style="background: linear-gradient(135deg, #FAF6EE 0%, #E34234 50%, #065F46 100%); width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; box-shadow: 0 4px 14px rgba(227,66,52,0.35);">🌿</div>
            <div>
                <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 1.15rem; color: #FAF6EE; letter-spacing: -0.02em;">VERDANT & CO.</div>
                <div style="font-size: 0.68rem; color: #E34234; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;">Ivory • Emerald • Vermilion</div>
            </div>
        </div>
        <p style="font-size: 0.76rem; color: #a3b8af; margin-top: 6px; margin-bottom: 18px; line-height: 1.4;">
            Reactive telemetry studio tailored in warm ivory, rich emerald green, and fiery vermilion.
        </p>
    """, unsafe_allow_html=True)

    theme_mode = st.selectbox(
        "🎨 Aesthetic Canvas",
        options=["✨ Warm Ivory Canvas (Editorial)", "🌿 Emerald Velvet (Executive Dark)"],
        index=0,
    )
    is_dark = "Dark" in theme_mode

    st.markdown("##### 🎛️ Simulation Parameters")
    preset_scenario = st.selectbox(
        "Market Growth Trajectory",
        options=["✨ Steady Progress", "🚀 High-Growth Wave", "⚡ Weekend Spikes", "📉 Volatile Market"],
        index=0,
    )

    col_side1, col_side2 = st.columns(2)
    with col_side1:
        time_horizon = st.slider("Window (Days)", 14, 180, 60, step=7)
    with col_side2:
        variance_factor = st.slider("Fluctuation", 0.2, 2.5, 0.9, step=0.1)

    all_categories = ["Cloud & SaaS", "Hardware", "Cybersecurity", "AI Workstations"]
    selected_cats = st.multiselect(
        "Segment Filtering",
        options=all_categories,
        default=all_categories,
    )

    st.markdown("---")
    st.markdown("##### 🧠 Reactive State Telemetry")

    if "session_runs" not in st.session_state:
        st.session_state.session_runs = 0
    if "last_action" not in st.session_state:
        st.session_state.last_action = "App Launched"
    if "bookmarked_records" not in st.session_state:
        st.session_state.bookmarked_records = []

    st.session_state.session_runs += 1

    st.markdown(f"""
        <div style="background: rgba(250, 246, 238, 0.08); border: 1px solid rgba(227, 66, 52, 0.35); border-top: 1.5px solid #FAF6EE; border-radius: 12px; padding: 12px 14px; font-size: 0.8rem; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
            <div style="color: #FAF6EE; font-weight: 600; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Top-to-Bottom Executions:</div>
            <div style="font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 1.35rem; color: #FAF6EE; text-shadow: 0 0 10px rgba(227,66,52,0.4);">#{st.session_state.session_runs}</div>
            <div style="color: #a3b8af; font-size: 0.72rem; margin-top: 4px;">Trigger: <span style="color: #E34234; font-weight: 700;">{st.session_state.last_action}</span></div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🔄 Reset HUD", use_container_width=True):
            st.session_state.session_runs = 1
            st.session_state.last_action = "HUD Wiped"
            st.session_state.bookmarked_records = []
            st.rerun()

    with col_btn2:
        if st.button("⚡ Ping State", use_container_width=True):
            st.session_state.last_action = f"Pinged @ {datetime.now().strftime('%H:%M:%S')}"
            st.rerun()


# -----------------------------------------------------------------------------
# 3. DYNAMIC CSS DESIGN SYSTEM (Warm Ivory, Emerald Green, Vermilion)
# -----------------------------------------------------------------------------
if not is_dark:
    # WARM IVORY EDITORIAL LIGHT
    APP_BG = "radial-gradient(circle at 8% 10%, rgba(227, 66, 52, 0.06) 0%, transparent 40%), radial-gradient(circle at 92% 15%, rgba(6, 95, 70, 0.08) 0%, transparent 45%), #FAF6EE"
    TEXT_COLOR = "#08261d"
    HERO_BG = "linear-gradient(135deg, #053325 0%, #032017 100%)"
    HERO_TITLE = "linear-gradient(135deg, #FAF6EE 20%, #F5EFE0 60%, #E34234 100%)"
    HERO_SUBTITLE = "#d5e2dc"
    CARD_BG = "linear-gradient(145deg, rgba(255, 255, 255, 0.95) 0%, rgba(250, 246, 238, 0.98) 100%)"
    CARD_BORDER = "1px solid rgba(6, 78, 59, 0.15)"
    CARD_BORDER_TOP = "2px solid #065F46"
    CARD_SHADOW = "0 8px 24px -4px rgba(4, 58, 43, 0.08)"
    CARD_TITLE_COLOR = "#4a675e"
    KPI_NUM_COLOR = "#043A2B"
    KPI_BADGE_EMERALD_BG = "rgba(6, 95, 70, 0.12)"
    KPI_BADGE_EMERALD_COLOR = "#047857"
    KPI_BADGE_VERMILION_BG = "rgba(227, 66, 52, 0.12)"
    KPI_BADGE_VERMILION_COLOR = "#C83224"
    TAB_BG = "rgba(240, 234, 222, 0.85)"
    TAB_ACTIVE_BG = "linear-gradient(135deg, #053325 0%, #04261C 100%)"
    TAB_ACTIVE_COLOR = "#FAF6EE"
    FLOW_BG = "linear-gradient(135deg, #FFFFFF 0%, #FAF6EE 100%)"
    FLOW_BORDER = "1px solid rgba(6, 78, 59, 0.18)"
    FLOW_TEXT = "#08261d"
    FLOW_DESC = "#4a675e"
else:
    # EMERALD VELVET EXECUTIVE DARK
    APP_BG = "radial-gradient(circle at 10% 8%, rgba(227, 66, 52, 0.1) 0%, transparent 40%), radial-gradient(circle at 90% 15%, rgba(250, 246, 238, 0.06) 0%, transparent 35%), #031710"
    TEXT_COLOR = "#FAF6EE"
    HERO_BG = "linear-gradient(135deg, rgba(6, 58, 43, 0.8) 0%, rgba(3, 23, 16, 0.9) 100%)"
    HERO_TITLE = "linear-gradient(135deg, #FAF6EE 20%, #F5EFE0 60%, #FF4633 100%)"
    HERO_SUBTITLE = "#a3b8af"
    CARD_BG = "linear-gradient(145deg, rgba(7, 44, 33, 0.75) 0%, rgba(3, 24, 17, 0.85) 100%)"
    CARD_BORDER = "1px solid rgba(250, 246, 238, 0.12)"
    CARD_BORDER_TOP = "1.5px solid #FAF6EE"
    CARD_SHADOW = "0 10px 30px -6px rgba(0, 0, 0, 0.6)"
    CARD_TITLE_COLOR = "#a3b8af"
    KPI_NUM_COLOR = "#FAF6EE"
    KPI_BADGE_EMERALD_BG = "rgba(16, 185, 129, 0.15)"
    KPI_BADGE_EMERALD_COLOR = "#10B981"
    KPI_BADGE_VERMILION_BG = "rgba(227, 66, 52, 0.2)"
    KPI_BADGE_VERMILION_COLOR = "#FF6B57"
    TAB_BG = "rgba(6, 44, 33, 0.7)"
    TAB_ACTIVE_BG = "linear-gradient(135deg, rgba(227, 66, 52, 0.3) 0%, rgba(250, 246, 238, 0.15) 100%)"
    TAB_ACTIVE_COLOR = "#FAF6EE"
    FLOW_BG = "linear-gradient(135deg, rgba(7, 44, 33, 0.7) 0%, rgba(3, 24, 17, 0.8) 100%)"
    FLOW_BORDER = "1px solid rgba(250, 246, 238, 0.15)"
    FLOW_TEXT = "#FAF6EE"
    FLOW_DESC = "#a3b8af"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    code, pre, .stCode {{
        font-family: 'JetBrains Mono', monospace !important;
    }}

    /* Global Canvas Styling */
    .stApp {{
        background: {APP_BG} !important;
        color: {TEXT_COLOR} !important;
    }}

    /* Top Hero Banner */
    .hero-banner {{
        background: {HERO_BG};
        backdrop-filter: blur(24px) saturate(190%);
        -webkit-backdrop-filter: blur(24px) saturate(190%);
        border: 1px solid rgba(250, 246, 238, 0.2);
        border-top: 2px solid #E34234;
        border-radius: 20px;
        padding: 28px 32px;
        margin-bottom: 24px;
        box-shadow: 0 16px 40px -10px rgba(4, 58, 43, 0.35);
        position: relative;
        overflow: hidden;
    }}

    .hero-banner::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, #FAF6EE 0%, #E34234 40%, #065F46 80%, #FAF6EE 100%);
    }}

    .badge-pill-heritage {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background: rgba(227, 66, 52, 0.18);
        border: 1px solid #E34234;
        color: #FAF6EE;
        margin-bottom: 12px;
    }}

    .hero-title {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 2.15rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: {HERO_TITLE};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 8px 0;
    }}

    .hero-subtitle {{
        color: {HERO_SUBTITLE};
        font-size: 0.95rem;
        margin: 0;
        line-height: 1.55;
        max-width: 820px;
    }}

    /* KPI Cards (High Legibility, Tabular Figures, Single Line) */
    .kpi-card {{
        background: {CARD_BG};
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: {CARD_BORDER};
        border-top: {CARD_BORDER_TOP};
        border-radius: 18px;
        padding: 20px 22px;
        min-height: 142px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: {CARD_SHADOW};
    }}

    .kpi-card:hover {{
        transform: translateY(-3px);
        border-color: #E34234;
        box-shadow: 0 14px 30px -6px rgba(227, 66, 52, 0.25);
    }}

    .kpi-title {{
        font-size: 0.76rem;
        font-weight: 700;
        color: {CARD_TITLE_COLOR};
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    .kpi-value {{
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif !important;
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: {KPI_NUM_COLOR} !important;
        letter-spacing: -0.03em !important;
        font-variant-numeric: tabular-nums !important;
        font-feature-settings: "tnum" !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        margin-bottom: 8px !important;
        line-height: 1.15 !important;
    }}

    .kpi-badge-emerald {{
        display: inline-flex;
        align-items: center;
        gap: 5px;
        font-size: 0.74rem;
        font-weight: 700;
        color: {KPI_BADGE_EMERALD_COLOR};
        background: {KPI_BADGE_EMERALD_BG};
        border: 1px solid {KPI_BADGE_EMERALD_COLOR};
        padding: 3px 9px;
        border-radius: 6px;
        width: fit-content;
        white-space: nowrap;
    }}

    .kpi-badge-vermilion {{
        display: inline-flex;
        align-items: center;
        gap: 5px;
        font-size: 0.74rem;
        font-weight: 700;
        color: {KPI_BADGE_VERMILION_COLOR};
        background: {KPI_BADGE_VERMILION_BG};
        border: 1px solid {KPI_BADGE_VERMILION_COLOR};
        padding: 3px 9px;
        border-radius: 6px;
        width: fit-content;
        white-space: nowrap;
    }}

    /* Workflow Cards */
    .flow-card {{
        background: {FLOW_BG};
        border: {FLOW_BORDER};
        border-top: 2px solid #065F46;
        border-radius: 14px;
        padding: 18px 18px;
        height: 100%;
        transition: all 0.25s ease;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    }}

    .flow-card:hover {{
        border-color: #E34234;
        border-top-color: #E34234;
        transform: translateY(-2px);
    }}

    .flow-num {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        border-radius: 50%;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 12px;
        font-weight: 800;
        background: linear-gradient(135deg, #E34234 0%, #065F46 100%);
        color: #FAF6EE;
        box-shadow: 0 2px 8px rgba(227, 66, 52, 0.4);
        margin-bottom: 10px;
    }}

    .flow-title {{
        font-weight: 700;
        font-size: 0.92rem;
        color: {FLOW_TEXT};
    }}

    .flow-desc {{
        color: {FLOW_DESC};
        font-size: 0.78rem;
        margin-top: 6px;
        line-height: 1.4;
    }}

    /* Custom Heritage Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background: {TAB_BG};
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(6, 78, 59, 0.15);
        margin-bottom: 22px;
    }}

    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px;
        color: {CARD_TITLE_COLOR};
        font-weight: 600;
        font-size: 0.9rem;
        padding: 8px 18px;
        transition: all 0.2s ease;
        border: 1px solid transparent !important;
        background: transparent !important;
    }}

    .stTabs [aria-selected="true"] {{
        background: {TAB_ACTIVE_BG} !important;
        color: {TAB_ACTIVE_COLOR} !important;
        border: 1px solid #E34234 !important;
        box-shadow: 0 4px 14px rgba(227, 66, 52, 0.2) !important;
        font-weight: 700 !important;
    }}

    /* Sidebar Background & Component Polish */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #04261C 0%, #021711 100%) !important;
        border-right: 1px solid rgba(250, 246, 238, 0.12);
        box-shadow: 8px 0 30px rgba(0, 0, 0, 0.4);
    }}

    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label {{
        color: #FAF6EE !important;
    }}

    /* Multiselect Tag Overrides in Emerald & Warm Ivory */
    .stMultiSelect [data-baseweb="tag"] {{
        background: rgba(6, 95, 70, 0.4) !important;
        border: 1px solid #10B981 !important;
        color: #FAF6EE !important;
        border-radius: 6px !important;
    }}
    .stMultiSelect [data-baseweb="tag"] span {{
        color: #FAF6EE !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
    }}
    .stMultiSelect [data-baseweb="tag"] [role="presentation"] svg {{
        fill: #FAF6EE !important;
    }}

    /* Sliders in Vermilion and Emerald */
    .stSlider [data-baseweb="slider"] [role="slider"] {{
        background-color: #E34234 !important;
        border: 2px solid #FAF6EE !important;
        box-shadow: 0 0 10px rgba(227, 66, 52, 0.7) !important;
    }}
    .stSlider div[data-testid="stSliderTickBar"] {{
        background-color: rgba(250, 246, 238, 0.15) !important;
    }}
    .stSlider [data-baseweb="slider"] div[class*="StyledTrack"] {{
        background: rgba(250, 246, 238, 0.15) !important;
    }}
    .stSlider [data-baseweb="slider"] div[class*="StyledTrack"] > div {{
        background: linear-gradient(90deg, #065F46, #E34234) !important;
    }}

    /* Buttons in Vermilion and Warm Ivory */
    .stButton>button {{
        border-radius: 10px;
        font-weight: 700;
        font-size: 0.88rem;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid #E34234;
        border-top: 1.2px solid #FAF6EE;
        background: linear-gradient(135deg, #E34234 0%, #C83224 100%);
        color: #FAF6EE;
        box-shadow: 0 4px 14px rgba(227, 66, 52, 0.3);
        padding: 8px 16px;
    }}

    .stButton>button:hover {{
        border-color: #FAF6EE;
        box-shadow: 0 6px 20px rgba(227, 66, 52, 0.5);
        transform: translateY(-1.5px);
        color: #FAF6EE;
        background: linear-gradient(135deg, #FF4633 0%, #E34234 100%);
    }}

    /* Download Buttons in Emerald */
    .stDownloadButton>button {{
        border-radius: 10px;
        font-weight: 700;
        border: 1px solid #065F46;
        border-top: 1.2px solid #FAF6EE;
        background: linear-gradient(135deg, #065F46 0%, #043A2B 100%);
        color: #FAF6EE;
        box-shadow: 0 4px 16px rgba(4, 58, 43, 0.25);
        transition: all 0.2s ease;
    }}
    .stDownloadButton>button:hover {{
        border-color: #E34234;
        box-shadow: 0 6px 22px rgba(227, 66, 52, 0.35);
        transform: translateY(-1.5px);
        color: #FAF6EE;
    }}

    .section-header {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: {TEXT_COLOR};
        letter-spacing: -0.01em;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .section-desc {{
        color: {CARD_TITLE_COLOR};
        font-size: 0.86rem;
        margin-bottom: 16px;
    }}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 4. HIGH-PERFORMANCE CACHED DATA PIPELINE
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def generate_master_dataset(days: int, noise: float, scenario: str, seed: int = 42):
    """
    Demonstrates Streamlit caching: Only recomputes when inputs change.
    """
    np.random.seed(seed)
    base_date = datetime.now() - timedelta(days=days)
    dates = [base_date + timedelta(days=i) for i in range(days)]

    if scenario == "🚀 High-Growth Wave":
        trend = np.linspace(40, 240, days) ** 1.15
    elif scenario == "⚡ Weekend Spikes":
        trend = np.linspace(70, 160, days)
        weekend_boost = np.array([32 if d.weekday() >= 5 else 0 for d in dates])
        trend += weekend_boost
    elif scenario == "📉 Volatile Market":
        trend = 110 + np.sin(np.linspace(0, 10, days)) * 48
        noise = noise * 1.9
    else:  # ✨ Steady Progress
        trend = np.linspace(70, 175, days)

    noise_arr = np.random.normal(0, noise * 12, days)
    revenue = np.maximum(30.0, trend + noise_arr)
    orders = (revenue * np.random.uniform(1.3, 1.9, days) + np.random.normal(0, 4, days)).astype(int)
    profit = revenue * np.random.uniform(0.28, 0.52, days)
    conversion_rate = np.clip(np.random.normal(3.5, 0.55, days), 0.8, 8.5)

    categories = np.random.choice(["Cloud & SaaS", "Hardware", "Cybersecurity", "AI Workstations"], size=days)
    regions = np.random.choice(["North America", "EMEA", "Asia-Pacific", "Latin America"], size=days)
    device = np.random.choice(["Desktop", "Mobile", "Tablet"], size=days, p=[0.55, 0.35, 0.10])

    df = pd.DataFrame({
        "Date": dates,
        "Revenue": np.round(revenue * 100, 2),
        "Orders": np.maximum(1, orders),
        "Profit": np.round(profit * 100, 2),
        "ConversionRate": np.round(conversion_rate, 2),
        "Category": categories,
        "Region": regions,
        "Device": device,
    })
    return df


# -----------------------------------------------------------------------------
# 5. DATA INVOCATION
# -----------------------------------------------------------------------------
start_compute = time.perf_counter()
raw_data = generate_master_dataset(
    days=time_horizon,
    noise=variance_factor,
    scenario=preset_scenario,
)

if selected_cats:
    active_df = raw_data[raw_data["Category"].isin(selected_cats)].copy()
else:
    active_df = raw_data.copy()

compute_time_ms = (time.perf_counter() - start_compute) * 1000


# -----------------------------------------------------------------------------
# 6. HERITAGE HERO BANNER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="badge-pill-heritage">🌿 Warm Ivory • Emerald Green • Vermilion</div>
    <h1 class="hero-title">Verdant Reactive Analytics Studio</h1>
    <p class="hero-subtitle">
        Executive telemetry dashboard curated with a classic luxury color harmony: Warm Ivory silk canvas, 
        authoritative Emerald Green structures, and fiery Vermilion callouts. Engineered with pure top-to-bottom reactivity.
    </p>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 7. HIGH-LEGIBILITY GLOSSY KPI CARDS (Tabular, Non-wrapping Figures)
# -----------------------------------------------------------------------------
total_rev = active_df["Revenue"].sum()
total_prof = active_df["Profit"].sum()
total_ord = active_df["Orders"].sum()
avg_conv = active_df["ConversionRate"].mean()
margin_pct = (total_prof / total_rev * 100) if total_rev else 0.0

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">
            <span>Gross Revenue</span>
            <span style="font-size: 13px;">💳</span>
        </div>
        <div class="kpi-value">${total_rev:,.0f}</div>
        <div class="kpi-badge-emerald">▲ {len(active_df)} Active Records</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">
            <span>Net Operating Profit</span>
            <span style="font-size: 13px;">📈</span>
        </div>
        <div class="kpi-value">${total_prof:,.0f}</div>
        <div class="kpi-badge-vermilion">● {margin_pct:.1f}% Net Return Margin</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">
            <span>Executed Orders</span>
            <span style="font-size: 13px;">📦</span>
        </div>
        <div class="kpi-value">{total_ord:,}</div>
        <div class="kpi-badge-emerald">◈ ${(total_rev / total_ord):,.1f} Mean Ticket</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">
            <span>Conversion Ratio</span>
            <span style="font-size: 13px;">⚡</span>
        </div>
        <div class="kpi-value">{avg_conv:.2f}%</div>
        <div class="kpi-badge-vermilion">⏱ {compute_time_ms:.1f}ms Cache Speed</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")


# -----------------------------------------------------------------------------
# 8. VISUALIZATION TABS (5 DEDICATED STUDIOS)
# -----------------------------------------------------------------------------
tab_native, tab_plotly, tab_seaborn, tab_architecture, tab_data = st.tabs([
    "📈 Native Glass Charts",
    "✨ Plotly Interactive Lab",
    "🎨 Seaborn & Matplotlib Studio",
    "⚙️ Reactive Architecture",
    "📋 Interactive Data Engine",
])


# =============================================================================
# TAB 1: NATIVE STREAMLIT CHARTS (Emerald Green & Vermilion)
# =============================================================================
with tab_native:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <div class="section-header">📈 Native Streamlit Visualization Engine</div>
            <div class="section-desc">
                High-performance Vega vector graphs rendered with Emerald Green revenue streams and Vermilion profit margins.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_nat1, col_nat2 = st.columns(2)

    with col_nat1:
        st.markdown("##### 1. Revenue & Profit Trajectory (`st.line_chart`)")
        timeline_df = active_df.groupby("Date")[["Revenue", "Profit"]].sum()
        st.line_chart(
            timeline_df,
            color=["#065F46", "#E34234"],
            use_container_width=True,
        )

    with col_nat2:
        st.markdown("##### 2. Order Frequency Area Fill (`st.area_chart`)")
        area_df = active_df.groupby("Date")["Orders"].sum()
        st.area_chart(
            area_df,
            color=["#047857"],
            use_container_width=True,
        )

    col_nat3, col_nat4 = st.columns([1.35, 1])

    with col_nat3:
        st.markdown("##### 3. Product Segment Revenue vs Profit (`st.bar_chart`)")
        category_bar = active_df.groupby("Category")[["Revenue", "Profit"]].sum()
        st.bar_chart(
            category_bar,
            color=["#065F46", "#E34234"],
            use_container_width=True,
        )

    with col_nat4:
        st.markdown("##### 4. Orders vs Conversion Rate (`st.scatter_chart`)")
        st.scatter_chart(
            active_df,
            x="Orders",
            y="ConversionRate",
            color="Category",
            size="Revenue",
            use_container_width=True,
        )


# =============================================================================
# TAB 2: PLOTLY INTERACTIVE LAB (Ivory, Emerald, Vermilion)
# =============================================================================
with tab_plotly:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <div class="section-header">✨ Plotly Interactive Visual Lab</div>
            <div class="section-desc">
                Client-side GPU charts rendered in Warm Ivory, Royal Emerald Green, and Vermilion tones.
            </div>
        </div>
    """, unsafe_allow_html=True)

    plot_col1, plot_col2 = st.columns(2)

    HERITAGE_PALETTE = ["#065F46", "#E34234", "#10B981", "#FF6B57", "#043A2B"]
    plotly_paper = "rgba(0,0,0,0)"
    plotly_plot = "rgba(6, 95, 70, 0.04)" if not is_dark else "rgba(250, 246, 238, 0.02)"
    font_color = "#08261d" if not is_dark else "#FAF6EE"
    grid_color = "rgba(6, 95, 70, 0.1)" if not is_dark else "rgba(250, 246, 238, 0.1)"

    with plot_col1:
        # Multi-dimensional Bubble Chart
        fig_bubble = px.scatter(
            active_df,
            x="Orders",
            y="Revenue",
            size="Profit",
            color="Category",
            hover_name="Category",
            hover_data={"Region": True, "Date": "|%B %d, %Y", "ConversionRate": ":.2f%"},
            color_discrete_sequence=HERITAGE_PALETTE,
            title="Portfolio Map (Bubble Size = Net Profit)",
            template="plotly_dark" if is_dark else "plotly_white",
        )
        fig_bubble.update_layout(
            paper_bgcolor=plotly_paper,
            plot_bgcolor=plotly_plot,
            font=dict(family="Plus Jakarta Sans", color=font_color),
            title_font=dict(family="Plus Jakarta Sans", size=14, color=font_color),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=20, r=20, t=50, b=20),
            xaxis=dict(gridcolor=grid_color),
            yaxis=dict(gridcolor=grid_color),
        )
        fig_bubble.update_traces(
            marker=dict(line=dict(width=1.2, color="#FAF6EE")),
        )
        st.plotly_chart(fig_bubble, use_container_width=True)

    with plot_col2:
        # Donut Chart
        region_df = active_df.groupby("Region", as_index=False)["Revenue"].sum()
        fig_donut = px.pie(
            region_df,
            names="Region",
            values="Revenue",
            hole=0.58,
            color_discrete_sequence=["#065F46", "#E34234", "#10B981", "#C83224"],
            title="Geographic Revenue Allocation",
            template="plotly_dark" if is_dark else "plotly_white",
        )
        fig_donut.update_traces(
            textposition="inside",
            textinfo="percent+label",
            marker=dict(line=dict(color="#FAF6EE", width=2)),
            pull=[0.04, 0, 0, 0],
        )
        fig_donut.update_layout(
            paper_bgcolor=plotly_paper,
            plot_bgcolor=plotly_paper,
            font=dict(family="Plus Jakarta Sans", color=font_color),
            title_font=dict(family="Plus Jakarta Sans", size=14, color=font_color),
            margin=dict(l=20, r=20, t=50, b=20),
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    # Full-Width Interactive Dual-Axis Line / Bar Chart
    st.markdown("##### 🚀 Dual-Axis Telemetry: Orders Intensity & Gross Revenue Stream")
    daily_roll = active_df.groupby("Date").agg({"Revenue": "sum", "Orders": "sum"}).reset_index()

    fig_dual = go.Figure()
    fig_dual.add_trace(go.Bar(
        x=daily_roll["Date"],
        y=daily_roll["Orders"],
        name="Orders Count",
        marker_color="rgba(6, 95, 70, 0.45)",
        marker_line=dict(color="#065F46", width=1),
        yaxis="y2",
    ))
    fig_dual.add_trace(go.Scatter(
        x=daily_roll["Date"],
        y=daily_roll["Revenue"],
        name="Gross Revenue ($)",
        mode="lines+markers",
        line=dict(color="#E34234", width=3, shape="spline"),
        marker=dict(size=6, color="#E34234", line=dict(color="#FAF6EE", width=1.5)),
        yaxis="y",
    ))

    fig_dual.update_layout(
        template="plotly_dark" if is_dark else "plotly_white",
        paper_bgcolor=plotly_paper,
        plot_bgcolor=plotly_plot,
        font=dict(family="Plus Jakarta Sans", color=font_color),
        yaxis=dict(
            title=dict(text="Gross Revenue ($)", font=dict(color="#E34234", size=12)),
            tickfont=dict(color="#E34234"),
            gridcolor=grid_color,
        ),
        yaxis2=dict(
            title=dict(text="Orders Transacted", font=dict(color="#065F46", size=12)),
            tickfont=dict(color="#065F46"),
            overlaying="y",
            side="right",
            gridcolor=grid_color,
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode="x unified",
    )
    st.plotly_chart(fig_dual, use_container_width=True)


# =============================================================================
# TAB 3: SEABORN & MATPLOTLIB SUITE (Ivory, Emerald, Vermilion)
# =============================================================================
with tab_seaborn:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <div class="section-header">🎨 Scientific & Statistical Visualizations</div>
            <div class="section-desc">
                High-definition Seaborn statistical outputs customized with Warm Ivory surfaces, Emerald density, and Vermilion spreads.
            </div>
        </div>
    """, unsafe_allow_html=True)

    fig_face = "#FAF6EE" if not is_dark else "#042017"
    axes_face = "#FFFFFF" if not is_dark else "#062b20"
    edge_color = "#E5DFD3" if not is_dark else "#0a4533"
    text_c = "#08261d" if not is_dark else "#FAF6EE"

    plt.rcParams.update({
        "figure.facecolor": fig_face,
        "axes.facecolor": axes_face,
        "axes.edgecolor": edge_color,
        "axes.labelcolor": text_c,
        "text.color": text_c,
        "xtick.color": text_c,
        "ytick.color": text_c,
        "grid.color": edge_color,
        "grid.alpha": 0.6,
        "font.sans-serif": "DejaVu Sans",
    })

    mat_col1, mat_col2 = st.columns(2)

    with mat_col1:
        st.markdown("##### 1. Revenue Density Distribution (`sns.histplot`)")
        fig_kde, ax_kde = plt.subplots(figsize=(7, 4.2))
        sns.histplot(
            active_df["Revenue"],
            kde=True,
            ax=ax_kde,
            color="#065F46",
            edgecolor=fig_face,
            line_kws={"linewidth": 2.5, "color": "#E34234"},
        )
        ax_kde.set_title("Revenue Probability Density Curve", fontsize=11, fontweight="bold", pad=12, color=text_c)
        ax_kde.set_xlabel("Revenue ($)", color=text_c)
        ax_kde.set_ylabel("Frequency", color=text_c)
        plt.tight_layout()
        st.pyplot(fig_kde)
        plt.close(fig_kde)

    with mat_col2:
        st.markdown("##### 2. Profit Dispersal by Category (`sns.boxplot`)")
        fig_box, ax_box = plt.subplots(figsize=(7, 4.2))
        sns.boxplot(
            data=active_df,
            x="Category",
            y="Profit",
            hue="Category",
            legend=False,
            ax=ax_box,
            palette=["#065F46", "#E34234", "#10B981", "#FF6B57"],
            linewidth=1.3,
        )
        ax_box.set_title("Profit Spread & Outliers", fontsize=11, fontweight="bold", pad=12, color=text_c)
        ax_box.set_xlabel("")
        ax_box.set_ylabel("Profit ($)", color=text_c)
        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()
        st.pyplot(fig_box)
        plt.close(fig_box)

    mat_col3, mat_col4 = st.columns(2)

    # Custom Ivory -> Emerald -> Vermilion Colormap
    heritage_cmap = mcolors.LinearSegmentedColormap.from_list(
        "heritage_cmap",
        ["#FAF6EE", "#065F46", "#E34234"],
    )

    with mat_col3:
        st.markdown("##### 3. Pearson Correlation Matrix (`sns.heatmap`)")
        corr_matrix = active_df[["Revenue", "Orders", "Profit", "ConversionRate"]].corr()
        fig_heat, ax_heat = plt.subplots(figsize=(7, 3.8))
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap=heritage_cmap,
            cbar=True,
            ax=ax_heat,
            linewidths=1.2,
            linecolor=fig_face,
            square=True,
            annot_kws={"color": "#031710", "weight": "bold"},
        )
        ax_heat.set_title("Metric Covariance Matrix", fontsize=11, fontweight="bold", pad=12, color=text_c)
        plt.tight_layout()
        st.pyplot(fig_heat)
        plt.close(fig_heat)

    with mat_col4:
        st.markdown("##### 4. Orders Intensity: Category vs Device Matrix")
        pivot_table = active_df.pivot_table(index="Category", columns="Device", values="Orders", aggfunc="sum")
        fig_piv, ax_piv = plt.subplots(figsize=(7, 3.8))
        sns.heatmap(
            pivot_table,
            annot=True,
            fmt="d",
            cmap=heritage_cmap,
            ax=ax_piv,
            linewidths=1.2,
            linecolor=fig_face,
            annot_kws={"color": "#031710", "weight": "bold"},
        )
        ax_piv.set_title("Total Volume Intensity Matrix", fontsize=11, fontweight="bold", pad=12, color=text_c)
        plt.tight_layout()
        st.pyplot(fig_piv)
        plt.close(fig_piv)


# =============================================================================
# TAB 4: STREAMLIT REACTIVE ARCHITECTURE DEEP DIVE
# =============================================================================
with tab_architecture:
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <div class="section-header">⚙️ Streamlit Unidirectional Reactive Architecture</div>
            <div class="section-desc">
                Streamlit eliminates complex boilerplate, state reducers, and manual DOM listeners.
                Every interaction triggers an ultra-fast, pure <strong>Top-to-Bottom Execution</strong> supported by caching and session state.
            </div>
        </div>
    """, unsafe_allow_html=True)

    w1, w2, w3, w4, w5 = st.columns(5)

    with w1:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">1</span>
            <div class="flow-title">User Event</div>
            <p class="flow-desc">
                User drags a slider, toggles a multiselect, or clicks a button.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w2:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">2</span>
            <div class="flow-title">Script Rerun</div>
            <p class="flow-desc">
                Python re-evaluates <code>main.py</code> linearly from line 1 to the end.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w3:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">3</span>
            <div class="flow-title">Cache Check</div>
            <p class="flow-desc">
                <code>@st.cache_data</code> skips compute if inputs did not change.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w4:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">4</span>
            <div class="flow-title">State Inject</div>
            <p class="flow-desc">
                <code>st.session_state</code> restores persistent variables across full reruns.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w5:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">5</span>
            <div class="flow-title">DOM Diffing</div>
            <p class="flow-desc">
                Streamlit's React client updates only the mutated elements via WebSockets.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("---")

    st.markdown("##### 🧪 Real-Time Caching Benchmark Experiment")
    st.caption("Inspect the exact execution delta between an uncached computation vs a memoized computation.")

    @st.cache_data
    def cached_heavy_calculation(n: int):
        time.sleep(0.7)
        return [i ** 2 for i in range(n)]

    def uncached_heavy_calculation(n: int):
        time.sleep(0.7)
        return [i ** 2 for i in range(n)]

    exp_col1, exp_col2 = st.columns(2)

    with exp_col1:
        if st.button("🚀 Run With @st.cache_data", use_container_width=True):
            t0 = time.perf_counter()
            res = cached_heavy_calculation(10000)
            elapsed = (time.perf_counter() - t0) * 1000
            st.success(f"Cached Computation Finished in: **{elapsed:.2f} ms**")
            st.caption("First run takes ~700ms. Subsequent runs take < 1ms!")

    with exp_col2:
        if st.button("⚠️ Run Without Caching", use_container_width=True):
            t0 = time.perf_counter()
            res = uncached_heavy_calculation(10000)
            elapsed = (time.perf_counter() - t0) * 1000
            st.warning(f"Uncached Computation Finished in: **{elapsed:.2f} ms**")
            st.caption("Every single click takes full 700ms penalty.")

    st.markdown("---")

    st.markdown("##### 📝 In-Memory Session State Note-Taker")
    st.caption("Hypotheses recorded here persist indefinitely across all slider adjustments, filter changes, and tab navigations.")

    note_col1, note_col2 = st.columns([3, 1])
    with note_col1:
        user_note = st.text_input("Enter telemetry note or hypothesis", placeholder="e.g. Q4 Cloud SaaS expansion shows 34% margin uplift")
    with note_col2:
        st.write("")
        st.write("")
        if st.button("📌 Pin Note", use_container_width=True):
            if user_note.strip():
                st.session_state.bookmarked_records.append({
                    "Timestamp": datetime.now().strftime("%H:%M:%S"),
                    "Note": user_note.strip(),
                    "RevenueAtCapture": f"${total_rev:,.0f}",
                })
                st.session_state.last_action = f"Pinned: '{user_note.strip()[:14]}...'"
                st.rerun()

    if st.session_state.bookmarked_records:
        st.markdown("**Your Active Session Bookmarks:**")
        st.dataframe(pd.DataFrame(st.session_state.bookmarked_records), use_container_width=True)
    else:
        st.info("No bookmarks saved yet. Type a note above and click Pin Note.")


# =============================================================================
# TAB 5: INTERACTIVE DATA ENGINE
# =============================================================================
with tab_data:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <div class="section-header">📋 Interactive Data Grid & Export Hub</div>
            <div class="section-desc">
                Inspect raw telemetry records, sort by critical dimensions, and export ready-to-use artifacts in CSV and JSON formats.
            </div>
        </div>
    """, unsafe_allow_html=True)

    search_col1, search_col2 = st.columns([2, 1])
    with search_col1:
        search_query = st.text_input("🔍 Quick Search by Segment or Region", placeholder="e.g. EMEA or AI Workstations")
    with search_col2:
        sort_by = st.selectbox("Sort Telemetry By", ["Revenue", "Profit", "Orders", "Date"], index=0)

    display_df = active_df.copy()
    if search_query:
        display_df = display_df[
            display_df["Category"].str.contains(search_query, case=False, na=False) |
            display_df["Region"].str.contains(search_query, case=False, na=False)
        ]

    display_df = display_df.sort_values(by=sort_by, ascending=False)

    st.dataframe(
        display_df,
        use_container_width=True,
        column_config={
            "Date": st.column_config.DateColumn("Date", format="YYYY-MM-DD"),
            "Revenue": st.column_config.NumberColumn("Revenue ($)", format="$%.2f"),
            "Profit": st.column_config.NumberColumn("Profit ($)", format="$%.2f"),
            "Orders": st.column_config.ProgressColumn(
                "Orders Volume",
                format="%d",
                min_value=0,
                max_value=int(active_df["Orders"].max()),
            ),
            "ConversionRate": st.column_config.NumberColumn("Conversion", format="%.2f%%"),
            "Category": st.column_config.TextColumn("Product Segment"),
            "Region": st.column_config.TextColumn("Market Region"),
            "Device": st.column_config.TextColumn("Primary Device"),
        },
    )

    st.markdown("##### 📥 Data Export Suite")
    exp_btn1, exp_btn2 = st.columns(2)

    with exp_btn1:
        csv_data = display_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📄 Export Filtered Dataset (CSV)",
            data=csv_data,
            file_name=f"verdant_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with exp_btn2:
        json_data = display_df.to_json(orient="records", date_format="iso").encode("utf-8")
        st.download_button(
            label="⚡ Export Filtered Dataset (JSON)",
            data=json_data,
            file_name=f"verdant_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True,
        )


# -----------------------------------------------------------------------------
# 9. FOOTER
# -----------------------------------------------------------------------------
st.markdown(f"""
<div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid rgba(6, 78, 59, 0.15); text-align: center; color: {CARD_TITLE_COLOR}; font-size: 0.8rem;">
    <span style="color: {TEXT_COLOR}; font-weight: 700;">Verdant & Co. Analytics</span> • Tailored in Warm Ivory, Royal Emerald Green & Vermilion • Built with Streamlit, Plotly & Seaborn
</div>
""", unsafe_allow_html=True)
