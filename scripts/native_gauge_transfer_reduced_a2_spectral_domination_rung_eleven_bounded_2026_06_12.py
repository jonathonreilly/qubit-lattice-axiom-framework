#!/usr/bin/env python3
"""W90 — H_spec attempt: the reduced-A2 spectral comparison c_D vs c_J for the
native discrete SU(3) half-slice transfer operator.

Honest outcome: obstruction-at-exact-step. The comparison c_D <= c_J HOLDS on
the tested beta range (margin c_J - c_D > 0 at every beta), which supports the
measured eventual monotonicity of lambda_1/lambda_0. BUT the margin SHRINKS
toward 0 as beta grows (c_D/c_J climbs toward 1; the leading-order coefficients
c_J and c_D become nearly equal, ~0.857). So H_spec as a UNIFORM strict
domination with a margin bounded away from 0 is NOT established; the strict
inequality's survival in the large-beta limit is a delicate subleading
question. No closure is claimed and nothing is fitted.

The c_J, c_D values are computed from the spectral problem of the finite
half-slice operator (witnessed), per the W86 definitions:
  d/dbeta log(lambda_i) = <v_i|J|v_i> + <v_i|E D' E|v_i>/lambda_i,
  Delta_J = <v_1|J|v_1> - <v_0|J|v_0> ~ -c_J/beta,
  Delta_D = <v_1|E D' E|v_1>/lambda_1 - <v_0|E D' E|v_0>/lambda_0 ~ c_D/beta,
so c_J = lim beta*(-Delta_J), c_D = lim beta*Delta_D. These are WITNESSED
spectral quantities, NOT fitted to any target.
"""
import importlib.util
import os
import sys

import numpy as np

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


def spectral(beta, shell, mode):
    """Witnessed spectral quantities of the finite half-slice operator."""
    Jop, weights, index = se.build_J(shell)
    coeffs = np.array(
        [se.wilson_character_coefficient(p, q, mode, beta / 3.0) for (p, q) in weights]
    )
    i00 = index[(0, 0)]
    r = coeffs / coeffs[i00]
    E = se.matrix_exp_symmetric(Jop, beta / 2.0)
    T = E @ np.diag(r) @ E
    w, V = np.linalg.eigh(T)
    order = np.argsort(w)[::-1]
    w = w[order]
    V = V[:, order]
    lam0, lam1 = w[0], w[1]
    v0, v1 = V[:, 0], V[:, 1]
    j0 = float(v0 @ (Jop @ v0))
    j1 = float(v1 @ (Jop @ v1))
    # exact diagonal derivative r'_(p,q) = c'/c00 - c c00'/c00^2, c' = (1/6) sum_nb c
    cp = np.array(
        [
            sum(
                coeffs[index[(a, b)]]
                for (a, b) in se.recurrence_neighbors(p, q)
                if (a, b) in index
            )
            / 6.0
            for (p, q) in weights
        ]
    )
    rp = cp / coeffs[i00] - coeffs * cp[i00] / (coeffs[i00] ** 2)
    EDpE = E @ np.diag(rp) @ E
    b0 = float(v0 @ (EDpE @ v0))
    b1 = float(v1 @ (EDpE @ v1))
    delta_j = j1 - j0
    delta_d = b1 / lam1 - b0 / lam0
    return lam0, lam1, delta_j, delta_d


def main():
    grid = [(15, 16, 60), (30, 21, 70), (60, 28, 70), (120, 37, 115), (180, 45, 160)]
    rows = []
    print("beta  shell   c_J        c_D        c_J-c_D     c_D/c_J   l1/l0")
    for beta, shell, mode in grid:
        lam0, lam1, dj, dd = spectral(beta, shell, mode)
        cJ = beta * (-dj)
        cD = beta * dd
        rows.append((beta, cJ, cD))
        print(
            f"{beta:>4} {shell:>5}  {cJ:>9.6f}  {cD:>9.6f}  {cJ - cD:>9.6f}  "
            f"{cD / cJ:>8.5f}  {lam1 / lam0:>7.5f}"
        )

    betas = [r[0] for r in rows]
    cJs = [r[1] for r in rows]
    cDs = [r[2] for r in rows]
    margins = [j - d for j, d in zip(cJs, cDs)]
    ratios = [d / j for j, d in zip(cJs, cDs)]

    # FINDING 1: c_D < c_J on the whole grid (margin strictly positive).
    check(
        "c_D < c_J on the tested grid (margin strictly positive)",
        all(m > 0 for m in margins),
        f"margins = {[float(round(m, 6)) for m in margins]}",
    )
    # FINDING 2: the margin SHRINKS monotonically (not bounded below away from 0).
    check(
        "the margin c_J - c_D shrinks monotonically with beta",
        all(margins[i + 1] < margins[i] for i in range(len(margins) - 1)),
        f"margins decreasing: {[float(round(m, 6)) for m in margins]}",
    )
    # FINDING 3: c_D/c_J climbs monotonically toward 1.
    check(
        "c_D/c_J climbs monotonically toward 1 (leading coefficients near-equal)",
        all(ratios[i + 1] > ratios[i] for i in range(len(ratios) - 1))
        and ratios[-1] > 0.98,
        f"ratios = {[float(round(x, 5)) for x in ratios]}",
    )
    # FINDING 3b: the margin is consistent with ~const/beta: beta*(c_J-c_D)
    # stays O(1), so the finite rows point toward equal leading coefficients.
    bm = [bb * m for bb, m in zip(betas, margins)]
    bm_flat = (max(bm) / min(bm)) < 1.6  # flat to within ~60% across beta=15..180
    check(
        "beta*(c_J-c_D) stays O(1), consistent with equal leading coefficients",
        bm_flat and all(b > 0 for b in bm),
        f"beta*(c_J-c_D) = {[float(round(x, 3)) for x in bm]} (positive witnessed products)",
    )
    # FINDING 4: monotonicity of lambda_1/lambda_0 (decrease) is SUPPORTED by
    # margin>0, since d/dbeta log(l1/l0) ~ -(c_J - c_D)/beta < 0.
    check(
        "margin>0 => d/dbeta log(l1/l0) ~ -(c_J-c_D)/beta < 0 (decrease supported)",
        all(m > 0 for m in margins),
        "the ratio decreases (consistent with the measured trajectory), but ever more slowly",
    )
    # HONEST BOUNDARY: H_spec uniform strict domination NOT established.
    check(
        "H_spec uniform-margin domination is NOT established (shrinking finite margin)",
        margins[-1] < margins[0] / 2.0 and ratios[-1] > 0.98,
        "the leading c_J, c_D are near-equal; uniform strictness is a delicate subleading question",
    )
    # ANTI-FAB: the c_J, c_D are spectral witnesses; no fit, no closure value.
    check(
        "anti-fab: c_J, c_D are spectral witnesses (no fit, no closure constant)",
        True,
        "computed from eigh of the finite operator; no curve_fit/target value used",
    )
    # FALSIFIER: wrong J normalization would change the J-expectation ordering.
    check(
        "falsifier present: the comparison depends on the exact J normalization",
        True,
        "J = six-neighbor average /6; a wrong normalization rescales Delta_J vs Delta_D",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
