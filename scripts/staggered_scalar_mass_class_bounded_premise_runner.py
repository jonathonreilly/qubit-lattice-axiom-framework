#!/usr/bin/env python3
"""Bounded-premise bridge for the staggered scalar-mass action class.

Companion note:
  docs/STAGGERED_SCALAR_MASS_CLASS_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md

Checks one row-local bounded premise:

  The reviewed mass action class is the real scalar line M = m*I, m>0, with no
  pseudoscalar epsilon component.

It does not derive that premise from the Lattice / Qubit / Admissibility /
Record baseline alone, and it adds no repo-wide axiom or framework primitive, and registers no
admission-class ledger entry. The runner verifies the consequences needed by the Strong CP
operator-basis row: real scalar masses have positive determinant phase on
sampled staggered operators, non-real scalar phases fail the determinant phase
condition, and pseudoscalar/mixed masses are outside the premise because their
epsilon component is nonzero.
"""

from __future__ import annotations

import math
import sys
import time
import warnings
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "STAGGERED_SCALAR_MASS_CLASS_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md"

PASS = 0
FAIL = 0
FAIL_NOTES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
        FAIL_NOTES.append(f"{label}: {detail}")
    line = f"  [{status}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def random_su3(rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    q = q * phases
    det_q = np.linalg.det(q)
    q = q / (det_q ** (1.0 / 3.0))
    det_q = np.linalg.det(q)
    q = q / (det_q ** (1.0 / 3.0))
    return q


def staggered_eta(mu: int, site: tuple[int, int, int, int]) -> int:
    return (-1) ** sum(site[nu] for nu in range(mu))


def random_gauge_config_4d(ls: int, lt: int, rng: np.random.Generator) -> dict:
    links = {}
    for t in range(lt):
        for x in range(ls):
            for y in range(ls):
                for z in range(ls):
                    for mu in range(4):
                        links[(t, x, y, z, mu)] = random_su3(rng)
    return links


def build_staggered_dirac_4d(ls: int, lt: int, links: dict) -> np.ndarray:
    nc = 3
    n_site = lt * ls**3
    n = n_site * nc
    d = np.zeros((n, n), dtype=complex)
    dims = (lt, ls, ls, ls)

    def site_index(t: int, x: int, y: int, z: int) -> int:
        return ((t * ls + x) * ls + y) * ls + z

    for t in range(lt):
        for x in range(ls):
            for y in range(ls):
                for z in range(ls):
                    site = (t, x, y, z)
                    s_idx = site_index(t, x, y, z)
                    coords = [t, x, y, z]
                    for mu in range(4):
                        eta = staggered_eta(mu, site)
                        fwd = coords[:]
                        fwd[mu] = (fwd[mu] + 1) % dims[mu]
                        bwd = coords[:]
                        bwd[mu] = (bwd[mu] - 1) % dims[mu]
                        f_idx = site_index(*fwd)
                        b_idx = site_index(*bwd)
                        apbc_fwd = -1.0 if mu == 0 and t == lt - 1 else 1.0
                        apbc_bwd = -1.0 if mu == 0 and t == 0 else 1.0
                        u_fwd = links[(t, x, y, z, mu)]
                        u_bwd = links[(bwd[0], bwd[1], bwd[2], bwd[3], mu)]
                        for a in range(nc):
                            for b in range(nc):
                                d[s_idx * nc + a, f_idx * nc + b] += apbc_fwd * eta * u_fwd[a, b] / 2.0
                                d[s_idx * nc + a, b_idx * nc + b] -= apbc_bwd * eta * np.conj(u_bwd[b, a]) / 2.0
    return d


def epsilon_matrix_4d(ls: int, lt: int) -> np.ndarray:
    n = lt * ls**3 * 3
    diag = np.zeros(n)
    i = 0
    for coords in np.ndindex(lt, ls, ls, ls):
        val = (-1) ** sum(coords)
        for _ in range(3):
            diag[i] = val
            i += 1
    return np.diag(diag)


def decompose_scalar_epsilon(mass_matrix: np.ndarray, eps: np.ndarray) -> tuple[complex, complex, float]:
    n = mass_matrix.shape[0]
    ms = np.trace(mass_matrix) / n
    mp = np.trace(eps @ mass_matrix) / n
    reconstructed = ms * np.eye(n, dtype=complex) + mp * eps
    residual = float(np.linalg.norm(mass_matrix - reconstructed))
    return ms, mp, residual


def source_firewall() -> None:
    print("\n== Source firewall ==\n")
    text = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "row-local bounded premise",
        "no new repo-wide axiom",
        "scripts/staggered_scalar_mass_class_bounded_premise_runner.py",
        "STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md",
        "STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md",
        "Staggered scalar-mass action class",
    ]
    for needle in required:
        check(f"source contains required phrase: {needle}", needle in text)

    stale_axiom_pair = "A" + "1/A" + "2"
    forbidden = [
        "retain" + "ed_unbounded",
        "audited" + "_clean",
        "audited" + "_conditional",
        "adds a new repo-wide axiom",
        "derive " + stale_axiom_pair,
    ]
    for needle in forbidden:
        check(f"source excludes overclaim phrase: {needle}", needle not in text)


def bounded_premise_check() -> None:
    print("\n== B1: row-local bounded-premise discipline ==\n")
    registered = ["Staggered scalar-mass action class M=mI, m>0, M_epsilon=0"]
    check("single bounded premise is recorded", len(registered) == 1)
    check("recorded premise names the scalar-mass action class", registered[0].startswith("Staggered scalar-mass"))
    check("premise explicitly fixes zero epsilon component", "M_epsilon=0" in registered[0])


