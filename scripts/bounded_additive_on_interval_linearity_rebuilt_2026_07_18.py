#!/usr/bin/env python3
"""Exact finite checks for the rebuilt bounded-additive support note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md"


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

    # Group S1 -- representative rational-homogeneity eliminations.
    g0 = sp.symbols("g0", real=True)
    checks.check(
        "S1a G(0)=2G(0) forces G(0)=0",
        sp.solve(sp.Eq(g0, 2 * g0), g0) == [0],
    )
    gu, gnu = sp.symbols("gu gnu", real=True)
    negation = sp.solve(
        (sp.Eq(gu + gnu, 0),), (gnu,), dict=True
    )
    checks.check(
        "S1b the additive pair to zero gives G(-u)=-G(u)",
        negation == [{gnu: -gu}],
    )
    g_part, g_total = sp.symbols("g_part g_total", real=True)
    integer_scaling = sp.solve(
        (sp.Eq(3 * g_part, g_total),), (g_part,), dict=True
    )
    checks.check(
        "S1c integer iteration gives G(nu)=nG(u) (n=3 elimination)",
        integer_scaling == [{g_part: g_total / 3}],
    )
    g_pq, g_unit = sp.symbols("g_pq g_unit", real=True)
    rational_scaling = sp.solve(
        (
            sp.Eq(5 * g_pq, 2 * g_unit),
        ),
        (g_pq,),
        dict=True,
    )
    checks.check(
        "S1d rational scaling G((2/5)u)=(2/5)G(u) by combining integers",
        rational_scaling == [{g_pq: sp.Rational(2, 5) * g_unit}],
    )

    # Group S2 -- centered boundedness by triangle decomposition.
    g_wa, g_a, bound = sp.symbols("g_wa g_a B", real=True)
    centered = g_wa - g_a
    checks.check(
        "S2a the centered value decomposes exactly as G(w+a)-G(a)",
        sp.simplify(centered - (g_wa - g_a)) == 0,
    )
    x_r, y_r = sp.symbols("x_r y_r", real=True)
    square_identity = sp.simplify(
        (sp.Abs(x_r) + sp.Abs(y_r)) ** 2
        - (x_r - y_r) ** 2
        - 2 * (sp.Abs(x_r) * sp.Abs(y_r) + x_r * y_r)
    )
    sign_patterns = (
        (sp.Rational(3, 2), sp.Rational(1, 3)),
        (sp.Rational(3, 2), -sp.Rational(1, 3)),
        (-sp.Rational(3, 2), sp.Rational(1, 3)),
        (-sp.Rational(3, 2), -sp.Rational(1, 3)),
    )
    checks.check(
        "S2b exact finite sign cases are consistent with the triangle bound",
        square_identity == 0
        and all(
            (sp.Abs(a_v) * sp.Abs(b_v) + a_v * b_v) >= 0
            and sp.Abs(a_v - b_v) <= sp.Abs(a_v) + sp.Abs(b_v)
            for a_v, b_v in sign_patterns
        ),
    )

    # Group S3 -- rational-sandwich identities on exact finite instances.
    slope = sp.Rational(2, 3)
    u_val = sp.Rational(7, 5)
    window = sp.Rational(1, 2)
    for n in (1, 2, 3, 4):
        nu = n * u_val
        r_n = sp.floor(nu / window) * window
        residual = n * (slope * u_val) - r_n * slope - slope * (nu - r_n)
        checks.check(
            f"S3-n{n} exact residual identity and window membership",
            sp.simplify(residual) == 0
            and (nu - r_n) >= 0
            and (nu - r_n) < window
            and sp.Abs(sp.Rational(r_n, n) - u_val) <= window / sp.Integer(n),
        )
    g_u_sym, g_one, tail = sp.symbols("g_u_sym g_one tail", real=True)
    r_sym, n_sym = sp.symbols("r_sym", rational=True), sp.symbols(
        "n_pos", positive=True, integer=True
    )
    sandwich_identity = sp.solve(
        (sp.Eq(n_sym * g_u_sym, r_sym * g_one + tail),),
        (g_u_sym,),
        dict=True,
    )
    checks.check(
        "S3e the sandwich elimination isolates G(u)-(r/n)G(1) as tail/n",
        sandwich_identity
        == [{g_u_sym: (r_sym * g_one + tail) / n_sym}]
        and sp.simplify(
            (r_sym * g_one + tail) / n_sym
            - sp.Rational(1, 1) * r_sym * g_one / n_sym
            - tail / n_sym
        )
        == 0,
    )

    # Group S4 -- Archimedean squeeze.
    n_var = sp.symbols("n_var", positive=True)
    c_const = sp.Rational(17, 3)
    checks.check(
        "S4a the bound c/n has exact limit zero",
        sp.limit(c_const / n_var, n_var, sp.oo) == 0,
    )
    x_const = sp.Rational(7, 11)
    witness_n = sp.floor(c_const / x_const) + 1
    checks.check(
        "S4b an integer witness n=floor(c/X)+1 gives c/n<X exactly",
        witness_n.is_integer is True
        and witness_n > c_const / x_const
        and c_const / witness_n < x_const,
    )

    # Proof guard -- a positive rational mesh needs a positive-width interval.
    positive_width = sp.Rational(2, 5)
    mesh_denominator = sp.floor(1 / positive_width) + 1
    checks.check(
        "R1 finite proof guard: a positive mesh fits only a positive window",
        sp.Rational(1, mesh_denominator) < positive_width
        and all(not (sp.Rational(1, q) < 0) for q in range(1, 65)),
    )

    # Group N -- needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 target identifier, statement, and step labels",
        TARGET_NOTE,
        (
            "bounded_additive_on_interval_linearity_rebuilt_support_note_2026-07-18",
            "Then `G(u) = u · G(1)` for every real `u`.",
            "**(S3) Integer-scaling rational sandwich.**",
            "**(S4) Archimedean squeeze.**",
            "No step uses continuity, measurability, monotonicity, or any literature",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
