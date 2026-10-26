#!/usr/bin/env python3
"""Supplied CKM/PMNS toy-data separation and conditional sign rule.

Two specified witnesses share an even polynomial stand-in and an independent
positive CKM sign, but have opposite odd signs. A stipulated coupling chooses
one witness. This does not establish physical selector/yield closure or the
absence of other framework laws. Historical stronger claims are withdrawn.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/HUBBLE_LANE5_C2_CKM_PMNS_RIGHT_SENSITIVE_SELECTOR_STRETCH_NOTE_2026-04-29.md",
    "docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md",
    "docs/DM_LEPTOGENESIS_PMNS_MINIMAL_A13_SHEET_SELECTOR_THEOREM_NOTE_2026-04-16.md",
    "docs/DM_LEPTOGENESIS_PMNS_SELECTOR_BANK_CP_SHEET_BLINDNESS_THEOREM_NOTE_2026-04-16.md",
    "docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md",
    "docs/PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md",
)

PASS_COUNT = 0
FAIL_COUNT = 0

np.set_printoptions(precision=10, suppress=True, linewidth=120)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def even_pmns_data(delta: float, q_plus: float, a13_abs: float) -> tuple[float, float, float]:
    """A minimal stand-in for the even response pair and A13 magnitude."""
    return (
        round(delta * delta + q_plus * q_plus, 12),
        round(delta * delta * q_plus * q_plus, 12),
        round(a13_abs, 12),
    )


def odd_pmns_data(delta: float, a13_abs: float) -> tuple[int, float]:
    sign = 1 if delta > 0 else -1
    return sign, sign * a13_abs


def ckm_cp_orientation() -> tuple[float, float, float, int]:
    rho = 1.0 / 6.0
    eta = math.sqrt(5.0) / 6.0
    delta = math.atan(math.sqrt(5.0))
    sign_eta = 1 if eta > 0.0 else -1
    return rho, eta, delta, sign_eta


def candidate_cross_sector_selector(sign_eta_ckm: int, a13_abs: float) -> float:
    return sign_eta_ckm * a13_abs


def test_authority_text() -> None:
    print("\n" + "=" * 88)
    print("PART 1: DOCUMENTARY INPUT OBSERVATIONS (NOT SCIENTIFIC PROOF)")
    print("=" * 88)

    own_note = read("docs/HUBBLE_LANE5_C2_CKM_PMNS_RIGHT_SENSITIVE_SELECTOR_STRETCH_NOTE_2026-04-29.md")
    check("Own note limits the witness to supplied toy data", "finite conditional toy-data separation" in own_note and "physical selector and yield remain open" in own_note)

    eta_audit = read("docs/HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md")
    a13 = read("docs/DM_LEPTOGENESIS_PMNS_MINIMAL_A13_SHEET_SELECTOR_THEOREM_NOTE_2026-04-16.md")
    blindness = read("docs/DM_LEPTOGENESIS_PMNS_SELECTOR_BANK_CP_SHEET_BLINDNESS_THEOREM_NOTE_2026-04-16.md")
    ckm = read("docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md")
    right = read("docs/PMNS_RIGHT_CONJUGACY_INVARIANT_NO_GO_NOTE.md")

    check(
        "Lane 5 eta audit names the right-sensitive Z3 doublet-block law",
        "right-sensitive" in eta_audit and "Z_3" in eta_audit and "doublet-block" in eta_audit,
    )
    check(
        "Parent records unresolved selector/yield and does not certify one sufficient gate",
        "unresolved physical selector/yield obligation" in eta_audit
        and "not a proof that a single gate is sufficient" in eta_audit,
    )
    check(
        "Historical A13 note contains the two sign labels",
        "sign of `A13`" in a13 and "A13 > 0" in a13 and "A13 < 0" in a13,
    )
    check(
        "Historical selector-bank note records its CP-sheet claim",
        "CP-sheet blind" in blindness and "delta -> -delta" in blindness,
    )
    check(
        "CKM note records the supplied positive-branch formula",
        "eta = sqrt(5)/6" in ckm and "tan(delta_CKM)" in ckm,
    )
    check(
        "Right-conjugacy note contains its named right-sensitive restriction",
        "non-conjugacy-invariant" in right and "right-sensitive" in right,
    )


def test_pmns_even_data_blindness() -> None:
    print("\n" + "=" * 88)
    print("PART 2: TWO TOY WITNESSES SHARE EVEN DATA AND DIFFER IN SIGN")
    print("=" * 88)

    rho_star = math.sqrt(6.0) / 3.0
    a13_abs = 2.0 * rho_star
    plus = {
        "delta": rho_star,
        "q_plus": rho_star,
        "a13_abs": a13_abs,
    }
    minus = {
        "delta": -rho_star,
        "q_plus": rho_star,
        "a13_abs": a13_abs,
    }

    even_plus = even_pmns_data(**plus)
    even_minus = even_pmns_data(**minus)
    odd_plus = odd_pmns_data(plus["delta"], plus["a13_abs"])
    odd_minus = odd_pmns_data(minus["delta"], minus["a13_abs"])

    print(f"  even(+sheet) = {even_plus}")
    print(f"  even(-sheet) = {even_minus}")
    print(f"  odd(+sheet)  = sign,A13 = {odd_plus}")
    print(f"  odd(-sheet)  = sign,A13 = {odd_minus}")

    check("The two sheets have identical even PMNS data", even_plus == even_minus)
    check("The same two sheets have opposite A13 sign", odd_plus[0] == -odd_minus[0])
    check("A selector using only the even data is sheet-blind", even_plus == even_minus and odd_plus != odd_minus)


def test_ckm_orientation_candidate_is_conditional() -> None:
    print("\n" + "=" * 88)
    print("PART 3: CKM ORIENTATION GIVES A COHERENT BUT CONDITIONAL SELECTOR")
    print("=" * 88)

    rho, eta, delta_ckm, sign_eta = ckm_cp_orientation()
    a13_abs = 2.0 * math.sqrt(6.0) / 3.0
    selected_a13 = candidate_cross_sector_selector(sign_eta, a13_abs)

    print(f"  rho_CKM={rho:.12f}")
    print(f"  eta_CKM={eta:.12f}")
    print(f"  delta_CKM={delta_ckm:.12f}")
    print(f"  candidate selected A13={selected_a13:.12f}")

    check("CKM CP coordinates obey rho=1/6", abs(rho - 1.0 / 6.0) < 1e-12)
    check("CKM CP coordinates obey eta=sqrt(5)/6", abs(eta - math.sqrt(5.0) / 6.0) < 1e-12)
    check("CKM orientation is positive on the named branch", sign_eta == 1)
    check("The candidate sign(A13)=sign(eta_CKM) selects A13>0", selected_a13 > 0.0)


def test_missing_typed_coupling_witness() -> None:
    print("\n" + "=" * 88)
    print("PART 4: STIPULATED MODEL HAS NO COUPLING PREMISE")
    print("=" * 88)

    sign_eta = ckm_cp_orientation()[3]
    a13_abs = 2.0 * math.sqrt(6.0) / 3.0

    world_plus = {
        "ckm_sign": sign_eta,
        "pmns_even": even_pmns_data(math.sqrt(6.0) / 3.0, math.sqrt(6.0) / 3.0, a13_abs),
        "pmns_a13": a13_abs,
    }
    world_minus = {
        "ckm_sign": sign_eta,
        "pmns_even": even_pmns_data(-math.sqrt(6.0) / 3.0, math.sqrt(6.0) / 3.0, a13_abs),
        "pmns_a13": -a13_abs,
    }

    # Stipulation of this toy configuration, not an exhaustive framework search.
    coupling_law_present = False
    current_data_distinguish_worlds = (
        world_plus["ckm_sign"] != world_minus["ckm_sign"]
        or world_plus["pmns_even"] != world_minus["pmns_even"]
    )
    conditional_law_would_select = candidate_cross_sector_selector(sign_eta, a13_abs) == world_plus["pmns_a13"]

    check("Two witnesses share CKM orientation and PMNS even data", not current_data_distinguish_worlds)
    check("The witnesses differ only in the PMNS A13 sign", world_plus["pmns_a13"] == -world_minus["pmns_a13"])
    check("A cross-sector sign law would select the constructive witness", conditional_law_would_select)
    check("The model flag stipulates no coupling premise (not a law-absence proof)", not coupling_law_present)
    check("Conditional rule selects one witness while model flag is false", conditional_law_would_select and not coupling_law_present)


def test_status_firewall() -> None:
    print("\n" + "=" * 88)
    print("PART 5: CLAIM-STATUS FIREWALL")
    print("=" * 88)

    # Historical configuration token retained; it establishes no no-go theorem.
    actual_current_surface_status = "no-go"
    conditional_surface_status = "conditional-support"
    open_imports = [
        "typed CKM CP orientation to PMNS dW_e^H coupling law",
        "canonical right-frame law or equivalent right-sensitive observable principle",
    ]
    proposal_allowed = False

    check("Historical no-go status token is configuration only, not a scientific result", actual_current_surface_status == "no-go")
    check("The candidate is only conditional support under a new coupling law", conditional_surface_status == "conditional-support")
    check("Two named model dependencies remain listed", len(open_imports) == 2)
    check("Configuration disallows stronger proposal wording", not proposal_allowed)


def main() -> int:
    print("=" * 88)
    print("LANE 5 C2: CKM/PMNS RIGHT-SENSITIVE SELECTOR STRETCH")
    print("=" * 88)
    print()
    print("Two supplied witnesses and an optional cross-sector sign rule.")
    print("No physical yield, selector closure or global law-absence claim.")

    test_authority_text()
    test_pmns_even_data_blindness()
    test_ckm_orientation_candidate_is_conditional()
    test_missing_typed_coupling_witness()
    test_status_firewall()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    print("per_element: checked -- three polynomial stand-in entries and two odd signs.")
    print("per_site: not executed -- no spatial sites occur in this toy model.")
    print("per_mode: checked -- two supplied sign witnesses, not a physical mode inventory.")
    print("per_block: not executed -- no microscopic matrix block is constructed.")
    print("lattice_wide: not executed -- finite toy data only; no lattice claim.")

    if FAIL_COUNT:
        print("C2 selector stretch runner failed; do not use the note.")
        return 1

    print("Result: supplied even-data witnesses differ in sign; physical questions remain open.")
    print("The supplied sign rule selects one witness when imposed; no yield follows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
