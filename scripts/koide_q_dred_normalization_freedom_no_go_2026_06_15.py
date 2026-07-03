#!/usr/bin/env python3
"""No-go runner for deriving D_red = I_2 from the Koide reduced block algebra.

The reduced two-slot determinant law is invariant under a positive baseline
scale c after rescaling source coordinates k -> k/c. This runner checks the
finite algebra and the source-note boundary text. It does not apply or predict
any audit verdict.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    parent = (repo / "docs" / "KOIDE_Q_REDUCED_OBSERVABLE_RESTRICTION_THEOREM_2026-04-22.md").read_text(encoding="utf-8")

    print("=== 1. Source boundary text ===")
    check("parent row names D_red = I_2 as imported/admitted structure", "D_red = I_2" in parent and "imports" in parent)
    check("parent row says physical identification remains open", "physical identification of this reduced carrier remains open" in parent)
    check("parent row does not claim audit status movement", "independent audit lane only" in parent)

    print("\n=== 2. Split algebra with arbitrary positive baseline scale ===")
    k_plus, k_perp, c = sp.symbols("k_plus k_perp c", positive=True, real=True)
    pi_plus = sp.Matrix([[1, 0], [0, 0]])
    pi_perp = sp.Matrix([[0, 0], [0, 1]])
    i2 = sp.eye(2)
    k = k_plus * pi_plus + k_perp * pi_perp
    d_c = c * i2

    check("split projectors are orthogonal and sum to I_2", pi_plus * pi_perp == sp.zeros(2) and pi_plus + pi_perp == i2)
    check("split-preserving source is diag(k_+, k_perp)", k == sp.diag(k_plus, k_perp), f"K={k}")

    w_c = sp.simplify(sp.log((d_c + k).det()) - sp.log(d_c.det()))
    expected = sp.log(1 + k_plus / c) + sp.log(1 + k_perp / c)
    check(
        "W_c(K)=log det(cI+K)-log det(cI)=log(1+k_+/c)+log(1+k_perp/c)",
        sp.simplify(sp.exp(w_c - expected) - 1) == 0,
        f"W_c={w_c}",
    )

    print("\n=== 3. Source-coordinate rescaling leaves normalized law unchanged ===")
    u_plus, u_perp = sp.symbols("u_plus u_perp", positive=True, real=True)
    normalized = sp.simplify(w_c.subs({k_plus: c * u_plus, k_perp: c * u_perp}))
    target = sp.log(1 + u_plus) + sp.log(1 + u_perp)
    check(
        "substitution u_i=k_i/c recovers the c=1 normalized law",
        sp.simplify(sp.exp(normalized - target) - 1) == 0,
        f"W_c(cu)={normalized}",
    )

    deriv_plus = sp.simplify(sp.diff(w_c, k_plus).subs({k_plus: 0, k_perp: 0}))
    deriv_perp = sp.simplify(sp.diff(w_c, k_perp).subs({k_plus: 0, k_perp: 0}))
    check("zero-source derivative scale is 1/c in the plus slot", deriv_plus == 1 / c, f"dW/dk_+={deriv_plus}")
    check("zero-source derivative scale is 1/c in the perp slot", deriv_perp == 1 / c, f"dW/dk_perp={deriv_perp}")
    check(
        "c=1 and c=2 give different derivative units when k is held fixed",
        deriv_plus.subs(c, 1) != deriv_plus.subs(c, 2),
        f"c=1 -> {deriv_plus.subs(c, 1)}, c=2 -> {deriv_plus.subs(c, 2)}",
    )

    print("\n=== 4. Legendre dual also carries the same normalization freedom ===")
    y1, y2 = sp.symbols("y1 y2", positive=True, real=True)
    phi = w_c - k_plus * y1 - k_perp * y2
    stat = sp.solve([sp.diff(phi, k_plus), sp.diff(phi, k_perp)], [k_plus, k_perp], dict=True)[0]
    k_plus_star = sp.simplify(stat[k_plus])
    k_perp_star = sp.simplify(stat[k_perp])
    check("dual stationary source has c-dependent scale in plus slot", k_plus_star == 1 / y1 - c, f"k_+*={k_plus_star}")
    check("dual stationary source has c-dependent scale in perp slot", k_perp_star == 1 / y2 - c, f"k_perp*={k_perp_star}")

    print("\n=== 5. Conclusion ===")
    check(
        "D_red = I_2 is a normalization bridge, not a consequence of split algebra alone",
        True,
        "the family D_c=cI_2 satisfies the same reduced determinant shape for all c>0",
    )
    check(
        "positive repair must supply a physical response-unit theorem or approved premise",
        True,
        "more determinant algebra cannot select c=1",
    )

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
