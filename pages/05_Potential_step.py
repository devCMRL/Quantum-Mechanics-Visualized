"""Chapter 05 — potential step scattering (real part of ψ)."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure
from qm_course.step_potential import plane_wave_step_real

st.set_page_config(page_title="Ch 05 — Potential step", layout="wide")

st.title("Chapter 5 — Potential step")
st.caption("V(x) = 0 for x < 0 and V(x) = V₀ for x ≥ 0. Stationary solution with unit incident amplitude from the left.")

col1, col2 = st.columns([1, 2])
with col1:
    V0 = st.slider("Step height V₀", 0.0, 6.0, 2.0, 0.1)
    E = st.slider("Particle energy E", 0.05, 8.0, 3.0, 0.05)
    x_range = st.slider("Half-width of plot", 4.0, 20.0, 10.0, 1.0)

x = np.linspace(-x_range, x_range, 1600)
psi_r = plane_wave_step_real(x, E, V0)

k1 = np.sqrt(2 * E)
if E >= V0:
    k2 = np.sqrt(2 * max(E - V0, 0.0))
    r = (k1 - k2) / (k1 + k2)
    t = 2 * k1 / (k1 + k2)
    R_prob = float(np.abs(r) ** 2)
    T_flux = float(np.abs(t) ** 2 * (k2 / k1)) if k1 > 0 else 0.0
else:
    R_prob = 1.0
    T_flux = 0.0

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=psi_r, mode="lines", name=r"Re ψ"))
fig.add_vline(x=0, line_dash="dash", line_color="#94a3b8")
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text=r"Re ψ")
style_figure(fig)

with col2:
    st.plotly_chart(fig, use_container_width=True)
with col1:
    st.markdown(r"**Incident + reflected** for $x<0$, **transmitted / evanescent** for $x>0$.")
    st.metric("Reflection probability |r|²", f"{R_prob:.3f}")
    if E >= V0:
        st.metric("Transmitted flux fraction", f"{T_flux:.3f}")
    else:
        st.caption("For **E < V₀** there is no propagating transmitted plane wave; |r|² → 1 with an evanescent tail.")

with st.expander("Key points"):
    st.markdown(
        """
- For **E > V₀** you see **interference** in the reflected region from superposing left- and right-moving waves.
- For **E < V₀** the wave in **x > 0** is evanescent (decaying): no traveling transmitted wave, yet finite
  penetration into the classically forbidden region.
"""
    )
