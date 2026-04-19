"""Chapter 15 — integrated lab: traveling waves, interference, two-qubit entanglement."""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from qm_course.double_slit import intensity_on_screen
from qm_course.figures import style_figure
from qm_course.two_qubit import (
    bloch_components,
    concurrence,
    ket_phi_minus,
    ket_phi_plus,
    ket_psi_minus,
    ket_psi_plus,
    ket_schmidt_real,
    ket_separable_plus_plus,
    ket_00,
    partial_trace_A,
    partial_trace_B,
    probabilities,
)

st.set_page_config(page_title="Ch 15 — Problem lab", layout="wide")

st.title("Chapter 15 — Problem laboratory")
st.caption(
    "Textbook-style setups with adjustable parameters: superposed traveling waves, Young-type interference, "
    "and two-qubit correlation / entanglement measures."
)

tab_tr, tab_yg, tab_2q = st.tabs(["Traveling waves", "Interference (Young)", "Two-qubit entanglement"])

with tab_tr:
    st.markdown(
        r"""
**Superposition of two plane de Broglie components** (scalar model):

$\psi(x,t) = A_1 e^{i(k_1 x - \omega_1 t)} + A_2 e^{i(k_2 x - \omega_2 t + \delta)}$.

Use **time** as a slider to sweep propagation; compare **Re ψ** and **|ψ|²** (interference in intensity).
"""
    )
    level = st.radio("Parameter level", ["Core", "Extended"], horizontal=True, key="tw_level")
    c1, c2 = st.columns([1, 2])
    with c1:
        k1 = st.slider("k₁", -3.0, 3.0, 1.2, 0.05, key="tw_k1")
        k2 = st.slider("k₂", -3.0, 3.0, 1.0, 0.05, key="tw_k2")
        delta = st.slider("Phase δ (rad)", 0.0, 2 * np.pi, 0.8, 0.05, key="tw_d")
        t = st.slider("Time t", 0.0, 15.0, 0.0, 0.05, key="tw_t")
        A1 = st.slider("Amplitude A₁", 0.0, 1.5, 1.0, 0.05, key="tw_a1")
        A2 = st.slider("Amplitude A₂", 0.0, 1.5, 1.0, 0.05, key="tw_a2")
        if level == "Extended":
            w1 = st.slider("ω₁", -4.0, 4.0, 1.2, 0.05, key="tw_w1")
            w2 = st.slider("ω₂", -4.0, 4.0, 1.0, 0.05, key="tw_w2")
        else:
            w1 = w2 = st.slider("Shared ω (both components)", -4.0, 4.0, 1.0, 0.05, key="tw_w")
    x = np.linspace(-12, 12, 1000)
    psi = A1 * np.exp(1j * (k1 * x - w1 * t)) + A2 * np.exp(1j * (k2 * x - w2 * t + delta))
    pr = np.real(psi)
    pi2 = np.abs(psi) ** 2
    fig_tw = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08, row_heights=[0.5, 0.5])
    fig_tw.add_trace(go.Scatter(x=x, y=pr, mode="lines", name=r"Re ψ", line=dict(color="#5b8def")), row=1, col=1)
    fig_tw.add_trace(go.Scatter(x=x, y=pi2, mode="lines", name=r"|ψ|²", line=dict(color="#f97316")), row=2, col=1)
    fig_tw.update_xaxes(title_text="x", row=2, col=1)
    fig_tw.update_yaxes(title_text=r"Re ψ", row=1, col=1)
    fig_tw.update_yaxes(title_text=r"|ψ|²", row=2, col=1)
    fig_tw.update_layout(height=560, template="plotly_dark", margin=dict(l=40, r=20, t=40, b=40), hovermode="x unified")
    with c2:
        st.plotly_chart(fig_tw, use_container_width=True)
    with c1:
        if level == "Core":
            st.caption("**Core:** one shared **ω** for both waves (like locking dispersion). Switch to **Extended** to decouple **ω₁**, **ω₂** (beats in time and space).")

with tab_yg:
    st.markdown(
        r"""
**Fraunhofer / Young pattern** (same scalar model as Chapter 11): two slits of width **a**, separation **d**,
screen distance **L**, wavenumber **k = 2π/λ**. Intensity vs transverse position **y** on the screen.
"""
    )
    ylev = st.radio("Parameter level", ["Standard", "Fine control"], horizontal=True, key="yg_lev")
    g1, g2 = st.columns([1, 2])
    with g1:
        d = st.slider("Slit separation d", 0.05, 2.0, 0.5, 0.01, key="yg_d")
        L = st.slider("Screen distance L", 0.5, 5.0, 2.0, 0.05, key="yg_L")
        lam = st.slider("Wavelength λ", 0.02, 0.5, 0.12, 0.005, key="yg_lam")
        y_max = st.slider("Half-width y on screen", 0.05, 0.6, 0.25, 0.01, key="yg_ymax")
        if ylev == "Fine control":
            a = st.slider("Slit width a", 0.02, 0.8, 0.15, 0.01, key="yg_a")
        else:
            a = 0.15
    k = 2 * np.pi / lam
    y = np.linspace(-y_max, y_max, 1200)
    I = intensity_on_screen(y, d=d, a=a, L=L, k=k, I0=1.0)
    I = I / (np.max(I) + 1e-12)
    fig_yg = go.Figure(go.Scatter(x=y * 1000, y=I, mode="lines", line=dict(color="#a78bfa")))
    fig_yg.update_xaxes(title_text="y on screen (arbitrary mm scale)")
    fig_yg.update_yaxes(title_text="Normalized intensity")
    style_figure(fig_yg, height=480)
    with g2:
        st.plotly_chart(fig_yg, use_container_width=True)
    with g1:
        if ylev == "Standard":
            st.caption("**Standard:** fixed slit width **a = 0.15**. Choose **Fine control** to vary **a** and watch the envelope tighten or widen.")

