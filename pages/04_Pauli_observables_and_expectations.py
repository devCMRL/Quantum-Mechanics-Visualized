"""Chapter 4 — Pauli matrices as qubit observables and expectation values."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.bloch import bloch_vector
from qm_course.figures import style_figure
from qm_course.qubit import (
    SIGMA_X,
    SIGMA_Y,
    SIGMA_Z,
    expectation_n_dot_sigma,
    expectation_pauli,
    ket_from_bloch,
)

st.set_page_config(page_title="Ch 4 — Pauli observables", layout="wide")

st.title("Chapter 4 — Pauli observables and ⟨A⟩")
st.caption("Hermitian Pauli matrices on ℂ²: expectations from the standard Bloch parametrization.")

col1, col2 = st.columns([1, 1])
with col1:
    theta_deg = st.slider("θ (deg)", 0.0, 180.0, 90.0, 1.0)
    phi_deg = st.slider("φ (deg)", 0.0, 360.0, 45.0, 1.0)
    theta = np.deg2rad(theta_deg)
    phi = np.deg2rad(phi_deg)
    ket = ket_from_bloch(theta, phi)
    st.markdown(r"**State** $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle$.")

with col2:
    st.subheader("Expectations (dimensionless Pauli)")
    ex = expectation_pauli(ket, SIGMA_X)
    ey = expectation_pauli(ket, SIGMA_Y)
    ez = expectation_pauli(ket, SIGMA_Z)
    st.metric("⟨σx⟩", f"{ex:.4f}")
    st.metric("⟨σy⟩", f"{ey:.4f}")
    st.metric("⟨σz⟩", f"{ez:.4f}")

st.subheader("Visualizations")
fig_b = go.Figure(
    data=[
        go.Bar(
            x=["⟨σx⟩", "⟨σy⟩", "⟨σz⟩"],
            y=[ex, ey, ez],
            marker_color=["#38bdf8", "#a78bfa", "#f97316"],
            text=[f"{ex:.3f}", f"{ey:.3f}", f"{ez:.3f}"],
            textposition="auto",
        )
    ]
)
fig_b.update_yaxes(title_text="Expectation value", range=[-1.15, 1.15])
fig_b.update_layout(showlegend=False)
style_figure(fig_b, height=380)

bx, by, bz = bloch_vector(theta, phi)
uu = np.linspace(0, 2 * np.pi, 40)
vv = np.linspace(0, np.pi, 20)
uu, vv = np.meshgrid(uu, vv)
xs = np.cos(uu) * np.sin(vv)
ys = np.sin(uu) * np.sin(vv)
zs = np.cos(vv)
fig_s = go.Figure()
fig_s.add_trace(
    go.Surface(
        x=xs,
        y=ys,
        z=zs,
        opacity=0.22,
        showscale=False,
        colorscale=[[0, "#475569"], [1, "#475569"]],
        hoverinfo="skip",
    )
)
fig_s.add_trace(
    go.Scatter3d(
        x=[0, bx],
        y=[0, by],
        z=[0, bz],
        mode="lines+markers",
        line=dict(color="#38bdf8", width=10),
        marker=dict(size=[0, 10], color=["#94a3b8", "#f97316"]),
        name=r"$\langle\boldsymbol{\sigma}\rangle$ direction",
    )
)
fig_s.update_layout(
    template="plotly_dark",
    height=420,
    margin=dict(l=0, r=0, t=30, b=0),
    scene=dict(
        aspectmode="data",
        xaxis=dict(range=[-1.1, 1.1], title="x"),
        yaxis=dict(range=[-1.1, 1.1], title="y"),
        zaxis=dict(range=[-1.1, 1.1], title="z"),
    ),
    showlegend=False,
)

vb1, vb2 = st.columns(2)
with vb1:
    st.plotly_chart(fig_b, use_container_width=True)
with vb2:
    st.caption("Bloch vector $(\\langle\\sigma_x\\rangle, \\langle\\sigma_y\\rangle, \\langle\\sigma_z\\rangle)$ for this pure state.")
    st.plotly_chart(fig_s, use_container_width=True)

st.divider()
st.subheader(r"Directional observable $\mathbf{n}\cdot\boldsymbol{\sigma}$ with $|\mathbf{n}|=1$")
u1, u2, u3 = st.columns(3)
with u1:
    nx = st.slider("nx", -1.0, 1.0, 0.0, 0.05)
with u2:
    ny = st.slider("ny", -1.0, 1.0, 0.0, 0.05)
with u3:
    nz = st.slider("nz", -1.0, 1.0, 1.0, 0.05)
val = expectation_n_dot_sigma(ket, nx, ny, nz)
st.metric(r"$\langle \mathbf{n}\cdot\boldsymbol{\sigma}\rangle$", f"{val:.4f}")

with st.expander("Pauli matrices (explicit Hermitian forms)"):
    st.latex(r"\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad"
             r"\sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad"
             r"\sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}")
    st.markdown(
        """
Each **σ** is Hermitian with spectrum **{+1, −1}**; therefore **⟨σk⟩ ∈ [−1, 1]** for any normalized state.
"""
    )

with st.expander("Key points"):
    st.markdown(
        r"""
- Expectation values **⟨σk⟩** are ensemble averages for identically prepared systems; here they are computed for a single declared pure state.
- For a pure qubit, $(\langle\sigma_x\rangle, \langle\sigma_y\rangle, \langle\sigma_z\rangle)$ equals
  $(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$, i.e. the Cartesian Bloch vector (Chapter 13).
"""
    )
