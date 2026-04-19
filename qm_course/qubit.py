"""Qubit Pauli algebra and common expectations (units ħ = 1, Pauli not divided by 2)."""

from __future__ import annotations

import numpy as np

SIGMA_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SIGMA_Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
SIGMA_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
IDENTITY = np.eye(2, dtype=complex)


def ket_from_bloch(theta: float, phi: float) -> np.ndarray:
    """|ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩."""
    return np.array(
        [np.cos(theta / 2), np.exp(1.0j * phi) * np.sin(theta / 2)],
        dtype=complex,
    )


def expectation_pauli(ket: np.ndarray, sigma: np.ndarray) -> float:
    return float(np.real(np.vdot(ket, sigma @ ket)))


def variance_pauli(ket: np.ndarray, sigma: np.ndarray) -> float:
    """For Pauli, σ² = I ⇒ Var(σ) = 1 − ⟨σ⟩²."""
    m = expectation_pauli(ket, sigma)
    return max(0.0, 1.0 - m * m)


def expectation_n_dot_sigma(ket: np.ndarray, nx: float, ny: float, nz: float) -> float:
    nvec = np.array([nx, ny, nz], dtype=float)
    nrm = float(np.linalg.norm(nvec))
    if nrm < 1e-12:
        return 0.0
    nx, ny, nz = nvec / nrm
    H = nx * SIGMA_X + ny * SIGMA_Y + nz * SIGMA_Z
    return expectation_pauli(ket, H)


def robertson_sigma_x_sigma_z(ket: np.ndarray) -> tuple[float, float, float, float]:
    """
    Inequality Δσx Δσz ≥ |⟨σy⟩| for Pauli matrices (pure qubit states).

    Returns (Δσx, Δσz, |⟨σy⟩|, (Δσx Δσz) − |⟨σy⟩|) which should be ≥ 0.
    """
    dsx = float(np.sqrt(variance_pauli(ket, SIGMA_X)))
    dsz = float(np.sqrt(variance_pauli(ket, SIGMA_Z)))
    lhs = dsx * dsz
    sigy = expectation_pauli(ket, SIGMA_Y)
    rhs = abs(sigy)
    return dsx, dsz, rhs, lhs - rhs
