#!/usr/bin/env python3
"""Literature-conditioned SM relativistic-DOF inventory arithmetic.

The runner checks three distinct layers without conflating them:

* citation hygiene: the source note names exact Husdal and Giovannini items
  and states the conditional thermal scope and import boundary;
* finite arithmetic: inventory factors parsed from the note give 28 bosonic
  and 90 fermionic states and hence 427/4 exactly; and
* dependency hygiene: the cited 7/8 authority is retained-grade.

The runner does not fetch, validate, or re-prove the external references.
Their truth and applicability remain literature inputs for independent review.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from math import prod
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"
WEIGHT_LEDGER = REPO_ROOT / (
    "docs/audit/data/ledger/hi/"
    "hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_"
    "narrow_theorem_note_2026-05-10.json"
)

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}
EXPECTED_BOSONS = {
    "gluons": ((8, 2), 16),
    "SU(2)_L gauge bosons": ((3, 2), 6),
    "U(1)_Y gauge boson": ((1, 2), 2),
    "complex Higgs doublet": ((4,), 4),
}
EXPECTED_FERMIONS = {
    "quarks": ((6, 3, 2, 2), 72),
    "charged leptons": ((3, 2, 2), 12),
    "active neutrinos": ((3, 2), 6),
}

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class InventoryEntry:
    name: str
    factors: tuple[int, ...]
    expected: int

    @property
    def count(self) -> int:
        return prod(self.factors)


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


BROKEN_BOSONS = [
    InventoryEntry("gluons_broken_bookkeeping", (8, 2), 16),
    InventoryEntry("photon", (1, 2), 2),
    InventoryEntry("massive_w_w_z", (3, 3), 9),
    InventoryEntry("higgs_scalar", (1,), 1),
]


def parse_inventory_table(text: str, heading: str) -> dict[str, InventoryEntry]:
    """Parse the factors and displayed counts from one Markdown table."""
    start = text.index(heading)
    end = text.index("\n\nTherefore", start)
    table_text = text[start:end]
    entries: dict[str, InventoryEntry] = {}
    pattern = re.compile(
        r"^\|\s*(?P<name>.*?)\s*\|.*?\|\s*`(?P<factors>[0-9 *]+)`\s*"
        r"\|\s*`(?P<count>[0-9]+)`\s*\|$"
    )
    for line in table_text.splitlines():
        match = pattern.fullmatch(line)
        if not match:
            continue
        name = match.group("name").replace("`", "")
        factors = tuple(int(piece.strip()) for piece in match.group("factors").split("*"))
        entries[name] = InventoryEntry(name, factors, int(match.group("count")))
    return entries


def literature_and_boundary_checks(text: str) -> None:
    flat = " ".join(text.split())
    weight_row = json.loads(WEIGHT_LEDGER.read_text(encoding="utf-8"))

    source_locators = [
        "[doi:10.3390/galaxies4040078](https://doi.org/10.3390/galaxies4040078)",
        "[arXiv:1609.04979](https://arxiv.org/abs/1609.04979)",
        "Section 3 and Table 1; Sections 4.3–4.5",
        "[arXiv:astro-ph/0703730](https://arxiv.org/abs/astro-ph/0703730)",
        "Appendix B.4, pp. 159–160, Eqs. (B.40)–(B.43)",
    ]
    for locator in source_locators:
        check(f"literature locator present: {locator}", locator in flat, kind="B")

    source_statements = [
        "totals them as `28` bosonic and `90` fermionic degrees of freedom",
        "approximation that chemical potentials are set to zero",
        "expands the quark count as `6*2*2*3=72`",
        "gives `18` leptonic states",
        "expands the bosonic count as `16+8+4=28`",
        "obtains `g_rho=g_s=106.75`",
    ]
    for statement in source_statements:
        check(f"source-to-claim mapping present: {statement}", statement in flat, kind="B")

    thermal_scope = [
        "minimal Standard Model particle content with three generations and one",
        "no thermally populated sterile/right-handed-neutrino states",
        "thermodynamic-equilibrium ideal plasma with chemical potentials neglected",
        "electroweak symmetry is restored",
        "interaction, finite-mass, threshold, decoupling",
        "beyond-Standard-Model corrections",
    ]
    for phrase in thermal_scope:
        check(f"conditional thermal scope contains: {phrase}", phrase in flat, kind="B")

    boundary_required = [
        "remain load-bearing literature inputs",
        "does not claim retained closure",
        "not framework derivations",
        "not chain-satisfying premises merely because they are cited",
        "does not fetch, reproduce, or independently prove the cited physics",
        "citations remove anonymous attribution; they do not close",
        "inventory remains a non-satisfying condition",
        "a new axiom, approved primitive, document-authority role, or audit verdict",
    ]
    for phrase in boundary_required:
        check(f"import boundary contains: {phrase}", phrase in flat, kind="B")

    exact_claim_bindings = [
        "Therefore `g_bosonic = 16 + 6 + 2 + 4 = 28`.",
        "Therefore `g_fermionic = 72 + 12 + 6 = 90`.",
        "= 28 + (7/8) * 90",
        "= 427/4",
        "= 106.75.",
    ]
    for binding in exact_claim_bindings:
        check(f"displayed arithmetic binding is exact: {binding}", binding in text)

    check(
        "7/8 dependency ledger claim id matches",
        weight_row.get("claim_id")
        == "hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10",
    )
    check(
        "7/8 dependency is retained-grade",
        weight_row.get("effective_status") in RETAINED_GRADE,
        str(weight_row.get("effective_status")),
    )
    check("7/8 dependency scope contains exact ratio", "7/8" in weight_row.get("claim_scope", ""))


def inventory_checks(text: str) -> None:
    print("\n=== finite inventory arithmetic ===")
    bosons = parse_inventory_table(text, "Unbroken electroweak bookkeeping.")
    fermions = parse_inventory_table(text, "Fermionic bookkeeping:")
    check("note has the exact expected bosonic sectors", set(bosons) == set(EXPECTED_BOSONS), str(sorted(bosons)))
    check("note has the exact expected fermionic sectors", set(fermions) == set(EXPECTED_FERMIONS), str(sorted(fermions)))

    for name, (factors, displayed) in [*EXPECTED_BOSONS.items(), *EXPECTED_FERMIONS.items()]:
        entry = bosons.get(name) or fermions.get(name)
        check(f"{name} row is present", entry is not None)
        if entry is None:
            continue
        check(f"{name} factors match the attributed inventory", entry.factors == factors, str(entry.factors))
        check(f"{name} displayed count matches the attributed inventory", entry.expected == displayed, str(entry.expected))
        check(f"{entry.name} multiplication", entry.count == entry.expected, f"{entry.factors} -> {entry.count}")

    for entry in BROKEN_BOSONS:
        check(f"{entry.name} multiplication", entry.count == entry.expected, f"{entry.factors} -> {entry.count}")

    g_bosonic = sum(entry.count for entry in bosons.values())
    g_fermionic = sum(entry.count for entry in fermions.values())
    broken_bosonic = sum(entry.count for entry in BROKEN_BOSONS)
    source_bosonic_breakdown = (16, 8, 4)
    source_leptonic_total = (
        fermions.get("charged leptons", InventoryEntry("missing", (), 0)).count
        + fermions.get("active neutrinos", InventoryEntry("missing", (), 0)).count
    )
    fermion_weight = Fraction(7, 8)
    g_star = Fraction(g_bosonic, 1) + fermion_weight * g_fermionic

    check("source bosonic grouping is 16+8+4", sum(source_bosonic_breakdown) == 28, str(source_bosonic_breakdown))
    electroweak_vector_total = (
        bosons.get("SU(2)_L gauge bosons", InventoryEntry("missing", (), 0)).count
        + bosons.get("U(1)_Y gauge boson", InventoryEntry("missing", (), 0)).count
    )
    check("local electroweak-vector rows refine source subtotal 8", electroweak_vector_total == 8, str(electroweak_vector_total))
    check("source leptonic total is charged 12 plus active-neutrino 6", source_leptonic_total == 18, str(source_leptonic_total))
    check("bosonic total is 28", g_bosonic == 28, str(g_bosonic))
    check("fermionic total is 90", g_fermionic == 90, str(g_fermionic))
    check("broken-phase bosonic total matches unbroken total", broken_bosonic == g_bosonic, str(broken_bosonic))
    check("fermion weight is 7/8", fermion_weight == Fraction(7, 8), str(fermion_weight))
    check("g_star exact fraction is 427/4", g_star == Fraction(427, 4), str(g_star))
    check("g_star decimal is 106.75", float(g_star) == 106.75, str(float(g_star)))
    active_neutrinos = fermions.get("active neutrinos", InventoryEntry("missing", (), 0)).count
    check("no right-handed-neutrino states are counted", active_neutrinos == 6, str(active_neutrinos))
    check(
        "broken-phase displayed bookkeeping is bound",
        "`16` gluon states + `2` photon states + `9` massive `W+, W-, Z` vector\n"
        "states + `1` Higgs scalar state = `28`" in text,
    )


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")
    print("=== literature attribution and dependency classification ===")
    literature_and_boundary_checks(text)
    inventory_checks(text)
    print("\nSM relativistic DOF finite inventory certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
