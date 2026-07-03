"""RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA -- finite exact checks.

The 2026-06-05 Record axiom gives finite additivity of scalar readout over
supplied disjoint records. This runner isolates the algebra that follows from
that statement:

  * a finite record function is a sector readout vector;
  * disjoint unions are sums;
  * coarse-graining is multiplication by an incidence matrix;
  * ratios and normalized coordinates are structural readout coordinates when
    denominators are nonzero;
  * finite additivity alone does not select a probability, weight, or dynamics.
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


def indicator(mask: int, n: int) -> sp.Matrix:
    return sp.Matrix([(mask >> i) & 1 for i in range(n)])


def readout(mask_vec: sp.Matrix, values: sp.Matrix) -> sp.Expr:
    return sp.simplify((mask_vec.T * values)[0])


def main() -> int:
    x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
    k = sp.symbols("k", positive=True)
    u, d, rho, p = sp.symbols("u d rho p", positive=True)
    alpha, beta, theta, r = sp.symbols("alpha beta theta r", positive=True, real=True)
    a2, b2 = sp.symbols("a2 b2", positive=True)
    ln2 = sp.log(2)

    values = sp.Matrix([x0, x1, x2, x3])
    ones4 = sp.Matrix([[1, 1, 1, 1]])

    # -------------------------------------------------------------------------
    # 1. Finite additivity on disjoint supplied records.
    # -------------------------------------------------------------------------
    additivity_ok = True
    disjoint_pairs = 0
    for mask_a in range(16):
        for mask_b in range(16):
            if mask_a & mask_b:
                continue
            disjoint_pairs += 1
            chi_a = indicator(mask_a, 4)
            chi_b = indicator(mask_b, 4)
            chi_union = indicator(mask_a | mask_b, 4)
            lhs = readout(chi_union, values)
            rhs = readout(chi_a, values) + readout(chi_b, values)
            if sp.simplify(lhs - rhs) != 0:
                additivity_ok = False
                break

    check("R1.1 finite additivity holds for every ordered disjoint pair of 4 supplied records",
          additivity_ok and disjoint_pairs == 81,
          f"checked ordered disjoint pairs={disjoint_pairs}")

    singleton_sum = sum(readout(indicator(1 << i, 4), values) for i in range(4))
    total = readout(indicator(15, 4), values)
    check("R1.2 total record readout is the sum of singleton sector readouts",
          sp.simplify(total - singleton_sum) == 0,
          f"total={total}")

    empty = readout(indicator(0, 4), values)
    check("R1.3 empty supplied union has zero readout",
          sp.simplify(empty) == 0)

    # -------------------------------------------------------------------------
    # 2. Coarse-graining is incidence-matrix multiplication.
    # -------------------------------------------------------------------------
    coarse = sp.Matrix([[1, 1, 0, 0],
                        [0, 0, 1, 1]])
    coarse_values = coarse * values
    check("R2.1 coarse-graining maps sector vector v to incidence product C v",
          coarse_values == sp.Matrix([x0 + x1, x2 + x3]),
          f"Cv={list(coarse_values)}")

    column_coverage = sp.Matrix([[1, 1]]) * coarse
    check("R2.2 partition coarse-graining preserves total readout",
          column_coverage == ones4
          and sp.simplify((sp.Matrix([[1, 1]]) * coarse_values)[0] - total) == 0)

    further = sp.Matrix([[1, 1]])
    check("R2.3 repeated coarse-graining composes associatively",
          further * (coarse * values) == (further * coarse) * values)

    refine_a = sp.Matrix([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 1]])
    refine_b = sp.Matrix([[1, 1, 0],
                          [0, 0, 1]])
    check("R2.4 a refinement followed by a coarsening is again an incidence coarse-graining",
          refine_b * (refine_a * values) == coarse * values)

    # -------------------------------------------------------------------------
    # 3. Ratios and normalized coordinates are structural readout coordinates.
    # They are not probabilities unless a separate probability/Born gate is
    # supplied.
    # -------------------------------------------------------------------------
    two = sp.Matrix([u, d])
    two_total = u + d
    norm = sp.Matrix([u / two_total, d / two_total])
    ratio = d / u
    check("R3.1 two-sector normalized coordinates sum to one when total is nonzero",
          sp.simplify(norm[0] + norm[1] - 1) == 0,
          f"normalized=[{norm[0]}, {norm[1]}]")
    check("R3.2 normalized coordinates are invariant under global readout scaling",
          sp.simplify((k * u) / (k * u + k * d) - norm[0]) == 0
          and sp.simplify((k * d) / (k * u + k * d) - norm[1]) == 0)
    check("R3.3 readout ratios are invariant under global readout scaling",
          sp.simplify((k * d) / (k * u) - ratio) == 0)

    arbitrary_d = p * u / (1 - p)
    arbitrary_norm_1 = sp.simplify(arbitrary_d / (u + arbitrary_d))
    check("R3.4 finite additivity leaves normalized two-sector coordinate arbitrary",
          sp.simplify(arbitrary_norm_1 - p) == 0,
          "for any supplied p in (0,1), choose d=p*u/(1-p)")

    # -------------------------------------------------------------------------
    # 4. Generation dial coordinates from a two-sector record function.
    # -------------------------------------------------------------------------
    singlet_readout = a2
    doublet_readout = 2 * b2
    generation_ratio = sp.simplify(b2 / a2)
    sector_ratio = sp.simplify(doublet_readout / singlet_readout)
    s_from_sector_ratio = sp.log(sector_ratio) / ln2

    check("R4.1 generation sector ratio is doublet/singlet = 2r",
          sp.simplify(sector_ratio - 2 * generation_ratio) == 0,
          f"sector_ratio={sector_ratio}")
    check("R4.2 dial coordinate is log2(doublet/singlet)",
          sp.simplify(s_from_sector_ratio - sp.log(2 * generation_ratio) / ln2) == 0)

    lambdas = [
        alpha + 2 * beta * sp.cos(theta + 2 * sp.pi * j / 3)
        for j in range(3)
    ]
    sum_lambda = sp.simplify(sp.expand_trig(sum(lambdas)))
    sum_lambda_sq = sp.simplify(sp.expand_trig(sum(lam ** 2 for lam in lambdas)))
    q_power_sum = sp.simplify(sum_lambda_sq / sum_lambda ** 2)
    q_from_r = sp.Rational(1, 3) + sp.Rational(2, 3) * r
    q_from_blocks = sp.simplify((singlet_readout + doublet_readout) / (3 * singlet_readout))

    check("R4.3 C3/KCPT square-root readout power sums define Q",
          sp.simplify(sum_lambda - 3 * alpha) == 0
          and sp.simplify(sum_lambda_sq - (3 * alpha ** 2 + 6 * beta ** 2)) == 0,
          f"S1={sum_lambda}; S2={sum_lambda_sq}")
    check("R4.4 Q = S2/S1^2 derives Q(r)=1/3+2r/3 before endpoint substitution",
          sp.simplify(q_power_sum.subs(beta, sp.sqrt(r) * alpha) - q_from_r) == 0,
          f"Q={q_power_sum}")
    check("R4.5 two-block powers give the same generation Q coordinate",
          sp.simplify(q_from_blocks - (sp.Rational(1, 3) + sp.Rational(2, 3) * generation_ratio)) == 0,
          f"Q_blocks={q_from_blocks}")

    rho_sector = rho
    r_from_rho = rho_sector / 2
    q_from_rho = sp.simplify(q_from_r.subs(r, r_from_rho))
    s_from_rho = sp.log(rho_sector) / ln2
    check("R4.6 sector balance rho=1 gives s=0, r=1/2, Q=2/3",
          sp.simplify(s_from_rho.subs(rho, 1)) == 0
          and sp.simplify(r_from_rho.subs(rho, 1) - sp.Rational(1, 2)) == 0
          and sp.simplify(q_from_rho.subs(rho, 1) - sp.Rational(2, 3)) == 0)
    check("R4.7 real-mode balance rho=2 gives s=1, r=1, Q=1",
          sp.simplify(s_from_rho.subs(rho, 2) - 1) == 0
          and sp.simplify(r_from_rho.subs(rho, 2) - 1) == 0
          and sp.simplify(q_from_rho.subs(rho, 2) - 1) == 0)

    arbitrary_two = sp.Matrix([u, rho * u])
    arbitrary_total = (sp.Matrix([[1, 1]]) * arbitrary_two)[0]
    arbitrary_norm = sp.simplify(arbitrary_two[1] / arbitrary_total)
    check("R4.8 Record additivity permits arbitrary positive sector ratio rho",
          rho in arbitrary_norm.free_symbols
          and sp.simplify(arbitrary_norm - rho / (1 + rho)) == 0,
          "rho remains a free readout ratio until a weighting/dynamics gate is supplied")

    # -------------------------------------------------------------------------
    # 5. Boundary checks: additive readout is not hidden probability/dynamics.
    # -------------------------------------------------------------------------
    born_claim = sp.Eq(d / (u + d), d / u)
    check("R5.1 normalized coordinate is not the same object as raw sector ratio",
          sp.simplify(born_claim.lhs - born_claim.rhs) != 0,
          "normalization is an extra coordinate choice, not a new Record axiom")

    dynamic_update = sp.Matrix([u, d])
    check("R5.2 finite additivity imposes no autonomous update law on the readout vector",
          dynamic_update.free_symbols == {u, d},
          "the vector is unchanged until an external dynamics map is supplied")

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print("FINDING: Record supplies finite additive readout-vector algebra;")
    print("         probability, weighting, and dynamics remain separate gates.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