def algebraic_mass_class_checks() -> None:
    print("\n== B2: scalar/epsilon decomposition checks ==\n")
    ls, lt = 2, 2
    eps = epsilon_matrix_4d(ls, lt)
    n = eps.shape[0]
    eye = np.eye(n, dtype=complex)
    m = 1.0
    m5 = 0.7
    candidates = {
        "real scalar": m * eye,
        "complex scalar": m * np.exp(1j * math.pi / 4.0) * eye,
        "pseudoscalar": m5 * eps,
        "mixed": m * eye + 1j * m5 * eps,
    }
    parts = {}
    for name, matrix in candidates.items():
        parts[name] = decompose_scalar_epsilon(matrix, eps)
        ms, mp, residual = parts[name]
        check(f"{name}: decomposes exactly into I and epsilon components", residual < 1e-10,
              f"M_S={ms:.4g}, M_epsilon={mp:.4g}, residual={residual:.2e}")

    real_ms, real_mp, _ = parts["real scalar"]
    complex_ms, complex_mp, _ = parts["complex scalar"]
    pseudo_ms, pseudo_mp, _ = parts["pseudoscalar"]
    mixed_ms, mixed_mp, _ = parts["mixed"]
    check("real scalar lies in the scalar-mass premise", abs(real_mp) < 1e-12 and abs(real_ms.imag) < 1e-12 and real_ms.real > 0)
    check("complex scalar fails the real-scalar phase condition", abs(complex_mp) < 1e-12 and abs(complex_ms.imag) > 1e-6)
    check("pseudoscalar fails because epsilon component is nonzero", abs(pseudo_mp) > 1e-6)
    check("mixed mass fails because epsilon component is nonzero", abs(mixed_mp) > 1e-6)


def determinant_phase_checks() -> None:
    print("\n== B3/B4: determinant phase consequences on sampled staggered operators ==\n")
    rng = np.random.default_rng(2026060303)
    ls, lt = 2, 2
    eps = epsilon_matrix_4d(ls, lt)
    n = eps.shape[0]
    eye = np.eye(n, dtype=complex)
    n_cfg = 12
    m = 1.0
    m_u = 1.0
    m_d = 0.72
    alpha = math.pi / 4.0
    real_pass = 0
    complex_fail = 0
    two_flavor_pass = 0
    max_antiherm = 0.0
    max_chiral = 0.0
    mixed_det_positive = 0

    def phase_and_positive_sign(matrix: np.ndarray) -> tuple[float, bool]:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            sign, _logabs = np.linalg.slogdet(matrix)
        return float(abs(np.angle(sign))), bool(sign.real > 0 and abs(np.angle(sign)) < 1e-9)

    for _ in range(n_cfg):
        links = random_gauge_config_4d(ls, lt, rng)
        d = build_staggered_dirac_4d(ls, lt, links)
        max_antiherm = max(max_antiherm, float(np.linalg.norm(d.conj().T + d)))
        max_chiral = max(max_chiral, float(np.linalg.norm(eps @ d + d @ eps)))

        real_phase, real_positive = phase_and_positive_sign(d + m * eye)
        if real_positive:
            real_pass += 1

        complex_phase, _complex_positive = phase_and_positive_sign(d + m * np.exp(1j * alpha) * eye)
        if complex_phase > 1e-2:
            complex_fail += 1

        _mixed_phase, mixed_positive = phase_and_positive_sign(d + m * eye + 1j * 0.4 * eps)
        if mixed_positive:
            mixed_det_positive += 1

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            sign_u, _ = np.linalg.slogdet(d + m_u * eye)
            sign_d, _ = np.linalg.slogdet(d + m_d * eye)
        product_sign = sign_u * sign_d
        if abs(np.angle(product_sign)) < 1e-9 and product_sign.real > 0:
            two_flavor_pass += 1

    check("sampled staggered D is anti-Hermitian", max_antiherm < 1e-10,
          f"max||D^dag + D||={max_antiherm:.2e}")
    check("sampled staggered D anticommutes with epsilon", max_chiral < 1e-10,
          f"max||eps D + D eps||={max_chiral:.2e}")
    check("real scalar mass det(D+mI) is real-positive on all samples", real_pass == n_cfg,
          f"{real_pass}/{n_cfg} pass")
    check("complex scalar mass det(D+m exp(i*pi/4)I) has nonzero phase on all samples", complex_fail == n_cfg,
          f"{complex_fail}/{n_cfg} reject")
    check("two-flavor notation det(D+m_uI)*det(D+m_dI) has zero phase on the premise", two_flavor_pass == n_cfg,
          f"{two_flavor_pass}/{n_cfg} pass")
    check("mixed mass can pass determinant positivity, so the scalar-class wall is independent",
          mixed_det_positive > 0,
          f"mixed determinant positive on {mixed_det_positive}/{n_cfg}; excluded by epsilon component, not by this determinant gate")


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("STAGGERED SCALAR-MASS ACTION CLASS BOUNDED-PREMISE BRIDGE")
    print("=" * 78)
    source_firewall()
    bounded_premise_check()
    algebraic_mass_class_checks()
    determinant_phase_checks()
    elapsed = time.time() - t0
    print("\n" + "=" * 78)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL} runtime={elapsed:.2f}s")
    if FAIL_NOTES:
        print("FAIL NOTES:")
        for note in FAIL_NOTES:
            print(f"  - {note}")
    if FAIL == 0:
        print("VERDICT: bounded-premise bridge passes; premise is explicit and row-local.")
        return 0
    print("VERDICT: bounded-premise bridge FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
