"""Chapter 08 — Bloch sphere for a pure qubit state."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.bloch import bloch_vector

st.set_page_config(page_title="Ch 08 — Bloch sphere", layout="wide")

st.title("Chapter 8 — Bloch sphere (spin-½ intuition)")
st.caption(
    r"Pure state $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\varphi}\sin\frac{\theta}{2}|1\rangle$ "
    "mapped to a unit vector on the sphere."
)

col1, col2 = st.columns([1, 2])
with col1:
    theta_deg = st.slider("Polar angle θ (degrees)", 0.0, 180.0, 60.0, 1.0)
    phi_deg = st.slider("Azimuth φ (degrees)", 0.0, 360.0, 30.0, 1.0)
    theta = np.deg2rad(theta_deg)
    phi = np.deg2rad(phi_deg)
    nx, ny, nz = bloch_vector(theta, phi)
    st.markdown(
        r"**Bloch vector** $\mathbf{n}=(\sin\theta\cos\varphi,\,\sin\theta\sin\varphi,\,\cos\theta)$."
    )
    st.write(f"n = ({nx:.3f}, {ny:.3f}, {nz:.3f})")

u = np.linspace(0, 2 * np.pi, 48)
v = np.linspace(0, np.pi, 24)
uu, vv = np.meshgrid(u, v)
xs = np.cos(uu) * np.sin(vv)
ys = np.sin(uu) * np.sin(vv)
zs = np.cos(vv)

fig = go.Figure()
fig.add_trace(
    go.Surface(
        x=xs,
        y=ys,
        z=zs,
        opacity=0.25,
        showscale=False,
        colorscale=[[0, "#475569"], [1, "#475569"]],
        hoverinfo="skip",
    )
)
fig.add_trace(
    go.Scatter3d(
        x=[0, nx],
        y=[0, ny],
        z=[0, nz],
        mode="lines+markers",
        line=dict(color="#38bdf8", width=8),
        marker=dict(size=[0, 8], color=["#94a3b8", "#f97316"]),
        name="n",
    )
)
fig.update_layout(
    template="plotly_dark",
    height=560,
    margin=dict(l=0, r=0, t=30, b=0),
    scene=dict(
        aspectmode="data",
        xaxis=dict(range=[-1.1, 1.1], title="x"),
        yaxis=dict(range=[-1.1, 1.1], title="y"),
        zaxis=dict(range=[-1.1, 1.1], title="z"),
    ),
    showlegend=False,
)

with col2:
    st.plotly_chart(fig, use_container_width=True)

with st.expander("Key points"):
    st.markdown(
        r"""
- **Opposite points** on the sphere correspond to **orthogonal** states.
- An overall phase factor on $|\psi\rangle$ does not move the Bloch vector; only the relative phase between $|0\rangle$
  and $|1\rangle$ (here, **φ**) rotates the vector in the **xy** plane.
"""
    )
