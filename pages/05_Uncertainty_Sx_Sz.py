"""Chapter 5 — Robertson-type uncertainty for Pauli σx and σz on a pure qubit."""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from qm_course.figures import style_figure
from qm_course.qubit import ket_from_bloch, robertson_sigma_x_sigma_z

st.set_page_config(page_title="Ch 5 — Uncertainty σx σz", layout="wide")

st.title("Chapter 5 — Uncertainty: Δσx Δσz vs |⟨σy⟩|")
st.caption(
    "Pure qubit from Bloch angles. For Pauli matrices, Δσx Δσz ≥ |⟨σy⟩| (Robertson form specialized to this pair)."
)

col1, col2 = st.columns([1, 2])
with col1:
    theta_deg = st.slider("θ (deg)", 0.0, 180.0, 70.0, 1.0)
    phi_deg = st.slider("φ (deg)", 0.0, 360.0, 120.0, 1.0)
    theta = np.deg2rad(theta_deg)
    phi = np.deg2rad(phi_deg)
    ket = ket_from_bloch(theta, phi)
    dsx, dsz, rhs, slack = robertson_sigma_x_sigma_z(ket)
    lhs = dsx * dsz
    st.metric("Δσx", f"{dsx:.4f}")
    st.metric("Δσz", f"{dsz:.4f}")
    st.metric("|⟨σy⟩|", f"{rhs:.4f}")
    st.metric("Δσx Δσz − |⟨σy⟩|", f"{slack:.4f}", help="Non-negative for the pure states shown here.")

fig = go.Figure(
    go.Bar(
        x=["Δσx Δσz", "|⟨σy⟩|"],
        y=[lhs, rhs],
        marker_color=["#38bdf8", "#f97316"],
    )
)
fig.update_yaxes(title_text="Value")
fig.update_layout(showlegend=False)
style_figure(fig, height=400)

with col2:
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
    r"""
Because **σx² = σz² = I**, each variance obeys $\Delta\sigma_x^2 = 1 - \langle\sigma_x\rangle^2$ (and analogously for **z**).
The bars compare **$\Delta\sigma_x\Delta\sigma_z$** to **$|\langle\sigma_y\rangle|$**, the Robertson lower bound for this Pauli pair on a pure state.
"""
)

with st.expander("Key points"):
    st.markdown(
        """
- Non-commuting observables constrain how sharply both can be narrow for one and the same pure state.
- Along **|0⟩** or **|1⟩**, one of **Δσx** or **Δσz** vanishes and **|⟨σy⟩|** vanishes, so the inequality holds with equality at zero.
"""
    )
