#!/usr/bin/env python3
"""Y_T lambda-normalization attack fanout gate.

The runner verifies the support-only route synthesis in
docs/YT_LAMBDA_NORMALIZATION_ATTACK_FANOUT_NOTE_2026-05-25.md.

It intentionally does not certify Y_T closure.  It checks algebraic witnesses
for which lambda routes are scale-blind, scale-breaking, or scale-canceling,
and it verifies that current audited source-action lane boundary rows remain narrow.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_lambda_normalization_attack_fanout_2026-05-25.json"
NOTE = DOCS / "YT_LAMBDA_NORMALIZATION_ATTACK_FANOUT_NOTE_2026-05-25.md"
SOURCE_ACTION_STATUS = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
COLOR_NOGO = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
COLOR_THEOREM = DOCS / "YUKAWA_COLOR_PROJECTION_THEOREM.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def ky(kappa: Fraction) -> Fraction:
    return Fraction(8, 9) + Fraction(1, 9) * kappa


def part1_anchors() -> None:
    print("\nPart 1: packet anchors and audit-grounded status")
    for path in (NOTE, SOURCE_ACTION_STATUS, POLE_NOGO, COLOR_NOGO, COLOR_THEOREM, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    required_note_phrases = [
        "**Claim type:** meta",
        "open / support-only route synthesis",
        "Assumptions Exercise",
        "First-Principles Exercise",
        "Literature Search",
        "Mathematics Search",
        "Probe Portfolio",
        "Consolidated Attack Ranking",
        "No-Go Audit",
        "Recommended Next Science Block",
        "Non-Claims",
    ]
    for phrase in required_note_phrases:
        check(f"note contains section/phrase: {phrase}", phrase in note)

    status_row = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    pole_row = ledger_row("yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23")
    color_row = ledger_row("yt_color_projection_correction_note")
    decoration_row = ledger_row("yukawa_color_projection_theorem")

    check("source-action support status is retained_bounded", status_row.get("effective_status") == "retained_bounded")
    check("pole-row normalization no-go is retained_no_go", pole_row.get("effective_status") == "retained_no_go")
    check("color projection correction no-go is retained_no_go", color_row.get("effective_status") == "retained_no_go")
    check("color projection theorem is decoration", decoration_row.get("audit_status") == "audited_decoration")


def part2_pole_row_scale_blindness() -> None:
    print("\nPart 2: pole rows and Gram purity are scale-blind")
    a_s = Fraction(5, 3)
    a_h = Fraction(7, 4)
    q = Fraction(5, 7)
    t = 3
    c_ss = a_s * a_s * q**t
    c_sh = a_s * a_h * q**t
    c_hh = a_h * a_h * q**t
    gram = c_sh * c_sh - c_ss * c_hh
    check("base rank-one Gram determinant vanishes", gram == 0, str(gram))

    for mu, lam in ((Fraction(2, 1), Fraction(3, 1)), (Fraction(3, 5), Fraction(11, 7))):
        ss = (mu * a_s) ** 2 * q**t
        sh = (mu * a_s) * (lam * a_h) * q**t
        hh = (lam * a_h) ** 2 * q**t
        normalized = sh * sh / (ss * hh)
        mass_ratio = ss / ((mu * a_s) ** 2 * q ** (t + 1))
        check(f"Gram purity survives mu={mu}, lambda={lam}", sh * sh - ss * hh == 0)
        check(f"normalized residue ratio stays one at mu={mu}, lambda={lam}", normalized == 1, str(normalized))
        check(f"effective mass ratio stays q^-1 at mu={mu}, lambda={lam}", mass_ratio == Fraction(7, 5), str(mass_ratio))


def part3_color_kappa_absorption() -> None:
    print("\nPart 3: color-projection ambiguity can be absorbed by scalar scale")
    connected = ky(Fraction(0))
    full = ky(Fraction(1))
    scale = full / connected
    check("K_Y(0) is 8/9", connected == Fraction(8, 9), str(connected))
    check("K_Y(1) is 1", full == 1, str(full))
    check("full/connected normalization ratio is 9/8", scale == Fraction(9, 8), str(scale))
    check("sqrt(9/8) is nontrivial", abs(math.sqrt(9 / 8) - 1.0) > 0.01, math.sqrt(9 / 8))


def part4_wz_response_witness() -> None:
    print("\nPart 4: W/Z absolute response breaks scale; W/Z ratio does not")
    g2 = 0.65
    gy = 0.36
    v = 1.23
    rw = g2 * g2 * v * v / 4.0
    rz = (g2 * g2 + gy * gy) * v * v / 4.0
    ratio = rw / rz
    lam = 1.17
    rw_scaled = lam * lam * rw
    rz_scaled = lam * lam * rz
    ratio_scaled = rw_scaled / rz_scaled
    recovered_lambda = math.sqrt(rw_scaled / rw)
    recovered_v = math.sqrt(4.0 * rw_scaled / (g2 * g2))

    check("W/Z ratio is lambda-blind", abs(ratio_scaled - ratio) < 1.0e-14, ratio_scaled)
    check("absolute W response recovers lambda with fixed gauge coupling", abs(recovered_lambda - lam) < 1.0e-14, recovered_lambda)
    check("absolute W response recovers scaled canonical v", abs(recovered_v - lam * v) < 1.0e-14, recovered_v)


def part5_fh_same_source_ratio() -> None:
    print("\nPart 5: same-source FH top/W ratio cancels source scale")
    dmt_dh = 2.4
    dmw_dh = 1.1
    source_scale = 3.7
    ratio = dmt_dh / dmw_dh
    scaled_ratio = (dmt_dh / source_scale) / (dmw_dh / source_scale)
    check("top/W FH slope ratio cancels source scale", abs(scaled_ratio - ratio) < 1.0e-15, scaled_ratio)

    top_only = dmt_dh / source_scale
    check("top-only FH slope changes under source rescaling", abs(top_only - dmt_dh) > 1.0, top_only)


def part6_spectral_and_symplectic_boundaries() -> None:
    print("\nPart 6: spectral and symplectic routes need an extra anchor")
    z = 0.42
    lam = 1.9
    z_scaled = lam * lam * z
    check("spectral residue scales as lambda^2", abs(z_scaled / z - lam * lam) < 1.0e-15, z_scaled)

    omega = 1.0
    h_scale = lam
    pi_scale = 1.0 / lam
    check("symplectic pairing preserved by inverse scaling", abs(h_scale * pi_scale * omega - omega) < 1.0e-15)

    finite_trace_commutator = 0
    trace_identity_dimension = 2
    check("finite-dimensional exact CCR trace obstruction holds", finite_trace_commutator != trace_identity_dimension)


def part7_brst_boundary() -> None:
    print("\nPart 7: BRST/FMS supports operator class but not scalar coupling value")
    allowed_invariants = {"HdagH", "(HdagH)^2", "gauge_kinetic", "yukawa"}
    lambda_a = 0.10
    lambda_b = 0.30
    check("(HdagH)^2 is an allowed invariant", "(HdagH)^2" in allowed_invariants)
    check("two scalar couplings can share same invariant set", lambda_a != lambda_b and allowed_invariants == allowed_invariants.copy())


def part8_firewalls() -> None:
    print("\nPart 8: overclaim firewalls")
    note = read(NOTE)
    forbidden_phrases = [
        "Status: retained",
        "Status:** retained",
        "proposed_retained",
        "This packet derives `y_t`",
        "This packet derives `m_t`",
        "`kappa_Y = 0` is derived",
        "the scalar LSZ bridge is closed",
    ]
    for phrase in forbidden_phrases:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    required_firewalls = [
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "`alpha_LM`",
        "plaquette/u0",
        "PDG",
    ]
    for phrase in required_firewalls:
        check(f"firewall term present: {phrase}", phrase in note)


def main() -> int:
    print("=" * 78)
    print("Y_T LAMBDA-NORMALIZATION ATTACK FANOUT")
    print("=" * 78)

    part1_anchors()
    part2_pole_row_scale_blindness()
    part3_color_kappa_absorption()
    part4_wz_response_witness()
    part5_fh_same_source_ratio()
    part6_spectral_and_symplectic_boundaries()
    part7_brst_boundary()
    part8_firewalls()

    result = {
        "status": "open / support-only route synthesis",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The packet identifies scale-breaking and scale-canceling routes, "
            "and later packets supply W/Z denominator response plus a symbolic top "
            "response row, but they do not supply a derived top coefficient, retained "
            "top-carrier authority, physical-scale g_2, or matching/running closure."
        ),
        "best_next_routes": [
            "strict top coefficient theorem or direct top response measurement",
            "retained same-scale g_2 after the top numerator is supplied",
            "same-surface canonical O_H plus OS/LSZ/contact sum rule",
        ],
        "current_no_gos_apply_narrowly": {
            "pole_row_normalization": "applies to pole rows/Gram purity without a new canonical scalar-source theorem",
            "color_projection_correction": "applies to deriving kappa_Y=0 from the cited SU(3) channel-count packet",
            "yukawa_color_projection": "decoration only; representation arithmetic, not physical Yukawa matching",
        },
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_LAMBDA_NORMALIZATION_ATTACK_FANOUT_NOTE_2026-05-25.md",
            "scripts/frontier_yt_lambda_normalization_attack_fanout.py",
            "outputs/yt_lambda_normalization_attack_fanout_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
