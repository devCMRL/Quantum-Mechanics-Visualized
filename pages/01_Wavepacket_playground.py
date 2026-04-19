"""Chapter 01 — free one-dimensional Gaussian wavepacket (real part)."""
import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure

st.set_page_config(page_title="Ch 01 — Wavepacket", layout="wide")

st.title("Chapter 1 — Gaussian wavepacket in 1D")
st.caption("Real part of a Gaussian envelope modulated by a plane wave: width, center, and wavenumber.")

col_ctrl, col_plot = st.columns([1, 2])

with col_ctrl:
    st.subheader("Controls")
    x0 = st.slider("Center x₀", -5.0, 5.0, 0.0, 0.1)
    sigma = st.slider("Width σ", 0.2, 3.0, 1.0, 0.05)
    k0 = st.slider("Wavenumber k₀", -3.0, 3.0, 1.5, 0.05)
    x_max = st.slider("Plot half-range", 4.0, 15.0, 8.0, 0.5)
    st.markdown(
        r"""
**Model** (unnormalized demo envelope):

$\psi(x) \propto e^{-(x-x_0)^2/(2\sigma^2)} \, e^{i k_0 x}$

**Shown:** $\mathrm{Re}\,\psi(x)$
"""
    )

x = np.linspace(-x_max, x_max, 800)
envelope = np.exp(-((x - x0) ** 2) / (2 * sigma**2))
psi_real = envelope * np.cos(k0 * x)

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=x,
        y=psi_real,
        mode="lines",
        name=r"Re ψ",
        line=dict(color="#5b8def", width=2),
    )
)
fig.add_trace(
    go.Scatter(
        x=x,
        y=envelope,
        mode="lines",
        name="Envelope",
        line=dict(color="#94a3b8", width=1, dash="dash"),
    )
)
fig.add_trace(
    go.Scatter(
        x=x,
        y=-envelope,
        mode="lines",
        name="−Envelope",
        line=dict(color="#94a3b8", width=1, dash="dash"),
        showlegend=False,
    )
)
fig.update_layout(
    xaxis_title="x",
    yaxis_title="Amplitude",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)
style_figure(fig)

with col_plot:
    st.plotly_chart(fig, use_container_width=True)

with st.expander("Key points"):
    st.markdown(
        """
- **σ** controls how many oscillations fit under the bell: smaller σ ⇒ more localized packet (fewer oscillations visible).
- **k₀** controls oscillation frequency in space (local wavelength λ ≈ 2π/k₀ for large k₀).
- **x₀** translates the pattern in **x**. Time evolution and potentials appear in later chapters (e.g. the infinite well and barrier modules).
"""
    )
