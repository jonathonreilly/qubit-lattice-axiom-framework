#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_MASS_DETERMINANT_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
THETA_PARENT = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ledger_row_by_path(path: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def main() -> int:
    print("theta mass determinant axiom-update no-go verifier")

    note = read(NOTE)
    minimal = read(MINIMAL)
    premises = json.loads(read(AXIOM_PREMISES))
    tier = json.loads(read(DECISION_HISTORY))
    registry = read(REGISTRY)
    theta_parent = read(THETA_PARENT)
    realized = read(REALIZED)
    kinetic = read(KINETIC)

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    registry_flat = flat(registry)
    theta_flat = flat(theta_parent)

    section("A. source presence and retained target")
    for path in [NOTE, MINIMAL, AXIOM_PREMISES, DECISION_HISTORY, LEDGER, REGISTRY, THETA_PARENT, REALIZED, KINETIC]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    row = ledger_row_by_path("docs/STRONG_CP_THETA_ZERO_NOTE.md")
    check("theta parent row is retained-grade", row.get("effective_status") in {"retained", "retained_bounded", "retained_no_go"}, row.get("effective_status"))
    check("theta parent row is audited_clean", row.get("audit_status") == "audited_clean", row.get("audit_status"))

    section("B. admission-era decision history boundary")
    theta = tier["retired_derivation_targets"]["strong_cp_theta_zero_note"]
    check("decision history preserves zero final admission count", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("theta entry is retired, not live", "strong_cp_theta_zero_note" not in tier.get("derivation_targets", {}))
    check("theta retired-target record is preserved", bool(theta))
    retirement = theta.get("retirement", {})
    check("theta disposition correction date is recorded", retirement.get("date") == "2026-07-11", retirement)
    check("theta retirement mechanism is retained derivation", "retained" in retirement.get("mechanism", ""))
    check(
        "historical theta minimum decomposition preserves two residual atoms",
        theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "gauge side",
        "mass side",
        "arg det M",
        "determinant-readout bridge",
        "K-real",
    ]:
        check(f"machine registry theta statement includes {phrase}", phrase in theta["statement"])
    check("decision history names theta mass side", "determinant-readout bridge" in flat(json.dumps(theta)))
    check("note has current-main posture line", "Current-main posture (2026-07-11)" in note)
    check("note records absence of an admission registry", "No admission registry is created." in note)
    check("note does not create an admission registry", "does not create any admission registry" in note)
    check("note says theta is not retired", "Theta is not retired." in note)
    check("note says no admission registry is created", "No admission registry is created." in note)

    section("C. approved premise-node and axiom non-supply")
    check(
        "premise registry canonical ids are the approved four",
        premises["canonical_ids"] == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
        premises["canonical_ids"],
    )
    minimal_note = premises["nodes"]["minimal_axioms"]["note"]
    for phrase in [
        "K/CPT structure",
        "central-sector decomposition",
        "source/action bridge",
        "physical observable bridge",
        "context-selection rule",
        "formation rule",
        "weighting",
        "probability",
    ]:
        check(f"premise registry withholds {phrase}", phrase in minimal_note)
    for phrase in [
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently",
        "Admissibility is not a dynamics axiom",
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "context selection",
        "K`/CPT orbit structure",
        "central-sector decomposition",
        "source/action and physical-observable identification",
        "the strong-CP theta gauge and mass-side derivation obligations",
    ]:
        check(f"minimal axiom excludes/scopes {phrase[:50]}", phrase in minimal_flat)

    section("D. approved primitive non-supply")
    for phrase in [
        "no state",
        "measure",
        "weighting",
        "probability rule",
        "normalization rule",
        "value",
    ]:
        check(f"realized primitive withholds {phrase}", phrase in flat(realized))
    for phrase in [
        "no mass ratio",
        "coupling",
        "mixing angle",
        "phase",
        "selector",
        "readout bridge",
        "empirical fit",
    ]:
        check(f"kinetic primitive withholds {phrase}", phrase in flat(kinetic))
    check("note says primitives do not supply bridge", "approved primitives" in note_flat and "do not supply" in note_flat)

    section("E. selected-surface parent boundary")
    for phrase in [
        "bounded selected-surface",
        "Wilson-plus-staggered scalar-mass surface",
        "positive real quark-mass orientation is part of that selected surface",
        "It does not derive from the minimal axiom surface",
        "scalar positive mass orientation",
        "not an unconditional strong-CP solution",
    ]:
        check(f"theta parent carries selected-surface boundary: {phrase[:48]}", phrase in theta_flat)
    check("note preserves selected-surface warning", "selected-surface theorem conditional on theta-free action" in note)

    section("F. determinant-character phase erasure algebra")
    phi, psi = sp.symbols("phi psi", real=True)
    nonzero_failures = []
    for k in range(-5, 6):
        character_equal = sp.simplify(sp.exp(sp.I * k * phi) - sp.exp(-sp.I * k * phi))
        if k == 0:
            check("k=0 character is K/CPT invariant", character_equal == 0)
        else:
            witness_phi = sp.pi / (2 * abs(k))
            witness = sp.simplify(sp.exp(sp.I * k * witness_phi) - sp.exp(-sp.I * k * witness_phi))
            ok = witness != 0
            check(f"k={k} character fails K/CPT invariance at witness", ok, witness)
            if ok:
                nonzero_failures.append(k)
    check("all scanned nonzero characters fail", nonzero_failures == [k for k in range(-5, 6) if k != 0], nonzero_failures)
    k_sym = sp.symbols("k", integer=True)
    check("sin(k phi)=0 all phi forces k=0 in scanned integers", all(k == 0 or sp.sin(k * sp.pi / (2 * abs(k))) != 0 for k in range(-5, 6)))

    section("G. K-evenness alone is too weak")
    cos_even = sp.simplify(sp.cos(-phi) - sp.cos(phi))
    check("cos(phi) is K-even", cos_even == 0)
    multiplicative_gap = sp.simplify(sp.cos(phi + psi) - sp.cos(phi) * sp.cos(psi))
    witness_gap = sp.N(multiplicative_gap.subs({phi: sp.pi / 3, psi: sp.pi / 5}))
    check("cos phase probe is not multiplicative", abs(float(witness_gap)) > 1e-6, witness_gap)
    additive_sum = sp.cos(phi) + sp.cos(psi)
    check("sum cos is finite-additive over two disjoint records", sp.simplify(additive_sum - sp.cos(phi) - sp.cos(psi)) == 0)
    check("sum cos is K-even recordwise", sp.simplify(additive_sum.subs({phi: -phi, psi: -psi}) - additive_sum) == 0)
    check("sum cos remains phase-sensitive", phi in additive_sum.free_symbols and psi in additive_sum.free_symbols)
    check("note carries hostile guard", "Record additivity alone also permits K-even phase-sensitive sums" in note_flat)

    section("H. note discipline")
    check("note Type header is no_go", "**Type:** no_go" in note)
    check("note Claim type header is no_go", "**Claim type:** no_go" in note)
    check("scope boundary blocks retirement", "does not derive, refute, re-grade, retire, or remove theta" in note_flat)
    check("audit boundary present", "**Audit boundary:** independent audit lane only." in note)
    check("primary runner link present", "scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py" in note)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    for phrase in [
        "The gauge-side winding account is untouched.",
        "No physical quark-sector determinant readout is derived.",
        "No positive real mass orientation is derived from the axioms.",
        "derive the action, determinant-channel, K/CPT registration, and exhaustion steps",
    ]:
        check(f"note carries boundary phrase: {phrase[:48]}", phrase in note_flat)
    forbidden = [
        "Theta is retired",
        "theta_bar = 0 is derived",
        "audited_clean",
        "effective_status = retained",
        "neutron electric dipole",
        "uses a fitted value",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    wall_names = set(re.findall(r"\bW_[A-Za-z0-9_]+", note))
    check("no wall names introduced", wall_names == set(), wall_names)

    section("I. markdown dependency and context control")
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "STRONG_CP_THETA_ZERO_NOTE.md",
        "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    for unlinked in [
        "THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md",
        "STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md",
        "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
    ]:
        check(f"context note not markdown-linked: {unlinked[:38]}", f"{unlinked}](" not in note)
    check("note line count is bounded", 160 <= len(note.splitlines()) <= 260, len(note.splitlines()))
    check("verification block states fail-zero threshold", "Expected close: `FAIL=0` with at least 100 checks." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 100 else 1


if __name__ == "__main__":
    raise SystemExit(main())
