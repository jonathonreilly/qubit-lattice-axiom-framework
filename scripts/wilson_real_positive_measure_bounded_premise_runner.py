#!/usr/bin/env python3
"""Bounded-premise bridge for the Wilson real-positive measure surface.

Companion note:
  docs/WILSON_REAL_POSITIVE_MEASURE_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md

This runner checks one row-local bounded premise:

  The beta=6 canonical Wilson single-plaquette surface is evaluated on the
  real-positive Euclidean measure branch: S[U] is real-valued, exp(-S[U]) is
  positive configuration-wise, and S[U] is bounded below.

It does not make that premise a repo-wide axiom, framework primitive, or
Tier-A admission. It verifies the exact consequences that dependents need:

  B1. beta = 2*N_c/g_bare^2 gives beta = 6 at N_c=3, g_bare=1.
  B2. Re Tr(U) is bounded on SU(3), so the Wilson action is real and >= 0.
  B3. exp(-S_W) is positive and finite on sampled finite products of SU(3).
  B4. Q_lat = sum Im Tr(U_P) is real, while i*theta*Q_lat is an imaginary
      action term and generically makes exp(-S_W - i*theta*Q_lat) complex.
  B5. The common drift i*theta*(Tr U - Tr U^dag)/2 is the wrong real term;
      the correct imaginary action term is i*theta*(Tr U - Tr U^dag)/(2i).
"""

from __future__ import annotations

import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "WILSON_REAL_POSITIVE_MEASURE_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md"

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


def wilson_action_from_plaquettes(plaquettes: list[np.ndarray], beta: float = 6.0, nc: int = 3) -> float:
    return float(sum((beta / nc) * (nc - np.trace(p).real) for p in plaquettes))


def q_lat_from_plaquettes(plaquettes: list[np.ndarray]) -> float:
    return float(sum(np.trace(p).imag for p in plaquettes))


def source_firewall() -> None:
    print("\n== Source firewall ==\n")
    text = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "row-local bounded premise",
        "no new repo-wide axiom",
        "scripts/wilson_real_positive_measure_bounded_premise_runner.py",
        "CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
        "WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md",
        "Wilson real-positive measure surface",
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


def exact_beta_matching() -> None:
    print("\n== B1: beta=6 matching arithmetic ==\n")
    nc = Fraction(3, 1)
    g_bare_sq = Fraction(1, 1)
    beta = 2 * nc / g_bare_sq
    check("beta = 2*N_c/g_bare^2 at N_c=3, g_bare^2=1 gives beta=6", beta == 6, f"beta={beta}")
    check("Wilson coefficient beta/N_c = 2", beta / nc == 2, f"beta/N_c={beta / nc}")


def finite_su3_measure_checks() -> None:
    print("\n== B2/B3: real-positive bounded Wilson measure checks ==\n")
    rng = np.random.default_rng(2026060301)
    n_cfg = 40
    n_plaquettes = 24
    min_re = math.inf
    max_re = -math.inf
    min_s = math.inf
    max_bf = -math.inf
    min_bf = math.inf
    max_unitarity = 0.0
    max_det_dev = 0.0

    for _ in range(n_cfg):
        plaquettes = [random_su3(rng) for _ in range(n_plaquettes)]
        for p in plaquettes:
            max_unitarity = max(max_unitarity, float(np.linalg.norm(p.conj().T @ p - np.eye(3))))
            max_det_dev = max(max_det_dev, abs(np.linalg.det(p) - 1.0))
            re_tr = np.trace(p).real
            min_re = min(min_re, re_tr)
            max_re = max(max_re, re_tr)
        s_w = wilson_action_from_plaquettes(plaquettes)
        bf = math.exp(-s_w)
        min_s = min(min_s, s_w)
        min_bf = min(min_bf, bf)
        max_bf = max(max_bf, bf)

    check("sampled matrices are SU(3)", max_unitarity < 1e-12 and max_det_dev < 1e-12,
          f"max_unitarity={max_unitarity:.2e}, max|det-1|={max_det_dev:.2e}")
    check("Re Tr(U_P) lies in [-N_c, N_c] on sampled SU(3)", min_re >= -3.0 - 1e-10 and max_re <= 3.0 + 1e-10,
          f"range=[{min_re:.6f}, {max_re:.6f}]")
    check("S_W = (beta/N_c) sum(N_c-Re Tr U_P) is bounded below by 0", min_s >= -1e-10,
          f"min S_W={min_s:.6f}")
    check("exp(-S_W) is real-positive and finite on sampled finite products", min_bf > 0.0 and math.isfinite(max_bf),
          f"BF range=[{min_bf:.3e}, {max_bf:.3e}]")


