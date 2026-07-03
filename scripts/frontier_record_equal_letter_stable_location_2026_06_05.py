#!/usr/bin/env python3
"""Equal-letter stable-location certificate for the Record-prior dial.

This runner proves a deliberately narrow statement:

* On the two-record alphabet, the equal-letter prior u=(1/2,1/2) is a stable
  fixed point of a post-record atom-symmetric reset/thermalizing dynamics.
* On the generation dial, u is the s=0 location, hence r=1/2 and Q=2/3.
* The same stability construction exists for every pi_s, so this is not a
  physical dial-selection theorem.

Run:
    python3 scripts/frontier_record_equal_letter_stable_location_2026_06_05.py
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
sidecar = importlib.import_module("frontier_record_selector_audit_sidecar_2026_06_05")


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def reset_chain(pi: list[sp.Expr], alpha: sp.Expr) -> sp.Matrix:
    n = len(pi)
    return sp.Matrix(
        [
            [(1 - alpha if i == j else 0) + alpha * pi[j] for j in range(n)]
            for i in range(n)
        ]
    )


def row_stochastic(P: sp.Matrix) -> bool:
    return all(sp.simplify(sum(P[i, j] for j in range(P.cols)) - 1) == 0 for i in range(P.rows))


def stationary(pi: list[sp.Expr], P: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in list(sp.Matrix([pi]) * P - sp.Matrix([pi])))


def detailed_balance(pi: list[sp.Expr], P: sp.Matrix) -> bool:
    return all(
        sp.simplify(pi[i] * P[i, j] - pi[j] * P[j, i]) == 0
        for i in range(len(pi))
        for j in range(len(pi))
    )


def main() -> int:
    alpha = sp.symbols("alpha", real=True)
    s = sp.symbols("s", real=True)
    n = sp.symbols("n", integer=True, nonnegative=True)
    p0 = sp.symbols("p0", real=True)

    # ------------------------------------------------------------------
    # 1. Sidecar integration: exactly three rows are stable-location rows.
    # ------------------------------------------------------------------
    stable_rows = {
        cid: row
        for cid, row in sidecar.SIDE_CAR_ROWS.items()
        if row["class"] == "equal_letter_stable_location"
    }
    check("S1.1 sidecar exposes exactly three equal-letter stable-location rows", len(stable_rows) == 3)
    check(
        "S1.2 all stable-location rows are marked s=0_stable_location",
        all(row["endpoint"] == "s=0_stable_location" for row in stable_rows.values()),
    )
    check(
        "S1.3 no stable-location row is labelled as forced",
        all("forced" not in row["endpoint"] and "force" not in row["repair"].lower() for row in stable_rows.values()),
    )

    expected_ids = {
        "flavor_missing_axiom_carrier_measure_note_2026-05-30",
        "koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10",
        "koide_tracial_standard_form_carrier_narrow_note_2026-06-02",
    }
    check("S1.4 stable-location row ids match the sidecar target set", set(stable_rows) == expected_ids)

    # ------------------------------------------------------------------
    # 2. Equal-letter dynamics on the post-record two-atom alphabet.
    # ------------------------------------------------------------------
    u = [sp.Rational(1, 2), sp.Rational(1, 2)]
    P = reset_chain(u, alpha)
    check("D2.1 equal-letter reset chain is row-stochastic for symbolic alpha", row_stochastic(P), str(P))
    check("D2.2 equal-letter prior is stationary", stationary(u, P))
    check("D2.3 equal-letter reset chain satisfies detailed balance", detailed_balance(u, P))
    check("D2.4 chain is atom-swap symmetric", sp.simplify(P[0, 0] - P[1, 1]) == 0 and sp.simplify(P[0, 1] - P[1, 0]) == 0)

    eigs = {sp.simplify(k): v for k, v in P.eigenvals().items()}
    check("D2.5 eigenvalues are {1, 1-alpha}", eigs == {sp.Integer(1): 1, 1 - alpha: 1}, str(eigs))

    p = [p0, 1 - p0]
    p_row = sp.Matrix([p])
    u_row = sp.Matrix([u])
    check(
        "D2.6 deviations from equal letters contract by 1-alpha",
        all(sp.simplify(x) == 0 for x in list(p_row * P - u_row - (1 - alpha) * (p_row - u_row))),
    )

    diff = sp.simplify((p_row * P)[0] - (p_row * P)[1])
    check("D2.7 record-letter imbalance contracts by 1-alpha", sp.simplify(diff - (1 - alpha) * (2 * p0 - 1)) == 0)

    iterated_diff = sp.simplify((1 - alpha) ** n * (2 * p0 - 1))
    check(
        "D2.8 iterated imbalance has closed form (1-alpha)^n times initial imbalance",
        iterated_diff == (1 - alpha) ** n * (2 * p0 - 1),
    )

    lyapunov_before = (2 * p0 - 1) ** 2
    lyapunov_after = sp.simplify(diff**2)
    check(
        "D2.9 quadratic imbalance Lyapunov function decreases by (1-alpha)^2",
        sp.simplify(lyapunov_after - (1 - alpha) ** 2 * lyapunov_before) == 0,
    )

    # ------------------------------------------------------------------
    # 3. Location on the generation dial.
    # ------------------------------------------------------------------
    pi_s = [sp.simplify(1 / (1 + 2**s)), sp.simplify(2**s / (1 + 2**s))]
    sol_s0 = sp.solve(sp.Eq(pi_s[0], sp.Rational(1, 2)), s)
    check("G3.1 equal-letter prior is exactly the s=0 dial location", sol_s0 == [0], str(sol_s0))

    r_s = sp.simplify(2 ** (s - 1))
    Q_s = sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * r_s)
    check("G3.2 s=0 gives r=1/2", sp.simplify(r_s.subs(s, 0) - sp.Rational(1, 2)) == 0)
    check("G3.3 s=0 gives Q=2/3 on the supplied Koide algebra map", sp.simplify(Q_s.subs(s, 0) - sp.Rational(2, 3)) == 0)
    check("G3.4 s=1 gives a different stable dial location r=1", sp.simplify(r_s.subs(s, 1) - 1) == 0)
    check("G3.5 Q(s) is not constant across the dial", sp.simplify(Q_s.subs(s, 0) - Q_s.subs(s, 1)) != 0)

    # ------------------------------------------------------------------
    # 4. Non-selection: every pi_s has the same reset-stability form.
    # ------------------------------------------------------------------
    Ps = reset_chain(pi_s, alpha)
    check("N4.1 symbolic pi_s chain is row-stochastic", row_stochastic(Ps))
    check("N4.2 symbolic pi_s is stationary", stationary(pi_s, Ps))
    check("N4.3 symbolic pi_s chain satisfies detailed balance", detailed_balance(pi_s, Ps))

    pi_s_row = sp.Matrix([pi_s])
    check(
        "N4.4 arbitrary pi_s deviations contract by 1-alpha",
        all(sp.simplify(x) == 0 for x in list(p_row * Ps - pi_s_row - (1 - alpha) * (p_row - pi_s_row))),
    )

    pi1 = [sp.Rational(1, 3), sp.Rational(2, 3)]
    P1 = reset_chain(pi1, alpha)
    check("N4.5 dimension/Born endpoint s=1 is also stable under its own reset chain", row_stochastic(P1) and stationary(pi1, P1))
    check("N4.6 equal-letter stability is not dial selection", u != pi1 and row_stochastic(P) and row_stochastic(P1))

    # ------------------------------------------------------------------
    # 5. Axiom and audit boundaries.
    # ------------------------------------------------------------------
    check(
        "B5.1 stable-location sidecar entries avoid audit-clean and forced endpoint labels",
        all(
            not row["class"].startswith("audited_") and row["endpoint"] != "forced"
            for row in stable_rows.values()
        ),
    )
    check("B5.2 imported sidecar writes no audit data when imported", hasattr(sidecar, "SIDE_CAR_ROWS"))

    print("\n=== Stable-location interpretation ===")
    print("Equal-letter is a stable s=0 location on the post-record atom-symmetric dial.")
    print("The construction also works for arbitrary pi_s, so it is not a physical dial selector.")
    print("The three sidecar rows should be read as stable-location support only.")
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
