"""
================================================================================
  ULTRA-MODERN STREAMLIT WORKFLOW & VISUALIZATION DASHBOARD
================================================================================
  Architecture & Concept:
  1. Reactive Top-to-Bottom Execution Model
  2. Performance Caching (@st.cache_data)
  3. Persistent State Management (st.session_state)
  4. Multi-Engine Charting (Streamlit Native, Plotly Interactive, Seaborn/Matplotlib)
  5. Glassmorphic Design System with Tailored CSS Micro-Interactions
================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & METADATA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Streamlit Flow | Next-Gen Analytics",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. ULTRA-MODERN CSS DESIGN SYSTEM (Glassmorphism, Neon Accents, Typography)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Global Typography & Background */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    code, pre, .stCode {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Gradient Background Aura */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 90% 80%, rgba(236, 72, 153, 0.08) 0%, transparent 40%),
                    #0b0f19;
        color: #f1f5f9;
    }

    /* Top Glass Navbar / Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 28px 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        position: relative;
        overflow: hidden;
    }
    
    .hero-banner::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899, #06b6d4);
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.4);
        color: #818cf8;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 8px 0;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1rem;
        margin: 0;
        line-height: 1.5;
        max-width: 800px;
    }

    /* Glass KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.015) 100%);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px 22px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }

    .kpi-card:hover {
        transform: translateY(-4px);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 12px 25px -8px rgba(99, 102, 241, 0.25);
    }

    .kpi-title {
        font-size: 0.82rem;
        font-weight: 600;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.02em;
        margin-bottom: 6px;
    }

    .kpi-delta-positive {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        font-size: 0.78rem;
        font-weight: 600;
        color: #34d399;
        background: rgba(52, 211, 153, 0.12);
        padding: 3px 8px;
        border-radius: 6px;
    }

    .kpi-delta-neutral {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        font-size: 0.78rem;
        font-weight: 600;
        color: #818cf8;
        background: rgba(129, 140, 248, 0.12);
        padding: 3px 8px;
        border-radius: 6px;
    }

    /* Interactive Workflow Architecture Step Cards */
    .flow-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 16px 18px;
        height: 100%;
        transition: border-color 0.2s;
    }
    .flow-card:hover {
        border-color: rgba(99, 102, 241, 0.5);
    }
    .flow-num {
        display: inline-block;
        width: 24px;
        height: 24px;
        line-height: 24px;
        text-align: center;
        border-radius: 50%;
        font-size: 12px;
        font-weight: 700;
        background: #6366f1;
        color: white;
        margin-bottom: 8px;
    }

    /* Tab Custom Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.03);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        color: #94a3b8;
        font-weight: 600;
        padding: 8px 18px;
        transition: all 0.2s ease;
        border: none !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.3) 0%, rgba(168, 85, 247, 0.3) 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(168, 85, 247, 0.5) !important;
    }

    /* Sidebar Polishing */
    section[data-testid="stSidebar"] {
        background-color: #080c14;
        border-right: 1px solid rgba(255, 255, 255, 0.07);
    }
    
    /* Buttons Customization */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s;
        border: 1px solid rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
        color: #e2e8f0;
    }
    .stButton>button:hover {
        border-color: #6366f1;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        transform: translateY(-1px);
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. HIGH-PERFORMANCE CACHING DATA GENERATOR
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def generate_master_dataset(days: int, noise: float, scenario: str, seed: int = 42):
    """
    Demonstrates Streamlit caching: Only recomputes when inputs (days, noise, scenario) change.
    """
    np.random.seed(seed)
    base_date = datetime.now() - timedelta(days=days)
    dates = [base_date + timedelta(days=i) for i in range(days)]

    # Scenario Modifiers
    multiplier = 1.0
    if scenario == "🚀 High-Growth Wave":
        trend = np.linspace(30, 220, days) ** 1.15
    elif scenario == "⚡ Weekend Spikes":
        trend = np.linspace(60, 140, days)
        weekend_boost = np.array([25 if d.weekday() >= 5 else 0 for d in dates])
        trend += weekend_boost
    elif scenario == "📉 Volatile Market":
        trend = 100 + np.sin(np.linspace(0, 10, days)) * 40
        noise = noise * 1.8
    else:  # Steady Progress
        trend = np.linspace(60, 160, days)

    noise_arr = np.random.normal(0, noise * 12, days)
    revenue = np.maximum(25.0, trend + noise_arr)
    orders = (revenue * np.random.uniform(1.2, 1.8, days) + np.random.normal(0, 5, days)).astype(int)
    profit = revenue * np.random.uniform(0.24, 0.48, days)
    conversion_rate = np.clip(np.random.normal(3.2, 0.6, days), 0.5, 7.5)

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
# 4. SIDEBAR: REACTIVE CONTROLS & STATE ENGINE
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
            <div style="background: linear-gradient(135deg, #6366f1, #ec4899); width: 34px; height: 34px; border-radius: 9px; display: flex; align-items: center; justify-content: center; font-size: 18px;">⚡</div>
            <div style="font-weight: 800; font-size: 1.15rem; color: #fff; letter-spacing: -0.02em;">Streamlit Hub</div>
        </div>
        <p style="font-size: 0.8rem; color: #64748b; margin-top: 0; margin-bottom: 20px;">
            Reactive Parameter Studio
        </p>
    """, unsafe_allow_html=True)

    st.markdown("##### 🎛️ Simulation Parameters")
    preset_scenario = st.selectbox(
        "Market Scenario",
        options=["✨ Steady Progress", "🚀 High-Growth Wave", "⚡ Weekend Spikes", "📉 Volatile Market"],
        index=0,
    )

    col_side1, col_side2 = st.columns(2)
    with col_side1:
        time_horizon = st.slider("Horizon (Days)", 14, 180, 60, step=7)
    with col_side2:
        variance_factor = st.slider("Volatility", 0.2, 2.5, 0.9, step=0.1)

    all_categories = ["Cloud & SaaS", "Hardware", "Cybersecurity", "AI Workstations"]
    selected_cats = st.multiselect(
        "Filter Product Segments",
        options=all_categories,
        default=all_categories,
    )

    st.markdown("---")
    st.markdown("##### 🧠 Session State Tracker")

    # Initialize session state variables if they do not exist
    if "session_runs" not in st.session_state:
        st.session_state.session_runs = 0
    if "last_action" not in st.session_state:
        st.session_state.last_action = "App Initialized"
    if "bookmarked_records" not in st.session_state:
        st.session_state.bookmarked_records = []

    st.session_state.session_runs += 1

    st.markdown(f"""
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 12px; font-size: 0.82rem;">
            <div style="color: #94a3b8; margin-bottom: 4px;">Top-to-Bottom Executions:</div>
            <div style="font-family: 'JetBrains Mono'; font-weight: 700; font-size: 1.1rem; color: #818cf8;">#{st.session_state.session_runs}</div>
            <div style="color: #64748b; font-size: 0.72rem; margin-top: 4px;">Last trigger: <span style="color: #cbd5e1;">{st.session_state.last_action}</span></div>
        </div>
    """, unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🔄 Reset State", use_container_width=True):
            st.session_state.session_runs = 1
            st.session_state.last_action = "State Cleared"
            st.session_state.bookmarked_records = []
            st.rerun()

    with col_btn2:
        if st.button("⚡ Ping State", use_container_width=True):
            st.session_state.last_action = f"Pinged @ {datetime.now().strftime('%H:%M:%S')}"
            st.rerun()


# -----------------------------------------------------------------------------
# 5. DATA PIPELINE & PERFORMANCE PROFILING
# -----------------------------------------------------------------------------
start_compute = time.perf_counter()
raw_data = generate_master_dataset(
    days=time_horizon,
    noise=variance_factor,
    scenario=preset_scenario,
)

# Apply reactive category filter
if selected_cats:
    active_df = raw_data[raw_data["Category"].isin(selected_cats)].copy()
else:
    active_df = raw_data.copy()

compute_time_ms = (time.perf_counter() - start_compute) * 1000


# -----------------------------------------------------------------------------
# 6. HERO HEADER & WORKFLOW EXPLAINER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="badge-pill">⚡ Streamlit Reactive Architecture</div>
    <h1 class="hero-title">Next-Gen Streamlit Workflow & Charts</h1>
    <p class="hero-subtitle">
        Explore how Streamlit's unidirectional execution lifecycle unifies state management, performance caching,
        and multiple visualization engines into a single reactive application.
    </p>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 7. METRIC CARDS (GLASSMORPHIC DESIGN)
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
        <div class="kpi-title">Gross Revenue</div>
        <div class="kpi-value">${total_rev:,.0f}</div>
        <div class="kpi-delta-positive">▲ {len(active_df)} Active Data Points</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Net Profit</div>
        <div class="kpi-value">${total_prof:,.0f}</div>
        <div class="kpi-delta-positive">● {margin_pct:.1f}% Avg Net Margin</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Orders</div>
        <div class="kpi-value">{total_ord:,}</div>
        <div class="kpi-delta-neutral">◈ ${(total_rev / total_ord):,.1f} Avg Basket</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Conversion</div>
        <div class="kpi-value">{avg_conv:.2f}%</div>
        <div class="kpi-delta-neutral">⏱ {compute_time_ms:.1f}ms cached retrieval</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")


# -----------------------------------------------------------------------------
# 8. VISUALIZATION TABS (THE CORE ENGINES)
# -----------------------------------------------------------------------------
tab_native, tab_plotly, tab_seaborn, tab_architecture, tab_data = st.tabs([
    "📈 Native Streamlit Charts",
    "✨ Plotly Interactive Studio",
    "🎨 Seaborn & Matplotlib Dark",
    "⚙️ Streamlit Architecture Deep Dive",
    "📋 Interactive Data Engine",
])


# =============================================================================
# TAB 1: NATIVE STREAMLIT CHARTS
# =============================================================================
with tab_native:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <h3 style="margin-bottom: 4px; font-weight: 700;">Native Streamlit Visualization Engine</h3>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Powered by Altair and Vega-Lite underneath. Highly optimized, responsive, and renders seamlessly with zero setup.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_nat1, col_nat2 = st.columns(2)

    with col_nat1:
        st.markdown("##### 1. Multi-Series Revenue & Profit Timeline (`st.line_chart`)")
        timeline_df = active_df.groupby("Date")[["Revenue", "Profit"]].sum()
        st.line_chart(
            timeline_df,
            color=["#6366f1", "#10b981"],
            use_container_width=True,
        )

    with col_nat2:
        st.markdown("##### 2. Order Volume Density (`st.area_chart`)")
        area_df = active_df.groupby("Date")["Orders"].sum()
        st.area_chart(
            area_df,
            color=["#a855f7"],
            use_container_width=True,
        )

    col_nat3, col_nat4 = st.columns([1.4, 1])

    with col_nat3:
        st.markdown("##### 3. Category Performance Comparison (`st.bar_chart`)")
        category_bar = active_df.groupby("Category")[["Revenue", "Profit"]].sum()
        st.bar_chart(
            category_bar,
            color=["#38bdf8", "#f43f5e"],
            use_container_width=True,
        )

    with col_nat4:
        st.markdown("##### 4. Order Volume vs Conversion (`st.scatter_chart`)")
        st.scatter_chart(
            active_df,
            x="Orders",
            y="ConversionRate",
            color="Category",
            size="Revenue",
            use_container_width=True,
        )


# =============================================================================
# TAB 2: PLOTLY INTERACTIVE CHARTS
# =============================================================================
with tab_plotly:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <h3 style="margin-bottom: 4px; font-weight: 700;">Plotly Interactive Visual Lab</h3>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Full client-side interactivity: panning, zooming, custom HTML tooltips, and dynamic categorical clustering.
            </p>
        </div>
    """, unsafe_allow_html=True)

    plot_col1, plot_col2 = st.columns(2)

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
            color_discrete_sequence=["#818cf8", "#f472b6", "#38bdf8", "#34d399"],
            title="Multi-Dimensional Portfolio Map (Size = Profit)",
            template="plotly_dark",
        )
        fig_bubble.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,0.02)",
            font=dict(family="Plus Jakarta Sans", color="#cbd5e1"),
            title_font=dict(size=14, color="#f1f5f9"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=20, r=20, t=50, b=20),
        )
        st.plotly_chart(fig_bubble, use_container_width=True)

    with plot_col2:
        # Donut Chart with Neon Aesthetics
        region_df = active_df.groupby("Region", as_index=False)["Revenue"].sum()
        fig_donut = px.pie(
            region_df,
            names="Region",
            values="Revenue",
            hole=0.55,
            color_discrete_sequence=["#6366f1", "#ec4899", "#06b6d4", "#f59e0b"],
            title="Geographic Revenue Allocation",
            template="plotly_dark",
        )
        fig_donut.update_traces(
            textposition="inside",
            textinfo="percent+label",
            marker=dict(line=dict(color="#0b0f19", width=2)),
        )
        fig_donut.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Plus Jakarta Sans", color="#cbd5e1"),
            title_font=dict(size=14, color="#f1f5f9"),
            margin=dict(l=20, r=20, t=50, b=20),
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    # Full-Width Interactive Dual-Axis Line / Bar Chart
    st.markdown("##### 🚀 Dual-Axis Financial Trend Explorer")
    daily_roll = active_df.groupby("Date").agg({"Revenue": "sum", "Orders": "sum"}).reset_index()

    fig_dual = go.Figure()
    fig_dual.add_trace(go.Bar(
        x=daily_roll["Date"],
        y=daily_roll["Orders"],
        name="Orders Count",
        marker_color="rgba(99, 102, 241, 0.4)",
        yaxis="y2",
    ))
    fig_dual.add_trace(go.Scatter(
        x=daily_roll["Date"],
        y=daily_roll["Revenue"],
        name="Gross Revenue ($)",
        mode="lines+markers",
        line=dict(color="#38bdf8", width=3, shape="spline"),
        marker=dict(size=6, color="#38bdf8"),
        yaxis="y",
    ))

    fig_dual.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)",
        font=dict(family="Plus Jakarta Sans", color="#cbd5e1"),
        yaxis=dict(
            title=dict(text="Revenue ($)", font=dict(color="#38bdf8")),
            tickfont=dict(color="#38bdf8"),
        ),
        yaxis2=dict(
            title=dict(text="Orders", font=dict(color="#818cf8")),
            tickfont=dict(color="#818cf8"),
            overlaying="y",
            side="right",
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode="x unified",
    )
    st.plotly_chart(fig_dual, use_container_width=True)


# =============================================================================
# TAB 3: SEABORN & MATPLOTLIB DARK SUITE
# =============================================================================
with tab_seaborn:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <h3 style="margin-bottom: 4px; font-weight: 700;">Scientific & Statistical Visualizations</h3>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Stylized Seaborn and Matplotlib outputs tailored with dark surfaces and modern color maps.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Configure custom dark aesthetics for Matplotlib & Seaborn
    plt.rcParams.update({
        "figure.facecolor": "#0e1422",
        "axes.facecolor": "#121a2d",
        "axes.edgecolor": "#1e293b",
        "axes.labelcolor": "#94a3b8",
        "text.color": "#f1f5f9",
        "xtick.color": "#64748b",
        "ytick.color": "#64748b",
        "grid.color": "#1e293b",
        "grid.alpha": 0.5,
        "font.sans-serif": "DejaVu Sans",
    })

    mat_col1, mat_col2 = st.columns(2)

    with mat_col1:
        st.markdown("##### 1. Kernel Density Distribution & Histogram")
        fig_kde, ax_kde = plt.subplots(figsize=(7, 4.2))
        sns.histplot(
            active_df["Revenue"],
            kde=True,
            ax=ax_kde,
            color="#6366f1",
            edgecolor="#1e293b",
            line_kws={"linewidth": 2.5, "color": "#ec4899"},
        )
        ax_kde.set_title("Revenue Probability Density", fontsize=11, fontweight="bold", pad=12)
        ax_kde.set_xlabel("Revenue ($)")
        ax_kde.set_ylabel("Density / Count")
        plt.tight_layout()
        st.pyplot(fig_kde)
        plt.close(fig_kde)

    with mat_col2:
        st.markdown("##### 2. Profit Margin Spread Across Categories")
        fig_box, ax_box = plt.subplots(figsize=(7, 4.2))
        sns.boxplot(
            data=active_df,
            x="Category",
            y="Profit",
            hue="Category",
            legend=False,
            ax=ax_box,
            palette=["#38bdf8", "#818cf8", "#f472b6", "#34d399"],
            linewidth=1.2,
        )
        ax_box.set_title("Profit Dispersal by Product Category", fontsize=11, fontweight="bold", pad=12)
        ax_box.set_xlabel("")
        ax_box.set_ylabel("Profit ($)")
        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()
        st.pyplot(fig_box)
        plt.close(fig_box)

    mat_col3, mat_col4 = st.columns(2)

    with mat_col3:
        st.markdown("##### 3. Feature Correlation Matrix Heatmap")
        corr_matrix = active_df[["Revenue", "Orders", "Profit", "ConversionRate"]].corr()
        fig_heat, ax_heat = plt.subplots(figsize=(7, 3.8))
        sns.heatmap(
            corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="mako",
            cbar=True,
            ax=ax_heat,
            linewidths=1,
            linecolor="#0e1422",
            square=True,
        )
        ax_heat.set_title("Pearson Correlation Coefficients", fontsize=11, fontweight="bold", pad=12)
        plt.tight_layout()
        st.pyplot(fig_heat)
        plt.close(fig_heat)

    with mat_col4:
        st.markdown("##### 4. Device vs Category Order Intensity")
        pivot_table = active_df.pivot_table(index="Category", columns="Device", values="Orders", aggfunc="sum")
        fig_piv, ax_piv = plt.subplots(figsize=(7, 3.8))
        sns.heatmap(
            pivot_table,
            annot=True,
            fmt="d",
            cmap="rocket",
            ax=ax_piv,
            linewidths=1,
            linecolor="#0e1422",
        )
        ax_piv.set_title("Total Orders: Device Category Matrix", fontsize=11, fontweight="bold", pad=12)
        plt.tight_layout()
        st.pyplot(fig_piv)
        plt.close(fig_piv)


# =============================================================================
# TAB 4: STREAMLIT ARCHITECTURE & WORKFLOW DEEP DIVE
# =============================================================================
with tab_architecture:
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h3 style="margin-bottom: 4px; font-weight: 700;">How Streamlit Actually Works Under the Hood</h3>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Streamlit does not use conventional request-response routing or manual DOM event wiring. 
                Instead, it implements a pure <strong>Unidirectional Reactive Dataflow</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 5-Stage Visual Workflow Cards
    w1, w2, w3, w4, w5 = st.columns(5)
    with w1:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">1</span>
            <div style="font-weight: 700; font-size: 0.9rem; color: #fff;">User Event</div>
            <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 6px;">
                User drags a slider, selects an option, or clicks a button.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w2:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">2</span>
            <div style="font-weight: 700; font-size: 0.9rem; color: #fff;">Full Rerun</div>
            <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 6px;">
                Python re-runs <code>main.py</code> completely from line 1 to the end.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w3:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">3</span>
            <div style="font-weight: 700; font-size: 0.9rem; color: #fff;">Cache Validation</div>
            <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 6px;">
                <code>@st.cache_data</code> skips recomputation if inputs did not change.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w4:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">4</span>
            <div style="font-weight: 700; font-size: 0.9rem; color: #fff;">State Retrieval</div>
            <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 6px;">
                <code>st.session_state</code> injects persisted variables across reruns.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with w5:
        st.markdown("""
        <div class="flow-card">
            <span class="flow-num">5</span>
            <div style="font-weight: 700; font-size: 0.9rem; color: #fff;">Virtual DOM Diff</div>
            <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 6px;">
                Streamlit updates only the browser DOM elements that changed.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Interactive Caching Benchmark Demo
    st.markdown("##### 🧪 Real-Time Caching Benchmark Experiment")
    st.caption("Compare execution time between an uncached computation vs a cached computation.")

    @st.cache_data
    def cached_heavy_calculation(n: int):
        time.sleep(0.8)  # Simulated heavy processing
        return [i ** 2 for i in range(n)]

    def uncached_heavy_calculation(n: int):
        time.sleep(0.8)
        return [i ** 2 for i in range(n)]

    exp_col1, exp_col2 = st.columns(2)

    with exp_col1:
        if st.button("🚀 Run With @st.cache_data", use_container_width=True):
            t0 = time.perf_counter()
            res = cached_heavy_calculation(10000)
            elapsed = (time.perf_counter() - t0) * 1000
            st.success(f"Cached Computation Finished in: **{elapsed:.2f} ms**")
            st.caption("First run takes ~800ms. Subsequent runs take < 1ms!")

    with exp_col2:
        if st.button("⚠️ Run Without Caching", use_container_width=True):
            t0 = time.perf_counter()
            res = uncached_heavy_calculation(10000)
            elapsed = (time.perf_counter() - t0) * 1000
            st.warning(f"Uncached Computation Finished in: **{elapsed:.2f} ms**")
            st.caption("Every single click takes full 800ms penalty.")

    st.markdown("---")

    # Interactive Session State Sandbox
    st.markdown("##### 📝 Interactive Session State Note-Taker")
    st.caption("Items added here persist across all filter changes, sliders, and tab navigations.")

    note_col1, note_col2 = st.columns([3, 1])
    with note_col1:
        user_note = st.text_input("Enter a bookmark tag or hypothesis", placeholder="e.g., Cyber Monday Surge Analysis")
    with note_col2:
        st.write("")
        st.write("")
        if st.button("📌 Bookmark Note", use_container_width=True):
            if user_note.strip():
                st.session_state.bookmarked_records.append({
                    "Timestamp": datetime.now().strftime("%H:%M:%S"),
                    "Note": user_note.strip(),
                    "TotalRevenueAtBookmark": f"${total_rev:,.0f}",
                })
                st.session_state.last_action = f"Added note: '{user_note.strip()[:15]}...'"
                st.rerun()

    if st.session_state.bookmarked_records:
        st.markdown("**Your Saved Bookmarks (In-Memory Session):**")
        st.dataframe(pd.DataFrame(st.session_state.bookmarked_records), use_container_width=True)
    else:
        st.info("No bookmarks saved yet. Type a note above and click Bookmark Note.")


# =============================================================================
# TAB 5: INTERACTIVE DATA ENGINE
# =============================================================================
with tab_data:
    st.markdown("""
        <div style="margin-bottom: 16px;">
            <h3 style="margin-bottom: 4px; font-weight: 700;">Interactive Data Grid & Export Hub</h3>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                Explore raw records with formatted column types (currency, progress indicators, dates) and export capability.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Search & Quick Slicer
    search_col1, search_col2 = st.columns([2, 1])
    with search_col1:
        search_query = st.text_input("🔍 Quick Search by Region or Category", placeholder="e.g. EMEA or AI Workstations")
    with search_col2:
        sort_by = st.selectbox("Sort Data By", ["Revenue", "Profit", "Orders", "Date"], index=0)

    display_df = active_df.copy()
    if search_query:
        display_df = display_df[
            display_df["Category"].str.contains(search_query, case=False, na=False) |
            display_df["Region"].str.contains(search_query, case=False, na=False)
        ]

    display_df = display_df.sort_values(by=sort_by, ascending=False)

    # Advanced Streamlit Column Configurations
    st.dataframe(
        display_df,
        use_container_width=True,
        column_config={
            "Date": st.column_config.DateColumn("Date", format="YYYY-MM-DD"),
            "Revenue": st.column_config.NumberColumn("Revenue", format="$%.2f"),
            "Profit": st.column_config.NumberColumn("Profit", format="$%.2f"),
            "Orders": st.column_config.ProgressColumn(
                "Orders Volume",
                format="%d",
                min_value=0,
                max_value=int(active_df["Orders"].max()),
            ),
            "ConversionRate": st.column_config.NumberColumn("Conversion", format="%.2f%%"),
            "Category": st.column_config.TextColumn("Category"),
            "Region": st.column_config.TextColumn("Region"),
            "Device": st.column_config.TextColumn("Device"),
        },
    )

    # Export Tools
    st.markdown("##### 📥 Data Export Center")
    exp_btn1, exp_btn2 = st.columns(2)

    with exp_btn1:
        csv_data = display_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📄 Download Filtered Dataset (CSV)",
            data=csv_data,
            file_name=f"analytics_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with exp_btn2:
        json_data = display_df.to_json(orient="records", date_format="iso").encode("utf-8")
        st.download_button(
            label="⚡ Download Dataset as JSON",
            data=json_data,
            file_name=f"analytics_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True,
        )


# -----------------------------------------------------------------------------
# 9. FOOTER
# -----------------------------------------------------------------------------
st.markdown("""
<div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid rgba(255, 255, 255, 0.08); text-align: center; color: #64748b; font-size: 0.8rem;">
    Streamlit Reactive Studio • Built with Python, Streamlit, Plotly, Seaborn & Custom CSS Architecture
</div>
""", unsafe_allow_html=True)
