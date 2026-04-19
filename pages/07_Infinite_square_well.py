"""Chapter 7 — infinite square well eigenstates and simple superpositions."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure
from qm_course.infinite_well import energy_eigenvalue, stationary_state, superposition

st.set_page_config(page_title="Ch 7 — Particle in a box", layout="wide")

st.title("Chapter 7 — Infinite square well")
st.caption("Box from x = 0 to L: stationary states sin(nπx/L) and a three-mode superposition.")

L = 1.0
x = np.linspace(0, L, 900)

tab1, tab2 = st.tabs(["Single eigenstate", "Superposition n = 1, 2, 3"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        n = st.slider("Quantum number n", 1, 12, 1)
        show_prob = st.toggle("Show |ψ|² instead of ψ", value=False)
        st.markdown(
            r"$\psi_n(x)=\sqrt{\tfrac{2}{L}}\sin\!\big(\tfrac{n\pi x}{L}\big),\quad"
            r"E_n=\tfrac{\hbar^2\pi^2 n^2}{2mL^2}$"
        )
        st.metric("Eₙ (units ħ²/mL²)", f"{energy_eigenvalue(n, L=L):.4f}")
    psi = stationary_state(x, n, L=L)
    y = psi**2 if show_prob else psi
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="|ψ|²" if show_prob else "ψ"))
    fig.add_vrect(x0=0, x1=L, fillcolor="#334155", opacity=0.15, line_width=0)
    fig.update_xaxes(title_text="x")
    fig.update_yaxes(title_text="|ψ|²" if show_prob else "ψ")
    style_figure(fig)
    with col2:
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    c1, c2 = st.columns([1, 2])
    with c1:
        a1 = st.slider("Amplitude for n = 1", -1.0, 1.0, 1.0, 0.05)
        a2 = st.slider("Amplitude for n = 2", -1.0, 1.0, 0.0, 0.05)
        a3 = st.slider("Amplitude for n = 3", -1.0, 1.0, 0.0, 0.05)
    coeffs = np.array([a1, a2, a3], dtype=complex)
    ns = np.array([1, 2, 3])
    norm = np.linalg.norm(coeffs)
    if norm < 1e-9:
        coeffs = np.array([1.0, 0.0, 0.0], dtype=complex)
        norm = 1.0
    coeffs = coeffs / norm
    psi = superposition(x, coeffs, ns, L=L)
    prob = np.abs(psi) ** 2
    E_exp = sum(abs(c) ** 2 * energy_eigenvalue(int(n), L=L) for c, n in zip(coeffs, ns, strict=True))
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=x, y=prob, mode="lines", name="|ψ|²"))
    fig2.update_xaxes(title_text="x")
    fig2.update_yaxes(title_text="|ψ|²")
    style_figure(fig2)
    with c2:
        st.plotly_chart(fig2, use_container_width=True)
    with c1:
        st.metric("⟨E⟩ (same units as Eₙ)", f"{E_exp:.4f}")
        probs = np.abs(coeffs) ** 2
        st.caption("Mode weights |cₙ|²: " + ", ".join(f"{p:.2f}" for p in probs))

with st.expander("Key points"):
    st.markdown(
        """
- Higher **n** adds more nodes: the **n**th level has **n − 1** interior nodes.
- A **superposition** is not an energy eigenstate unless only one coefficient is nonzero; **|ψ|²** is time-dependent
  (Chapter 14).
"""
    )
