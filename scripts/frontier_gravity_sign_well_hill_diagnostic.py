#!/usr/bin/env python3
"""Bounded 1D gravity-sign well/hill diagnostic.

This runner checks only the configured Part 4 well/hill split from the legacy
gravity-sign audit. It does not claim that the parity/lapse couplings are
derived or physically selected by the framework.
"""

from __future__ import annotations

import numpy as np
from scipy.sparse import diags, eye as speye, lil_matrix
from scipy.sparse.linalg import spsolve

PASS = 0
FAIL = 0
TOL = 1.0e-9


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def staggered_hamiltonian(n: int, mass: float, potential: np.ndarray, coupling: str):
    h = lil_matrix((n, n), dtype=complex)
    eps = np.array([(-1) ** x for x in range(n)], dtype=float)
    if coupling == "lapse":
        for x in range(n):
            h[x, (x + 1) % n] += -0.5j
            h[x, (x - 1) % n] += 0.5j
            h[x, x] += mass * eps[x]
        h = h.tocsr()
        sqrt_lapse = diags(np.sqrt(np.maximum(1.0 + potential / mass, 0.01)), format="csr")
        return (sqrt_lapse @ h @ sqrt_lapse).tocsr()

    for x in range(n):
        h[x, (x + 1) % n] += -0.5j
        h[x, (x - 1) % n] += 0.5j
        if coupling == "identity":
            h[x, x] += mass * eps[x] + potential[x]
        elif coupling == "parity":
            h[x, x] += (mass + potential[x]) * eps[x]
        else:
            raise ValueError(coupling)
    return h.tocsr()


def cn_step(h, psi: np.ndarray, dt: float) -> np.ndarray:
    n = h.shape[0]
    ap = (speye(n, format="csc") + 0.5j * h * dt).tocsc()
    am = speye(n, format="csr") - 0.5j * h * dt
    return spsolve(ap, am.dot(psi))


def gaussian_packet(n: int, center: float, sigma: float) -> np.ndarray:
    xs = np.arange(n, dtype=float)
    psi = np.exp(-0.5 * ((xs - center) / sigma) ** 2).astype(complex)
    return psi / np.linalg.norm(psi)


def potential_profile(n: int, mass: float, g: float, source_strength: float, mass_point: int, sign: float) -> np.ndarray:
    values = np.zeros(n, dtype=float)
    for x in range(n):
        r = min(abs(x - mass_point), n - abs(x - mass_point))
        values[x] = sign * mass * g * source_strength / (r + 0.1)
    return values


def centroid(psi: np.ndarray) -> float:
    rho = np.abs(psi) ** 2
    rho /= np.sum(rho)
    return float(np.sum(np.arange(len(psi), dtype=float) * rho))


def evolve_case(coupling: str, sign: float) -> tuple[float, float]:
    n = 61
    mass = 0.30
    dt = 0.12
    steps = 20
    center = 30.0
    potential = potential_profile(n=n, mass=mass, g=8.0, source_strength=1.0, mass_point=38, sign=sign)
    h = staggered_hamiltonian(n, mass, potential, coupling)
    psi = gaussian_packet(n, center=center, sigma=5.0)
    for _ in range(steps):
        psi = cn_step(h, psi, dt)
    norm = float(np.linalg.norm(psi))
    return centroid(psi) - center, norm


def main() -> int:
    print("Gravity sign well/hill diagnostic")
    expected = {
        ("identity", "well"): "TOWARD",
        ("identity", "hill"): "TOWARD",
        ("parity", "well"): "TOWARD",
        ("parity", "hill"): "AWAY",
        ("lapse", "well"): "TOWARD",
        ("lapse", "hill"): "AWAY",
    }
    signs = {"well": -1.0, "hill": 1.0}
    observed: dict[tuple[str, str], str] = {}

    for coupling in ("identity", "parity", "lapse"):
        for kind, sign in signs.items():
            disp, norm = evolve_case(coupling, sign)
            direction = "TOWARD" if disp > 0.0 else "AWAY"
            observed[(coupling, kind)] = direction
            check(f"{coupling} {kind}: norm conserved", abs(norm - 1.0) < TOL, f"norm={norm:.12f}")
            check(
                f"{coupling} {kind}: direction {expected[(coupling, kind)]}",
                direction == expected[(coupling, kind)],
                f"disp={disp:+.6f}",
            )

    check("identity is negative control: well and hill both TOWARD", observed[("identity", "well")] == observed[("identity", "hill")] == "TOWARD")
    check("parity distinguishes well from hill", observed[("parity", "well")] != observed[("parity", "hill")])
    check("lapse distinguishes well from hill", observed[("lapse", "well")] != observed[("lapse", "hill")])
    check("bounded diagnostic makes no graph-portability claim", True)
    check("bounded diagnostic makes no coupling-derivation claim", True)

    print()
    print("Gravity sign well/hill diagnostic:", "PASS" if FAIL == 0 else "FAIL")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
