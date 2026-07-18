#!/usr/bin/env python3
"""Exact checks for the post-erasure odd-side structure note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/THETA_POST_ERASURE_ODD_SIDE_LOG_EQUIVALENCE_AND_ADDITIVITY_INCOMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-18.md"
PARENT_NOTE = ROOT / "docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
ERASURE_NOTE = ROOT / "docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"


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

    # Group M -- modulus and the exponential bridge.
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
        "M2 exponential and logarithmic bridges are exact on the stated domains",
        sp.simplify(sp.exp(u) * sp.exp(v) - sp.exp(u + v)) == 0
        and sp.expand_log(sp.log(x * y), force=False)
        == sp.log(x) + sp.log(y),
    )
    s = sp.symbols("s", real=True)
    power_G = sp.expand_log(sp.log((sp.exp(u)) ** s), force=False)
    checks.check(
        "M3 power-family consistency instance G(u)=s*u",
        sp.simplify(power_G - s * u) == 0,
    )

    # Group T1 -- log equivalence, both directions (strict positivity).
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
    g_part, g_rest, g_total = sp.symbols("g_part g_rest g_total", real=True)
    r_fold = sp.solve(
        (sp.Eq(3 * g_part + g_rest, g_total), sp.Eq(g_rest, 0)),
        (g_part, g_rest),
        dict=True,
    )
    checks.check(
        "T1c rational-homogeneity elimination instance",
        r_fold == [{g_part: g_total / 3, g_rest: 0}],
    )

    # Group D -- degeneracy lemma.
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

    # Group INC -- scalar-additivity incompatibility on the slice.
    checks.check(
        "INC1 the additive shape at the unit block forces F(1)=0",
        sp.solve(sp.Eq(f_one, 2 * f_one), f_one) == [0],
    )
    fa = sp.symbols("fa", real=True)
    inc2 = sp.reduce_inequalities([fa >= 0, -fa >= 0, fa > 0], fa)
    inc2_solution = sp.reduce_inequalities([fa >= 0, -fa >= 0], fa)
    checks.check(
        "INC2 nonnegative pair summing to zero has no positive member",
        (inc2 is sp.false or inc2 == False)
        and inc2_solution == sp.Eq(fa, 0),
    )
    checks.check(
        "INC3 identity witness: multiplicative but scalar-additivity fails 6 != 5",
        2 * 3 == 6 and 2 + 3 == 5 and 6 != 5
        and sp.simplify((x * y) - x * y) == 0,
    )

    # Group B -- non-reconstruction discriminator and phase-silence.
    def good(zv):
        return zv / sp.Abs(zv)

    def bad(zv):
        return sp.exp(sp.I * sp.sin(sp.arg(zv)))

    checks.check(
        "B1 discriminator pair shares zero logarithmic modulus at unit modulus",
        sp.simplify(sp.log(sp.Abs(good(sp.I)))) == 0
        and sp.simplify(sp.log(sp.Abs(bad(sp.I)))) == 0,
    )
    checks.check(
        "B2 good character is multiplicative at the pair (i, i)",
        sp.simplify(good(sp.I * sp.I) - good(sp.I) * good(sp.I)) == 0,
    )
    checks.check(
        "B3 twisted readout is not multiplicative at the pair (i, i)",
        sp.simplify(bad(sp.I * sp.I) - 1) == 0
        and sp.simplify(bad(sp.I) ** 2 - sp.exp(2 * sp.I)) == 0
        and bad(sp.I * sp.I) != bad(sp.I) ** 2,
    )
    full = lambda zv: sp.exp(sp.I * sp.arg(zv)) * sp.Abs(zv) ** s
    fixed = sp.Rational(5, 2)
    checks.check(
        "B4 pre-erasure phase-silence contrast at fixed modulus",
        full(sp.exp(sp.I * 0)) == 1
        and full(sp.exp(sp.I * sp.pi / 2)) == sp.I
        and sp.simplify(
            sp.expand_log(sp.log(sp.Abs(full(fixed * sp.exp(sp.I * 0)))), force=False)
            - sp.expand_log(
                sp.log(sp.Abs(full(fixed * sp.exp(sp.I * sp.pi / 2)))),
                force=False,
            )
        )
        == 0,
    )

    # Group N -- source needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 parent odd-side ingredient needle",
        PARENT_NOTE,
        "an independently supplied quark-side odd-side ingredient",
    )
    checks.needle(
        "N2 erasure-note phase-free family needle",
        ERASURE_NOTE,
        "the invariant\nmembers of this determinant-character family are "
        "phase-free functions of `|det|`",
    )
    checks.needle(
        "N3 target identifier and label needles",
        TARGET_NOTE,
        (
            "theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_bounded_theorem_note_2026-07-18",
            "**(P-hom, slice form)**",
            "**(P-log)**",
            "**(P-add, slice form)**",
            "admits only the degenerate readout",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
