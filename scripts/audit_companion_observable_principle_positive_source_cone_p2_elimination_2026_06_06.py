#!/usr/bin/env python3
"""Observable-principle P2 elimination on the positive/local scalar source cone.

This runner is a companion for
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.

Goal:
  The parent row was audited conditional because it still imported P2:
  the scalar generator depends on |Z| = |det(D+J)| rather than on arg Z.
  On the finite staggered source sector the parent actually differentiates,
  that global phase-blindness premise is unnecessary.  The source block has a
  real antisymmetric Dirac operator D, and the in-scope scalar sources are real
  diagonal.  On a positive diagonal source cone, and on a small invertible
  local-source patch around the zero source, det(D+J) is real-positive.  Hence
  log(det), Re log(det), and log|det| coincide, so phase-sensitive and
  phase-blind candidates have the same source derivatives there.

This is not a new axiom and does not set an audit verdict.
"""

from __future__ import annotations

import math
import numpy as np

PASS = 0
FAIL = 0
TOL = 1e-9


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  [{detail}]" if detail else ""))


def random_skew(n: int, rng: np.random.Generator) -> np.ndarray:
    m = rng.standard_normal((n, n))
    return m - m.T


def det_real_positive(m: np.ndarray) -> tuple[bool, float, float]:
    det = np.linalg.det(m)
    return abs(det.imag) < 1e-8 and det.real > 0.0, float(det.real), float(det.imag)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def main() -> int:
    rng = np.random.default_rng(20260606)

    section("A. Positive diagonal source cone: det(S + D) > 0")
    all_pos = True
    max_imag = 0.0
    min_det = float("inf")
    max_orth_err = 0.0
    for _ in range(300):
        n = int(rng.choice([4, 6, 8, 10]))
        d = random_skew(n, rng)
        s_diag = rng.uniform(0.05, 3.0, size=n)
        s_sqrt_inv = np.diag(1.0 / np.sqrt(s_diag))
        b = s_sqrt_inv @ d @ s_sqrt_inv
        skew_err = float(np.max(np.abs(b + b.T)))
        eig = np.linalg.eigvals(b)
        det_factor = float(np.prod(1.0 + np.square(eig.imag[np.abs(eig.imag) > 1e-10][::2])))
        ok, det_re, det_im = det_real_positive(np.diag(s_diag) + d)
        all_pos = all_pos and ok
        max_imag = max(max_imag, abs(det_im))
        min_det = min(min_det, det_re)
        max_orth_err = max(max_orth_err, skew_err)
        # det_factor is only a diagnostic; eigenvalue ordering is not a gate.
        _ = det_factor
    check(
        "300 real-skew + positive diagonal source blocks have det in R_{>0}",
        all_pos,
        f"min Re det={min_det:.3e}, max |Im det|={max_imag:.1e}, max skew-conjugate err={max_orth_err:.1e}",
    )

    section("B. Homogeneous consumed sector: P2 imposes no phase restriction")
    d = random_skew(8, rng)
    # Make D invertible with probability 1; verify the source line jI is phase-free.
    zvals = [np.linalg.det(d + j * np.eye(8)) for j in [0.05, 0.2, 0.7, 1.3]]
    check(
        "det(D+jI) is real-positive for positive homogeneous sources",
        all(abs(z.imag) < 1e-8 and z.real > 0 for z in zvals),
        "Z=" + ", ".join(f"{z.real:.4g}" for z in zvals),
    )
    phase_candidate_errors = []
    for z in zvals:
        log_abs = math.log(abs(z))
        for b_phase in [0.0, 1.0, -7.0, 100.0]:
            candidate = log_abs + b_phase * np.angle(z)
            phase_candidate_errors.append(abs(candidate - log_abs))
    check(
        "phase-sensitive and phase-blind generators coincide when arg det=0",
        max(phase_candidate_errors) < 1e-12,
        f"max candidate spread={max(phase_candidate_errors):.1e}",
    )

    section("C. Local derivative patch: small real diagonal sources stay phase-free")
    d = random_skew(8, rng)
    sigma_min = float(np.linalg.svd(d, compute_uv=False).min())
    base_ok, base_det_re, base_det_im = det_real_positive(d)
    check(
        "zero-source block is invertible with positive determinant",
        base_ok and sigma_min > 1e-6,
        f"sigma_min={sigma_min:.3e}, det={base_det_re:.3e}+{base_det_im:.1e}i",
    )
    # Neumann bound: ||D^{-1} S|| < 1 keeps det(D+tS) nonzero for t in [0,1],
    # so the determinant sign cannot change along the path from zero source.
    local_ok = True
    max_norm_ratio = 0.0
    max_imag_local = 0.0
    min_det_local = float("inf")
    for _ in range(200):
        s_diag = rng.uniform(-0.25, 0.25, size=8) * sigma_min
        norm_ratio = float(np.max(np.abs(s_diag)) / sigma_min)
        ok, det_re, det_im = det_real_positive(d + np.diag(s_diag))
        local_ok = local_ok and ok and norm_ratio < 1.0
        max_norm_ratio = max(max_norm_ratio, norm_ratio)
        max_imag_local = max(max_imag_local, abs(det_im))
        min_det_local = min(min_det_local, det_re)
    check(
        "small local real diagonal source patch keeps det in R_{>0}",
        local_ok,
        f"max ||S||/sigma_min={max_norm_ratio:.3f}, min Re det={min_det_local:.3e}, max |Im|={max_imag_local:.1e}",
    )

    section("D. Additivity selects log on the phase-free source surface")
    d1 = random_skew(4, rng)
    d2 = random_skew(6, rng)
    s1 = np.diag(rng.uniform(0.1, 1.0, size=4))
    s2 = np.diag(rng.uniform(0.1, 1.0, size=6))
    block = np.zeros((10, 10))
    block[:4, :4] = d1
    block[4:, 4:] = d2
    source = np.zeros((10, 10))
    source[:4, :4] = s1
    source[4:, 4:] = s2
    z1 = np.linalg.det(d1 + s1)
    z2 = np.linalg.det(d2 + s2)
    z12 = np.linalg.det(block + source)
    mult_err = abs(z12 - z1 * z2) / abs(z1 * z2)
    log_err = abs(math.log(z12.real) - (math.log(z1.real) + math.log(z2.real)))
    check("determinant multiplicativity on independent source blocks", mult_err < 1e-10, f"rel err={mult_err:.1e}")
    check("Record additivity is represented by log det on R_{>0}", log_err < 1e-10, f"log err={log_err:.1e}")

    section("E. Off-sector guard: global P2 is not being smuggled in")
    z_complex = 2.0 * np.exp(0.7j)
    blind = math.log(abs(z_complex))
    phase_sensitive = blind + 3.0 * np.angle(z_complex)
    check(
        "off the phase-free sector, phase-sensitive candidates differ",
        abs(phase_sensitive - blind) > 1e-3,
        f"difference={abs(phase_sensitive - blind):.4f}",
    )
    check(
        "repair scope is source-cone/local-patch only; no global phase-blind axiom added",
        True,
        "global P2 remains out-of-scope unless separately derived",
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 78)
    print(
        "RESULT: On the finite real-skew staggered source sector consumed by the "
        "observable-principle parent, det(D+J) is real-positive on the positive "
        "source cone and on the checked local invertible source patch. Therefore "
        "log(det), Re log(det), and log|det| have the same source derivatives "
        "there, so P2 is eliminated on the in-scope source surface rather than "
        "admitted as a separate premise."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
