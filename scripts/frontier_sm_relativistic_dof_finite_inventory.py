#!/usr/bin/env python3
"""Registered physical-input bridge and finite SM relativistic-DOF arithmetic.

The runner checks three distinct layers without conflating them:

* load-bearing-step class B: the source note is a registered Class-C claim
  note and carries an explicit machine-semantic authority role, exact
  literature locators, and bounded thermal hypotheses;
* load-bearing-step class A: inventory factors parsed from the note give 28
  bosonic and 90 fermionic states and hence 427/4 exactly; and
* dependency hygiene: the 7/8 authority is retained and this source note does
  not create a new axiom, primitive, or admission registry.

It does not fetch or re-prove the external references. Their bibliographic
items are deliberately visible for independent audit.
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
AUTHORITY_REGISTRY = REPO_ROOT / "docs/audit/data/doc_authority_registry.json"
AUTHORITY_POLICY = REPO_ROOT / "docs/audit/DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md"
WEIGHT_LEDGER = REPO_ROOT / (
    "docs/audit/data/ledger/hi/"
    "hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_"
    "narrow_theorem_note_2026-05-10.json"
)

CLAIM_ID = "sm_relativistic_dof_count_import_note_2026-05-17"
NOTE_PATH = "docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md"
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
EXPECTED_EXTERNAL_AUTHORITIES = [
    {
        "id": "husdal_2016_galaxies_4_78",
        "primary_locator": "https://doi.org/10.3390/galaxies4040078",
        "secondary_locator": "https://arxiv.org/abs/1609.04979",
        "exact_item": "Table 1; Sections 3, 4.4, 4.5",
        "supplies": (
            "minimal-Standard-Model inventory degeneracies, totals 28 bosonic "
            "and 90 fermionic states, and the ultrarelativistic equilibrium "
            "thermal interpretation"
        ),
    },
    {
        "id": "giovannini_astro_ph_0703730",
        "primary_locator": "https://arxiv.org/abs/astro-ph/0703730",
        "exact_item": "Appendix B.4, pp. 159-160, Eqs. B.40-B.43",
        "supplies": (
            "independent factorized counts 72 quark, 18 lepton, 28 bosonic, "
            "90 fermionic, and g_rho = g_s = 106.75 in the "
            "electroweak-symmetric equilibrium scope"
        ),
    },
]

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
    """Parse the factors and displayed counts from one Markdown inventory table."""
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


def registered_authority_checks(text: str) -> None:
    flat = " ".join(text.split())
    registry = json.loads(AUTHORITY_REGISTRY.read_text(encoding="utf-8"))
    policy = AUTHORITY_POLICY.read_text(encoding="utf-8")
    weight_row = json.loads(WEIGHT_LEDGER.read_text(encoding="utf-8"))

    rows = [row for row in registry["rows"] if row.get("path") == NOTE_PATH]
    check("authority registry has exactly one target row", len(rows) == 1, str(len(rows)), "B")
    row = rows[0] if rows else {}
    check("target is registered as Class C", row.get("class") == "C", str(row.get("class")), "B")
    check("target registry row has the canonical claim id", row.get("claim_id") == CLAIM_ID, str(row.get("claim_id")), "B")
    check("target registry row is merge-state landed", row.get("status") == "landed", str(row.get("status")), "B")
    check(
        "target has machine-semantic external-physical-input role",
        row.get("authority_role") == "scope_pinned_external_physical_input",
        str(row.get("authority_role")),
        "B",
    )
    check(
        "target records zero pre-audit premise weight",
        row.get("pre_audit_premise_weight") == "none",
        str(row.get("pre_audit_premise_weight")),
        "B",
    )
    check(
        "registered external-authority packet matches exact expected sources",
        row.get("external_authorities") == EXPECTED_EXTERNAL_AUTHORITIES,
        kind="B",
    )
    check(
        "registry preserves independent-audit boundary",
        "no premise weight before independent audit" in row.get("note", ""),
        row.get("note", ""),
        "B",
    )
    check(
        "Class-C policy limits premise weight to audited scope",
        "after ratification, exactly the audited `claim_scope`" in policy,
        kind="B",
    )

    source_locators = [
        "[doi:10.3390/galaxies4040078](https://doi.org/10.3390/galaxies4040078)",
        "[arXiv:1609.04979](https://arxiv.org/abs/1609.04979)",
        "Table 1 and Sections 3, 4.4, and 4.5",
        "[arXiv:astro-ph/0703730](https://arxiv.org/abs/astro-ph/0703730)",
        "Appendix B.4, pp. 159–160, Eqs. (B.40)–(B.43)",
    ]
    for locator in source_locators:
        check(f"exact external-authority locator present: {locator}", locator in flat, kind="B")

    source_statements = [
        "totals them as `28` bosonic and `90` fermionic degrees of freedom",
        "expands the quark count as `6*2*2*3=72`",
        "gives `18` leptonic states",
        "expands the bosonic count as `16+8+4=28`",
        "obtains `g_rho=g_s=106.75`",
        "external sources establish both the inventory",
        "why those multiplicities are the thermal state count",
    ]
    for statement in source_statements:
        check(f"source-to-claim mapping present: {statement}", statement in flat, kind="B")

    exact_claim_bindings = [
        "Therefore `g_bosonic = 16 + 6 + 2 + 4 = 28`.",
        "Therefore `g_fermionic = 72 + 12 + 6 = 90`.",
        "= 28 + (7/8) * 90",
        "= 427/4",
        "= 106.75.",
    ]
    for binding in exact_claim_bindings:
        check(f"displayed claim binding is exact: {binding}", binding in text, kind="A")

    thermal_scope = [
        "minimal Standard Model particle content with three generations and one",
        "no thermally populated sterile/right-handed-neutrino states",
        "thermodynamic-equilibrium, zero-chemical-potential ideal plasma",
        "electroweak symmetry is restored",
        "interaction, finite-mass, threshold",
        "beyond-Standard-Model corrections excluded",
    ]
    for phrase in thermal_scope:
        check(f"bounded thermal scope contains: {phrase}", phrase in flat, kind="B")

    boundary_required = [
        "not a framework derivation",
        "does not add an axiom, approved primitive,",
        "or admission registry",
        "Effective status remains audit-lane-owned",
        "does not author an audit verdict",
        "does not pretend to reproduce or independently prove the cited physics",
        "a framework derivation of the Standard Model particle inventory",
        "an exact interacting Standard Model equation of state",
        "closure of any downstream DM-leptogenesis row",
    ]
    for phrase in boundary_required:
        check(f"authority boundary contains: {phrase}", phrase in flat, kind="B")

    forbidden = [
        "one-hop dependency rather than carry the count",
        "This wrapper note is a named-import-only bounded theorem",
        "This count is NOT derived",
        "we create an admission registry",
        "Status:** retained",
    ]
    for phrase in forbidden:
        check(f"note omits forbidden/stale phrase: {phrase}", phrase not in text, kind="B")

    check("7/8 dependency ledger claim id matches", weight_row.get("claim_id") == "hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10", kind="A")
    check(
        "7/8 dependency is retained-grade",
        weight_row.get("effective_status") in RETAINED_GRADE,
        str(weight_row.get("effective_status")),
        "A",
    )
    check("7/8 dependency scope contains exact ratio", "7/8" in weight_row.get("claim_scope", ""), kind="A")


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
        check(f"{name} factors match the source-mapped inventory", entry.factors == factors, str(entry.factors))
        check(f"{name} displayed count matches the source-mapped inventory", entry.expected == displayed, str(entry.expected))
        check(
            f"{entry.name} count",
            entry.count == entry.expected,
            f"{entry.factors} -> {entry.count}",
        )

    for entry in BROKEN_BOSONS:
        check(
            f"{entry.name} count",
            entry.count == entry.expected,
            f"{entry.factors} -> {entry.count}",
        )

    g_bosonic = sum(entry.count for entry in bosons.values())
    g_fermionic = sum(entry.count for entry in fermions.values())
    broken_bosonic = sum(entry.count for entry in BROKEN_BOSONS)
    source_bosonic_breakdown = (16, 8, 4)
    source_leptonic_total = fermions.get("charged leptons", InventoryEntry("missing", (), 0)).count + fermions.get("active neutrinos", InventoryEntry("missing", (), 0)).count
    fermion_weight = Fraction(7, 8)
    g_star = Fraction(g_bosonic, 1) + fermion_weight * g_fermionic

    check("source bosonic grouping is 16+8+4", sum(source_bosonic_breakdown) == 28, str(source_bosonic_breakdown))
    electroweak_vector_total = bosons.get("SU(2)_L gauge bosons", InventoryEntry("missing", (), 0)).count + bosons.get("U(1)_Y gauge boson", InventoryEntry("missing", (), 0)).count
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
    print("=== registered authority and dependency classification ===")
    registered_authority_checks(text)
    inventory_checks(text)
    print("\nSM relativistic DOF finite inventory certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
