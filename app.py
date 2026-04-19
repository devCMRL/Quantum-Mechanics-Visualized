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

st.markdown("#### Part I — Postulates, Hilbert space, measurement")
st.markdown(
    r"""
| Ch. | Topic | Focus |
|---:|--------|--------|
| 10 | Five postulates roadmap | Axioms mapped to chapter content |
| 11 | Finite Hilbert space | Vectors in **ℂ^N**, norm, inner product, metric on rays |
| 12 | Born rule and measurement | **2×2** Hermitian **H**, Born weights, single-shot sampling |
| 13 | Pauli observables | Expectations **⟨σx⟩, ⟨σy⟩, ⟨σz⟩**, directional **⟨n·σ⟩** |
| 14 | Uncertainty (σx, σz) | Product **Δσx Δσz** vs **|⟨σy⟩|** |
"""
)

st.markdown("#### Part II — Wave mechanics and models")
st.markdown(
    r"""
| Ch. | Topic | Focus |
|---:|--------|--------|
| 1 | Free Gaussian packet | **Re ψ(x)** vs width, shift, wavenumber |
| 2 | Infinite square well | Eigenstates and three-mode superposition |
| 3 | Harmonic oscillator | **|ψₙ|²** and classical turning points (**ħ = m = ω = 1**) |
| 4 | Rectangular barrier | Transmission **T(E)** and schematic **V(x)** |
| 5 | Potential step | **Re ψ**, reflection probability, flux above threshold |
| 6 | Double-slit interference | Fraunhofer intensity vs geometry and wavelength |
| 7 | Hydrogen angular factor | **|Y_ℓ^m|²** on the unit sphere |
| 8 | Bloch sphere | Pure qubit state from polar angles |
| 9 | Time evolution in a box | Four-level superposition and **|ψ(x,t)|²** |
"""
)
