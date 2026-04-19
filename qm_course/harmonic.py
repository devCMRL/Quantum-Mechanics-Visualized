"""1D quantum harmonic oscillator (units ħ=m=ω=1)."""

from __future__ import annotations

import math

import numpy as np
from scipy.special import eval_hermite


def psi_n(x: np.ndarray, n: int) -> np.ndarray:
    """Dimensionless oscillator eigenfunctions on the real line."""
    xi = np.asarray(x, dtype=float)
    Hn = eval_hermite(n, xi)
    norm = (2.0**n * math.factorial(n) * math.sqrt(math.pi)) ** 0.5
    return (np.pi ** (-0.25)) * np.exp(-(xi**2) / 2) * Hn / norm


def energy_eigenvalue(n: int) -> float:
    return n + 0.5
