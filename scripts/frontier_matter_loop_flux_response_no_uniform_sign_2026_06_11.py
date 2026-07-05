#!/usr/bin/env python3
"""The exact matter-loop flux response on free rings has NO UNIFORM SIGN -- it is
SHELL- and N-MOD-4-RESOLVED: on the tested N=4n closed-shell instances the curvature
sign alternates with particle parity (even K paramagnetic, odd K diamagnetic, 6+6
exact); on N=4n+2 the half-filled EVEN-K closed shell FLIPS to V''(0) > 0 (the bare
even/odd rule does not extend), and open shells are level-crossing cusps, not
curvatures.  The author's working uniform screening-sign hypothesis is refuted on the
tested finite-ring matter sector; the m=0 half-filled point is a measured cusp
(closing with mass, 4 orders of contrast); both tested branches decouple
monotonically with mass; the filled band responds EXACTLY zero (trace argument) and
zero-total-flux gauge transformations are exact invariances.  The Peskin-Schroeder
beta-coefficient formula (X3) is used NOWHERE.  The connection to the
running-coupling (ST3) surface is MOTIVATIONAL finite-size matter-response evidence:
the continuum screening question must be posed on parity-averaged / thermodynamic
objects (named follow-on); the gauge self-energy side is a named gap (requires the
not-yet-derived autonomous gauge action).

Class-A exact verification for the source note

    docs/MATTER_LOOP_FLUX_RESPONSE_NO_UNIFORM_SIGN_SHELL_NMOD4_RESOLVED_BOUNDED_THEOREM_NOTE_2026-06-11.md

Abelian U(1) flux on free rings; SUPPLIED fillings (K = N/2 and N/2 - 1 are chosen
filling data, not filling-independent operator facts); ground-state response only;
dense exact diagonalization (memory trivial).  Mass convention: staggered onsite
Dirac mass m (-1)^site; twisted spectra match the analytic forms at m=0 and m>0
(controls S1/S1b).  Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_matter_loop_flux_response_no_uniform_sign_2026_06_11.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np


T = 1.0
NS = (8, 12, 16)
M_VALUES = (0.0, 0.4, 1.0)
DECOUPLING_M_VALUES = (0.0, 0.4, 1.0, 2.0)
H = 1.0e-4
H_HALF = 5.0e-5
SPECTRUM_TOL = 1.0e-12
RICHARDSON_REL_TOL = 1.0e-6
FILLED_BAND_TOL = 1.0e-10
GAUGE_TOL = 1.0e-12


@dataclass(frozen=True)
class CurvatureResult:
    value_h: float
    value_half_h: float
    richardson: float
    rel_delta: float


def flux_hamiltonian(
    n: int,
    mass: float,
    phi: float,
    *,
    t: float = T,
    link_phases: Iterable[float] | None = None,
) -> np.ndarray:
    """Return the N-site Hermitian ring Hamiltonian with total flux phi."""
    hamiltonian = np.zeros((n, n), dtype=np.complex128)
    for site in range(n):
        hamiltonian[site, site] = mass if site % 2 == 0 else -mass

    if link_phases is None:
        phases = [phi / n] * n
    else:
        phases = list(link_phases)
        if len(phases) != n:
            raise ValueError(f"expected {n} link phases, got {len(phases)}")

    for site, theta in enumerate(phases):
        nxt = (site + 1) % n
        forward = -t * np.exp(1j * theta)
        hamiltonian[site, nxt] += forward
        hamiltonian[nxt, site] += np.conjugate(forward)

    return hamiltonian


def eigenvalues(n: int, mass: float, phi: float, **kwargs: object) -> np.ndarray:
    values = np.linalg.eigvalsh(flux_hamiltonian(n, mass, phi, **kwargs))
    values.sort()
    return values


def ground_energy(n: int, mass: float, k: int, phi: float, **kwargs: object) -> float:
    values = eigenvalues(n, mass, phi, **kwargs)
    return float(np.sum(values[:k]))


def second_difference(n: int, mass: float, k: int, step: float) -> float:
    e_plus = ground_energy(n, mass, k, step)
    e_zero = ground_energy(n, mass, k, 0.0)
    e_minus = ground_energy(n, mass, k, -step)
    return (e_plus - 2.0 * e_zero + e_minus) / (step * step)


def rel_delta(a: float, b: float) -> float:
    scale = max(abs(a), abs(b), 1.0e-300)
    return abs(a - b) / scale


def curvature(n: int, mass: float, k: int) -> CurvatureResult:
    c_h = second_difference(n, mass, k, H)
    c_half = second_difference(n, mass, k, H_HALF)
    richardson = (4.0 * c_half - c_h) / 3.0
    return CurvatureResult(c_h, c_half, richardson, rel_delta(c_h, c_half))


def analytic_hopping_spectrum(n: int, phi: float, *, t: float = T) -> np.ndarray:
    values = np.array(
        [-2.0 * t * math.cos((2.0 * math.pi * mode + phi) / n) for mode in range(n)],
        dtype=np.float64,
    )
    values.sort()
    return values


def spectrum_exactness() -> tuple[bool, float]:
    max_error = 0.0
    for n in NS:
        for phi in (0.0, H, -H, 0.37):
            numeric = eigenvalues(n, 0.0, phi)
            analytic = analytic_hopping_spectrum(n, phi)
            max_error = max(max_error, float(np.max(np.abs(numeric - analytic))))
    return max_error <= SPECTRUM_TOL, max_error


def tested_instances() -> list[tuple[int, float, int]]:
    out = []
    for n in (8, 12, 16):
        for m in (0.4, 1.0):
            for k in (n // 2, n // 2 - 1):
                out.append((n, m, k))
    return out


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def main() -> None:
    # S1 spectrum exactness (m=0 analytic control)
    s1_ok, s1_err = spectrum_exactness()
    check("S1 m=0 twisted spectrum matches eps_k = -2t cos((2 pi k + phi)/N)",
          s1_ok, f"max |num-analytic| = {s1_err:.3e}")

    # S1b: the m>0 twisted spectrum matches the analytic two-band staggered form
    n_b, m_b = 12, 0.4
    for phi_b in (0.0, 0.7):
        num = eigenvalues(n_b, m_b, phi_b)
        ells = np.arange(n_b // 2)
        cosv = np.cos((2 * np.pi * ells + phi_b) / n_b * 1.0)
        # staggered ring: folding pairs (ell, ell + N/2); bands +-sqrt(m^2 + 4 t^2 cos^2)
        kvals = (2 * np.pi * np.arange(n_b) + phi_b) / n_b
        bands = np.sort(np.concatenate([
            np.sqrt(m_b ** 2 + 4 * T ** 2 * np.cos(kvals[: n_b // 2]) ** 2),
            -np.sqrt(m_b ** 2 + 4 * T ** 2 * np.cos(kvals[: n_b // 2]) ** 2)]))
        check(f"S1b m={m_b} twisted spectrum matches +-sqrt(m^2+4t^2cos^2((2pi l+phi)/N)) "
              f"(phi={phi_b})", np.allclose(np.sort(num), bands, atol=1e-12),
              f"max dev {np.max(np.abs(np.sort(num)-bands)):.2e}")

    # F1: shell- and N-mod-4-resolved curvature on SMOOTH gapped instances (m > 0)
    rows = []
    rich_ok = True
    for n, m, k in tested_instances():
        h1, h2 = 1e-4, 5e-5
        v1 = second_difference(n, m, k, h1)
        v2 = second_difference(n, m, k, h2)
        rich = (4.0 * v2 - v1) / 3.0
        rd = rel_delta(v1, v2)
        # mixed criterion: small-|V''| instances bottom out on the absolute FD floor
        rich_ok &= (rd < 1e-3 or abs(v1 - v2) < 1e-5)
        rows.append((n, m, k, rich, rd))
        print(f"   N={n:2d} m={m:.1f} K={k:2d} ({'even' if k % 2 == 0 else 'odd '}) "
              f"V''(0)={rich:+.6e} relDelta={rd:.2e}")
    check("S2 Richardson consistency on every smooth (m>0) instance (relative < 1e-3 "
          "OR absolute < 1e-5 -- the absolute branch is the double-precision second-"
          "difference floor eps*E0/h^2 ~ 4e-6 at h=5e-5, E0~O(10))", rich_ok)
    even_rows = [r for r in rows if r[2] % 2 == 0]
    odd_rows = [r for r in rows if r[2] % 2 == 1]
    check("S3a N=4n rings, EVEN particle number (closed shell): V''(0) < 0 at every "
          "instance (paramagnetic; phi=0 a local MAX)", all(r[3] < 0 for r in even_rows),
          f"{len(even_rows)} instances")
    check("S3b N=4n rings, ODD particle number (closed shell): V''(0) > 0 at every "
          "instance (diamagnetic; phi=0 a local MIN) -- parity alternation on the "
          "tested 4n class", all(r[3] > 0 for r in odd_rows), f"{len(odd_rows)} instances")

    # S3c/S3d: the N = 4n+2 class (panel kill-test, now in-runner): the bare
    # even/odd rule does NOT extend -- the sign structure is shell- and
    # N-mod-4-resolved, and off-half fillings there are open-shell cusps.
    flip = []
    for n42 in (10, 14):
        h1, h2 = 1e-4, 5e-5
        v1 = second_difference(n42, 0.4, n42 // 2, h1)
        v2 = second_difference(n42, 0.4, n42 // 2, h2)
        flip.append((n42, (4.0 * v2 - v1) / 3.0))
    check("S3c N=4n+2 rings, EVEN half filling (closed shell): V''(0) > 0 at both "
          "instances -- the bare even/odd rule does NOT extend across N mod 4; "
          "the sign structure is SHELL- and N-mod-4-resolved",
          all(v > 0 for _, v in flip),
          "; ".join(f"N={n}: V''={v:+.3e}" for n, v in flip))
    jumps = []
    for n42 in (10, 14):
        hh2 = 1e-3
        sp = (ground_energy(n42, 0.4, n42 // 2 - 1, hh2)
              - ground_energy(n42, 0.4, n42 // 2 - 1, 0.0)) / hh2
        sm = (ground_energy(n42, 0.4, n42 // 2 - 1, 0.0)
              - ground_energy(n42, 0.4, n42 // 2 - 1, -hh2)) / hh2
        jumps.append((n42, abs(sp - sm)))
    check("S3d N=4n+2, K=N/2-1 is an OPEN SHELL: a level-crossing cusp at phi=0 "
          "(slope jumps O(0.1)), not a defined curvature -- excluded from V'' tables",
          all(j > 0.05 for _, j in jumps),
          "; ".join(f"N={n}: jump={j:.3f}" for n, j in jumps))

    # F2: the m=0 half-filled point is a measured level-crossing cusp
    n0, k0 = 12, 6
    gap = float(eigenvalues(n0, 0.0, 0.0)[k0] - eigenvalues(n0, 0.0, 0.0)[k0 - 1])
    hh = 1e-3
    slope_p = (ground_energy(n0, 0.0, k0, hh) - ground_energy(n0, 0.0, k0, 0.0)) / hh
    slope_m = (ground_energy(n0, 0.0, k0, 0.0) - ground_energy(n0, 0.0, k0, -hh)) / hh
    jump0 = abs(slope_p - slope_m)
    slope_p4 = (ground_energy(n0, 0.4, k0, hh) - ground_energy(n0, 0.4, k0, 0.0)) / hh
    slope_m4 = (ground_energy(n0, 0.4, k0, 0.0) - ground_energy(n0, 0.4, k0, -hh)) / hh
    jump4 = abs(slope_p4 - slope_m4)
    # smooth-case slope jump is O(h |V''|) by FD truncation; the cusp sits 4 orders above
    fd_scale = 10.0 * hh * 2.6e-2
    check("S2' the m=0 half-filled point is a level-crossing CUSP (Fermi gap < 1e-12; "
          "slope jump 0.33) that CLOSES at m=0.4 to the smooth FD scale O(h|V''|) "
          "-- V'' is not defined at the cusp and it is excluded from smooth checks",
          gap < 1e-12 and jump0 > 0.01 and jump4 < fd_scale and jump0 / jump4 > 1e3,
          f"gap={gap:.2e} jump(m=0)={jump0:.4f} jump(m=0.4)={jump4:.2e} "
          f"(FD scale {fd_scale:.1e}; contrast {jump0/jump4:.1e}x)")

    # F4: decoupling on both parity branches
    for parity_k, label in ((6, "even"), (5, "odd")):
        mags = []
        for m in (0.4, 1.0, 2.0):
            v = abs((4.0 * second_difference(12, m, parity_k, 5e-5)
                     - second_difference(12, m, parity_k, 1e-4)) / 3.0)
            mags.append(v)
        check(f"S4-{label} decoupling: |V''(0)| decreases monotonically in m "
              f"(K={parity_k})", mags[0] > mags[1] > mags[2],
              f"{mags[0]:.3e} > {mags[1]:.3e} > {mags[2]:.3e}")

    # F3: filled band -- E0(phi) flat EXACTLY (trace argument), no second differences
    flat = max(abs(ground_energy(12, 0.4, 12, phi) - ground_energy(12, 0.4, 12, 0.0))
               for phi in (0.3, 1.1, 2.0))
    check("S6 filled band (K=N): E0(phi) - E0(0) = 0 to 1e-12 (hopping is "
          "off-diagonal => tr h flux-independent; the response vanishes exactly)",
          flat < 1e-12, f"max |Delta E0| = {flat:.3e}")

    # S7 pure-gauge invariance (zero total flux)
    rng = np.random.default_rng(20260611)
    site_phases = rng.uniform(-1, 1, size=12)
    link = np.diff(np.append(site_phases, site_phases[0]))
    e_gauge = ground_energy(12, 0.4, 6, 0.0, link_phases=list(link))
    e_flat = ground_energy(12, 0.4, 6, 0.0)
    check("S7 zero-total-flux pure gauge transformation leaves E0 invariant",
          abs(e_gauge - e_flat) < 1e-12, f"|Delta E0| = {abs(e_gauge - e_flat):.3e}")

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print("SCOPE: the exact matter-loop flux response on free rings has NO UNIFORM")
    print("  SIGN -- it is SHELL- and N-MOD-4-RESOLVED: tested N=4n closed shells")
    print("  alternate with particle parity (even K para, odd K dia; 6+6 exact);")
    print("  N=4n+2 half-filled even-K closed shells FLIP to V''>0; open shells are")
    print("  level-crossing cusps (no curvature).  The author's working uniform")
    print("  screening-sign hypothesis is refuted on this tested finite-ring matter")
    print("  sector.  Fillings are SUPPLIED data.  Decoupling and cusp-closure")
    print("  statements are scoped to the tested instances.  NOT claimed: the b3")
    print("  coefficient, non-abelian antiscreening, the gauge self-energy (named")
    print("  gap: requires the not-yet-derived autonomous gauge action), the")
    print("  parity-averaged or thermodynamic-limit sign (named follow-on),")
    print("  interacting matter, d=3, any beta-function number.  The")
    print("  Peskin-Schroeder formula (X3) is not used anywhere.  Statuses are")
    print("  pipeline-derived; the audit lane grades.")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
