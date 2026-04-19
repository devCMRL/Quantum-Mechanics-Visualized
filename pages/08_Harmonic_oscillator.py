"""Chapter 8 — 1D harmonic oscillator stationary states."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure
from qm_course.harmonic import energy_eigenvalue, psi_n

st.set_page_config(page_title="Ch 8 — Harmonic oscillator", layout="wide")

st.title("Chapter 8 — Quantum harmonic oscillator")
st.caption("Units ħ = m = ω = 1. Stationary-state probability density |ψₙ|².")

col1, col2 = st.columns([1, 2])
with col1:
    n = st.slider("Level n", 0, 16, 0)
    x_max = st.slider("Plot range |x|", 2.0, 10.0, 6.0, 0.5)
    overlay_classical = st.toggle("Overlay classical turning points ±√(2E)", value=True)
    st.markdown(r"**Energy** $E_n = \hbar\omega(n+\tfrac{1}{2})$ → in these units $E_n = n + \tfrac{1}{2}$.")

x = np.linspace(-x_max, x_max, 900)
psi = psi_n(x, n)
prob = psi**2

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=prob, mode="lines", name="|ψₙ|²"))
if overlay_classical:
    E = energy_eigenvalue(n)
    x_tp = np.sqrt(2 * E)
    fig.add_vline(x=x_tp, line_dash="dash", line_color="#f97316", annotation_text="x_tp")
    fig.add_vline(x=-x_tp, line_dash="dash", line_color="#f97316")
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text="|ψ|²")
style_figure(fig)

with col2:
    st.plotly_chart(fig, use_container_width=True)
with col1:
    st.metric("Eₙ", f"{energy_eigenvalue(n):.3f}")

with st.expander("Key points"):
    st.markdown(
        """
- The oscillator spectrum is **evenly spaced**: ΔE = ħω between neighbours (here ΔE = 1).
- **Classical turning points** separate classically allowed vs forbidden regions for that energy; the
  quantum wavefunction is still nonzero beyond them (tunneling into the “forbidden” region).
"""
    )
