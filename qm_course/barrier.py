"""Rectangular barrier V(x)=V0 on [0,a], zero elsewhere (units m=ħ=1)."""

from __future__ import annotations

import numpy as np


def transmission_probability(E: np.ndarray, V0: float, a: float, m: float = 1.0) -> np.ndarray:
    """Transmission coefficient T(E) for a plane wave incident from the left."""
    E = np.maximum(np.asarray(E, dtype=float), 1e-15)
    V0 = float(V0)
    a = float(a)
    m = float(m)

    T = np.zeros_like(E, dtype=float)

    mask_osc = E >= V0
    if np.any(mask_osc):
        k = np.sqrt(2 * m * E[mask_osc])
        k2 = np.sqrt(2 * m * (E[mask_osc] - V0))
        sin2 = np.sin(k2 * a) ** 2
        T_osc = 4 * (k**2) * (k2**2) / (4 * (k**2) * (k2**2) + (k**2 - k2**2) ** 2 * sin2 + 1e-30)
        T[mask_osc] = np.clip(T_osc, 0.0, 1.0)

    mask_tun = (E > 0) & (E < V0)
    if np.any(mask_tun):
        k = np.sqrt(2 * m * E[mask_tun])
        kappa = np.sqrt(2 * m * (V0 - E[mask_tun]))
        sinh2 = np.sinh(kappa * a) ** 2
        T_tun = 4 * (k**2) * (kappa**2) / (4 * (k**2) * (kappa**2) + (k**2 + kappa**2) ** 2 * sinh2 + 1e-30)
        T[mask_tun] = np.clip(T_tun, 0.0, 1.0)

    return T
