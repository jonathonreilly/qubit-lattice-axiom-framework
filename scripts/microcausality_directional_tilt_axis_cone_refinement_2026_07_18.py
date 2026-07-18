#!/usr/bin/env python3
"""Exact checks for the directional-tilt axis-cone refinement note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_DIRECTIONAL_TILT_AXIS_CONE_REFINEMENT_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK03_NOTE = ROOT / (
    "docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "D1", "D2", "D3", "D4", "D5",
    "I1", "O1", "A1", "A2", "A3",
    "V1", "V2", "V3",
    "N1", "N2", "N3", "N4",
]


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition):
        ok = bool(condition)
        self.labels.append(label.split()[0])
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
        if self.labels != EXPECTED_LABELS:
            print(
                "FAIL: gate-manifest drift: labels "
                f"{self.labels} != expected {EXPECTED_LABELS}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def add(p, q):
    return tuple(a + b for a, b in zip(p, q))


def bond_key(p, q):
    return frozenset((p, q))


def incident_bonds(site, radius):
    out = set()
    for d in AXES:
        for sg in (1, -1):
            other = add(site, tuple(sg * c for c in d))
            if all(-radius <= c <= radius for c in other):
                out.add(bond_key(site, other))
    return out


def adjacent_bonds(bond, radius):
    out = set()
    for s in bond:
        out |= incident_bonds(s, radius)
    out.discard(bond)
    return out


def phi(bond):
    return sum(p[0] for p in bond)


def delta_table(start_bond, radius):
    table = {}
    for nb in adjacent_bonds(start_bond, radius):
        d = phi(nb) - phi(start_bond)
        table[d] = table.get(d, 0) + 1
    return table


def main():
    checks = CheckRunner()
    origin = (0, 0, 0)

    par = bond_key(origin, (1, 0, 0))
    tab_par_4 = delta_table(par, 4)
    tab_par_6 = delta_table(par, 6)
    checks.check(
        "D1 parallel-start height-change table {-2:1,-1:4,+1:4,+2:1}, "
        "box-stable (radii 4 and 6)",
        tab_par_4 == {-2: 1, -1: 4, 1: 4, 2: 1}
        and tab_par_6 == {-2: 1, -1: 4, 1: 4, 2: 1},
    )
    tr2 = bond_key(origin, (0, 1, 0))
    tr3 = bond_key(origin, (0, 0, 1))
    expect_tr = {-1: 2, 0: 6, 1: 2}
    checks.check(
        "D2 transverse-start table {-1:2,0:6,+1:2} for BOTH transverse "
        "orientations, box-stable",
        delta_table(tr2, 4) == expect_tr
        and delta_table(tr3, 4) == expect_tr
        and delta_table(tr2, 6) == expect_tr
        and delta_table(tr3, 6) == expect_tr,
    )

    y = sp.Symbol("y", positive=True)
    s_par_from_table = sum(
        cnt * y**d for d, cnt in tab_par_4.items()
    )
    s_perp_from_table = sum(
        cnt * y**d for d, cnt in delta_table(tr2, 4).items()
    )
    s_par = y**2 + 4 * y + 4 / y + y**-2
    s_perp = 2 * y + 6 + 2 / y
    checks.check(
        "D3 tilt polynomials match the enumerated tables term-by-term, "
        "and S_par(1) = S_perp(1) = 10",
        sp.simplify(s_par_from_table - s_par) == 0
        and sp.simplify(s_perp_from_table - s_perp) == 0
        and s_par.subs(y, 1) == 10
        and s_perp.subs(y, 1) == 10,
    )
    diff_factored = (y - 1) ** 2 * (y**2 + 4 * y + 1) / y**2
    checks.check(
        "D4 domination factorization S_par - S_perp = "
        "(y-1)^2 (y^2+4y+1)/y^2 with every factor nonnegative for y > 0",
        sp.simplify(s_par - s_perp - diff_factored) == 0
        and ((y - 1) ** 2).is_nonnegative
        and (y**2 + 4 * y + 1).is_positive
        and (y**2).is_positive,
    )
    checks.check(
        "D5 row bound: both step types tilt-sum below S_par for y >= 1 "
        "(domination is exact; equality only at y = 1)",
        sp.simplify((s_par - s_perp).subs(y, 1)) == 0
        and sp.simplify((s_par - s_perp).subs(y, sp.Rational(5, 2)))
        == sp.Rational(9, 4) * sp.Rational(69, 4) / sp.Rational(25, 4)
        and sp.simplify(
            (s_par - s_perp).subs(y, sp.Rational(5, 2))
        ).is_positive
        is True,
    )

    y52 = sp.Rational(5, 2)
    ind_ok = (
        y52 ** (0) == 1
        and y52 ** (1) >= 1
        and y52 ** (-1) < 1
        and y52 ** (-1) > 0
    )
    checks.check(
        "I1 indicator bound instances: y^(gain-m) >= 1 at gain = m, m+1 "
        "and positive below (y = 5/2)",
        ind_ok,
    )

    def phi_range_at(r, radius):
        vals = set()
        rng = range(-radius, radius + 1)
        for b in range(-radius, radius + 1):
            for c in rng:
                site = (r, b, c)
                for bond in incident_bonds(site, radius):
                    vals.add(phi(bond))
        return vals

    range0 = phi_range_at(0, 3)
    range3 = phi_range_at(3, 4)
    checks.check(
        "O1 hyperplane phi-ranges {2r-1, 2r, 2r+1} at r = 0 and r = 3, "
        "and the offset arithmetic (2(a+m)-1) - (2a+1) = 2m - 2",
        range0 == {-1, 0, 1}
        and range3 == {5, 6, 7}
        and sp.simplify(
            (2 * (sp.Symbol("a") + sp.Symbol("m")) - 1)
            - (2 * sp.Symbol("a") + 1)
            - (2 * sp.Symbol("m") - 2)
        )
        == 0,
    )

    j_s, t_s, s_s, a_n, b_n, n_s, m_s = sp.symbols(
        "j_s t_s s_s a_n b_n n_s m_s", positive=True
    )
    k = sp.Symbol("k", integer=True, positive=True)
    series = sp.Sum(
        (2 * j_s * s_s * t_s) ** k / sp.factorial(k), (k, 1, sp.oo)
    ).doit()
    display_lhs = (
        2 * a_n * (2 * j_s * b_n) * n_s
        * y ** (-(2 * m_s - 2))
        * (1 / (2 * j_s * s_s))
        * (sp.exp(2 * j_s * s_s * t_s) - 1)
    )
    display_rhs = (
        2 * a_n * b_n * n_s * (y**2 / s_s)
        * y ** (-2 * m_s)
        * (sp.exp(2 * j_s * s_s * t_s) - 1)
    )
    checks.check(
        "A1 assembly: sum_{k>=1} (2JSt)^k/k! = e^{2JSt} - 1 and the "
        "display bookkeeping identity",
        sp.simplify(series - (sp.exp(2 * j_s * s_s * t_s) - 1)) == 0
        and sp.simplify(display_lhs - display_rhs) == 0,
    )
    m_int = sp.Symbol("m_int", integer=True, positive=True)
    checks.check(
        "A2 logarithm-free display at y = 5/2: y^(-2m) = (4/25)^m and "
        "4/25 < 1",
        sp.simplify(y52 ** (-2 * m_int) - sp.Rational(4, 25) ** m_int) == 0
        and sp.Rational(4, 25) < 1,
    )
    k_term = (
        2 * a_n * (2 * j_s) ** (k - 1) * (2 * j_s * b_n)
        * (n_s * s_s ** (k - 1) * y ** (-(2 * m_s - 2)))
        * t_s**k / sp.factorial(k)
    )
    summed = sp.Sum(k_term, (k, 1, sp.oo)).doit()
    checks.check(
        "A3 sibling k-term reconstructed (prefactor 2||A||(2J)^(k-1), "
        "base 2J||B||, tilted count, t^k/k!) and summed to the display",
        sp.simplify(summed - display_rhs) == 0,
    )

    checks.check(
        "V1 S_par(5/2) = 1801/100 exactly",
        sp.simplify(s_par.subs(y, y52) - sp.Rational(1801, 100)) == 0,
    )
    e_low = sp.Rational(1957, 720)
    ln_low = sp.Rational(312, 343)
    atanh_pt = (1 + sp.Rational(3, 7)) / (1 - sp.Rational(3, 7))
    e_partial = sum(sp.Rational(1, sp.factorial(n)) for n in range(7))
    margin = 20 * e_low * ln_low - sp.Rational(1801, 100)
    bracket_chain = (
        e_partial == e_low
        and sp.simplify(sp.E - e_low).is_positive is True
        and sp.simplify(sp.log(y52) - ln_low).is_positive is True
        and atanh_pt == y52
        and 2 * (sp.Rational(3, 7) + sp.Rational(3, 7) ** 3 / 3) == ln_low
        and margin == sp.Rational(3234971, 102900)
        and margin > 0
    )
    direct = (
        sp.simplify(
            20 * sp.E * sp.log(y52) - sp.Rational(1801, 100)
        ).is_positive
        is True
    )
    checks.check(
        "V2 certified parent comparison: exact finite sums "
        "(sum 1/n! = 1957/720; two-term atanh = 312/343), sign brackets, "
        "and the exact rational margin 3234971/102900 > 0",
        bracket_chain and direct,
    )
    scan = {
        sp.Rational(5, 4): sp.Rational(4161, 400),
        sp.Rational(3, 2): sp.Rational(409, 36),
        sp.Integer(2): sp.Rational(57, 4),
        sp.Integer(3): sp.Rational(202, 9),
        sp.Integer(4): sp.Rational(529, 16),
    }
    scan_values_ok = all(
        sp.simplify(s_par.subs(y, yv) - sv) == 0 for yv, sv in scan.items()
    )
    scan_best = all(
        sp.simplify(
            sv * sp.log(y52) - sp.Rational(1801, 100) * sp.log(yv)
        ).is_positive
        is True
        for yv, sv in scan.items()
    )
    checks.check(
        "V3 scan-best against ALL FIVE other scan points (S_par values "
        "gated, exact comparisons; scan-best only, no global optimality)",
        scan_values_ok and scan_best,
    )

    # Group N -- presence needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 sibling authorities: chain identifier and non-sharpness "
        "sentence taken as this note's target",
        BLOCK03_NOTE,
        (
            "microcausality_all_time_volume_uniform_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "Neither `20J` nor `20eJ` is claimed sharp.",
        ),
    )
    checks.needle(
        "N2 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    checks.needle(
        "N3 target identifiers, theorem, honest boundaries",
        TARGET_NOTE,
        (
            "microcausality_directional_tilt_axis_cone_refinement_"
            "bounded_theorem_note_2026-07-18",
            "**Theorem (axis-cone refinement).**",
            "optimality over all real `y > 1` is open",
            "for diagonal separations `m ≪ d` the sibling's can be "
            "stronger — stated, not hidden",
            "the decay factor is exactly `(4/25)^m` per axis-site",
        ),
    )
    checks.needle(
        "N4 No-Go section structure: all eight items and the Status line",
        TARGET_NOTE,
        (
            "**N1 route inventory (residuals first).**",
            "**N2 hypothesis independence (pairwise) — ATTEMPTED.**",
            "**N3 hidden-wall scan — ATTEMPTED.**",
            "**N4 dependency roles, per citation — ATTEMPTED.**",
            "**N5 rhetoric audit — ATTEMPTED.**",
            "**N6 partial-closure scan — ATTEMPTED.**",
            "**N7 steelman (strongest counterarguments, answered) — "
            "ATTEMPTED.**",
            "**N8 prior-wall echo — ATTEMPTED.**",
            "**Status: PASS**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
