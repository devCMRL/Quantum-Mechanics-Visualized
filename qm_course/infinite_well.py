"""Infinite square well on [0, L] (units: ħ=m=L=1 unless noted)."""

from __future__ import annotations

import numpy as np


def energy_eigenvalue(n: int, L: float = 1.0, m: float = 1.0) -> float:
    """E_n = (ħ² π² n²) / (2 m L²). With ħ=1: π² n² / (2 m L²)."""
    return (np.pi**2) * (n**2) / (2 * m * (L**2))


def stationary_state(x: np.ndarray, n: int, L: float = 1.0) -> np.ndarray:
    """Unnormalized sin basis on [0,L]; zero outside."""
    psi = np.zeros_like(x, dtype=float)
    inside = (x >= 0) & (x <= L)
    psi[inside] = np.sqrt(2 / L) * np.sin(n * np.pi * x[inside] / L)
    return psi


def superposition(
    x: np.ndarray,
    coeffs: np.ndarray,
    ns: np.ndarray,
    L: float = 1.0,
) -> np.ndarray:
    """ψ(x) = Σ_j c_j φ_{n_j}(x) with real c_j; ns are mode indices (integers >=1)."""
    psi = np.zeros_like(x, dtype=complex)
    c = np.asarray(coeffs, dtype=complex)
    for coeff, n in zip(c, ns, strict=True):
        psi += coeff * stationary_state(x, int(n), L=L)
    return psi


def time_evolve_coeffs(coeffs: np.ndarray, ns: np.ndarray, t: float, L: float = 1.0, m: float = 1.0) -> np.ndarray:
    """c_n(t) = c_n(0) exp(-i E_n t / ħ), ħ=1."""
    E = np.array([energy_eigenvalue(int(n), L=L, m=m) for n in ns])
    return np.asarray(coeffs, dtype=complex) * np.exp(-1j * E * t)
