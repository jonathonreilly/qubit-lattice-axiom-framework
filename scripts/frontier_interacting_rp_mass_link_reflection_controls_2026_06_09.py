#!/usr/bin/env python3
"""Companion controls for the interacting full-algebra RP packet.

This source-hash-pinned runner covers two controls that are intentionally kept
out of the larger primary runner's summary:

1. the positive-det/per-config PSD mass scan down to m=0.01 on the SU(3)
   full-algebra carrier;
2. the non-conjugating link-reflection control, which breaks Hermiticity and PSD.

The companion imports the primary runner's finite algebra implementation instead
of reimplementing the Wick/OS machinery.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path

import numpy as np

import frontier_interacting_rp_full_algebra_2026_06_05 as rp


ROOT = Path(__file__).resolve().parent.parent
PRIMARY = ROOT / "scripts" / "frontier_interacting_rp_full_algebra_2026_06_05.py"
NOTE = ROOT / "docs" / "INTERACTING_RP_FULL_ALGEBRA_FIXED_A_GAUGE_INVARIANT_FOUR_FERMION_BOUNDED_NOTE_2026-06-05.md"
EXPECTED_PRIMARY_SHA256 = "7b3185987a8b7bf745dec44a6fcdcaa82dfe94fbe8bc3632b870bf150cd587b0"
TOL = 1e-9

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primary_source_guard() -> bool:
    actual = sha256(PRIMARY)
    return check(
        "primary full-algebra runner source hash is pinned",
        actual == EXPECTED_PRIMARY_SHA256,
        f"expected={EXPECTED_PRIMARY_SHA256}; actual={actual}",
    )


def source_note_guard() -> bool:
    note = NOTE.read_text(encoding="utf-8")
    required = [
        "frontier_interacting_rp_mass_link_reflection_controls_2026_06_09.py",
        "frontier_interacting_rp_mass_link_reflection_controls_2026_06_09.txt",
        "m = 0.01",
        "non-conjugating",
    ]
    missing = [phrase for phrase in required if phrase not in note]
    return check(
        "source note names companion controls and cache",
        not missing,
        f"missing={missing}",
    )


def sym_min_eig(matrix: np.ndarray) -> float:
    hermitian = 0.5 * (matrix + matrix.conj().T)
    return float(np.linalg.eigvalsh(hermitian).min())


def run_mass_scan() -> bool:
    print("\nMASS SCAN: SU(3) full algebra, positive det and per-config PSD")
    print("-" * 86)
    print(
        f"{'m':>8s} {'avg_min_eig':>14s} {'per_cfg_min':>14s} "
        f"{'det_min':>14s} {'baryon_diag':>14s} {'herm':>10s}"
    )
    all_ok = True
    for idx, mass in enumerate([0.5, 0.1, 0.05, 0.01]):
        rp.RNG = np.random.default_rng(20260609 + idx)
        carrier = rp.Carrier(Ns=2, nc=3, nt=2, m=mass)
        configs, weights = rp.haar_configs("su3", Ns=2, n_cfg=20, beta=4.0)
        labels, gram, det_min, n_det_nonpos, diag = rp.full_algebra_gram(
            carrier, configs, weights, wrong=False
        )
        herm = float(np.max(np.abs(gram - gram.conj().T)))
        avg_min = sym_min_eig(gram)
        per_cfg_min = math.inf
        for links in configs:
            _labels_u, gram_u = rp._perconfig_gram(carrier, links)
            per_cfg_min = min(per_cfg_min, sym_min_eig(gram_u))
        baryon_idx = [i for i, label in enumerate(labels) if label.startswith("baryon")]
        baryon_diag = min(diag[i] for i in baryon_idx)
        row_ok = (
            det_min > 0.0
            and n_det_nonpos == 0
            and avg_min > -TOL
            and per_cfg_min > -TOL
            and baryon_diag > 1e-6
            and herm < 1e-8
        )
        all_ok = all_ok and row_ok
        print(
            f"{mass:8.2g} {avg_min:+14.6e} {per_cfg_min:+14.6e} "
            f"{det_min:+14.6e} {baryon_diag:+14.6e} {herm:10.2e}"
        )
    return check(
        "mass scan remains positive through m=0.01",
        all_ok,
        "det(M)>0, U-averaged and per-config Grams PSD, baryon diagonal nonzero",
    )


def theta_without_link_conjugation(coeff, factors, carrier):
    """Wrong control: reverse/order-reflect fields but do not conjugate coefficients."""
    reflected = []
    sign = 1.0
    for kind, x, color, time in reversed(factors):
        reflected_kind = "cb" if kind == "c" else "c"
        reflected_time = -1 - time
        sign *= -1.0
        reflected.append((reflected_kind, carrier.idx(reflected_time, x, color)))
    return coeff * sign, reflected


def perconfig_gram_without_link_conjugation(carrier, links):
    minv = np.linalg.inv(carrier.build_M(links))
    basis = rp.build_basis(carrier, links, t_op=0, include_products=True)
    labels = [label for label, _operator in basis]
    n = len(basis)
    gram = np.zeros((n, n), dtype=complex)
    thetas = [
        [theta_without_link_conjugation(coeff, factors, carrier) for coeff, factors in operator]
        for _label, operator in basis
    ]
    rights = [
        [rp.mono_to_idx(coeff, factors, carrier) for coeff, factors in operator]
        for _label, operator in basis
    ]
    for left in range(n):
        for right in range(n):
            acc = 0.0 + 0.0j
            for coeff_l, factors_l in thetas[left]:
                if coeff_l == 0:
                    continue
                for coeff_r, factors_r in rights[right]:
                    if coeff_r == 0:
                        continue
                    acc += coeff_l * coeff_r * rp.wick(factors_l + factors_r, minv)
            gram[left, right] = acc
    return labels, gram


def run_nonconjugating_control() -> bool:
    print("\nNON-CONJUGATING LINK-REFLECTION CONTROL")
    print("-" * 86)
    rp.RNG = np.random.default_rng(20260610)
    carrier = rp.Carrier(Ns=2, nc=3, nt=2, m=0.5)
    configs, _weights = rp.haar_configs("su3", Ns=2, n_cfg=5, beta=4.0)
    worst_correct_min = math.inf
    worst_wrong_herm = 0.0
    most_negative_wrong = math.inf
    print(f"{'cfg':>4s} {'correct_min':>14s} {'wrong_herm':>14s} {'wrong_sym_min':>14s}")
    for cfg, links in enumerate(configs):
        _labels_ok, gram_ok = rp._perconfig_gram(carrier, links)
        correct_min = sym_min_eig(gram_ok)
        _labels_bad, gram_bad = perconfig_gram_without_link_conjugation(carrier, links)
        wrong_herm = float(np.max(np.abs(gram_bad - gram_bad.conj().T)))
        wrong_min = sym_min_eig(gram_bad)
        worst_correct_min = min(worst_correct_min, correct_min)
        worst_wrong_herm = max(worst_wrong_herm, wrong_herm)
        most_negative_wrong = min(most_negative_wrong, wrong_min)
        print(f"{cfg:4d} {correct_min:+14.6e} {wrong_herm:14.6e} {wrong_min:+14.6e}")
    return check(
        "non-conjugating link reflection breaks Hermiticity and PSD",
        worst_correct_min > -TOL and worst_wrong_herm > 1e-3 and most_negative_wrong < -1e-3,
        (
            f"correct_min={worst_correct_min:+.6e}; "
            f"wrong_herm={worst_wrong_herm:.6e}; wrong_min={most_negative_wrong:+.6e}"
        ),
    )


def main() -> int:
    print("Interacting RP mass/link-reflection companion controls")
    print("=" * 86)
    primary_source_guard()
    source_note_guard()
    run_mass_scan()
    run_nonconjugating_control()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
