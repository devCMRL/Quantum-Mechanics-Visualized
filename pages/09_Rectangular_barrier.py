"""Chapter 9 — rectangular barrier transmission."""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from qm_course.barrier import transmission_probability
from qm_course.figures import style_figure

st.set_page_config(page_title="Ch 9 — Barrier tunneling", layout="wide")

st.title("Chapter 9 — Rectangular barrier")
st.caption("Analytic transmission T(E) for a barrier V₀ on [0, a] with m = ħ = 1.")

col1, col2 = st.columns([1, 2])
with col1:
    V0 = st.slider("Barrier height V₀", 0.5, 8.0, 3.0, 0.1)
    a = st.slider("Barrier width a", 0.2, 4.0, 1.5, 0.05)
    E_max = st.slider("Maximum energy on axis", 2.0, 15.0, 8.0, 0.5)

E = np.linspace(0.02, E_max, 1200)
T = transmission_probability(E, V0=V0, a=a)

fig = make_subplots(rows=2, cols=1, row_heights=[0.62, 0.38], vertical_spacing=0.12)
fig.add_trace(go.Scatter(x=E, y=T, mode="lines", name="T(E)"), row=1, col=1)
fig.add_hline(y=1.0, line_dash="dot", line_color="#64748b", row=1, col=1)
fig.add_hline(y=V0, line_dash="dash", line_color="#f97316", row=2, col=1, annotation_text="V₀")
# schematic: V(x)
xs = np.concatenate([[-2, 0], np.linspace(0, a, 80), [a, a + 2]])
Vs = np.concatenate([[0, 0], np.full(80, V0), [0, 0]])
fig.add_trace(go.Scatter(x=xs, y=Vs, mode="lines", fill="tozeroy", name="V(x)"), row=2, col=1)
fig.update_xaxes(title_text="E", row=1, col=1)
fig.update_yaxes(title_text="T", range=[0, 1.05], row=1, col=1)
fig.update_xaxes(title_text="x (schematic)", row=2, col=1)
fig.update_yaxes(title_text="V", row=2, col=1)
style_figure(fig, height=560)
fig.update_layout(hovermode="x unified", showlegend=False)

with col2:
    st.plotly_chart(fig, use_container_width=True)
with col1:
    st.markdown(
        r"""
**Tunneling:** for **E < V₀**, T(E) is generally **nonzero** — a classical particle would be fully reflected.

**Above barrier:** for **E > V₀**, T(E) oscillates because reflected and transmitted waves interfere.
"""
    )

with st.expander("Key points"):
    st.markdown(
        """
- Thicker or higher barriers **suppress** tunneling, but do not eliminate it at any fixed E < V₀.
- When **E > V₀**, resonant-like features in T(E) come from **interference** of multiple paths inside the barrier region.
"""
    )
