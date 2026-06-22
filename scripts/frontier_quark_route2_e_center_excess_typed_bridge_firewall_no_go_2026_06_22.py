#!/usr/bin/env python3
"""Typed-bridge firewall for the Route-2 E-center excess 7/8.

The Route-2 endpoint can be restated as q_E - 1 = 7/8.  This runner checks
whether same-rational 7/8 appearances can be reused as that E-center excess
without a typed Route-2 readout bridge.

Status:
  no-go for same-rational import.  The rational 7/8 is exactly the target
  excess, but using another-context 7/8 as q_E-1 is the target premise unless
  a theorem types it as the Route-2 E-center readout slot.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

EXCESS_TARGET = Fraction(7, 8)
Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2, 1)
Q_E_TARGET = Fraction(15, 8)
RHO_E_TARGET = Fraction(21, 4)
C_TE_TARGET = Fraction(-8, 9)
R_CONN = Fraction(8, 9)


@dataclass(frozen=True)
class Candidate:
    name: str
    value: Fraction
    typed_route2_excess: bool
    context: str


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def endpoint_from_excess(excess: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Fraction(1, 1) + excess
    rho_e = Fraction(6, 1) * excess
    center_te = SHELL_TE * Q_T / q_e
    return q_e, rho_e, center_te


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def part1_target_chain() -> None:
    print("PART 1: target excess algebra")
    q_e, rho_e, center_te = endpoint_from_excess(EXCESS_TARGET)
    check("E-center excess target is 7/8", EXCESS_TARGET == Fraction(7, 8))
    check("7/8 excess gives q_E=15/8", q_e == Q_E_TARGET, f"q_E={q_e}")
    check("7/8 excess gives rho_E=21/4", rho_e == RHO_E_TARGET, f"rho_E={rho_e}")
    check("7/8 excess gives center T/E=-8/9 with q_T=5/6 and shell T/E=-2", center_te == C_TE_TARGET, f"c_TE={center_te}")
    check("reverse chain recovers excess from rho_E", RHO_E_TARGET / 6 == EXCESS_TARGET)


def part2_candidate_inventory() -> None:
    print()
    print("PART 2: same-rational candidate inventory")
    candidates = (
        Candidate("route2_e_center_excess", Fraction(7, 8), True, "target typed slot"),
        Candidate("apbc_fourth_power_factor", Fraction(7, 8), False, "APBC / hierarchy context"),
        Candidate("fermi_bose_thermal_ratio", Fraction(7, 8), False, "thermal/statistical context"),
        Candidate("taste_weight", Fraction(7, 18), False, "taste/radian inventory context"),
        Candidate("rconn_as_excess_control", R_CONN, False, "center-ratio color support, not excess"),
    )
    for candidate in candidates:
        q_e, rho_e, center_te = endpoint_from_excess(candidate.value)
        print(f"  {candidate.name}: value={candidate.value}, q_E={q_e}, rho_E={rho_e}, c_TE={center_te}")
        check(f"{candidate.name} has exact rational value", isinstance(candidate.value, Fraction), candidate.context)

    typed_hits = [c.name for c in candidates if c.typed_route2_excess and c.value == EXCESS_TARGET]
    same_rational_untyped = [c.name for c in candidates if (not c.typed_route2_excess) and c.value == EXCESS_TARGET]
    check("only the typed Route-2 excess candidate closes the excess slot", typed_hits == ["route2_e_center_excess"], str(typed_hits))
    check("same-rational untyped 7/8 appearances are present but not closing", same_rational_untyped == ["apbc_fourth_power_factor", "fermi_bose_thermal_ratio"], str(same_rational_untyped))
    check("taste weight used as excess misses the endpoint", endpoint_from_excess(Fraction(7, 18))[1] == Fraction(7, 3))
    check("R_conn used as excess misses the endpoint", endpoint_from_excess(R_CONN)[1] == Fraction(16, 3))


def part3_apbc_root_and_rconn_roles() -> None:
    print()
    print("PART 3: role controls")
    check("APBC fourth root is not the rational 7/8 itself", EXCESS_TARGET**4 != EXCESS_TARGET, f"(7/8)^4={EXCESS_TARGET**4}")
    q_e_from_rconn_bridge = SHELL_TE * Q_T / (-R_CONN)
    rho_from_rconn_bridge = Fraction(6, 1) * (q_e_from_rconn_bridge - 1)
    check("typed c_TE=-R_conn bridge would give q_E=15/8", q_e_from_rconn_bridge == Q_E_TARGET, f"q_E={q_e_from_rconn_bridge}")
    check("typed c_TE=-R_conn bridge would give rho_E=21/4", rho_from_rconn_bridge == RHO_E_TARGET, f"rho_E={rho_from_rconn_bridge}")
    check("R_conn is exact as center-ratio bridge, not as excess", R_CONN != EXCESS_TARGET and -R_CONN == C_TE_TARGET)
    wrong_sign_qe = SHELL_TE * Q_T / R_CONN
    check("using positive R_conn as center ratio gives wrong signed q_E", wrong_sign_qe != Q_E_TARGET, f"q_E={wrong_sign_qe}")


def part4_authority_markers() -> None:
    print()
    print("PART 4: current authority markers")
    natur = note_text("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    rconn = note_text("QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md")
    measured = note_text("QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md")
    hierarchy = note_text("HIERARCHY_ALPHA_BARE_FOUR_PI_CONTINUUM_MEASURE_CONTENT_ATTRIBUTION_BOUNDED_NOTE_2026-05-26.md")
    check("naturality note names missing E-center primitive", "additional E-center endpoint ratio" in natur)
    check("naturality note leaves rho_E free", "rho_E` free" in natur or "rho_E` gives" in natur)
    check("Rconn note states bridge is conditional", "If that bridge lands" in rconn)
    check("Rconn note has exact -8/9 conditional chain", "c_TE = -F_adj = -8/9" in rconn)
    check("measured calibration note says no derivation of 21/4 is claimed", "no derivation of 21/4" in measured)
    check("hierarchy note contains APBC 7/8 in non-Route-2 context", "(7/8)^(1/4)" in hierarchy or "(7/8)^{1/4}" in hierarchy)


def part5_note_and_status_firewall() -> None:
    print()
    print("PART 5: note and status firewall")
    note = note_text("QUARK_ROUTE2_E_CENTER_EXCESS_TYPED_BRIDGE_FIREWALL_NO_GO_NOTE_2026-06-22.md")
    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for same-rational E-center excess import",
        "This is not an audit verdict",
        "does not close the parent",
        "same rational number != same typed Route-2 readout theorem",
        "does not rule out future E-center theorems",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note)
    banned = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned:
        check(f"note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 E-center excess typed-bridge firewall no-go")
    print("Status: no-go for same-rational E-center excess import; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_target_chain()
    part2_candidate_inventory()
    part3_apbc_root_and_rconn_roles()
    part4_authority_markers()
    part5_note_and_status_firewall()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: E-center excess typed-bridge firewall checks failed.")
        return 1
    print(
        "VERDICT: no-go for same-rational import.  The number 7/8 closes "
        "the E-center excess only when typed as q_E-1 in the Route-2 readout "
        "slot, or supplied by an equivalent typed bridge."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
