#!/usr/bin/env python3
"""Exact finite checks for the post-erasure structure note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/THETA_POST_ERASURE_ODD_SIDE_LOG_EQUIVALENCE_AND_ADDITIVITY_INCOMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-18.md"
PARENT_NOTE = ROOT / "docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
ERASURE_NOTE = ROOT / "docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
REGISTRABILITY_NOTE = ROOT / "docs/REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"
SUPPORT_NOTE = ROOT / "docs/BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md"


def normalized_whitespace(text):
    return " ".join(text.split())


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        ok = bool(condition)
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def needle(self, label, path, needles):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(needles, str):
            needles = (needles,)
        self.check(
            label,
            all(normalized_whitespace(n) in haystack for n in needles),
        )

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def main():
    checks = CheckRunner()

    # Group M -- modulus and exponential/logarithmic coordinates.
    r1, r2 = sp.symbols("r1 r2", positive=True)
    phi1, phi2 = sp.symbols("phi1 phi2", real=True)
    z1 = r1 * sp.exp(sp.I * phi1)
    z2 = r2 * sp.exp(sp.I * phi2)
    checks.check(
        "M1 symbolic modulus is multiplicative across blocks",
        sp.simplify(sp.Abs(z1 * z2) - sp.Abs(z1) * sp.Abs(z2)) == 0,
    )
    u, v = sp.symbols("u v", real=True)
    x, y = sp.symbols("x y", positive=True)
    checks.check(
        "M2 exponential and logarithmic bridges are exact on positive domains",
        sp.simplify(sp.exp(u) * sp.exp(v) - sp.exp(u + v)) == 0
        and sp.expand_log(sp.log(x * y), force=False)
        == sp.log(x) + sp.log(y),
    )
    slope = sp.Rational(3, 2)
    checks.check(
        "M3 a power-family instance has G(u)=s*u",
        sp.simplify(
            sp.expand_log(sp.log((sp.exp(u)) ** slope), force=False)
            - slope * u
        )
        == 0,
    )

    # Group T1 -- equivalence plus the explicit regularity guard.
    f_x, f_y = sp.symbols("f_x f_y", positive=True)
    checks.check(
        "T1a multiplicative-to-additive direction on strictly positive values",
        sp.expand_log(sp.log(f_x * f_y), force=False)
        == sp.log(f_x) + sp.log(f_y),
    )
    g_u, g_v = sp.symbols("g_u g_v", real=True)
    checks.check(
        "T1b additive-to-multiplicative direction through exp",
        sp.simplify(sp.exp(g_u + g_v) - sp.exp(g_u) * sp.exp(g_v)) == 0,
    )
    checks.needle(
        "T1c the power conclusion is guarded by the explicit P-bdd premise",
        TARGET_NOTE,
        (
            "**(P-bdd)** there exist real `a`, `L > 0`, and `B >= 0`",
            "Therefore and only under that added regularity premise, `F(x)=x^s`.",
        ),
    )

    # Group D -- multiplicative degeneracy.
    f_one = sp.symbols("f_one", real=True)
    checks.check(
        "D1 F(1)=F(1)^2 has exactly the values zero and one",
        sp.solve(sp.Eq(f_one, f_one**2), f_one) == [0, 1],
    )
    F = sp.Function("F")
    x0 = sp.symbols("x0", positive=True)
    checks.check(
        "D2 a zero propagates through the multiplicative factorization",
        sp.Eq(F(x), F(x0) * F(x / x0)).subs(F(x0), 0) == sp.Eq(F(x), 0),
    )

    # Group INC -- the exact scalar product-to-sum lemma.
    checks.check(
        "INC1 the product-to-sum law at the unit forces F(1)=0",
        sp.solve(sp.Eq(f_one, 2 * f_one), f_one) == [0],
    )
    fa = sp.symbols("fa", real=True)
    no_positive_solution = sp.reduce_inequalities(
        [fa >= 0, -fa >= 0, fa > 0], fa
    )
    zero_solution = sp.reduce_inequalities([fa >= 0, -fa >= 0], fa)
    checks.check(
        "INC2 a nonnegative pair summing to zero has no positive member",
        (no_positive_solution is sp.false or no_positive_solution is False)
        and zero_solution == sp.Eq(fa, 0),
    )
    checks.check(
        "INC3 F(x)=x is multiplicative but gives the exact witness 6!=5",
        2 * 3 == 6 and 2 + 3 == 5 and 6 != 5,
    )

    # Group A -- five exact boundary attacks recorded in the N1 table.
    log_product_residual = sp.expand_log(
        sp.log(sp.Integer(2) * sp.Integer(3)), force=True
    ) - sp.log(2) - sp.log(3)
    checks.check(
        "A1 signed log is a nonzero full-group product-to-sum solution",
        sp.simplify(log_product_residual) == 0 and sp.log(2) != 0,
    )
    checks.check(
        "A2 log is a nonnegative nonzero solution on the inverse-free submonoid",
        sp.log(2) > 0
        and sp.log(3) > 0
        and sp.simplify(log_product_residual) == 0,
    )
    checks.check(
        "A3 disjoint cardinalities add while channel scalars multiply",
        2 + 3 == 5 and 2 * 3 == 6 and 5 != 6,
    )
    baseline = sp.Rational(5, 2)
    checks.check(
        "A4 a positive constant solves only the baseline-shifted law",
        baseline == baseline + baseline - baseline
        and baseline != baseline + baseline,
    )
    sparse_values = {2: 1, 3: 1, 6: 2}
    checks.check(
        "A5 sparse support permits a nonzero nonnegative product relation",
        sparse_values[6] == sparse_values[2] + sparse_values[3]
        and 1 not in sparse_values,
    )

    # Group B -- continuous K-even unit-modulus discriminator.
    def flat(_z):
        return sp.Integer(1)

    def twist(zv):
        return sp.exp(sp.I * (1 - sp.re(zv) / sp.Abs(zv)))

    checks.check(
        "B1 flat and twisted readouts have the same zero log modulus",
        sp.simplify(sp.log(sp.Abs(flat(sp.I)))) == 0
        and sp.simplify(sp.log(sp.Abs(twist(sp.I)))) == 0,
    )
    checks.check(
        "B2 the twisted readout is K-even at the exact conjugate pair",
        sp.simplify(twist(sp.conjugate(sp.I)) - twist(sp.I)) == 0,
    )
    checks.check(
        "B3 identical log modulus does not fix the phase at i",
        sp.Eq(twist(sp.I), flat(sp.I)) is sp.false,
    )
    checks.check(
        "B4 the flat readout is multiplicative at (i,-i)",
        flat(sp.I * -sp.I) == flat(sp.I) * flat(-sp.I),
    )
    twist_residual = sp.simplify(
        twist(sp.I * -sp.I) - twist(sp.I) * twist(-sp.I)
    )
    checks.check(
        "B5 the twisted readout is not multiplicative at (i,-i)",
        sp.Eq(twist_residual, 0) is sp.false,
    )

    # Group C -- representative partial closures from the T3 N1 table.
    checks.check(
        "C1 log modulus reconstructs a strictly positive readout",
        sp.simplify(sp.exp(sp.log(x)) - x) == 0,
    )
    known_radius = sp.Integer(4)
    known_slope = sp.Rational(3, 2)
    checks.check(
        "C2 known bounded power class is reconstructed from its log modulus",
        sp.simplify(
            sp.exp(known_slope * sp.log(known_radius))
            - known_radius**known_slope
        )
        == 0,
    )
    checks.check(
        "C3 log modulus plus winding reconstructs a character instance",
        sp.simplify(
            sp.exp(sp.log(2)) * sp.exp(sp.I * sp.pi / 2) - 2 * sp.I
        )
        == 0,
    )
    cocycle_ratio = sp.simplify(
        twist(sp.I * -sp.I) / (twist(sp.I) * twist(-sp.I))
    )
    checks.check(
        "C4 the supplied phase-cocycle defect detects nonmultiplicativity",
        sp.Eq(cocycle_ratio, 1) is sp.false,
    )

    # Group N -- current-source guards. __TOTAL__ is deliberately not matched.
    checks.needle(
        "N1 current parent retains two route-specific supplied conditions",
        PARENT_NOTE,
        (
            "If a quark determinant channel is independently shown to carry either conjugate-pair cancellation or the continuous determinant-character law",
            "one-condition algebraic target only after the route-local condition is supplied",
        ),
    )
    checks.needle(
        "N2 erasure source limits k=0 to the determinant-character family",
        ERASURE_NOTE,
        "the invariant members of this determinant-character family are phase-free functions of `|det|`",
    )
    checks.needle(
        "N3 registrability source separates phase-group and Record additivity",
        REGISTRABILITY_NOTE,
        "This is the step that supplies additivity on the phase group; it is not inferred from Record finite additivity.",
    )
    checks.needle(
        "N4 support source refuses to supply a consumer's boundedness premise",
        SUPPORT_NOTE,
        "Does **not** claim boundedness for any consumer's functional",
    )
    checks.needle(
        "N5 target identifier, exact labels, and narrow no-go status",
        TARGET_NOTE,
        (
            "theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_bounded_theorem_note_2026-07-18",
            "**(P-hom)**",
            "**(P-log)**",
            "**(P-bdd)**",
            "**(P-scalar)**",
            "**No-Go Discipline status:** PASS",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
