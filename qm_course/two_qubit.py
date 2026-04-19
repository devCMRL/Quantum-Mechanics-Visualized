"""Two-qubit pure states: probabilities, partial traces, Bloch components."""

from __future__ import annotations

import numpy as np

from qm_course.qubit import SIGMA_X, SIGMA_Y, SIGMA_Z


def ket_00() -> np.ndarray:
    return np.array([1, 0, 0, 0], dtype=complex)


def ket_11() -> np.ndarray:
    return np.array([0, 0, 0, 1], dtype=complex)


def ket_phi_plus() -> np.ndarray:
    return (ket_00() + ket_11()) / np.sqrt(2)


def ket_phi_minus() -> np.ndarray:
    return (ket_00() - ket_11()) / np.sqrt(2)


def ket_psi_plus() -> np.ndarray:
    return (np.array([0, 1, 0, 0], dtype=complex) + np.array([0, 0, 1, 0], dtype=complex)) / np.sqrt(2)


def ket_psi_minus() -> np.ndarray:
    return (np.array([0, 1, 0, 0], dtype=complex) - np.array([0, 0, 1, 0], dtype=complex)) / np.sqrt(2)


def ket_separable_plus_plus() -> np.ndarray:
    p = (np.array([1, 1], dtype=complex) / np.sqrt(2.0))
    return np.kron(p, p)


def ket_schmidt_real(theta: float, phi: float) -> np.ndarray:
    """cos θ |00⟩ + e^{iφ} sin θ |11⟩ (normalized)."""
    return np.cos(theta) * ket_00() + np.exp(1j * phi) * np.sin(theta) * ket_11()


def probabilities(psi: np.ndarray) -> np.ndarray:
    psi = np.asarray(psi, dtype=complex).reshape(4)
    p = np.real(np.conjugate(psi) * psi)
    return np.maximum(p, 0.0)


def partial_trace_A(psi: np.ndarray) -> np.ndarray:
    """Trace out qubit B (right tensor factor); basis |ij⟩ with index 2i + j."""
    psi = np.asarray(psi, dtype=complex).reshape(4)
    rho = np.outer(psi, np.conjugate(psi))
    ra = np.zeros((2, 2), dtype=complex)
    for i in range(2):
        for ip in range(2):
            ra[i, ip] = sum(rho[2 * i + j, 2 * ip + j] for j in range(2))
    return ra


def partial_trace_B(psi: np.ndarray) -> np.ndarray:
    psi = np.asarray(psi, dtype=complex).reshape(4)
    rho = np.outer(psi, np.conjugate(psi))
    rb = np.zeros((2, 2), dtype=complex)
    for j in range(2):
        for jp in range(2):
            rb[j, jp] = sum(rho[2 * i + j, 2 * i + jp] for i in range(2))
    return rb


def bloch_components(rho: np.ndarray) -> tuple[float, float, float]:
    """Expectation (Tr ρσx, Tr ρσy, Tr ρσz) for a qubit density matrix ρ."""
    nx = float(np.real(np.trace(rho @ SIGMA_X)))
    ny = float(np.real(np.trace(rho @ SIGMA_Y)))
    nz = float(np.real(np.trace(rho @ SIGMA_Z)))
    return nx, ny, nz


def concurrence(psi: np.ndarray) -> float:
    """Concurrence of a normalized two-qubit pure state (basis |00⟩,|01⟩,|10⟩,|11⟩). Range [0, 1]."""
    a, b, c, d = np.asarray(psi, dtype=complex).reshape(4)
    return float(np.clip(2.0 * np.abs(a * d - b * c), 0.0, 1.0))
