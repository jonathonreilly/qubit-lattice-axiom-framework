#!/usr/bin/env python3
"""Finite commuting-source proof for the PWC cumulant generator row.

Companion:
  docs/PWC_DERIVATION_FROM_CUMULANT_GENERATING_FUNCTIONAL_NARROW_THEOREM_NOTE_2026-05-22.md

This runner proves the row's narrow finite-scope content directly on a
finite qubit-region algebra:

  W[J] = log Tr(rho exp(-J)) - log Tr(rho)

for mutually commuting bounded source observables.  The proof is
framework-native in the only sense claimed here: once a finite region
state rho_ref and commuting source family are supplied, the trace
functional reduces to the joint spectral measure of those commuting
observables and the derivatives of W are exactly connected cumulants
with the fixed (-1)^n source-sign bookkeeping.

It does not derive rho_ref, noncommuting ordering, a path-integral
measure, or a physical source-production law.
"""
from __future__ import annotations

from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "PWC_DERIVATION_FROM_CUMULANT_GENERATING_FUNCTIONAL_NARROW_THEOREM_NOTE_2026-05-22.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        print(f"[FAIL] {label}")
    if detail:
        print(f"       {detail}")


def exact_mean(weights, values):
    total = sum(weights)
    return sp.simplify(sum(w * v for w, v in zip(weights, values)) / total)


def exact_moment(weights, *columns):
    total = sum(weights)
    acc = 0
    for i, w in enumerate(weights):
        term = w
        for col in columns:
            term *= col[i]
        acc += term
    return sp.simplify(acc / total)


def at_zero(expr, *symbols):
    return sp.simplify(expr.subs({s: 0 for s in symbols}))


def main() -> int:
    print("PWC commuting-source cumulant-generator finite proof")
    print("=" * 72)

    jx, jy = sp.symbols("j_x j_y")

    # A concrete finite spectral measure on a two-qubit region.  The
    # positive integer weights are an unnormalized finite-region state in
    # a common eigenbasis of two commuting self-adjoint source observables.
    weights = [sp.Integer(2), sp.Integer(3), sp.Integer(5), sp.Integer(7)]
    x_vals = [sp.Integer(0), sp.Integer(1), sp.Integer(3), sp.Integer(4)]
    y_vals = [sp.Integer(2), sp.Integer(-1), sp.Integer(0), sp.Integer(5)]
    total = sum(weights)

    z = sum(
        w * sp.exp(-(jx * x + jy * y))
        for w, x, y in zip(weights, x_vals, y_vals)
    )
    w_func = sp.log(z) - sp.log(total)

    ex = exact_mean(weights, x_vals)
    ey = exact_mean(weights, y_vals)
    ex2 = exact_moment(weights, x_vals, x_vals)
    ey2 = exact_moment(weights, y_vals, y_vals)
    exy = exact_moment(weights, x_vals, y_vals)
    ex3 = exact_moment(weights, x_vals, x_vals, x_vals)
    exxy = exact_moment(weights, x_vals, x_vals, y_vals)

    cov_xy = sp.simplify(exy - ex * ey)
    var_x = sp.simplify(ex2 - ex**2)
    kappa_xxx = sp.simplify(ex3 - 3 * ex2 * ex + 2 * ex**3)
    kappa_xxy = sp.simplify(exxy - ex2 * ey - 2 * exy * ex + 2 * ex**2 * ey)

    print("\n[A] exact derivative/cumulant identities")
    check("W[0] = 0 for the unnormalized finite state", at_zero(w_func, jx, jy) == 0)
    check(
        "first derivative carries the fixed source sign: d_x W(0) = -E[X]",
        at_zero(sp.diff(w_func, jx), jx, jy) == -ex,
        f"d_x={at_zero(sp.diff(w_func, jx), jx, jy)}, -E[X]={-ex}",
    )
    check(
        "first derivative in second source: d_y W(0) = -E[Y]",
        at_zero(sp.diff(w_func, jy), jx, jy) == -ey,
        f"d_y={at_zero(sp.diff(w_func, jy), jx, jy)}, -E[Y]={-ey}",
    )
    check(
        "second mixed derivative gives connected covariance",
        at_zero(sp.diff(w_func, jx, jy), jx, jy) == cov_xy,
        f"d_xy={at_zero(sp.diff(w_func, jx, jy), jx, jy)}, cov={cov_xy}",
    )
    check(
        "second same-source derivative gives variance",
        at_zero(sp.diff(w_func, jx, jx), jx, jy) == var_x,
        f"d_xx={at_zero(sp.diff(w_func, jx, jx), jx, jy)}, var={var_x}",
    )
    check(
        "third derivative has (-1)^3 cumulant sign",
        at_zero(sp.diff(w_func, jx, jx, jx), jx, jy) == -kappa_xxx,
        f"d_xxx={at_zero(sp.diff(w_func, jx, jx, jx), jx, jy)}, -kappa={-kappa_xxx}",
    )
    check(
        "third mixed derivative has (-1)^3 connected cumulant sign",
        at_zero(sp.diff(w_func, jx, jx, jy), jx, jy) == -kappa_xxy,
        f"d_xxy={at_zero(sp.diff(w_func, jx, jx, jy), jx, jy)}, -kappa={-kappa_xxy}",
    )

    print("\n[B] trace form equals the joint spectral-measure form")
    rho_diag = [sp.Rational(w, total) for w in weights]
    trace_form = sum(
        p * sp.exp(-(jx * x + jy * y))
        for p, x, y in zip(rho_diag, x_vals, y_vals)
    )
    spectral_form = z / total
    check(
        "commuting trace formula reduces exactly to the joint spectral measure",
        sp.simplify(trace_form - spectral_form) == 0,
    )
    check(
        "normalized and unnormalized formulas differ only by the -log Tr(rho) shift",
        sp.simplify(sp.log(trace_form) - w_func) == 0,
    )

    print("\n[C] falsifiers: the logarithm and connected form are load-bearing")
    raw_mgf = z / total
    raw_second = at_zero(sp.diff(raw_mgf, jx, jy), jx, jy)
    check(
        "dropping log gives the raw moment, not the connected covariance",
        raw_second != cov_xy and raw_second == exy,
        f"raw d_xy={raw_second}, E[XY]={exy}, connected={cov_xy}",
    )
    linear_inside_log = -sum(
        sp.Rational(w, total) * (jx * x + jy * y)
        for w, x, y in zip(weights, x_vals, y_vals)
    )
    check(
        "moving log inside/linearizing loses the connected second cumulant",
        at_zero(sp.diff(linear_inside_log, jx, jy), jx, jy) == 0
        and cov_xy != 0,
        f"linearized d_xy=0, connected={cov_xy}",
    )

    print("\n[D] source-boundary checks")
    note = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    check("source note cites this finite proof runner", "pwc_commuting_cgf_framework_native_2026_06_17.py" in note)
    check(
        "source note makes textbook references parallel, not load-bearing",
        "parallel provenance" in note_flat
        and "not as load-bearing premises" in note_flat,
    )
    check(
        "source note keeps rho_ref and noncommuting ordering out of scope",
        "does not derive `rho_ref`" in note_flat
        and "Noncommuting source families remain outside this theorem" in note_flat,
    )

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
