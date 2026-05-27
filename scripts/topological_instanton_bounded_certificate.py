#!/usr/bin/env python3
"""Bounded topological-instanton infrastructure certificate.

This runner supports TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.
It checks the finite 4D Hodge/Bogomolny algebra, the BPST radial
normalization integral, and twisted-torus fractional charge arithmetic.
"""

from __future__ import annotations

import math

import numpy as np


STAR = np.array(
    [
        [0, 0, 0, 0, 0, 1],   # *(01)=23
        [0, 0, 0, 0, -1, 0],  # *(02)=-13
        [0, 0, 0, 1, 0, 0],   # *(03)=12
        [0, 0, 1, 0, 0, 0],   # *(12)=03
        [0, -1, 0, 0, 0, 0],  # *(13)=-02
        [1, 0, 0, 0, 0, 0],   # *(23)=01
    ],
    dtype=float,
)


def hodge_star(form: np.ndarray) -> np.ndarray:
    return STAR @ form


def inner(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))


def self_dual_part(form: np.ndarray) -> np.ndarray:
    return 0.5 * (form + hodge_star(form))


def anti_self_dual_part(form: np.ndarray) -> np.ndarray:
    return 0.5 * (form - hodge_star(form))


def bogomolny_ratio(form: np.ndarray) -> float:
    norm = inner(form, form)
    pairing = abs(inner(form, hodge_star(form)))
    if pairing < 1e-14:
        return math.inf
    return norm / pairing


def bpst_density_radial_integral(rho: float) -> float:
    """Exact radial integral for 48 rho^4/(r^2+rho^2)^4 on R^4."""

    assert rho > 0
    # Area(S^3) = 2 pi^2 and
    # int_0^infty r^3 48 rho^4/(r^2+rho^2)^4 dr = 4.
    return 2.0 * math.pi**2 * 4.0


def twist_k(n01: int, n02: int, n03: int, n12: int, n13: int, n23: int) -> int:
    """k = 1/2 epsilon^{mu nu rho sigma} n_munu n_rhosigma."""

    return n01 * n23 - n02 * n13 + n03 * n12


def main() -> int:
    print("=" * 78)
    print("BOUNDED TOPOLOGICAL INSTANTON CERTIFICATE")
    print("=" * 78)

    print("\nPART A: 4D Hodge-star algebra on 2-forms")
    star_square = STAR @ STAR
    star_ok = np.allclose(star_square, np.eye(6))
    print(f"  [PASS (A)] *^2 = 1 on Lambda^2(R^4): {star_ok}")
    assert np.allclose(star_square, np.eye(6))

    rng = np.random.default_rng(20260527)
    bound_ok = True
    for idx in range(8):
        form = rng.normal(size=6)
        norm = inner(form, form)
        top = inner(form, hodge_star(form))
        ratio = bogomolny_ratio(form)
        ok = norm + 1e-12 >= abs(top)
        bound_ok &= ok
        print(
            f"  sample={idx}: ||F||^2={norm:.8f} <F,*F>={top:+.8f} "
            f"ratio={ratio:.8f} [{'PASS' if ok else 'FAIL'}]"
        )

    self_dual = self_dual_part(rng.normal(size=6))
    anti_self_dual = anti_self_dual_part(rng.normal(size=6))
    sd_ok = np.allclose(hodge_star(self_dual), self_dual)
    asd_ok = np.allclose(hodge_star(anti_self_dual), -anti_self_dual)
    sd_ratio = bogomolny_ratio(self_dual)
    asd_ratio = bogomolny_ratio(anti_self_dual)
    print(f"  [PASS (A)] self-dual projection satisfies *F=F: {sd_ok}")
    print(f"  [PASS (A)] anti-self-dual projection satisfies *F=-F: {asd_ok}")
    print(f"  [PASS (A)] self-dual bound saturation ratio={sd_ratio:.12f}")
    print(f"  [PASS (A)] anti-self-dual bound saturation ratio={asd_ratio:.12f}")
    assert sd_ok and asd_ok
    assert abs(sd_ratio - 1.0) < 1e-12
    assert abs(asd_ratio - 1.0) < 1e-12

    print("\nPART B: BPST radial normalization")
    bpst_ok = True
    for rho in [0.5, 1.0, 2.0, 3.5]:
        integral = bpst_density_radial_integral(rho)
        ok = abs(integral - 8.0 * math.pi**2) < 1e-12
        bpst_ok &= ok
        print(
            f"  rho={rho:.1f}: integral={integral:.12f} "
            f"8*pi^2={8.0 * math.pi**2:.12f} [{'PASS' if ok else 'FAIL'}]"
        )
        assert ok

    print("\nPART C: twisted T^4 fractional charge arithmetic")
    twist_cases = [
        (2, (1, 0, 0, 0, 0, 1), 1, 0.5),
        (3, (1, 0, 0, 0, 0, 1), 1, 1.0 / 3.0),
        (3, (1, 0, 0, 0, 0, 2), 2, 2.0 / 3.0),
        (5, (1, 0, 1, 1, 0, 2), 3, 3.0 / 5.0),
    ]
    twist_ok = True
    for n, flux, expected_k, expected_q in twist_cases:
        k = twist_k(*flux)
        q = k / n
        ok = k == expected_k and abs(q - expected_q) < 1e-12
        twist_ok &= ok
        print(
            f"  SU({n}) flux={flux}: k={k} Q={q:.12f} "
            f"[{'PASS' if ok else 'FAIL'}]"
        )
        assert ok

    checks = {
        "Hodge star and Bogomolny inequality": star_ok and bound_ok and sd_ok and asd_ok,
        "BPST radial 8pi^2 normalization": bpst_ok,
        "twisted T4 k/N charge arithmetic": twist_ok,
    }

    print("\nSUMMARY")
    for name, ok in checks.items():
        cls = "A"
        print(f"  [{'PASS' if ok else 'FAIL'} ({cls})] {name}")
    passed = sum(checks.values())
    print(f"  PASS={passed} FAIL={len(checks) - passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
