#!/usr/bin/env python3
"""Bounded 1D gravity-sign well/hill diagnostic.

This runner checks only the configured Part 4 well/hill split from the legacy
gravity-sign audit. It does not claim that the parity/lapse couplings are
derived or physically selected by the framework.

Scope repair 2026-05-28
-----------------------
The bounded claim is narrowed to the identity (negative control) and parity
finite-sign reproduction. Those two couplings are pure on-site Hamiltonian
modifications and never apply any regularization: their code path does not
touch ``sqrt(N)`` or any floor.

The lapse coupling builds ``sqrt(N) H sqrt(N)`` with ``N = 1 + Phi/m``. For the
configured well potential the lapse goes deeply negative (``N`` reaches about
-79 with 15 sites at ``N <= 0``). The previous runner silently floored ``N`` to
0.01 before taking ``sqrt(N)``; that floor was unstated and load-bearing for the
lapse direction. The auditor verdict was that the lapse part does not close
against the cited lapse form. This runner therefore moves the lapse coupling out
of the bounded PASS/FAIL accounting and into an explicitly labelled, explicitly
floored diagnostic that reports the floor and the count of non-positive ``N``
sites. No floor is applied silently, and no floored lapse result is counted as
part of what closes. The lapse-closure part is OPEN; see the note.
"""

from __future__ import annotations

import numpy as np
from pathlib import Path
from scipy.sparse import diags, eye as speye, lil_matrix
from scipy.sparse.linalg import spsolve

NOTE = Path(__file__).resolve().parents[1] / "docs/GRAVITY_SIGN_AUDIT_2026-04-10.md"
PASS = 0
FAIL = 0
TOL = 1.0e-9

# Explicit, stated regularization for the OPEN lapse diagnostic only.
# This floor is NOT part of the bounded claim; it is printed loudly below.
LAPSE_FLOOR = 0.01


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
    """Build the on-site coupling Hamiltonian.

    identity / parity: pure on-site modification, no regularization applied.
    lapse: OPEN diagnostic only. The lapse N = 1 + Phi/m can be non-positive
    for the configured well; this path applies an EXPLICIT stated floor
    (LAPSE_FLOOR) and is not part of the bounded claim.
    """
    h = lil_matrix((n, n), dtype=complex)
    eps = np.array([(-1) ** x for x in range(n)], dtype=float)
    if coupling == "lapse":
        for x in range(n):
            h[x, (x + 1) % n] += -0.5j
            h[x, (x - 1) % n] += 0.5j
            h[x, x] += mass * eps[x]
        h = h.tocsr()
        lapse = 1.0 + potential / mass
        # EXPLICIT stated regularization (not silent): floor printed by caller.
        floored = np.maximum(lapse, LAPSE_FLOOR)
        sqrt_lapse = diags(np.sqrt(floored), format="csr")
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


def evolve_case(coupling: str, sign: float) -> tuple[float, float, np.ndarray]:
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
    return centroid(psi) - center, norm, potential


def lapse_negativity_report(sign: float) -> tuple[int, float]:
    """Return (count of N<=0 sites, min N) for the configured potential."""
    n = 61
    mass = 0.30
    potential = potential_profile(n=n, mass=mass, g=8.0, source_strength=1.0, mass_point=38, sign=sign)
    lapse = 1.0 + potential / mass
    return int(np.sum(lapse <= 0.0)), float(lapse.min())


def main() -> int:
    print("Gravity sign well/hill diagnostic")
    note_text = NOTE.read_text(encoding="utf-8")
    required_boundary = [
        "configured finite 1D diagnostic",
        "framework derivation of physical gravity sign",
        "No graph self-gravity result.",
        "No irregular-graph directional observable closure.",
        "No retained verdict and no direct ledger retag.",
        # The note must state the lapse-closure part is open and the floor explicit.
        "lapse-closure part is open",
        "explicit",
    ]
    for phrase in required_boundary:
        check(f"note boundary contains: {phrase}", phrase in note_text)

    signs = {"well": -1.0, "hill": 1.0}

    # ----------------------------------------------------------------------
    # BOUNDED CLAIM: identity (negative control) + parity finite-sign split.
    # These couplings never touch sqrt(N) or any floor.
    # ----------------------------------------------------------------------
    print()
    print("Bounded claim (no regularization applied; identity + parity only):")
    bounded_expected = {
        ("identity", "well"): "TOWARD",
        ("identity", "hill"): "TOWARD",
        ("parity", "well"): "TOWARD",
        ("parity", "hill"): "AWAY",
    }
    observed: dict[tuple[str, str], str] = {}
    for coupling in ("identity", "parity"):
        for kind, sign in signs.items():
            disp, norm, _ = evolve_case(coupling, sign)
            direction = "TOWARD" if disp > 0.0 else "AWAY"
            observed[(coupling, kind)] = direction
            check(f"{coupling} {kind}: norm conserved", abs(norm - 1.0) < TOL, f"norm={norm:.12f}")
            check(
                f"{coupling} {kind}: direction {bounded_expected[(coupling, kind)]}",
                direction == bounded_expected[(coupling, kind)],
                f"disp={disp:+.6f}",
            )

    check("identity is negative control: well and hill both TOWARD", observed[("identity", "well")] == observed[("identity", "hill")] == "TOWARD")
    check("parity distinguishes well from hill", observed[("parity", "well")] != observed[("parity", "hill")])

    # ----------------------------------------------------------------------
    # OPEN DIAGNOSTIC: lapse coupling. The configured well drives N negative,
    # so an EXPLICIT floor is required. This is reported, not silent, and is
    # NOT part of the bounded PASS/FAIL accounting.
    # ----------------------------------------------------------------------
    print()
    print("OPEN lapse diagnostic (NOT part of the bounded claim):")
    print(f"  Explicit lapse regularization: N -> max(N, {LAPSE_FLOOR}) before sqrt(N).")
    for kind, sign in signs.items():
        neg_count, n_min = lapse_negativity_report(sign)
        disp, norm, _ = evolve_case("lapse", sign)
        direction = "TOWARD" if disp > 0.0 else "AWAY"
        floored_note = (
            f"FLOOR ACTIVE: {neg_count} sites with N<=0, min N={n_min:.4f}"
            if neg_count > 0
            else f"no floor needed: min N={n_min:.4f}"
        )
        print(
            f"  lapse {kind}: {direction}  disp={disp:+.6f}  norm={norm:.12f}  [{floored_note}]"
        )
    print(
        "  NOTE: the lapse well/hill split depends on the explicitly floored,"
        " non-positive lapse above. It does NOT close against the cited lapse"
        " form and is OPEN. See docs/GRAVITY_SIGN_AUDIT_2026-04-10.md."
    )

    print()
    print("Gravity sign well/hill diagnostic:", "PASS" if FAIL == 0 else "FAIL")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
