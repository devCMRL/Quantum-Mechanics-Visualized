"""Chapter 2 — finite-dimensional complex Hilbert space (column kets)."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure
from qm_course.finite_hilbert import inner, norm, normalize

st.set_page_config(page_title="Ch 2 — Finite Hilbert space", layout="wide")

st.title("Chapter 2 — Finite-dimensional Hilbert space")
st.caption(r"Column vectors in $\mathbb{C}^N$: normalization, inner product, and distance between normalized rays.")

dim = st.radio("Dimension N", [2, 3, 4], horizontal=True)

st.subheader(r"Ket $|\psi\rangle$ — edit complex components")
cols = st.columns(dim)
re = []
im = []
defaults = {2: ([1.0, 0.25], [0.0, 0.5]), 3: ([1.0, 0.3, 0.0], [0.0, 0.4, 0.6]), 4: ([1.0, 0.2, 0.0, 0.1], [0.0, 0.3, 0.5, 0.0])}
dr, di = defaults[dim]
for i in range(dim):
    with cols[i]:
        st.markdown(f"**{i}**")
        re.append(st.slider(f"Re c{i}", -1.0, 1.0, float(dr[i]), 0.05, key=f"re{i}"))
        im.append(st.slider(f"Im c{i}", -1.0, 1.0, float(di[i]), 0.05, key=f"im{i}"))

psi = np.array([complex(r, ii) for r, ii in zip(re, im, strict=True)])
npsi = norm(psi)
st.metric(r"$\|\psi\|$", f"{npsi:.4f}")
if st.button("Normalize |ψ⟩ (in-place in session)"):
    if npsi < 1e-9:
        st.warning("Norm is numerically zero; adjust the components before normalizing.")
    else:
        psi_n = normalize(psi)
        for i in range(dim):
            st.session_state[f"re{i}"] = float(np.real(psi_n[i]))
            st.session_state[f"im{i}"] = float(np.imag(psi_n[i]))
        st.rerun()

st.divider()
st.subheader("Visualizations")
psi_plot = normalize(psi) if npsi > 1e-12 else np.zeros(dim, dtype=complex)
w = np.abs(psi_plot) ** 2
fig1 = go.Figure(
    go.Bar(
        x=[str(i) for i in range(dim)],
        y=w,
        marker_color="#5b8def",
        name=r"$|c_i|^2$",
    )
)
fig1.update_xaxes(title_text="Basis index (computational)")
fig1.update_yaxes(title_text=r"$|c_i|^2$ for normalized $|\psi\rangle$", range=[0, max(1.05 * w.max(), 0.05)])
fig1.update_layout(showlegend=False)
style_figure(fig1, height=360)

theta_circle = np.linspace(0, 2 * np.pi, 120)
fig2 = go.Figure()
fig2.add_trace(
    go.Scatter(
        x=np.cos(theta_circle),
        y=np.sin(theta_circle),
        mode="lines",
        line=dict(color="#475569", dash="dash"),
        name="Unit circle",
    )
)
fig2.add_trace(
    go.Scatter(
        x=np.real(psi),
        y=np.imag(psi),
        mode="markers+text",
        text=[str(i) for i in range(dim)],
        textposition="top center",
        marker=dict(size=12, color="#f97316"),
        name=r"$c_i$",
    )
)
fig2.update_xaxes(title_text=r"$\mathrm{Re}\,c_i$", scaleanchor="y", scaleratio=1)
fig2.update_yaxes(title_text=r"$\mathrm{Im}\,c_i$")
fig2.update_layout(showlegend=False)
style_figure(fig2, height=360)

cvis1, cvis2 = st.columns(2)
with cvis1:
    st.plotly_chart(fig1, use_container_width=True)
with cvis2:
    st.caption("Coefficients in the complex plane (unnormalized components; dashed circle is unit modulus).")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.subheader(r"Second ket $|\phi\rangle$ (for inner product)")
use_phi = st.toggle("Show ⟨φ|ψ⟩ and Hilbert distance", value=True)
if use_phi:
    cols2 = st.columns(dim)
    re2, im2 = [], []
    for i in range(dim):
        with cols2[i]:
            re2.append(st.slider(f"φ Re {i}", -1.0, 1.0, 1.0 if i == 0 else 0.0, 0.05, key=f"pre{i}"))
            im2.append(st.slider(f"φ Im {i}", -1.0, 1.0, 0.0, 0.05, key=f"pim{i}"))
    phi = np.array([complex(r, ii) for r, ii in zip(re2, im2, strict=True)])
    ip = inner(phi, psi)
    phi_n = normalize(phi)
    psi_u = normalize(psi)
    dist = float(np.linalg.norm(psi_u - phi_n))
    st.latex(rf"\langle\phi|\psi\rangle = {ip.real:.4f} + {ip.imag:.4f}\,i")
    st.metric(r"$\|\,|\hat\psi\rangle - |\hat\phi\rangle\,\|$ (normalized kets)", f"{dist:.4f}")

with st.expander("Key points"):
    st.markdown(
        r"""
- **Normalization** is the statement $\langle\psi|\psi\rangle=1$: probabilities later come from **squared
  magnitudes** of overlaps.
- The **inner product** $\langle\phi|\psi\rangle$ measures **alignment** in complex space; its modulus enters
  **Born’s rule** (next chapter).
"""
    )
