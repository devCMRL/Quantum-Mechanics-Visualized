"""Hydrogen angular probability |Y_l^m|^² on the unit sphere."""

from __future__ import annotations

import numpy as np

try:
    from scipy.special import sph_harm_y
except ImportError:  # pragma: no cover - older SciPy
    from scipy.special import sph_harm as _sph_harm_legacy

    def sph_harm_y(n, m, theta, phi):
        return _sph_harm_legacy(m, n, phi, theta)


def angular_probability_mesh(l: int, m: int, n_theta: int = 90, n_phi: int = 120):
    theta = np.linspace(0.0, np.pi, n_theta)
    phi = np.linspace(0.0, 2 * np.pi, n_phi)
    TH, PH = np.meshgrid(theta, phi, indexing="ij")
    Y = sph_harm_y(l, m, TH, PH)
    prob = np.real(Y * np.conj(Y))
    X = np.sin(TH) * np.cos(PH)
    Yc = np.sin(TH) * np.sin(PH)
    Z = np.cos(TH)
    return X, Yc, Z, prob
