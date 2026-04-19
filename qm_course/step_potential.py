"""Potential step V=0 for x<0 and V=V0 for x>0 (units m=ħ=1)."""

from __future__ import annotations

import numpy as np


def psi_step_complex(x: np.ndarray, E: float, V0: float, m: float = 1.0) -> np.ndarray:
    """Stationary scattering state: unit incident amplitude from the left."""
    E = max(float(E), 1e-9)
    V0 = float(V0)
    k1 = np.sqrt(2 * m * E + 0j)

    psi = np.zeros_like(x, dtype=complex)
    left = x < 0
    right = x >= 0

    if E >= V0:
        k2 = np.sqrt(2 * m * (E - V0) + 0j)
        r = (k1 - k2) / (k1 + k2)
        t = 2 * k1 / (k1 + k2)
        psi[left] = np.exp(1j * k1 * x[left]) + r * np.exp(-1j * k1 * x[left])
        psi[right] = t * np.exp(1j * k2 * x[right])
    else:
        kappa = float(np.sqrt(2 * m * (V0 - E)))
        r = (k1 - 1j * kappa) / (k1 + 1j * kappa)
        t = 2 * k1 / (k1 + 1j * kappa)
        psi[left] = np.exp(1j * k1 * x[left]) + r * np.exp(-1j * k1 * x[left])
        psi[right] = t * np.exp(-kappa * x[right])

    return psi


def plane_wave_step_real(x: np.ndarray, E: float, V0: float, m: float = 1.0) -> np.ndarray:
    return np.real(psi_step_complex(x, E, V0, m=m))
