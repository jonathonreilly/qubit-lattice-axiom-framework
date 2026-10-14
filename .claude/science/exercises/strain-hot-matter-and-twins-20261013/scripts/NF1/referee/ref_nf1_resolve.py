"""Referee re-solve of NF-1's three rows with corrected taste multiplicity.

The worker correctly derives one staggered field as one quarter of a naive
four-component full-zone trace, but its solve multiplies that already-divided
row by N_s/4.  Here the total is N_s * (naive/4), as required for N_s
staggered fields (two continuum Dirac tastes per field).
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "flat"))
os.chdir(ROOT / "flat")

import smud_lib  # noqa: E402
from content4 import scalw  # noqa: E402
from r1712_lib import photonGw, xi  # noqa: E402
from zz import mu_E  # noqa: E402


NSCALAR = 4.0
NVECTOR = 12.0
MASS = 0.01
PHOTON_BG = 0.6
PHOTON_FW = 0.5
PHOTON_N = int(os.environ.get("NF1_REF_PHOTON_N", "32"))


def photon_rows() -> tuple[dict[str, np.ndarray], float]:
    law = photonGw(PHOTON_BG, PHOTON_FW * (np.pi - PHOTON_BG))
    coeff: dict[str, np.ndarray] = {}
    for polarization in ("T2g", "Eg"):
        values = np.array(
            [xi(law, PHOTON_N, polarization, "VWa", lam=a)[0] for a in (0.0, 1.0, -1.0)]
        )
        coeff[polarization] = np.array(
            [values[0], 0.5 * (values[1] - values[2]), 0.5 * (values[1] + values[2]) - values[0]]
        )
    g, f = law.samples(1 << 14)
    return coeff, 2 * mu_E(g, f, 1e-3)


def solve_content(n_staggered: float, photon: dict[str, np.ndarray], photon_mu: float) -> None:
    calls = 0

    def components(z: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        nonlocal calls
        calls += 1
        bs, bf, a = z
        scalar = scalw(bs, 1.0, MASS, vert="U")[0][:3]
        staggered = smud_lib.dirac(bf, 0.0, m=MASS)[:3] / 4.0
        vector = np.array(
            [
                photon["T2g"] @ np.array([1.0, a, a * a]),
                photon["Eg"] @ np.array([1.0, a, a * a]),
                photon_mu,
            ]
        )
        total = NSCALAR * scalar + n_staggered * staggered + NVECTOR * vector
        return total, scalar, staggered, vector

    def residual(z: np.ndarray) -> np.ndarray:
        return components(z)[0] * 1e3

    starts = (
        np.array([2.4, 0.44, -0.104]),
        np.array([2.8, 0.32, -0.103]),
    )
    fits = []
    for start in starts:
        fit = least_squares(
            residual,
            start,
            bounds=([0.2, 0.05, -1.0], [3.12, 1.4, 1.0]),
            xtol=1e-12,
            ftol=1e-12,
            gtol=1e-12,
            diff_step=2e-6,
            max_nfev=50,
        )
        fits.append(fit)
    fit = min(fits, key=lambda item: np.linalg.norm(item.fun))
    total, scalar, staggered, vector = components(fit.x)
    jacobian = fit.jac / 1e3
    singular = np.linalg.svd(jacobian, compute_uv=False)
    print(
        f"N_s={n_staggered:.2f}: success={fit.success}, calls={calls}, "
        f"costnorm={np.linalg.norm(total):.6e}, active={fit.active_mask.tolist()}"
    )
    print(f"  knobs b_s={fit.x[0]:.9f} b_f={fit.x[1]:.9f} a={fit.x[2]:+.9f}")
    print(f"  per staggered field={staggered}")
    print(
        "  contributions scalar/staggered/vector="
        f"{NSCALAR * scalar} / {n_staggered * staggered} / {NVECTOR * vector}"
    )
    print(f"  total={total}; singular={singular}; det={np.linalg.det(jacobian):+.6e}", flush=True)


def main() -> None:
    begin = time.time()
    photon, photon_mu = photon_rows()
    print(
        f"photon gammaG_w({PHOTON_BG}, fw={PHOTON_FW}) N={PHOTON_N}: "
        f"T={photon['T2g']} E={photon['Eg']} muE={photon_mu:+.8e}",
        flush=True,
    )
    content = tuple(float(x) for x in os.environ.get("NF1_REF_CONTENT", "11.25,16,22.5").split(","))
    for n_staggered in content:
        solve_content(n_staggered, photon, photon_mu)
    print(f"elapsed={time.time() - begin:.1f}s")


if __name__ == "__main__":
    main()
