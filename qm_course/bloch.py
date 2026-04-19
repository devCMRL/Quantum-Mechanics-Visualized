"""Bloch-sphere coordinates for a pure qubit state."""

from __future__ import annotations

import numpy as np


def bloch_vector(theta: float, phi: float) -> tuple[float, float, float]:
    """|ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩  →  (nx, ny, nz) on the unit sphere."""
    return (
        float(np.sin(theta) * np.cos(phi)),
        float(np.sin(theta) * np.sin(phi)),
        float(np.cos(theta)),
    )
