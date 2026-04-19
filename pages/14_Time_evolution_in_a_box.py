"""Chapter 14 — time evolution of a superposition in an infinite well."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure
from qm_course.infinite_well import energy_eigenvalue, stationary_state, time_evolve_coeffs

st.set_page_config(page_title="Ch 14 — Time evolution", layout="wide")

st.title("Chapter 14 — Time evolution in a box")
st.caption("Superposition of the four lowest box levels; |ψ|² evolves as each component picks up its energy phase e^{-iEₙt/ħ}.")

L = 1.0
x = np.linspace(0, L, 900)
ns = np.array([1, 2, 3, 4])

col1, col2 = st.columns([1, 2])
with col1:
    a1 = st.slider("Re c₁ at t = 0", -1.0, 1.0, 1.0, 0.05)
    a2 = st.slider("Re c₂ at t = 0", -1.0, 1.0, 0.35, 0.05)
    a3 = st.slider("Re c₃ at t = 0", -1.0, 1.0, 0.0, 0.05)
    a4 = st.slider("Re c₄ at t = 0", -1.0, 1.0, 0.0, 0.05)
    t = st.slider("Time t (units ħ = 1)", 0.0, 6.0, 0.0, 0.02)

c0 = np.array([a1, a2, a3, a4], dtype=complex)
nrm = np.linalg.norm(c0)
if nrm < 1e-9:
    c0 = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    nrm = 1.0
c0 = c0 / nrm
ct = time_evolve_coeffs(c0, ns, t=t, L=L)

psi = np.zeros_like(x, dtype=complex)
for c, n in zip(ct, ns, strict=True):
    psi += c * stationary_state(x, int(n), L=L)
prob = np.abs(psi) ** 2

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=prob, mode="lines", name="|ψ(x,t)|²"))
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text="|ψ|²")
style_figure(fig)

with col2:
    st.plotly_chart(fig, use_container_width=True)

E_exp = float(sum(abs(c) ** 2 * energy_eigenvalue(int(n), L=L) for c, n in zip(ct, ns, strict=True)))
with col1:
    st.metric("⟨E⟩ at this time", f"{E_exp:.4f}")
    st.caption("Small increments in **t** resolve beating between close eigenfrequencies.")

with st.expander("Key points"):
    st.markdown(
        """
- Each energy eigenstate only picks up a **phase** in time, so **|ψₙ|²** is static.
- A **superposition** beats because each term rotates at its own frequency **Eₙ/ħ**; **|ψ|²** generically **moves**.
"""
    )
