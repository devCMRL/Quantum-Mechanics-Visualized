import streamlit as st

st.set_page_config(
    page_title="QM Visual",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("QM Visual")
st.caption("Interactive quantum mechanics: formalism in finite dimensions and representative wave-mechanics models.")

st.markdown(
    """
Use the **sidebar** to open a chapter. Each page combines short analytic context with adjustable parameters and figures.

Expand **Key points** at the bottom of a chapter for a concise summary of the physics illustrated there.
"""
)

st.divider()
st.subheader("Course index")

st.markdown("#### Part I — Postulates, Hilbert space, measurement (Ch. 1–5)")
st.markdown(
    r"""
| Ch. | Topic | Focus |
|---:|--------|--------|
| 1 | Five postulates roadmap | Axioms mapped to chapter content |
| 2 | Finite Hilbert space | Vectors in **ℂ^N**, norm, inner product, metric on rays |
| 3 | Born rule and measurement | **2×2** Hermitian **H**, Born weights, single-shot sampling |
| 4 | Pauli observables | Expectations **⟨σx⟩, ⟨σy⟩, ⟨σz⟩**, directional **⟨n·σ⟩** |
| 5 | Uncertainty (σx, σz) | Product **Δσx Δσz** vs **|⟨σy⟩|** |
"""
)

st.markdown("#### Part II — Wave mechanics and models (Ch. 6–14)")
st.markdown(
    r"""
| Ch. | Topic | Focus |
|---:|--------|--------|
| 6 | Free Gaussian packet | **Re ψ(x)** vs width, shift, wavenumber |
| 7 | Infinite square well | Eigenstates and three-mode superposition |
| 8 | Harmonic oscillator | **|ψₙ|²** and classical turning points (**ħ = m = ω = 1**) |
| 9 | Rectangular barrier | Transmission **T(E)** and schematic **V(x)** |
| 10 | Potential step | **Re ψ**, reflection probability, flux above threshold |
| 11 | Double-slit interference | Fraunhofer intensity vs geometry and wavelength |
| 12 | Hydrogen angular factor | **|Y_ℓ^m|²** on the unit sphere |
| 13 | Bloch sphere | Pure qubit state from polar angles |
| 14 | Time evolution in a box | Four-level superposition and **|ψ(x,t)|²** |
"""
)
