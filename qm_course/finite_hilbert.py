"""Finite-dimensional complex Hilbert space helpers (column kets)."""

from __future__ import annotations

import numpy as np


def as_ket(coeffs: np.ndarray) -> np.ndarray:
    v = np.asarray(coeffs, dtype=complex).reshape(-1)
    return v


def norm(v: np.ndarray) -> float:
    return float(np.linalg.norm(as_ket(v)))


def normalize(v: np.ndarray) -> np.ndarray:
    v = as_ket(v)
    n = norm(v)
    if n < 1e-15:
        return np.zeros_like(v)
    return v / n


def inner(bra: np.ndarray, ket: np.ndarray) -> complex:
    """⟨bra|ket⟩ using column vectors: conjugate(bra)ᵀ ket."""
    return complex(np.vdot(as_ket(bra), as_ket(ket)))


def expectation(H: np.ndarray, ket: np.ndarray) -> complex:
    """⟨ψ|H|ψ⟩ with ket normalized (caller should normalize)."""
    psi = as_ket(ket)
    return complex(np.vdot(psi, H @ psi))


def variance(H: np.ndarray, ket: np.ndarray) -> float:
    """Var(H) = ⟨H²⟩ − ⟨H⟩² for Hermitian H."""
    psi = as_ket(ket)
    e1 = expectation(H, psi)
    e2 = expectation(H @ H, psi)
    return float(np.real(e2 - e1**2))


def born_probabilities(H: np.ndarray, ket: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Spectral decomposition of Hermitian H: return eigenvalues, eigenvectors as columns,
    expansion coefficients c_i = ⟨E_i|ψ⟩, and Born weights p_i = |c_i|².
    """
    psi = as_ket(ket)
    nrm = norm(psi)
    if nrm < 1e-15:
        psi = np.zeros_like(psi, dtype=complex)
        psi[0] = 1.0 + 0.0j
    else:
        psi = psi / nrm
    evals, evecs = np.linalg.eigh(H)
    c = np.conj(evecs.T) @ psi
    p = np.real(c * np.conj(c))
    p = np.maximum(p, 0.0)
    s = p.sum()
    if s > 1e-15:
        p = p / s
    return evals, evecs, c, p
