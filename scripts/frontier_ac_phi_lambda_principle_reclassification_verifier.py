#!/usr/bin/env python3
"""Check the AC_phi_lambda principle-grade reclassification meta note.

This runner is a review-hygiene check, not a physics proof. It verifies:

  - the note is classified as meta and does not declare pipeline status;
  - the reclassification of AC_phi_lambda (charged-lepton sharpening) as
    a framework principle is stated explicitly and cited to the Tier-A
    registry's existing principle-grade pattern for P1;
  - the chain-of-custody note's L1-L10 structural content is correctly
    identified as retained / retained_bounded (no claim of derivation
    change);
  - the no-go portfolio (three AC_phi_lambda rows + three charged-lepton
    sharpening anchors) is named correctly;
  - the reclassification is stated as conditional / SHARPENED, not as
    strict closure;
  - the note does not promote any retained theorem or claim Q=2/3 /
    r=1/2 is derived;
  - the note does not add a new mathematical axiom and does not propose
    a framework axiom change;
  - the note does not load PDG values as derivation input;
  - the note does not modify the Tier-A registry note or
    tier_a_admissions.json (registry text remains the authority);
  - cross-references to the precedent reclassification (radian), Tier-A
    registry, chain-of-custody note, P1 principle-grade analog, and the
    no-go portfolio are present;
  - audit-lane authority is preserved (status verdict deferred per
    precedent);
  - the radian precedent is cited as the meta-source-note +
    paired-verifier governance template.

Companion to:
  - ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md (Tier-A registry)
  - STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md (AC_phi_lambda parent)
  - CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md
  - RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md (precedent)
  - CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md (umbrella)
  - OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md (P1 parent)
  - OBSERVABLE_PRINCIPLE_P1_BRIDGE_EXTENSIVITY_PRIMITIVE_NARROW_NOTE_2026-05-21.md
    (P1 principle-grade analog)
  - MINIMAL_AXIOMS_2026-05-20.md (A1+A2 baseline)
"""

