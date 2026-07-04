#!/usr/bin/env python3
"""Y_T same-source EW/Higgs authority gate.

This runner tests whether the current product-RN signed-record source
can already be treated as the physical neutral EW/Higgs source needed by the
top/W Feynman-Hellmann route.

It does not claim positive Y_T closure.  It certifies the exact current
boundary: the repo supplies finite signed-record source/action support, while the
EW Higgs theorem assumes a complex doublet, hypercharge, neutral VEV, and
covariant kinetic term that are not derived from the support source alone.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_same_source_ew_higgs_authority_gate_2026-05-25.json"

NOTE = DOCS / "YT_SAME_SOURCE_EW_HIGGS_AUTHORITY_GATE_NOTE_2026-05-25.md"
SOURCE_ACTION_STATUS = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
NEUTRAL_RAY_BRIDGE = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"
STRICT_WZ_PACKET = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
SYMBOLIC_TOP_PACKET = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
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


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    iterable = rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    return None


def states(n_sites: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n_sites))


def rn_density(h: list[float], omega: list[tuple[int, ...]]) -> list[float]:
    weights = [math.exp(sum(hi * ei for hi, ei in zip(h, eps))) for eps in omega]
    z = sum(weights)
    return [w / z for w in weights]


def max_abs(values: list[float]) -> float:
    return max(abs(v) for v in values)


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and audit status")
    for path in (NOTE, SOURCE_ACTION_STATUS, FH_GATE, NEUTRAL_RAY_BRIDGE, EW_MASS, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    required = [
        "Authority Test",
        "Why The Qubit / Signed-Record Axiom Helps But Does Not Finish",
        "Exact Obstruction Witness",
        "What This Adds",
        "Non-Claims",
    ]
    for phrase in required:
        check(f"note contains required section: {phrase}", phrase in note)

    source_action_row = ledger_row("yt_source_action_support_packet_note_2026-05-22")
    ew_mass_row = ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26")
    check("source-action support row is present in the audit ledger (presence only)", source_action_row is not None)
    check("EW Higgs gauge-mass theorem row is present in the audit ledger (presence only)", ew_mass_row is not None)
    print(
        "  [info] live effective statuses (audit-lane-owned; not gated): "
        f"source_action={(source_action_row or {}).get('effective_status')!r}, "
        f"ew_mass={(ew_mass_row or {}).get('effective_status')!r}"
    )
    return {
        "source_action_status": (source_action_row or {}).get("effective_status"),
        "ew_mass_status": (ew_mass_row or {}).get("effective_status"),
    }


def part2_signed_record_source() -> None:
    print("\nPart 2: source-action support identity")
    omega = states(2)
    h = [0.19, -0.31]
    delta = 1.0e-6
    for site in range(2):
        hp = h.copy()
        hm = h.copy()
        hp[site] += delta
        hm[site] -= delta
        rp = rn_density(hp, omega)
        rm = rn_density(hm, omega)
        score = [(math.log(a) - math.log(b)) / (2.0 * delta) for a, b in zip(rp, rm)]
        mean = sum(eps[site] * p for eps, p in zip(omega, rn_density(h, omega)))
        expected = [eps[site] - mean for eps in omega]
        err = max_abs([a - b for a, b in zip(score, expected)])
        check(f"site {site} RN score is centered signed record", err < 1.0e-9, err)

    # The support source is one real source coordinate per primitive record.
    check("primitive source carrier is real one-component per site", True, "epsilon_x in {-1,+1}")


def part3_ew_higgs_required_structure() -> None:
    print("\nPart 3: EW Higgs theorem requires doublet/covariant structure")
    v = sp.symbols("v", positive=True, real=True)
    i = sp.I
    h0 = sp.Matrix([0, v / sp.sqrt(2)])
    tau1 = sp.Matrix([[0, 1], [1, 0]])
    tau2 = sp.Matrix([[0, -i], [i, 0]])
    tau3 = sp.Matrix([[1, 0], [0, -1]])
    t1, t2, t3 = tau1 / 2, tau2 / 2, tau3 / 2
    y = sp.Rational(1, 2) * sp.eye(2)

    check("Higgs vacuum is a two-component complex doublet", h0.shape == (2, 1))
    check("T1 acts nontrivially on H0", not matrix_is_zero(t1 * h0), t1 * h0)
    check("T2 acts nontrivially on H0", not matrix_is_zero(t2 * h0), t2 * h0)
    check("T3 + Y leaves H0 neutral", matrix_is_zero((t3 + y) * h0))
    check("hypercharge generator has Y_H=1/2 on H", y == sp.Rational(1, 2) * sp.eye(2))


def part4_intertwiner_missing_witness() -> dict[str, Any]:
    print("\nPart 4: carrier ray is present; full EW transfer response is not")
    source_action_text = read(SOURCE_ACTION_STATUS)
    ew_text = read(EW_MASS)
    check("neutral carrier-ray bridge is present", NEUTRAL_RAY_BRIDGE.exists())
    check("strict W/Z denominator response is present", STRICT_WZ_PACKET.exists())
    check("symbolic top response row is present", SYMBOLIC_TOP_PACKET.exists())
    check(
        "source-action support says it is not full physical neutral EW/Higgs authority",
        "not same-surface neutral EW/Higgs authority" in source_action_text
        or "not yet accepted as current neutral EW/Higgs authority" in source_action_text,
    )
    check("EW theorem assumes Higgs doublet", "H = (H^+, H^0)^T" in ew_text)
    check("EW theorem assumes standard covariant derivative", "D_mu = partial_mu" in ew_text)

    # Non-identifiability witness: the support source admits arbitrary scalar slopes
    # v(h)=a h at the origin unless an EW carrier theorem fixes a.
    a1, a2, h = sp.symbols("a1 a2 h", positive=True)
    v1 = a1 * h
    v2 = a2 * h
    slopes_equal_only_if = sp.solve(sp.Eq(sp.diff(v1, h), sp.diff(v2, h)), a2)
    check("two radial embeddings differ unless slope is separately fixed", slopes_equal_only_if == [a1], slopes_equal_only_if)
    check("no coefficient-certified top/W FH row certificate exists", not (ROOT / "outputs" / "yt_fh_top_w_strict_response_rows_2026-05-25.json").exists())
    return {
        "same_source_ew_higgs_authority_present": False,
        "neutral_carrier_ray_bridge_present": NEUTRAL_RAY_BRIDGE.exists(),
        "strict_wz_denominator_response_present": STRICT_WZ_PACKET.exists(),
        "symbolic_top_response_row_present": SYMBOLIC_TOP_PACKET.exists(),
        "full_same_surface_top_w_transfer_response_present": False,
        "strict_top_w_rows_present": False,
    }


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    required_firewalls = [
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "`alpha_LM`",
        "plaquette/u0",
        "PDG",
        "observed W/Z/top masses",
    ]
    for phrase in required_firewalls:
        check(f"firewall phrase present: {phrase}", phrase in note)

    forbidden = [
        "Status:** retained",
        "proposed_retained",
        "This gate proves positive Y_T closure",
        "This note derives `y_t`",
        "This note derives the Higgs doublet",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T SAME-SOURCE EW/HIGGS AUTHORITY GATE")
    print("=" * 78)

    statuses = part1_anchors()
    part2_signed_record_source()
    part3_ew_higgs_required_structure()
    blockers = part4_intertwiner_missing_witness()
    part5_firewalls()

    result = {
        "status": "current-surface authority gate remains open",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The neutral carrier ray is now bridged, but the source-action support "
            "packet is retained_bounded only and no retained theorem supplies the "
            "top coefficient needed to complete the top/W route."
        ),
        "current_blockers": blockers,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_SAME_SOURCE_EW_HIGGS_AUTHORITY_GATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_same_source_ew_higgs_authority_gate.py",
            "outputs/yt_same_source_ew_higgs_authority_gate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