with tab_2q:
    st.markdown(
        r"""
**Two-qubit pure state** in the computational basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$.

**Heatmap:** joint probabilities $|c_{ij}|^2$. **Reduced Bloch vectors:** $(\mathrm{Tr}\,\rho\sigma_x, \ldots)$ for each subsystem.

**Concurrence** $C = 2|ad - bc|$ quantifies two-qubit entanglement ($C=1$ for Bell states, $0$ for product states).
"""
    )
    fam = st.selectbox(
        "State family",
        [
            "|Φ+⟩ (Bell)",
            "|Φ−⟩",
            "|Ψ+⟩",
            "|Ψ−⟩",
            "|00⟩ (product)",
            "|++⟩ product",
            "Schmidt cos θ|00⟩ + e^{iφ} sin θ|11⟩",
        ],
        key="qb_fam",
    )
    if "Schmidt" in fam:
        ctheta = st.slider("θ", 0.0, np.pi / 2, np.pi / 4, 0.02, key="qb_th")
        cphi = st.slider("φ (phase on |11⟩)", 0.0, 2 * np.pi, 0.0, 0.05, key="qb_ph")
    else:
        ctheta, cphi = np.pi / 4, 0.0
    if fam == "|Φ+⟩ (Bell)":
        q = ket_phi_plus()
    elif fam == "|Φ−⟩":
        q = ket_phi_minus()
    elif fam == "|Ψ+⟩":
        q = ket_psi_plus()
    elif fam == "|Ψ−⟩":
        q = ket_psi_minus()
    elif fam == "|00⟩ (product)":
        q = ket_00()
    elif fam == "|++⟩ product":
        q = ket_separable_plus_plus()
    else:
        q = ket_schmidt_real(ctheta, cphi)
    q = q / (np.linalg.norm(q) + 1e-15)
    p4 = probabilities(q)
    C = concurrence(q)
    ra = partial_trace_A(q)
    rb = partial_trace_B(q)
    bx, by, bz = bloch_components(ra)
    b2x, b2y, b2z = bloch_components(rb)

    h1, h2 = st.columns(2)
    with h1:
        st.metric("Concurrence C", f"{C:.4f}")
    with h2:
        st.metric("Purity Tr ρ_A²", f"{float(np.real(np.trace(ra @ ra))):.4f}")

    M = p4.reshape(2, 2)
    fig_h = go.Figure(
        data=go.Heatmap(
            z=np.real(M),
            x=["j = 0", "j = 1"],
            y=["i = 0", "i = 1"],
            colorscale="Viridis",
            zmin=0,
            zmax=max(float(M.max()), 0.05),
            colorbar=dict(title="|c_ij|²"),
        )
    )
    fig_h.update_layout(height=340, template="plotly_dark", margin=dict(l=60, r=20, t=40, b=40))
    fig_b = go.Figure(
        data=[
            go.Bar(name="Qubit A", x=["nx", "ny", "nz"], y=[bx, by, bz], marker_color="#38bdf8"),
            go.Bar(name="Qubit B", x=["nx", "ny", "nz"], y=[b2x, b2y, b2z], marker_color="#f97316"),
        ]
    )
    fig_b.update_layout(barmode="group", legend=dict(orientation="h", y=1.06, x=1))
    fig_b.update_yaxes(title_text="Reduced Bloch components", range=[-1.15, 1.15])
    style_figure(fig_b, height=380)
    hq1, hq2 = st.columns(2)
    with hq1:
        st.plotly_chart(fig_h, use_container_width=True)
    with hq2:
        st.plotly_chart(fig_b, use_container_width=True)
    st.caption(
        "For |Φ±⟩ and |Ψ±⟩, each reduced state is maximally mixed: Bloch vector ≈ **0** while **C = 1**. "
        "For |++⟩, Bloch vectors align along **+x** on both subsystems and **C = 0**."
    )

with st.expander("Key points"):
    st.markdown(
        r"""
- **Traveling waves:** changing **t** moves phase fronts; unequal **k** or **ω** produces beats in **Re ψ** and moving structure in **|ψ|²**.
- **Young pattern:** fringe spacing scales with **λL/d**; slit width **a** modulates the single-slit envelope.
- **Entanglement:** nonzero **concurrence** with **product** reduced Bloch vectors (both near **0**) is the hallmark of **Bell-type** correlations in this minimal **2×2** display.
"""
    )
