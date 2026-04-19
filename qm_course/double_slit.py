"""Two-slit interference intensity (scalar wave model)."""

from __future__ import annotations

import numpy as np


def intensity_on_screen(
    y: np.ndarray,
    d: float,
    a: float,
    L: float,
    k: float,
    I0: float = 1.0,
) -> np.ndarray:
    """
    Fraunhofer-style pattern along transverse coordinate y on a screen at distance L.
    d: slit separation, a: slit width, k: wavenumber 2π/λ.
    """
    theta = y / L
    beta = 0.5 * k * a * theta
    delta = 0.5 * k * d * theta
    single = np.sinc(beta / np.pi)  # numpy sinc is sin(pi x)/(pi x)
    twin = np.cos(delta) ** 2
    return I0 * (single**2) * twin