from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "AC_PHI_LAMBDA_PRINCIPLE_RECLASSIFICATION_NOTE_2026-06-03.md"
TIER_A_REGISTRY = ROOT / "docs" / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
TIER_A_DATA = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
PARENT_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
CHAIN_OF_CUSTODY = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md"
RADIAN_PRECEDENT = ROOT / "docs" / "RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md"
CONVENTIONS_UMBRELLA = ROOT / "docs" / "CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md"
P1_PARENT = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md"
P1_EXTENSIVITY_ANALOG = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_EXTENSIVITY_PRIMITIVE_NARROW_NOTE_2026-05-21.md"
)
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" | {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def main() -> int:
    for path, label in [
        (NOTE, "AC_phi_lambda principle-grade reclassification note"),
        (TIER_A_REGISTRY, "Tier-A admitted-input registry note"),
        (TIER_A_DATA, "Tier-A admissions data file"),
        (PARENT_GATE, "AC_phi_lambda canonical parent (staggered-Dirac realization gate)"),
        (CHAIN_OF_CUSTODY, "charged-lepton Koide value chain-of-custody note"),
        (RADIAN_PRECEDENT, "radian-unit-convention reclassification precedent"),
        (CONVENTIONS_UMBRELLA, "conventions-unification companion note"),
        (P1_PARENT, "P1 observable-principle parent note"),
        (P1_EXTENSIVITY_ANALOG, "P1 extensivity-primitive principle-grade analog note"),
        (MINIMAL_AXIOMS, "minimal axioms note"),
    ]:
        if not path.exists():
            print(f"missing {label}: {path}")
            return 1

    note = NOTE.read_text()
    registry = TIER_A_REGISTRY.read_text()
    parent = PARENT_GATE.read_text()
    chain = CHAIN_OF_CUSTODY.read_text()
    radian = RADIAN_PRECEDENT.read_text()
    minimal = MINIMAL_AXIOMS.read_text()
    p1_analog = P1_EXTENSIVITY_ANALOG.read_text()
    tier_a_data = json.loads(TIER_A_DATA.read_text())

    print("AC_phi_lambda principle-grade reclassification check")
    print(f"note: {NOTE.relative_to(ROOT)}")
    print()

    # ---- classification ----
    check("source note is meta (Type)", "**Type:** meta" in note)
    check("source note is meta (Claim type)", "**Claim type:** meta" in note)
    check(
        "does not declare effective_status value",
        not re.search(r"effective_status\s*:\s*[A-Za-z]+", note),
    )
    check(
        "does not declare audit-clean verdict token",
        "audited" + "_clean" not in note,
    )
    check(
        "does not add a new mathematical axiom",
        ("does not add a new mathematical axiom" in note.lower())
        or ("does not propose any framework axiom change" in note.lower())
        or ("A1+A2" in note and "still suffice" in note),
    )

    # ---- core reclassification statement ----
    check(
        "reclassification of AC_phi_lambda as framework principle stated explicitly",
        "framework principle" in note.lower()
        and (
            "reclassif" in note.lower()
        ),
    )
    check(
        "principle-grade parallel to P1 cited",
        "principle-grade" in note.lower()
        and "P1" in note,
    )
    check(
        "Tier-A registry cited explicitly",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23" in note,
    )
    check(
        "AC_phi_lambda canonical parent (staggered-Dirac gate) cited",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03" in note,
    )
    check(
        "radian precedent reclassification cited",
        "RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv" in note,
    )
    check(
        "P1 principle-grade analog (extensivity primitive) cited",
        "OBSERVABLE_PRINCIPLE_P1_BRIDGE_EXTENSIVITY_PRIMITIVE_NARROW_NOTE_2026-05-21" in note,
    )

    # ---- charged-lepton sharpening content (K-reality + det_C) ----
    check(
        "K-reality selector named",
        "K-reality" in note,
    )
    check(
        "det_C / equal-power-per-block selector named",
        "det_C" in note and "equal-power-per-block" in note,
    )
    check(
        "charged-lepton sharpening 2026-06-02 cited",
        "CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02" in note
        and "charged-lepton" in note.lower(),
    )

    # ---- no-go portfolio: three AC_phi_lambda rows from registry ----
    for portfolio_row in [
        "koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24",
        "koide_delta_lattice_wilson_selected_eigenline_no_go_note_2026-04-24",
        "koide_delta_marked_relative_cobordism_no_go_note_2026-04-24",
    ]:
        check(
            f"no-go portfolio row named: {portfolio_row}",
            portfolio_row in note,
        )

    # ---- no-go portfolio: three charged-lepton sharpening anchors ----
    for sharp_anchor in [
        "KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21",
        "KOIDE_Q_DELTA_RESIDUAL_COHOMOLOGY_OBSTRUCTION_NO_GO_NOTE_2026-04-24",
        "KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16",
    ]:
        check(
            f"charged-lepton sharpening anchor cited: {sharp_anchor}",
            sharp_anchor in note,
        )

    # ---- chain-of-custody structural content correctly identified ----
    check(
        "L6 exact Q(r) cited correctly",
        "Q = 1/3 + (2/3) r" in note or "Q = 1/3 + (2/3)r" in note,
    )
    check(
        "L7 topological 2/9 cited",
        "2/9" in note and "topological" in note.lower(),
    )
    check(
        "L9 r=1/2 equipartition stationary-point characterization cited",
        "r = 1/2" in note
        and ("equipartition" in note.lower() or "2-sector" in note.lower())
        and "stationary" in note.lower(),
    )
    check(
        "L10 Q=2/3 <=> r=1/2 biconditional cited",
        "Q = 2/3" in note and ("r = 1/2" in note) and ("⟺" in note or "<=>" in note),
    )

    # ---- conditional / sharpened framing ----
    check(
        "reclassification stated conditionally",
        "conditional" in note.lower(),
    )
    check(
        "SHARPENED framing explicitly stated",
        "SHARPENED" in note,
    )
    check(
        "three honest framings present",
        "CLOSURE" in note and "STRUCTURAL OBSTRUCTION" in note and "SHARPENED" in note,
    )

    # ---- audit hygiene: no PDG numerical loading ----
    pdg_numeric_patterns = [
        r"m_e\s*=\s*0\.51",
        r"m_μ\s*=\s*105",
        r"m_τ\s*=\s*1\.77\d",
        r"m_e\s*=\s*0\.000511",
        r"m_τ\s*=\s*1\.7771",
    ]
    empirical_loading = False
    for pat in pdg_numeric_patterns:
        if re.search(pat, note, flags=re.IGNORECASE):
            empirical_loading = True
            break
    check(
        "no PDG numerical mass values inserted as derivation input",
        not empirical_loading,
    )
    check(
        "explicitly disclaims PDG-input use",
        "PDG values as derivation input" in note
        or "does not load PDG" in note.lower()
        or "PDG appears nowhere" in note,
    )

    # ---- forbidden promotions ----
    def has_affirmative_match(pattern: str, text: str) -> bool:
        """True iff there is at least one match NOT preceded (within ~80 chars)
        by a negation token."""
        for m in re.finditer(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            head = text[max(0, m.start() - 80): m.start()].lower()
            negators = (
                "not ",
                "no ",
                "never",
                "without",
                "absent",
                "unaffected",
                "unchanged",
                "claim ",
                "does not",
                "is not",
                "doesn't",
            )
            if any(neg in head for neg in negators):
                continue
            return True
        return False

    forbidden_promotions = [
        ("Q=2/3 derivation claimed", r"Q\s*=\s*2/3\s+is\s+derived"),
        ("r=1/2 derivation claimed", r"r\s*=\s*1/2\s+is\s+derived"),
        ("AC_phi_lambda closure by declaration",
         r"AC_φλ\s+is\s+(now\s+)?closed"),
        ("specific theorem promoted to retained",
         r"theorem\s+(?:is\s+)?(?:now\s+)?promoted\s+to\s+retained"),
        ("Tier-A registry row removed",
         r"removes?\s+AC_φλ\s+from\s+the\s+Tier-A"),
    ]
    for label, pattern in forbidden_promotions:
        check(
            f"forbidden promotion absent: {label}",
            not has_affirmative_match(pattern, note),
        )

    # ---- AC_phi_lambda remains in the Tier-A registry ----
    check(
        "explicit statement that AC_phi_lambda stays in tier_a_admissions.json",
        "tier_a_admissions.json" in note
        and ("UNCHANGED" in note or "unchanged" in note),
    )
    check(
        "explicit statement that Tier-A registry note text is unchanged",
        "Tier-A registry" in note
        and (
            "unchanged" in note.lower()
            or "is unchanged" in note.lower()
        ),
    )
    check(
        "explicit statement that no claim_type / effective_status field is modified",
        "claim_type" in note and "effective_status" in note,
    )

    # ---- chain-of-custody standing preserved ----
    check(
        "chain-of-custody derived-modulo-AC_phi_lambda standing preserved",
        "derived-modulo-`AC_φλ`" in note or "derived-modulo-AC_φλ" in note,
    )

    # ---- review-loop rule present ----
    check(
        "review-loop rule present",
        "Review-loop rule" in note or "review-loop rule" in note.lower(),
    )

    # ---- audit-lane authority preserved ----
    check(
        "audit-lane authority preserved",
        "audit lane" in note.lower() and "authority" in note.lower(),
    )

    # ---- principle-grade pattern vs unit-convention pattern (parallel to P / radian) ----
    check(
        "meta-source-note + paired-verifier governance template explicitly cited (radian precedent)",
        "meta-source-note" in note.lower()
        or "meta source-note" in note.lower(),
    )
    check(
        "explicit distinction between P1 principle-grade and P unit-convention",
        "unit convention" in note.lower()
        and "principle" in note.lower(),
    )

    # ---- baseline alignment (A1+A2 unchanged) ----
    check(
        "minimal axioms note has physical Cl(3) A1",
        "the physical local algebra is `Cl(3,0)`" in minimal
        or "the physical local algebra is `Cl(3)`" in minimal,
    )
    check(
        "minimal axioms note has physical Z^3 A2",
        "The lattice sites form the cubic lattice `Z^3`" in minimal
        or "the physical spatial substrate is the cubic" in minimal,
    )
    check(
        "note states A1+A2 still suffice (no axiom change)",
        "A1+A2" in note and "still suffice" in note,
    )

    # ---- Tier-A registry confirms AC_phi_lambda is row 2 with label AC_phi_lambda ----
    check(
        "Tier-A registry data: AC_phi_lambda label present",
        any(
            v.get("label") == "AC_phi_lambda"
            for v in tier_a_data.get("derivation_targets", {}).values()
        ),
    )
    check(
        "Tier-A registry data: AC_phi_lambda canonical id matches staggered-Dirac gate",
        "staggered_dirac_realization_gate_note_2026-05-03"
        in tier_a_data.get("derivation_targets", {}),
    )

    # ---- Tier-A registry confirms P1 is principle-grade (mild) ----
    check(
        "Tier-A registry confirms P1 principle-grade (mild)",
        "principle-grade* (mild)" in registry
        or "principle-grade (mild)" in registry
        or "*principle-grade*" in registry,
    )

    # ---- chain-of-custody anchors confirmed retained / retained_bounded ----
    check(
        "chain-of-custody confirms L6 exact Q(r) is retained",
        "exact `Q = 1/3 + (2/3)r`" in chain
        and "retained" in chain,
    )
    check(
        "chain-of-custody confirms L9 r=1/2 equipartition is bounded candidate",
        "2-sector equipartition" in chain
        and "bounded candidate" in chain,
    )

    # ---- radian precedent confirms it is itself meta and a precedent for reclassification ----
    check(
        "radian precedent is itself meta",
        "**Claim type:** meta" in radian,
    )
    check(
        "radian precedent is a reclassification (per file name + body)",
        "reclassif" in radian.lower(),
    )

    # ---- P1 extensivity-primitive analog is the principle-grade pattern ----
    check(
        "P1 extensivity-primitive analog discusses extensivity premise",
        "extensivity premise" in p1_analog.lower(),
    )

    # ---- bottom line present ----
    check(
        "bottom-line verdict present",
        "Bottom line" in note or "Verdict:" in note,
    )

    # ---- comparison table to principle-grade stratification present ----
    check(
        "comparison table to P1 / P stratification present",
        "P1" in note and "P` (radian-bridge)" in note,
    )

    # ---- scope limit: charged-lepton sector only ----
    check(
        "scope limit (charged-lepton sector only) stated",
        "broader generation-mass-pattern admission across all" in note
        or "charged-lepton sector specifically" in note.lower()
        or ("charged-lepton" in note.lower() and "sector" in note.lower()),
    )

    # ---- explicit non-derivation of r=1/2 / Q=2/3 ----
    check(
        "explicit non-derivation of r=1/2 / Q=2/3 stated",
        "Derive `r = 1/2` or `Q = 2/3`" in note
        or "does not derive" in note.lower()
        and "r = 1/2" in note,
    )

    # ---- staggered-Dirac open_gate unchanged ----
    check(
        "parent gate (staggered-Dirac realization) open_gate preserved",
        "open_gate" in note or "Claim closure of the staggered-Dirac realization gate" in note,
    )
    check(
        "staggered-Dirac parent gate file confirmed open_gate on disk",
        "**Type:** open_gate" in parent,
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print(
        "AC_phi_lambda principle-grade reclassification check passed: "
        "AC_phi_lambda (charged-lepton sharpening) proposed as framework "
        "principle parallel to P1, conditional / SHARPENED, no retained "
        "theorem promoted, no new axiom, no PDG input, Tier-A registry "
        "unchanged, chain-of-custody standing preserved."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
