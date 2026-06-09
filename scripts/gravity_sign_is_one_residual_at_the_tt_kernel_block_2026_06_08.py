"""Bounded gravity-sign residual locator at the scalar-W TT kernel.

This runner checks the sign identity under supplied source/action premises and
the finite tensor-algebra fact that the scalar-W metric Hessian annihilates
transverse-traceless spin-2 perturbations. It does not derive G>0, a
framework gravitational action, or a new primitive.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(cond)
    FAIL += int(not cond)
    return cond


def main() -> int:
    print("GRAVITY SIGN: bounded scalar-W TT-kernel residual locator")
    print("=" * 78)

    numerator_tensor = 0.5
    source_sq = 1.0

    def tt_kinetic_coeff(kappa: float) -> float:
        return 1.0 / (2.0 * kappa)

    def exchange_potential(kappa: float) -> float:
        return -kappa * numerator_tensor * source_sq

    same_sign = all(
        np.sign(tt_kinetic_coeff(kappa)) == np.sign(kappa)
        and np.sign(-exchange_potential(kappa)) == np.sign(kappa)
        for kappa in (-3.0, -1.0, -0.2, 0.2, 1.0, 3.0)
    )
    check(
        "K1 exchange-sign identity under supplied source/action premises",
        same_sign
        and tt_kinetic_coeff(+1.0) > 0
        and exchange_potential(+1.0) < 0
        and tt_kinetic_coeff(-1.0) < 0
        and exchange_potential(-1.0) > 0,
        f"kappa=+1: K_TT={tt_kinetic_coeff(1):+.2f}, V={exchange_potential(1):+.2f}; "
        f"kappa=-1: K_TT={tt_kinetic_coeff(-1):+.2f}, V={exchange_potential(-1):+.2f}",
    )

    rng = np.random.default_rng(0)
    tt_in_kernel = True
    max_overlap = 0.0
    n_checked = 0

    for _ in range(2000):
        q = rng.standard_normal(3)
        qhat = 2.0 * np.sin(q / 2.0)
        norm = np.linalg.norm(qhat)
        if norm < 1e-8:
            continue

        n = qhat / norm
        trial = rng.standard_normal(3)
        e1 = trial - (trial @ n) * n
        e1_norm = np.linalg.norm(e1)
        if e1_norm < 1e-8:
            continue
        e1 = e1 / e1_norm
        e2 = np.cross(n, e1)

        h_plus = np.outer(e1, e1) - np.outer(e2, e2)
        h_cross = np.outer(e1, e2) + np.outer(e2, e1)

        for h_tt in (h_plus, h_cross):
            n_checked += 1
            transverse = np.linalg.norm(qhat @ h_tt) < 1e-9
            traceless = abs(np.trace(h_tt)) < 1e-9
            contraction = float(qhat @ h_tt @ qhat)
            hessian_quadratic = contraction * contraction
            max_overlap = max(max_overlap, abs(contraction))
            if not (transverse and traceless) or hessian_quadratic > 1e-18:
                tt_in_kernel = False

    check(
        "K2 scalar-W Hessian annihilates TT spin-2 samples",
        tt_in_kernel and n_checked > 0,
        f"checked={n_checked}, max |qhat qhat : h_TT|={max_overlap:.2e}",
    )

    note = Path(
        "docs/GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md"
    ).read_text(encoding="utf-8")
    guardrails = [
        "This is a bounded residual-location result, not a closure",
        "scalar-`W` route cannot determine",
        "No global",
        "no new primitive, axiom, Tier-A admission",
        "does not mean matter, stress",
    ]
    check(
        "K3 source note keeps the route boundary explicit",
        all(item in note for item in guardrails),
        "guardrails present for bounded scope, scalar-W-only kernel, no-go discipline, and no primitive",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: PASS for the bounded route locator. Under supplied source/action premises,\n"
        "the attraction sign tracks the healthy spin-2 kinetic sign. The scalar-W metric\n"
        "Hessian is rank-one longitudinal and annihilates TT perturbations, so that route\n"
        "cannot determine the spin-2 kinetic sign. Geometric, full stress-response, and\n"
        "RP/unitarity routes remain open."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
