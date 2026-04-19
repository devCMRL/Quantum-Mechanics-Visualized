"""Chapter 2 — finite-dimensional complex Hilbert space (column kets)."""

import numpy as np
import streamlit as st

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
