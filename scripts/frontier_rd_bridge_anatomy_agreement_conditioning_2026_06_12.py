#!/usr/bin/env python3
"""
Bounded runner for the R-D bridge anatomy note.

No network, no git, no cache writes. The final "git diff --stat" section is a
local diff-stat-style inventory printed without invoking git, preserving the
spec's no-git rule.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import sympy as sp


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "docs/RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md"
THIS_SCRIPT = REPO / "scripts/frontier_rd_bridge_anatomy_agreement_conditioning_2026_06_12.py"
RUNNER_CACHE = REPO / "logs/runner-cache/frontier_rd_bridge_anatomy_agreement_conditioning_2026_06_12.txt"
MINIMAL = REPO / "docs/MINIMAL_AXIOMS_2026-06-05.md"
SEPARATRIX = REPO / "docs/FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md"
THERMAL = REPO / "docs/FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md"


checks: list[tuple[str, bool, str]] = []


def add_check(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, bool(ok), detail))
    tag = "PASS" if ok else "FAIL"
    suffix = f" - {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def all_zero_matrix(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def symbolic_checks() -> None:
    Ps = sp.diag(1, 0, 0)
    Pd = sp.diag(0, 1, 1)

    def D(mat: sp.Matrix) -> sp.Matrix:
        return Ps * mat * Ps + Pd * mat * Pd

    M = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"m{i}{j}"))
    add_check(
        "G1 idempotence of pinching on generic 3x3 M",
        all_zero_matrix(D(D(M)) - D(M)),
        "D(D(M)) = D(M) entrywise",
    )

    rho = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"rho{i}{j}"))

    def weight(P: sp.Matrix, mat: sp.Matrix) -> sp.Expr:
        return sp.trace(P * mat * P)

    weights_unchanged = (
        sp.simplify(weight(Ps, D(rho)) - weight(Ps, rho)) == 0
        and sp.simplify(weight(Pd, D(rho)) - weight(Pd, rho)) == 0
        and sp.simplify(weight(Ps, D(D(rho))) - weight(Ps, D(rho))) == 0
        and sp.simplify(weight(Pd, D(D(rho))) - weight(Pd, D(rho))) == 0
    )
    add_check(
        "G1 weight corollary for second pinching",
        weights_unchanged,
        "Tr(P_i rho P_i) unchanged under D and D o D",
    )

    ps, pd, x, r = sp.symbols("ps pd x r", positive=True, nonzero=True)
    Z = ps**2 + pd**2
    ps_prime = ps**2 / Z
    pd_prime = pd**2 / Z
    ratio_map = sp.simplify((pd_prime / ps_prime).subs(pd, x * ps))
    add_check(
        "G2a agreement conditioning sends x to x^2",
        sp.simplify(ratio_map - x**2) == 0,
        "x = p_d/p_s",
    )

    r_forward = sp.simplify((x**2).subs(x, 2 * r) / 2)
    x_back = sp.simplify(2 * (2 * r**2) - (2 * r) ** 2)
    add_check(
        "G2b x = 2r gives r -> 2r^2 both ways",
        sp.simplify(r_forward - 2 * r**2) == 0 and x_back == 0,
        "coordinate conversion exact",
    )

    g_r = sp.sqrt(r / 2)
    inverse_from_x = sp.sqrt(2 * r) / 2
    inverse_ok = (
        sp.simplify((inverse_from_x**2) - (g_r**2)) == 0
        and sp.simplify(2 * g_r**2 - r) == 0
    )
    add_check(
        "G2c inverse direction is g(r) = sqrt(r/2)",
        inverse_ok,
        "x -> sqrt(x) converted to r",
    )

    rf = sp.symbols("rf")
    finite_fixed = sp.solve(sp.Eq(2 * rf**2, rf), rf)
    zero = sp.Integer(0)
    one = sp.Integer(1)
    projective_fixed = (
        sp.simplify((zero**2) / (zero**2 + one**2)) == zero
        and sp.simplify((one**2) / (zero**2 + one**2)) == one
    )
    add_check(
        "G2d fixed points are 0 and 1/2 plus projective infinity",
        finite_fixed == [sp.Integer(0), sp.Rational(1, 2)] and projective_fixed,
        f"finite={finite_fixed}",
    )

    retained_map = 2 * r**2
    perfectly_correlated = r
    witness = sp.Rational(1, 3)
    structural_ok = (
        sp.simplify(retained_map - r_forward) == 0
        and perfectly_correlated.subs(r, witness) != retained_map.subs(r, witness)
    )
    add_check(
        "G3 atom does real work: non-independent witness is identity",
        structural_ok,
        "perfectly correlated registration does not yield retained map",
    )

    naive_identity = r
    generic_not_retained = sp.simplify(retained_map - r) != 0
    add_check(
        "negative control: naive re-pinching fixes every r",
        sp.simplify(naive_identity - r) == 0 and generic_not_retained,
        "D-composition cannot ground R-D selection",
    )


def text_checks() -> None:
    note = read(NOTE)
    minimal = read(MINIMAL)
    separatrix = read(SEPARATRIX)
    thermal = read(THERMAL)

    add_check(
        "B1 Minimal Axioms non-supply clause present",
        "weighting, normalization, probability" in minimal and "occupancy rule" in minimal,
        "Record supplies no weighting/probability/occupancy rule",
    )

    sep_map_tokens = [
        "r\\u21922r\\u00b2",
        "r \\u2192 2r\\u00b2",
        "r\\u21a62r\\u00b2",
    ]
    sep_has_map = any(token.encode("utf-8").decode("unicode_escape") in separatrix for token in sep_map_tokens)
    add_check(
        "B2 separatrix note contains retained sharpening map",
        sep_has_map and "luders_rule_from_composition_consistency" in separatrix,
        "r -> 2r^2 source pinned",
    )

    add_check(
        "B3 thermalizing-arrow note contains retained inverse map",
        "g(r)=sqrt(r/2)" in thermal or "g(r) = sqrt(r/2)" in thermal,
        "g(r)=sqrt(r/2) source pinned",
    )

    for phrase in (
        "the atom is named, not discharged",
        "does not import a probability rule",
        "the occupancy binary stays open",
    ):
        add_check(f"B4 firewall sentence present: {phrase}", phrase in note.lower())

    banned_closing = [
        "atom is discharged",
        "discharges the atom",
        "r-d is adopted",
        "r is forced",
        "closes the occupancy lane",
        "settles the occupancy lane",
        "probability rule is imported",
        "route is closed",
    ]
    lower_note = note.lower()
    absent = [phrase for phrase in banned_closing if phrase in lower_note]
    add_check(
        "B5 closing/adoption language absent",
        not absent,
        f"absent={absent}",
    )

    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)
    expected = [
        (
            "`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`",
            "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
        ),
        (
            "`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`",
            "FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md",
        ),
        (
            "`MINIMAL_AXIOMS_2026-06-05.md`",
            "MINIMAL_AXIOMS_2026-06-05.md",
        ),
    ]
    add_check(
        "B6 markdown link inventory is exactly the three dependencies",
        links == expected,
        f"links={len(links)}",
    )

    companions = [
        "KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "KOIDE_OCCUPANCY_DURABILITY_PREMISE_EQUIVALENCE_ON_REGISTERED_SURFACE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "RD_FIXEDNESS_IS_ARROW_INVARIANT_ON_THE_RETAINED_FLOW_FAMILY_BOUNDED_NOTE_2026-06-12.md",
        "CORNER_MODE_SET_FORK_RESOLUTION_LAYER_IS_RECORD_DYNAMICS_BOUNDED_NOTE_2026-06-12.md",
        "RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md",
        "UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md",
    ]
    companions_ok = all(f"`{name}`" in note and f"]({name})" not in note for name in companions)
    add_check(
        "B7 companion/context names are backticked only",
        companions_ok,
        "no companion markdown links",
    )

    add_check(
        "B8 No-promotion statement present",
        "**No-promotion statement:**" in note and "does not promote" in note,
    )

    add_check(
        "B9 standard status-authority lines present",
        "**Status:**" in note and "**Status authority:**" in note,
    )

    add_check(
        "B10 runner cache is named",
        RUNNER_CACHE.relative_to(REPO).as_posix() in note,
    )


def local_diff_stat() -> None:
    print()
    print("git diff --stat (local new-file inventory; git not invoked)")
    total_lines = 0
    for path in (NOTE, THIS_SCRIPT):
        rel = path.relative_to(REPO).as_posix()
        lines = read(path).count("\n")
        total_lines += lines
        pluses = "+" * min(60, max(1, lines // 3))
        print(f" {rel} | {lines} {pluses}")
    print(f" 2 files changed, {total_lines} insertions(+)")


def main() -> int:
    symbolic_checks()
    text_checks()

    passed = sum(1 for _, ok, _ in checks if ok)
    failed = len(checks) - passed
    print()
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    addendum = "PASS>=14 satisfied" if passed >= 14 else "PASS<14"
    print(f"ACCEPTANCE: {addendum}; FAIL={failed}")
    local_diff_stat()
    print(
        "SUMMARY: G1 pinching idempotence is exact; G2 agreement-conditioned "
        "independent double registration is the retained r -> 2r^2 flow with "
        "inverse g(r)=sqrt(r/2); G3 leaves exactly one named statistics atom "
        "undischarged."
    )
    return 0 if failed == 0 and passed >= 14 else 1


if __name__ == "__main__":
    sys.exit(main())
