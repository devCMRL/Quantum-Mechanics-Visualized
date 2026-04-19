"""Chapter 06 — two-slit interference (scalar wave model)."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.double_slit import intensity_on_screen
from qm_course.figures import style_figure

st.set_page_config(page_title="Ch 06 — Double slit", layout="wide")

st.title("Chapter 6 — Double-slit interference")
st.caption("Scalar Fraunhofer diffraction: two slits with finite width (small-angle approximation).")

col1, col2 = st.columns([1, 2])
with col1:
    d = st.slider("Slit separation d", 0.05, 2.0, 0.5, 0.01)
    a = st.slider("Slit width a", 0.02, 0.8, 0.15, 0.01)
    L = st.slider("Screen distance L", 0.5, 5.0, 2.0, 0.05)
    lam = st.slider("Wavelength λ", 0.02, 0.5, 0.12, 0.005)
    y_max = st.slider("Half-width on screen y", 0.05, 0.6, 0.25, 0.01)

k = 2 * np.pi / lam
y = np.linspace(-y_max, y_max, 1200)
I = intensity_on_screen(y, d=d, a=a, L=L, k=k, I0=1.0)
I = I / (np.max(I) + 1e-12)

fig = go.Figure()
fig.add_trace(go.Scatter(x=y * 1000, y=I, mode="lines", name="Normalized I"))
fig.update_xaxes(title_text="y on screen (mm, arbitrary scale)")
fig.update_yaxes(title_text="Intensity (normalized)")
style_figure(fig)

with col2:
    st.plotly_chart(fig, use_container_width=True)
with col1:
    st.markdown(
        r"""
**Single-slit envelope** × **double-slit fringes**. Small-angle approximations: $\theta \approx y/L$.

This is a **classical wave** model, but it previews **which-path** vs **interference** language used later
for quantum probability amplitudes.
"""
    )

with st.expander("Key points"):
    st.markdown(
        """
- **Wider slits** (larger **a**) tighten the overall envelope: the central lobe becomes narrower.
- **Larger separation d** packs fringes closer in angle (more oscillations across the same screen width).
"""
    )
