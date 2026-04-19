"""Chapter 12 — hydrogen angular probability on the sphere."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.hydrogen_angular import angular_probability_mesh

st.set_page_config(page_title="Ch 12 — Hydrogen angular", layout="wide")

st.title("Chapter 12 — Hydrogen: angular probability density")
st.caption("Angular probability density |Y_ℓ^m(θ, φ)|² on the unit sphere (radial factor omitted).")

col1, col2 = st.columns([1, 2])
with col1:
    l = st.select_slider("Orbital quantum number l", options=list(range(0, 5)))
    m_options = list(range(-l, l + 1))
    m = st.select_slider("Magnetic quantum number m", options=m_options, value=0)
    gamma = st.slider("Color scale gamma", 0.3, 2.0, 0.7, 0.05)
    st.markdown(
        r"**Probability density** on the sphere for the angular factor in hydrogen-like atoms: "
        r"$|Y_{\ell}^{m}(\theta,\phi)|^2$."
    )

X, Y, Z, P = angular_probability_mesh(l, m, n_theta=72, n_phi=96)
P_vis = P ** float(gamma)
P_vis = P_vis / (np.max(P_vis) + 1e-12)

fig = go.Figure(
    data=[
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            surfacecolor=P_vis,
            colorscale="Viridis",
            showscale=True,
            colorbar=dict(title="|Y|² (γ-scaled)"),
        )
    ]
)
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="data",
    ),
    margin=dict(l=0, r=0, t=30, b=0),
    template="plotly_dark",
    height=560,
)

with col2:
    st.plotly_chart(fig, use_container_width=True)
with col1:
    st.caption("Rotate the surface with the pointer. Exponent γ < 1 rescales low-amplitude regions for contrast.")

with st.expander("Key points"):
    st.markdown(
        """
- **ℓ** controls overall angular complexity; **m** picks the quantization axis component and breaks rotational
  symmetry visibly when **m ≠ 0**.
- This is only the **angular** factor; adding radial functions **Rₙₗ(r)** produces full 3D probability clouds in space.
"""
    )
