"""Chapter 10 — standard postulates mapped to course chapters."""

import streamlit as st

st.set_page_config(page_title="Ch 10 — Postulates roadmap", layout="wide")

st.title("Chapter 10 — Five postulates (roadmap)")
st.caption("Standard axioms and the chapters where each is exercised numerically.")

st.markdown(
    r"""
Most undergraduate treatments organize quantum mechanics around five structural statements. Below, each is
stated briefly and tied to the corresponding modules in this course.

### 1. States (Hilbert space)
A pure state is a normalized vector $|\psi\rangle$ in a complex inner-product space $\mathcal{H}$.
One-dimensional wavefunctions $\psi(x)$ and two-level (qubit) states in $\mathbb{C}^2$ are the two representations used most heavily here.

**Chapters:** **11** (finite-dimensional $\mathbb{C}^N$), **1–3**, **9** (position representation on a line), **8** (qubit geometry).

### 2. Observables (self-adjoint operators)
Physical quantities correspond to Hermitian operators $A = A^\dagger$; spectral values are admissible measurement outcomes when the usual idealizations apply.

**Chapters:** **13** (Pauli matrices on $\mathbb{C}^2$), **12** (a Hamiltonian as a $2\times2$ observable), **2–3** (Hamiltonian eigenfunctions in concrete potentials).

### 3. Measurement (Born rule)
For an ideal projective measurement in an orthonormal basis $\{|u_i\rangle\}$, outcome $i$ occurs with probability
$p_i = |\langle u_i|\psi\rangle|^2$. After the event, the state is taken to lie along $|u_i\rangle$ (up to phase) in the textbook collapse picture.

**Chapters:** **12** (Born weights and repeated sampling of one observable).

### 4. Time evolution (Schrödinger equation)
Isolated systems evolve unitarily: $|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$.

**Chapters:** **9** (superposition of box eigenstates with time-dependent relative phases). Chapter **14** addresses static uncertainty relations at a fixed time, not unitary evolution.

### 5. Identical particles
Many-body wavefunctions must carry the correct permutation symmetry (bosonic or fermionic). Symmetrized product bases and antisymmetric Slater-type constructions are standard material but lie outside the present chapter list.

---

Chapters **11–14** concentrate on finite-dimensional algebra, measurement, and Pauli-based uncertainty; chapters **1–9** concentrate on one-dimensional stationary and time-dependent problems plus one spherical-harmonic visualization.
"""
)

st.markdown(
    """
**Suggested order:** 11 → 12 → 13 → 14, then 2 and 9 for eigenfunction expansions and their time dependence.
"""
)
