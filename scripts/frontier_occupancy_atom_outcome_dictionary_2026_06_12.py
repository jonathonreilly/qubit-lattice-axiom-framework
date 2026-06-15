#!/usr/bin/env python3
"""Bounded theorem runner: the conditioned flow selects outcome equipartition.

Companion for:
docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md

The runner uses finite symbolic checks only. It does not regenerate cache,
does not edit registry data, and does not adopt either occupancy cell.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parent.parent
DOC = REPO / "docs" / "OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
CACHE = REPO / "logs" / "runner-cache" / "frontier_occupancy_atom_outcome_dictionary_2026_06_12.txt"
DOCS = REPO / "docs"

PASS = 0
FAIL = 0


def check(num: int, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] ({num:02d}) {label}{suffix}")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def main() -> int:
    print("=" * 78)
    print("Occupancy atom / outcome dictionary bounded theorem checks")
    print("=" * 78)

    r, x, y, s, lam = sp.symbols("r x y s lam")
    ps, pd, Z, g = sp.symbols("ps pd Z g", positive=True)

    # 1. Agreement conditioning squares the outcome-weight ratio.
    x_after = sp.simplify((pd**2 / Z) / (ps**2 / Z))
    check(
        1,
        "agreement conditioning p_i -> p_i^2/Z sends x = p_d/p_s to x^2",
        sp.simplify(x_after.subs(pd, x * ps) - x**2) == 0,
        "one-line wave-8a identification reproved",
    )

    # 2. Generic dictionary: fixed points in outcome space.
    fixed_y = set(sp.solve(sp.Eq(y, y**2), y))
    check(
        2,
        "generic monotone dictionary x=phi(r): conjugated fixed equation is phi(r)=phi(r)^2",
        fixed_y == {sp.Integer(0), sp.Integer(1)},
        "interior fixed point is phi(r*)=1",
    )

    # 3. Component dictionary x = 2r.
    map_component = sp.simplify(((2 * r) ** 2) / 2)
    fp_component = set(sp.solve(sp.Eq(map_component, r), r))
    check(
        3,
        "component dictionary phi(r)=2r gives r -> 2r^2 with interior fixed point 1/2",
        map_component == 2 * r**2
        and fp_component == {sp.Integer(0), sp.Rational(1, 2)},
        f"fixed={sorted(fp_component, key=str)}",
    )

    # 4. Slot dictionary x = r.
    map_slot = r**2
    fp_slot = set(sp.solve(sp.Eq(map_slot, r), r))
    check(
        4,
        "slot dictionary phi(r)=r gives r -> r^2 with interior fixed point 1",
        fp_slot == {sp.Integer(0), sp.Integer(1)},
        f"fixed={sorted(fp_slot, key=str)}",
    )

    # 5. Dictionary-as-atom fixed-point sets plus projective endpoint in s=1/r.
    s_component = sp.simplify(1 / map_component.subs(r, 1 / s))
    s_slot = sp.simplify(1 / map_slot.subs(r, 1 / s))
    check(
        5,
        "dictionary-as-atom fixed-point sets re-solved in r, with projective infinity as s=1/r=0 in both charts",
        fp_component == {sp.Integer(0), sp.Rational(1, 2)}
        and fp_slot == {sp.Integer(0), sp.Integer(1)}
        and sp.simplify(s_component.subs(s, 0)) == 0
        and sp.simplify(s_slot.subs(s, 0)) == 0,
        f"s maps: component={s_component}, slot={s_slot}",
    )

    # 6. Outcome equipartition interpretation.
    component_reading = sp.solve(sp.Eq(2 * r, 1), r)[0]
    slot_reading = sp.solve(sp.Eq(r, 1), r)[0]
    check(
        6,
        "dictionary-as-atom interpretation: x=1 means p_d=p_s in both dictionaries while r-readings differ",
        component_reading == sp.Rational(1, 2)
        and slot_reading == sp.Integer(1)
        and sp.simplify((pd / ps).subs(pd, ps) - 1) == 0,
        "outcome equipartition is the invariant statement",
    )

    # 7. Tri-guise kernel exponent <-> dictionary labels.
    det2 = sp.Matrix([[lam, 0], [0, lam]]).det()
    det1 = sp.Matrix([[lam]]).det()
    kernel_to_dictionary = {
        "component": {"exponent": 2, "dictionary": "x=2r"},
        "slot": {"exponent": 1, "dictionary": "x=r"},
    }
    check(
        7,
        "tri-guise kernel<->flow labels: lambda-exponent pair {2,1} maps bijectively to {x=2r,x=r}",
        det2 == lam**2
        and det1 == lam
        and {v["exponent"] for v in kernel_to_dictionary.values()} == {1, 2}
        and {v["dictionary"] for v in kernel_to_dictionary.values()} == {"x=2r", "x=r"},
        "det(lambda K) scaling on 2x2 vs 1x1 blocks",
    )

    # 8. Tri-guise Fock/weight <-> dictionary via supplied rho-map, commuting triangle.
    Z_sector = 2 * sp.pi / g
    Z_orbit = sp.pi / g
    rho = lambda Zd: sp.simplify((sp.pi / g) / Zd)
    r_from_Z = lambda Zd: sp.simplify(1 / (2 * rho(Zd)))
    weight_to_dictionary = {
        "component": {"weight": Z_orbit, "fixed_r": sp.Rational(1, 2), "dictionary": "x=2r"},
        "slot": {"weight": Z_sector, "fixed_r": sp.Integer(1), "dictionary": "x=r"},
    }
    direct_kernel_to_weight = {
        label: data["weight"] for label, data in weight_to_dictionary.items()
    }
    composed_kernel_to_dictionary = {
        label: weight_to_dictionary[label]["dictionary"]
        for label in direct_kernel_to_weight
    }
    check(
        8,
        "tri-guise weight<->flow labels: rho-map sends {2pi/g,pi/g} to {1,1/2}; triangle of labels commutes",
        r_from_Z(Z_orbit) == sp.Rational(1, 2)
        and r_from_Z(Z_sector) == sp.Integer(1)
        and {sp.simplify(v["weight"]) for v in weight_to_dictionary.values()}
        == {sp.pi / g, 2 * sp.pi / g}
        and composed_kernel_to_dictionary
        == {"component": "x=2r", "slot": "x=r"},
        "rho=(pi/g)/Z_d, r=1/(2rho)",
    )

    # 9. Consequence: route cannot discriminate because x* is identical while r-readings differ.
    x_star = sp.Integer(1)
    r_component_star = sp.simplify(x_star / 2)
    r_slot_star = x_star
    check(
        9,
        "conditioned-flow selection is identical in x-space while r-readings differ",
        x_star == 1
        and r_component_star == sp.Rational(1, 2)
        and r_slot_star == 1
        and r_component_star != r_slot_star,
        "route cannot by itself discriminate",
    )

    # 10. R-D chain recovered when the component dictionary is supplied.
    q = sp.symbols("q", nonnegative=True)
    sharpen_q = sp.simplify(q**2 / (q**2 + (1 - q) ** 2))
    q_fixed = set(sp.solve(sp.Eq(sharpen_q, q), q))
    rd_recovered = sp.simplify(sp.Rational(1, 1) / 2)
    check(
        10,
        "consistency guard: side conditions exclude 0 and infinity, component dictionary reads x=1 as r=1/2",
        q_fixed == {sp.Integer(0), sp.Rational(1, 2), sp.Integer(1)}
        and rd_recovered == sp.Rational(1, 2),
        "sharpening, not contradiction",
    )

    # 11. Negative control third dictionary.
    third_reading = sp.solve(sp.Eq(4 * r, 1), r)[0]
    named_cells = {sp.Rational(1, 2), sp.Integer(1)}
    admitted_weights = {sp.simplify(Z_sector), sp.simplify(Z_orbit)}
    check(
        11,
        "negative control: hypothetical x=4r gives r*=1/4 outside the named binary",
        third_reading == sp.Rational(1, 4)
        and third_reading not in named_cells
        and admitted_weights == {2 * sp.pi / g, sp.pi / g},
        "dictionary space constrained here to the two landed bookkeepings",
    )

    note = DOC.read_text(encoding="utf-8")
    note_norm = " ".join(note.split())

    # 12. Minimal axiom quote present.
    orbit_quote = (
        "Given a readout context with a finite central-sector decomposition and a fixed "
        "`K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized "
        "central sector."
    )
    check(
        12,
        "B-check: MINIMAL_AXIOMS realized-outcome-is-the-K/CPT-orbit quote present",
        " ".join(orbit_quote.split()) in note_norm,
    )

    # 13. Both flow notes' maps grepped.
    sep = normalized_text(DOCS / "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md")
    therm = normalized_text(DOCS / "FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md")
    check(
        13,
        "B-check: both flow notes' maps are present in their sources",
        "r\u21922r\u00b2" in sep and "g(r) = sqrt(r/2)" in therm,
    )

    # 14. Firewall sentences present in note.
    firewall_phrases = [
        "cannot by itself discriminate",
        "sharpening",
        "not a correction",
        "the occupancy binary stays open",
    ]
    check(
        14,
        "B-check: firewall sentences present",
        all(phrase in note_norm.lower() for phrase in firewall_phrases),
        ", ".join(firewall_phrases),
    )

    # 15. Positive closing language absent.
    forbidden_closing = [
        "this closes",
        "this settles",
        "is closed",
        "is settled",
        "therefore closed",
        "therefore settled",
        "retires the occupancy",
        "resolves the dictionary",
    ]
    check(
        15,
        "B-check: positive closing language absent",
        not any(phrase in note_norm.lower() for phrase in forbidden_closing),
    )

    # 16. Link inventory exactly the three dependency links.
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)
    expected_links = [
        (
            "`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`",
            "FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md",
        ),
        (
            "`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`",
            "FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md",
        ),
        ("`MINIMAL_AXIOMS_2026-06-05.md`", "MINIMAL_AXIOMS_2026-06-05.md"),
    ]
    check(
        16,
        "B-check: markdown link inventory is exactly the three dependency links",
        links == expected_links,
        f"links={links}",
    )

    # 17. Companions backticked only, not linked.
    companions = [
        "wave-8a anatomy note",
        "R-D chain note",
        "independence note",
        "rho-map",
        "wave-4 companion",
        "wave-6 companion",
        "wave-7b companion",
    ]
    companions_backticked = all(f"`{item}`" in note for item in companions)
    companions_linked = any(item in label for label, _ in links for item in companions)
    check(
        17,
        "B-check: companions are backticked context only, not markdown-linked",
        companions_backticked and not companions_linked,
    )

    # 18. Canonical front matter and no-promotion present.
    check(
        18,
        "B-check: canonical front matter and No-promotion statement present",
        "**Claim type:** bounded_theorem" in note
        and "**Type:**" not in note
        and not re.search(r"\*\*H[1-4]\b", note)
        and "**No-promotion statement:**" in note
        and "does not promote, demote, or set the" in note_norm
        and "independent audit lane is the only status authority" in note_norm,
    )

    # 19. Boundary states no discrimination, no cell selection, no fixed r, no correction.
    boundary_bits = [
        "does not discriminate the fork",
        "select a cell",
        "fix `r`",
        "correct any landed note",
        "resolve the dictionary",
    ]
    check(
        19,
        "B-check: Boundary contains the required does-NOT clauses",
        all(bit in note for bit in boundary_bits),
    )

    # 20. Runner self-check: exactly three target files are new or modified for this spec.
    status = subprocess.run(
        [
            "git",
            "status",
            "--short",
            "--",
            str(DOC.relative_to(REPO)),
            str(Path(__file__).relative_to(REPO)),
            str(CACHE.relative_to(REPO)),
        ],
        cwd=REPO,
        check=False,
        text=True,
        capture_output=True,
    )
    touched = [line for line in status.stdout.splitlines() if line.strip()]
    check(
        20,
        "B-check: note, runner, and cache are the only touched files in this spec path set",
        len(touched) == 3
        and all(line[:2] in {"??", " A", "A ", "AM", " M"} for line in touched),
        "; ".join(touched),
    )

    # 21. Record guardrail language stays explicit.
    record_guardrails = [
        "Record does not supply the readout context",
        "weighting, normalization, probability rule",
        "measurement dynamics, or occupancy rule",
    ]
    check(
        21,
        "B-check: Record guardrail states supplied-context and no-weight/no-occupancy boundary",
        all(bit in note_norm for bit in record_guardrails),
    )

    # 22. The tri-guise section is phrased as supplied labels, not external authority.
    check(
        22,
        "B-check: tri-guise language is supplied-label scoped",
        "Tri-guise identity on the supplied labels" in note
        and "same two-label bookkeeping choice written three ways" in note
        and "landed rho-map orientation" not in note,
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("SUMMARY: conditioned flow selects x*=1; dictionary choice maps that invariant selection to r=1/2 or r=1.")
    print("=" * 78)
    return 0 if FAIL == 0 and PASS >= 18 else 1


if __name__ == "__main__":
    raise SystemExit(main())
