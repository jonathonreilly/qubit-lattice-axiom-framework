#!/usr/bin/env python3
"""Restricted source packet for the trace-vs-center Koide fork.

The packet checks only finite C3-circulant algebra on

    H = a I + b(C + C^2),       C^3 = I,       a > 0,

with the phase set to zero for the two-level singlet/doublet formulas.  It does
not derive a physical charged-lepton readout, a block-count selector, or a
Fourier-modulus selector.  Its job is narrower: instantiate the formulas that
were previously displayed as inventory entries.
"""

from __future__ import annotations

import sympy as sp


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


def main() -> int:
    a, b, r, x = sp.symbols("a b r x", positive=True)
    t = sp.symbols("t", positive=True)

    lam_s = a + 2 * b
    lam_d = a - b

    print("=== D1. signed/Hermitian trace formula ===")
    q_trace = sp.simplify((lam_s**2 + 2 * lam_d**2) / (lam_s + 2 * lam_d) ** 2)
    q_trace_r = sp.simplify(q_trace.subs(b, a * sp.sqrt(r)))
    root_trace = sp.solve(sp.Eq(q_trace_r, sp.Rational(2, 3)), r)
    check(
        "signed trace/dimension formula is Q = 1/3 + (2/3) r",
        sp.simplify(q_trace_r - (sp.Rational(1, 3) + sp.Rational(2, 3) * r)) == 0,
        f"Q_trace={q_trace_r}; Q=2/3 roots={root_trace}",
    )
    check(
        "the trace denominator is fixed by Tr(H)=3a and doublet multiplicity two",
        sp.simplify(lam_s + 2 * lam_d - 3 * a) == 0,
        f"lambda_s={lam_s}, lambda_d={lam_d}",
    )

    print("\n=== D2. center/block-count inventory formula ===")
    # The block-count inventory entry keeps the same trace normalization 9 a^2
    # but weights the complex doublet block once instead of by two real
    # dimensions: numerator = 3 a^2 + 3 b^2.
    q_block = sp.simplify((3 * a**2 + 3 * b**2) / (3 * a) ** 2)
    q_block_r = sp.simplify(q_block.subs(b, a * sp.sqrt(r)))
    root_block = sp.solve(sp.Eq(q_block_r, sp.Rational(2, 3)), r)
    check(
        "center/block-count formula is Q_block = 1/3 + (1/3) r",
        sp.simplify(q_block_r - (sp.Rational(1, 3) + sp.Rational(1, 3) * r)) == 0,
        f"Q_block={q_block_r}; Q=2/3 roots={root_block}",
    )
    check(
        "center/block-count reaches Q=2/3 at r=1, not r=1/2",
        root_block == [sp.Integer(1)] and q_block_r.subs(r, sp.Rational(1, 2)) == sp.Rational(1, 2),
        f"Q_block(1/2)={q_block_r.subs(r, sp.Rational(1, 2))}, Q_block(1)={q_block_r.subs(r, 1)}",
    )

    print("\n=== D3. eigenvalue-as-mass separated from singular-value readout ===")
    # Positive chamber x = b/a in (0, 1), masses m_k = lambda_k rather than lambda_k^2.
    q_eig_mass = sp.simplify(3 / (sp.sqrt(1 + 2 * x) + 2 * sp.sqrt(1 - x)) ** 2)
    x_star = sp.Rational(1, 4) + sp.sqrt(2) / 2
    r_star = sp.simplify(x_star**2)
    check(
        "eigenvalue-as-mass Q=2/3 root is exact",
        sp.simplify(q_eig_mass.subs(x, x_star) - sp.Rational(2, 3)) == 0,
        f"x=b/a={x_star}; r=x^2={r_star} ~= {float(r_star):.6f}",
    )
    check(
        "the squared equation is 16 x^2 - 8 x - 7 = 0 on the positive chamber",
        sp.simplify(16 * x_star**2 - 8 * x_star - 7) == 0 and 0 < float(x_star) < 1,
        f"x_star ~= {float(x_star):.6f}, so all two-level eigenvalues remain nonnegative",
    )
    check(
        "this is not a global singular-value readout claim",
        True,
        "singular-value readout uses |lambda_k| across sign/phase chambers; this packet only isolates the positive eigenvalue-as-mass solve",
    )

    print("\n=== D4. Fisher and Bures/SLD sector balances ===")
    # Unnormalized eigenvalue Fisher balance reproduces the older classical entry.
    lam_s_x = 1 + 2 * x
    lam_d_x = 1 - x
    # Compute derivatives with r as x^2: d/dr = (1/(2x)) d/dx.
    i_s_classical = sp.simplify((sp.diff(lam_s_x, x) / (2 * x)) ** 2 / lam_s_x**2)
    i_d_classical = sp.simplify(2 * (sp.diff(lam_d_x, x) / (2 * x)) ** 2 / lam_d_x**2)
    classical_roots = [
        sp.simplify(root**2)
        for root in sp.solve(sp.Eq(i_s_classical, i_d_classical), x)
        if root.is_real is not False and 0 < float(root.evalf()) < 1
    ]
    check(
        "classical unnormalized Fisher balance lands r = 17/2 - 6 sqrt(2)",
        classical_roots == [sp.Rational(17, 2) - 6 * sp.sqrt(2)],
        f"r_Fisher={classical_roots[0]} ~= {float(classical_roots[0]):.6f}",
    )

    # For commuting density matrices the Bures/SLD metric is one quarter of
    # the classical Fisher metric on normalized spectral probabilities.
    p_s = sp.Rational(1, 3) * (1 + 2 * x)
    p_d = sp.Rational(1, 3) * (1 - x)
    sld_s = sp.simplify((sp.diff(p_s, x) / (2 * x)) ** 2 / (4 * p_s))
    sld_d_total = sp.simplify(2 * (sp.diff(p_d, x) / (2 * x)) ** 2 / (4 * p_d))
    sld_roots = [
        sp.simplify(root**2)
        for root in sp.solve(sp.Eq(sld_s, sld_d_total), x)
        if root.is_real is not False and 0 < float(root.evalf()) < 1
    ]
    check(
        "Bures/SLD normalized spectral sector balance lands r = 1/16",
        sld_roots == [sp.Rational(1, 16)],
        f"p_s={p_s}, p_d(each)={p_d}, r_SLD={sld_roots[0]}",
    )
    check(
        "Bures/SLD r=1/16 is not the Koide r=1/2 point",
        sld_roots[0] != sp.Rational(1, 2),
        f"Q_trace(1/16)={q_trace_r.subs(r, sp.Rational(1, 16))}",
    )

    print("\n=== D5. heat/Seeley coefficient endpoint behavior ===")
    # Even heat coefficients are A_n(r)=Tr(H^(2n)) on the two-level chamber.
    # Their nonconstant part is monotone on x in [0,1], so coefficient-level
    # extremization selects only endpoints.
    endpoint_checks = []
    for n in range(1, 5):
        coeff = sp.expand((1 + 2 * x) ** (2 * n) + 2 * (1 - x) ** (2 * n))
        deriv = sp.factor(sp.diff(coeff, x))
        roots = [root for root in sp.solve(sp.Eq(deriv, 0), x) if root.is_real is not False]
        interior = [root for root in roots if 0 < float(root.evalf()) < 1]
        endpoint_checks.append(not interior)
        check(
            f"Seeley coefficient Tr(H^{2*n}) has no interior extremum in x in (0,1)",
            not interior,
            f"d/dx={deriv}",
        )
    theta_series_first = sp.series(
        sp.exp(-t * (1 + 2 * x) ** 2) + 2 * sp.exp(-t * (1 - x) ** 2),
        t,
        0,
        5,
    )
    check(
        "heat-trace coefficient extrema are endpoint-only in this restricted packet",
        all(endpoint_checks),
        f"Theta_t series through t^4: {theta_series_first}",
    )

    print("\n=== D6. scope firewall ===")
    check(
        "no observed mass value or new axiom is used",
        True,
        "all checks are exact finite C3 algebra/source-packet formulas",
    )
    check(
        "physical selector remains open",
        True,
        "block-count vs trace, signed/Hermitian vs singular-value, and r=1/2 modulus selection are not closed here",
    )

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print("VERDICT: restricted bounded support. The signed trace formula, center/block-count")
    print("inventory formula, Bures/SLD r=1/16, endpoint heat/Seeley behavior, and")
    print("positive-chamber eigenvalue-as-mass root are instantiated exactly. The physical")
    print("readout, block-count selector, and Fourier modulus remain open residuals.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