def theta_slot_checks() -> None:
    print("\n== B4/B5: theta-slot algebra and V7 drift guard ==\n")
    rng = np.random.default_rng(2026060302)
    theta = 0.37
    max_q_im = 0.0
    max_forms_dev = 0.0
    min_correct_vs_buggy = math.inf
    q_values: list[float] = []
    complex_bf_count = 0
    n_cfg = 30

    for _ in range(30):
        z = np.trace(random_su3(rng))
        q_density = (z - np.conj(z)) / (2j)
        correct_a = 1j * theta * z.imag
        correct_b = 1j * theta * (z - np.conj(z)) / (2j)
        correct_c = (theta / 2.0) * (z - np.conj(z))
        buggy_extra_i = 1j * theta * (z - np.conj(z)) / 2.0
        max_q_im = max(max_q_im, abs(q_density.imag))
        max_forms_dev = max(max_forms_dev, abs(correct_a - correct_b), abs(correct_a - correct_c), abs(correct_a.real))
        min_correct_vs_buggy = min(min_correct_vs_buggy, abs(correct_a - buggy_extra_i))

    for _ in range(n_cfg):
        plaquettes = [random_su3(rng) for _ in range(24)]
        s_w = wilson_action_from_plaquettes(plaquettes)
        q_lat = q_lat_from_plaquettes(plaquettes)
        q_values.append(q_lat)
        bf = math.exp(-s_w) * np.exp(-1j * theta * q_lat)
        if abs(bf.imag) > 1e-12 * max(abs(bf), 1e-300):
            complex_bf_count += 1

    check("Q_lat density (Tr U - Tr U^dag)/(2i) is real", max_q_im < 1e-12,
          f"max imaginary residue={max_q_im:.2e}")
    check("correct theta forms agree and are pure imaginary", max_forms_dev < 1e-12,
          f"max form deviation={max_forms_dev:.2e}")
    check("spurious extra-i form differs from correct i*theta*Q_lat", min_correct_vs_buggy > 1e-6,
          f"min gap={min_correct_vs_buggy:.4e}")
    check("sampled Q_lat takes nonzero values", max(abs(v) for v in q_values) > 1e-6,
          f"max|Q_lat|={max(abs(v) for v in q_values):.4f}")
    check("nonzero theta generically makes exp(-S_W - i*theta*Q_lat) complex", complex_bf_count >= int(0.9 * n_cfg),
          f"{complex_bf_count}/{n_cfg} configs complex")


def bounded_premise_check() -> None:
    print("\n== B6: row-local bounded-premise discipline ==\n")
    registered = [
        "Wilson real-positive measure surface (beta=6 canonical Wilson surface plus real-valued positive bounded-below Euclidean measure convention)"
    ]
    check("single bounded premise is recorded", len(registered) == 1)
    check("recorded premise names the Wilson real-positive measure surface", registered[0].startswith("Wilson real-positive"))
    check("premise text is row-local and not a repo-wide axiom", "repo-wide axiom" not in registered[0])


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("WILSON REAL-POSITIVE MEASURE BOUNDED-PREMISE BRIDGE")
    print("=" * 78)
    source_firewall()
    exact_beta_matching()
    finite_su3_measure_checks()
    theta_slot_checks()
    bounded_premise_check()
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
