"""Independent numerical/analytic checks for C5 R19-24.

This does not import the worker runner.  It reconstructs the G(b) symbol from
its stated derivative using direct scipy quadrature (rather than the archived
spline), integrates Euclidean time adaptively, and evaluates the two-loop
coordinate moments independently.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad, quad_vec


def smooth_step(x: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    left = np.exp(-1.0 / x)
    right = np.exp(-1.0 / (1.0 - x))
    return float(left / (left + right))


def g_symbol(k: np.ndarray, b: float = 2.526103698477) -> np.ndarray:
    """G(b)=h^2 from h'=1-smooth_step((|k|-b)/(pi-b))."""
    a = np.abs((k + np.pi) % (2.0 * np.pi) - np.pi)
    w = np.pi - b
    h = np.empty_like(a)
    for index, value in np.ndenumerate(a):
        if value <= b:
            h[index] = value
        else:
            integral = quad(
                lambda z: smooth_step((z - b) / w),
                b,
                float(value),
                epsabs=2e-14,
                epsrel=2e-14,
            )[0]
            h[index] = value - integral
    return h * h


def sunset_euclidean(L: int, mass: float, edge: str) -> tuple[float, float, float]:
    k = 2.0 * np.pi * np.fft.fftfreq(L)
    if edge == "NN":
        one_dimensional = 4.0 * np.sin(k / 2.0) ** 2
    elif edge == "G(2.526)":
        one_dimensional = g_symbol(k)
    else:
        raise ValueError(edge)

    energy = np.sqrt(
        mass * mass
        + one_dimensional[:, None, None]
        + one_dimensional[None, :, None]
        + one_dimensional[None, None, :]
    )
    x = np.fft.fftfreq(L) * L
    x1_squared = x[:, None, None] ** 2

    def moments(tau: float) -> np.ndarray:
        propagator = np.fft.ifftn(np.exp(-energy * tau) / (2.0 * energy)).real
        cube = propagator**3
        return np.array(
            [2.0 * np.sum(x1_squared * cube), 2.0 * tau * tau * np.sum(cube)]
        )

    # The omitted tail is bounded by the mass gap and is negligible here.
    ax2, at2 = quad_vec(
        moments,
        0.0,
        120.0,
        epsabs=2e-12,
        epsrel=2e-10,
        limit=300,
    )[0]
    prefactor = -1.0 / 6.0
    dp2 = prefactor * (-0.5 * ax2)
    dw2 = prefactor * (-0.5 * at2)
    return float(dp2 - dw2), float(dp2), float(dw2)


def z4_control(L: int, mass: float) -> tuple[float, float, float]:
    k = 2.0 * np.pi * np.fft.fftfreq(L)
    one_dimensional = 4.0 * np.sin(k / 2.0) ** 2
    denominator = (
        mass * mass
        + one_dimensional[:, None, None, None]
        + one_dimensional[None, :, None, None]
        + one_dimensional[None, None, :, None]
        + one_dimensional[None, None, None, :]
    )
    cube = np.fft.ifftn(1.0 / denominator).real**3
    x = np.fft.fftfreq(L) * L
    prefactor = -1.0 / 6.0
    dt2 = prefactor * (-0.5) * np.sum(x[:, None, None, None] ** 2 * cube)
    dx2 = prefactor * (-0.5) * np.sum(x[None, :, None, None] ** 2 * cube)
    return float(dx2 - dt2), float(dx2), float(dt2)


def main() -> None:
    conversion = (16.0 * np.pi**2) ** 2
    print("one-loop: tadpole is momentum independent, so delta_c2/lambda = 0 exactly")
    for edge in ("NN", "G(2.526)"):
        shift, dp2, dw2 = sunset_euclidean(64, 0.2, edge)
        print(
            f"{edge:8s} L=64 m=0.2: shift/lambda^2={shift:+.9e}; "
            f"normalized={shift * conversion:+.6f}; dp2={dp2:+.9e}; dw2={dw2:+.9e}"
        )
    residual, dx2, dt2 = z4_control(24, 0.3)
    print(
        f"Z4 L=24 m=0.3: residual/lambda^2={residual:+.9e}; "
        f"dx2={dx2:+.9e}; dt2={dt2:+.9e}"
    )


if __name__ == "__main__":
    main()
