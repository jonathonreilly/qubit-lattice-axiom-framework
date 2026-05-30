#!/usr/bin/env python3
"""Narrow Hilbert-Schmidt trace-Casimir rigidity certificate.

This runner deliberately checks only the R1-R3 algebraic core for
docs/G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md.
It does not certify physical connection equivalence, Wilson matching/routing,
or an unconditional g_bare = 1 derivation.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm


PASS = 0
FAIL = 0

I3 = np.eye(3, dtype=complex)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  {tag} {name}{suffix}")


def close(a, b, tol: float = 1e-9) -> bool:
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) <= tol


def gell_mann_lambdas() -> list[np.ndarray]:
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex)
        / math.sqrt(3),
    ]


def generators(n_f: float = 0.5) -> list[np.ndarray]:
    scale = math.sqrt(2.0 * n_f)
    return [scale * lam / 2.0 for lam in gell_mann_lambdas()]


def gram(ts: list[np.ndarray]) -> np.ndarray:
    return np.array([[np.trace(a @ b).real for b in ts] for a in ts])


def casimir(ts: list[np.ndarray]) -> np.ndarray:
    return sum((t @ t for t in ts), np.zeros((3, 3), dtype=complex))


def projection_matrix(ts: list[np.ndarray], u: np.ndarray, n_f: float = 0.5) -> np.ndarray:
    """Adjoint matrix M with U T_a U^dag = sum_b M_ba T_b."""
    n = len(ts)
    out = np.zeros((n, n), dtype=float)
    for a, ta in enumerate(ts):
        t_ad = u @ ta @ u.conj().T
        for b, tb in enumerate(ts):
            out[b, a] = np.trace(tb @ t_ad).real / n_f
    return out


def check_source_firewall() -> None:
    text = Path("docs/G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md").read_text(
        encoding="utf-8"
    )
    check("source declares bounded theorem", "**Claim type:** bounded_theorem" in text)
    check("source names narrow runner", "frontier_g_bare_hs_rigidity_narrow.py" in text)
    check("source excludes former R4/R5 claims", "not part of this row's binding claim" in text)
    check("source excludes Wilson routing authority", "must not be cited as\nauthority for those claims" in text)
    check("source excludes g_bare promotion", "package-wide `g_bare` promotion" in text)


def main() -> int:
    print("=" * 88)
    print("G_BARE HS RIGIDITY NARROW CERTIFICATE")
    print("Binding scope: R1-R3 trace-Casimir rigidity only")
    print("=" * 88)

    ts = generators(0.5)
    g = gram(ts)
    target_g = 0.5 * np.eye(8)
    check("canonical trace Gram Tr(T_a T_b)=delta_ab/2", close(g, target_g))

    c0 = casimir(ts)
    check("canonical Casimir sum_a T_a T_a=(4/3)I_3", close(c0, (4.0 / 3.0) * I3))

    rng = np.random.default_rng(20260527)
    for trial in range(5):
        coeffs = rng.normal(size=8)
        h = sum((coeffs[i] * ts[i] for i in range(8)), np.zeros((3, 3), dtype=complex))
        u = expm(1j * h)
        m = projection_matrix(ts, u, n_f=0.5)
        after = m.T @ g @ m
        check(
            f"Ad-invariance of B_HS under sampled SU(3) action {trial + 1}",
            close(after, g, tol=1e-7),
            f"error={np.linalg.norm(after - g):.2e}",
        )

    for n_f in [0.25, 0.5, 1.0, 2.0]:
        ts_nf = generators(n_f)
        g_nf = gram(ts_nf)
        c_nf = casimir(ts_nf)
        check(
            f"trace Gram has selected normalization N_F={n_f}",
            close(g_nf, n_f * np.eye(8)),
        )
        check(
            f"Casimir obeys C_F=(8/3)N_F at N_F={n_f}",
            close(c_nf, (8.0 / 3.0) * n_f * I3),
        )

    for scale in [0.5, math.sqrt(2.0), 2.0, 3.0, -1.0, 1.0]:
        scaled = [scale * t for t in ts]
        g_scaled = gram(scaled)
        c_scaled = casimir(scaled)
        scale_sq = scale * scale
        check(
            f"Gram scales by c^2 for c={scale:.6g}",
            close(g_scaled, scale_sq * target_g),
        )
        check(
            f"Casimir scales by c^2 for c={scale:.6g}",
            close(c_scaled, scale_sq * (4.0 / 3.0) * I3),
        )
        preserves_both = close(g_scaled, target_g) and close(c_scaled, (4.0 / 3.0) * I3)
        expected = abs(scale_sq - 1.0) <= 1e-12
        check(
            f"joint preservation iff c^2=1 for c={scale:.6g}",
            preserves_both == expected,
        )

    check_source_firewall()

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RUNNER STATUS: FAIL")
        return 1
    print("RUNNER STATUS: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
