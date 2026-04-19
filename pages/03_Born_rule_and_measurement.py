"""Chapter 3 — Born rule, expectation value of H, and projective measurement sampling."""

import numpy as np
import streamlit as st

from qm_course.finite_hilbert import born_probabilities, expectation, normalize

st.set_page_config(page_title="Ch 3 — Born rule", layout="wide")

st.title("Chapter 3 — Born rule and measuring an observable")
st.caption(
    "Real symmetric 2×2 Hamiltonian **H**: expansion in the eigenbasis, Born weights **pᵢ**, and single-shot sampling."
)

if "meas_hist" not in st.session_state:
    st.session_state.meas_hist = []

colA, colB = st.columns([1, 1])

with colA:
    st.subheader("Hamiltonian (real symmetric)")
    h00 = st.slider("H₀₀", -2.0, 2.0, 0.3, 0.05)
    h11 = st.slider("H₁₁", -2.0, 2.0, -0.4, 0.05)
    h01 = st.slider("Re H₀₁ = Re H₁₀", -1.5, 1.5, 0.45, 0.05)
    H = np.array([[h00, h01], [h01, h11]], dtype=complex)

with colB:
    st.subheader(r"State $|\psi\rangle$")
    r0 = st.slider("Re c₀", -1.0, 1.0, 0.85, 0.05)
    i0 = st.slider("Im c₀", -1.0, 1.0, 0.1, 0.05)
    r1 = st.slider("Re c₁", -1.0, 1.0, 0.2, 0.05)
    i1 = st.slider("Im c₁", -1.0, 1.0, 0.35, 0.05)
    psi = normalize(np.array([complex(r0, i0), complex(r1, i1)]))

evals, evecs, c, p = born_probabilities(H, psi)
eh = expectation(H, psi)

st.divider()
st.subheader("Spectral view")
mcol1, mcol2, mcol3 = st.columns(3)
with mcol1:
    st.metric(r"$\langle H\rangle$", f"{np.real(eh):.4f}")
with mcol2:
    st.metric(r"$p_0 = |c_0|^2$", f"{p[0]:.4f}")
with mcol3:
    st.metric(r"$p_1 = |c_1|^2$", f"{p[1]:.4f}")

st.markdown(
    rf"""
Eigenvalues **E₀ = {evals[0]:.4f}**, **E₁ = {evals[1]:.4f}** (ascending order).

Expansion coefficients **cᵢ = ⟨Eᵢ|ψ⟩** (display): c₀ = {c[0]:.3f}, c₁ = {c[1]:.3f}.
"""
)

if st.button("Draw one **H** outcome (Born distribution)", type="primary"):
    idx = int(np.random.choice([0, 1], p=p))
    st.session_state["last_idx"] = idx
    st.session_state.meas_hist.append(idx)
    st.success(
        f"Recorded outcome **i = {idx}**; eigenvalue **E_{idx} = {evals[idx]:.4f}**. "
        f"The post-measurement pure state lies along eigenvector **{idx}** of **H**."
    )

if st.session_state.meas_hist:
    hist = np.bincount(np.array(st.session_state.meas_hist, dtype=int), minlength=2)
    total = hist.sum()
    st.caption(
        f"Empirical frequencies after {total} trials: outcome 0 → {hist[0]/total:.2%}, "
        f"outcome 1 → {hist[1]/total:.2%}."
    )
    if st.button("Clear measurement history"):
        st.session_state.meas_hist = []
        st.session_state.pop("last_idx", None)
        st.rerun()

with st.expander("Key points"):
    st.markdown(
        r"""
- **Born weights** are $p_i = |\langle E_i|\psi\rangle|^2$ in the eigenbasis of the measured observable (**H**).
- For a normalized state, **$\langle H\rangle = \sum_i p_i E_i$** equals **$\langle\psi|H|\psi\rangle$**.
"""
    )
