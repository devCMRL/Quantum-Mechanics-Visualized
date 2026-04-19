"""Shared Plotly layout defaults for chapter pages."""

from __future__ import annotations

from plotly.graph_objects import Figure


def style_figure(fig: Figure, height: int = 520) -> Figure:
    fig.update_layout(
        height=height,
        template="plotly_dark",
        margin=dict(l=40, r=20, t=40, b=40),
        hovermode="x unified",
    )
    return fig
