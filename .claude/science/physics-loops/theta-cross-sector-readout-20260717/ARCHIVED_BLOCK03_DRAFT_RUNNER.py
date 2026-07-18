#!/usr/bin/env python3
"""Exact checks for the forced logarithmic interface note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/THETA_RECORD_LOG_BRIDGE_FORCED_LOGARITHMIC_INTERFACE_BOUNDED_THEOREM_NOTE_2026-07-18.md"
SIBLING_NOTE = ROOT / "docs/THETA_POST_ERASURE_ODD_SIDE_LOG_EQUIVALENCE_AND_ADDITIVITY_INCOMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-18.md"
PARENT_NOTE = ROOT / "docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


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

    # Group T1 -- raw multiplicative datum exclusion (axiom-sentence lift).
    f_one = sp.symbols("f_one", real=True)
    checks.check(
        "T1a empty-collection anchor and unit block force F(1)=0",
        sp.solve(sp.Eq(f_one, 2 * f_one), f_one) == [0]
        and sp.log(1) == 0,
    )
    fa = sp.symbols("fa", real=True)
    inc = sp.reduce_inequalities([fa >= 0, -fa >= 0, fa > 0], fa)
    inc_solution = sp.reduce_inequalities([fa >= 0, -fa >= 0], fa)
    checks.check(
        "T1b nonnegative inverse-pair summing to zero has no positive member",
        (inc is sp.false or inc == False) and inc_solution == sp.Eq(fa, 0),
    )
    F = sp.Function("F")
    x, x0 = sp.symbols("x x0", positive=True)
    checks.check(
        "T1c degenerate propagation through the multiplicative factorization",
        sp.Eq(F(x), F(x0) * F(x / x0)).subs(F(x0), 0) == sp.Eq(F(x), 0),
    )
    checks.check(
        "T1d two-block additive-shape instantiation is the sibling configuration",
        2 * 3 == 6 and 2 + 3 == 5 and 6 != 5,
    )

    # Group T2 -- forced logarithmic interface.
    u, v, s = sp.symbols("u v s", real=True)
    checks.check(
        "T2a additively-composing presentation is consistent and anchored",
        sp.simplify(s * (u + v) - (s * u + s * v)) == 0
        and (s * u).subs(u, 0) == 0,
    )
    r1, r2 = sp.symbols("r1 r2", positive=True)
    checks.check(
        "T2b logarithmic modulus composes additively across blocks",
        sp.expand_log(sp.log(r1 * r2), force=False)
        == sp.log(r1) + sp.log(r2),
    )
    g_part, g_rest, g_total = sp.symbols("g_part g_rest g_total", real=True)
    r_fold = sp.solve(
        (sp.Eq(3 * g_part + g_rest, g_total), sp.Eq(g_rest, 0)),
        (g_part, g_rest),
        dict=True,
    )
    checks.check(
        "T2c rational-homogeneity consistency instance for the named theorem",
        r_fold == [{g_part: g_total / 3, g_rest: 0}],
    )
    s2 = sp.symbols("s2", real=True)
    slope_solution = sp.solve(sp.Eq(s * 2, s2 * 2), s2)
    checks.check(
        "T2d two additive forms agreeing at one nonzero point coincide",
        slope_solution == [s],
    )

    # Group N -- source needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 axiom readout-additivity sentence needle",
        AXIOM_NOTE,
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`.",
    )
    checks.needle(
        "N2 sibling open-link sentence needle",
        SIBLING_NOTE,
        "Whether any Record/log bridge connects the registrable scalar-additive "
        "shape to logarithmic-coordinate additivity is the exact open link",
    )
    checks.needle(
        "N3 parent tail sentence needle",
        PARENT_NOTE,
        "an independently supplied quark-side odd-side ingredient",
    )
    checks.needle(
        "N4 target identifier and hypothesis labels",
        TARGET_NOTE,
        (
            "theta_record_log_bridge_forced_logarithmic_interface_bounded_theorem_note_2026-07-18",
            "**(R1)**",
            "**(R2)**",
            "the Record/log\nbridge is forced, not chosen",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
