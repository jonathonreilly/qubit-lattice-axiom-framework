#!/usr/bin/env python3
"""Finite W85 Wilson-to-saddle witness on an open native-gauge gate.

This runner intentionally does not certify a uniform K_W bound and does not
resolve W85. It checks a small active-window sample for the W85 target

    rho = sqrt(beta) | beta^(-3/2) r_(p,q)(beta) - H(x,y) exp(-Q(x,y)) |

against the comparison polynomial K_geom(a) from the existing W84 surface, and
it verifies that the finite-mode coefficient computation is stable under a
mode-doubling probe on the sampled cells.
"""

import importlib.util
import math
import os
import sys


_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(
    _HERE, "frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py"
)
_spec = importlib.util.spec_from_file_location("se_perron", _SRC)
se = importlib.util.module_from_spec(_spec)
sys.modules["se_perron"] = se
_spec.loader.exec_module(se)

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{tag}: {name}")
    if detail:
        print(f"      {detail}")


def kgeom(a):
    return 6 * a**4 + 3 * a**2 + 3 * a + 1


def coefficient_ratio(p, q, beta, mode):
    c00 = se.wilson_character_coefficient(0, 0, mode, beta / 3.0)
    return se.wilson_character_coefficient(p, q, mode, beta / 3.0) / c00


def rho(p, q, beta, mode):
    sb = math.sqrt(beta)
    x, y = p / sb, q / sb
    r = coefficient_ratio(p, q, beta, mode)
    H = x * y * (x + y) / 2.0
    Q = x * x + x * y + y * y
    lead = H * math.exp(-Q)
    return math.sqrt(beta) * abs(beta**-1.5 * r - lead), max(x, y)


def main():
    betas = [108, 300, 600]
    grid_cells = [
        (0.7, 0.7),
        (1.0, 0.6),
        (1.3, 1.0),
        (0.5, 1.4),
        (1.6, 1.2),
        (0.9, 0.9),
    ]
    by_cell = {c: [] for c in grid_cells}
    all_sampled_under_kgeom = True
    max_ratio = -1.0
    worst = None
    max_mode_delta = 0.0

    print("beta   (x,y)     rho(sample)    K_geom(a)    rho/K_geom    mode_delta")
    for beta in betas:
        mode = int(0.8 * beta) + 30
        mode2 = 2 * mode
        sb = math.sqrt(beta)
        for (cx, cy) in grid_cells:
            p, q = int(round(cx * sb)), int(round(cy * sb))
            rr, a = rho(p, q, beta, mode)
            rr2, _ = rho(p, q, beta, mode2)
            mode_delta = abs(rr2 - rr)
            Kg = kgeom(a)
            ratio = rr / Kg
            by_cell[(cx, cy)].append(rr)
            all_sampled_under_kgeom = all_sampled_under_kgeom and (rr <= Kg)
            if ratio > max_ratio:
                max_ratio = ratio
                worst = (beta, cx, cy, rr, Kg, ratio)
            max_mode_delta = max(max_mode_delta, mode_delta)
            print(
                f"{beta:>5} ({cx:.1f},{cy:.1f})  {rr:>10.5f}   "
                f"{Kg:>10.2f}   {ratio:>8.4f}   {mode_delta:.2e}"
            )

    check(
        "sampled W85 cells satisfy rho <= K_geom(a)",
        all_sampled_under_kgeom,
        "finite sample only; no uniform K_W bound is inferred",
    )

    stable = True
    detail = []
    for c, vals in by_cell.items():
        spread = max(vals) / max(min(vals), 1e-12)
        stable = stable and spread < 3.0
        detail.append(f"{c}:{[round(v, 4) for v in vals]}")
    check(
        "sampled rho values are beta-stable on the checked cells",
        stable,
        "; ".join(detail[:3]),
    )

    check(
        "finite-mode coefficient probe is stable under mode doubling",
        max_mode_delta < 1e-10,
        f"max |rho(mode)-rho(2*mode)| = {max_mode_delta:.2e}",
    )

    mode = int(0.8 * 300) + 30
    sb = math.sqrt(300)
    p, q = int(round(1.0 * sb)), int(round(0.6 * sb))
    x, y = p / sb, q / sb
    r = coefficient_ratio(p, q, 300, mode)
    wrongH = x + y
    rho_wrong = math.sqrt(300) * abs(
        300**-1.5 * r - wrongH * math.exp(-(x * x + x * y + y * y))
    )
    rho_right = rho(p, q, 300, mode)[0]
    check(
        "falsifier: wrong saddle prefactor inflates rho on the sampled cell",
        rho_wrong > 5 * rho_right,
        f"wrong-H rho = {rho_wrong:.3f} >> correct-H rho = {rho_right:.3f}",
    )

    if worst is not None:
        beta, cx, cy, rr, Kg, ratio = worst
        print(
            f"INFO: worst sampled ratio beta={beta}, cell=({cx:.1f},{cy:.1f}), "
            f"rho={rr:.5f}, K_geom={Kg:.2f}, ratio={ratio:.4f}"
        )
    print("INFO: W85 remains open; this runner is finite sampled support only.")
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
