#!/usr/bin/env python3
"""Y_T FH top mass-response physical-intervention bridge.

This runner checks the conditional bridge:

    physical top deformation = primitive RN/Fisher source for O_top
      -> dM_t/dh fixed by the normalized top component
      -> top/W FH response readout returns y_33 = 1/sqrt(6)

The runner is intentionally a support gate.  It also records that the current
surface still lacks independent physical-intervention acceptance or strict
same-source top/W pole-response evidence.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_fh_top_mass_response_physical_intervention_bridge_2026-05-25.json"

NOTE = DOCS / "YT_FH_TOP_MASS_RESPONSE_PHYSICAL_INTERVENTION_BRIDGE_NOTE_2026-05-25.md"
PHYSICAL_INTERVENTION = DOCS / "YT_PHYSICAL_TOP_INTERVENTION_IDENTIFICATION_CANDIDATE_NOTE_2026-05-25.md"
OP_BRIDGE = DOCS / "YT_OPERATIONAL_SOURCE_ACTION_BRIDGE_THEOREM_ATTEMPT_NOTE_2026-05-25.md"
FISHER_UNIT = DOCS / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
FH_TOP_W = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
STRICT_WZ = DOCS / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
SYMBOLIC_TOP = DOCS / "YT_STRICT_SYMBOLIC_TOP_RESPONSE_ROW_PACKET_NOTE_2026-05-25.md"
TOP_COEFF_NOGO = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
EW_MASS = DOCS / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

STRICT_TOP_W_ROWS = OUTPUT.parent / "yt_fh_top_w_strict_response_rows_2026-05-25.json"

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


def one_line(text: str) -> str:
    return " ".join(text.split())


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    rows = json.loads(read(LEDGER))["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    iterable = rows
    for row in iterable:
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
    return None


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and authority boundary")
    for path in (
        NOTE,
        PHYSICAL_INTERVENTION,
        OP_BRIDGE,
        FISHER_UNIT,
        FH_TOP_W,
        STRICT_WZ,
        SYMBOLIC_TOP,
        TOP_COEFF_NOGO,
        EW_MASS,
        LEDGER,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Transfer-Matrix FH Readout",
        "Conditional Top Response Contract",
        "Lambda Family Boundary",
        "What This Adds",
        "What Remains Open",
        "Non-Claims",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    status_rows = {
        "yt_source_action_support": ledger_row("yt_source_action_support_packet_note_2026-05-22"),
        "ew_higgs_mass": ledger_row("ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26"),
        "source_action_gate": ledger_row("observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21"),
    }
    statuses = {
        "physical_top_intervention": "open_gate_candidate",
        **{key: None if row is None else row.get("effective_status") for key, row in status_rows.items()},
    }
    check("YT source-action support row is present in the audit ledger (presence only)", status_rows["yt_source_action_support"] is not None)
    check("EW Higgs mass diagonalization row is present in the audit ledger (presence only)", status_rows["ew_higgs_mass"] is not None)
    check("source-action gate row is present in the audit ledger (presence only)", status_rows["source_action_gate"] is not None)
    print(
        "  [info] live effective statuses (audit-lane-owned; not gated): "
        f"{statuses}"
    )

    check("physical-intervention candidate remains open gate", "not retained" in read(PHYSICAL_INTERVENTION))
    check("operational bridge supplies RN action identity", "S_h = S_0 - h O + c(h) I" in read(OP_BRIDGE))
    check("Fisher unit packet supplies lambda=1 branch", "lambda = 1" in read(FISHER_UNIT))
    check("FH top/W route supplies response readout", "y_t = (g_2 / sqrt(2))" in read(FH_TOP_W))
    symbolic_top_text = read(SYMBOLIC_TOP)
    check(
        "symbolic top row leaves coefficient free",
        "free generation-matrix coefficient" in symbolic_top_text
        or "coefficient y_33 remains free" in symbolic_top_text,
    )
    check("top coefficient no-go remains recorded", "does not determine `y_t`" in read(TOP_COEFF_NOGO))
    return statuses


def part2_transfer_matrix_identity() -> None:
    print("\nPart 2: transfer-matrix FH pole derivative")
    h, a_t = sp.symbols("h a_t", positive=True)
    lam_t = sp.Function("Lambda_t")(h)
    lam_0 = sp.Function("Lambda_0")(h)
    mass = -sp.log(lam_t / lam_0) / a_t
    derivative = sp.diff(mass, h)
    expected = -(sp.diff(lam_t, h) / lam_t - sp.diff(lam_0, h) / lam_0) / a_t
    check("d[-log(Lambda_t/Lambda_0)/a_t]/dh identity", is_zero(derivative - expected), derivative)


def part3_normalized_top_source() -> dict[str, str]:
    print("\nPart 3: normalized top source and primitive unit")
    n = sp.Integer(6)
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(n)] * n)
    scaled = lam * u
    fisher_norm = sp.simplify(scaled.dot(scaled))
    check("democratic top source vector has unit norm", is_zero(u.dot(u) - 1), sp.simplify(u.dot(u)))
    check("single top component is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])
    check("scaled physical source family has Fisher norm lambda^2", is_zero(fisher_norm - lam**2), fisher_norm)
    check("primitive source unit selects lambda=1 in this branch", sp.solve(sp.Eq(fisher_norm, 1), lam) == [1])
    return {"top_component": "1/sqrt(6)", "primitive_branch_lambda": "1"}


def part4_mass_response_contract() -> dict[str, str]:
    print("\nPart 4: FH top/W mass-response contract")
    g2, dv_dh, lam = sp.symbols("g_2 dv_dh lambda", positive=True)
    y_primitive = 1 / sp.sqrt(6)
    dmt_primitive = sp.simplify(y_primitive * dv_dh / sp.sqrt(2))
    dmw = sp.simplify(g2 * dv_dh / 2)
    ratio = sp.simplify(dmt_primitive / dmw)
    recovered = sp.simplify(g2 / sp.sqrt(2) * ratio)
    check("primitive top response row", is_zero(dmt_primitive - dv_dh / sp.sqrt(12)), dmt_primitive)
    check("top/W response ratio has predicted value", is_zero(ratio - sp.sqrt(2) / (g2 * sp.sqrt(6))), ratio)
    check("FH response readout returns y_33=1/sqrt(6)", is_zero(recovered - 1 / sp.sqrt(6)), recovered)

    dmt_scaled = sp.simplify(lam * y_primitive * dv_dh / sp.sqrt(2))
    ratio_scaled = sp.simplify(dmt_scaled / dmw)
    recovered_scaled = sp.simplify(g2 / sp.sqrt(2) * ratio_scaled)
    check("lambda-scaled branch returns y_33(lambda)=lambda/sqrt(6)", is_zero(recovered_scaled - lam / sp.sqrt(6)), recovered_scaled)

    c = sp.symbols("c", positive=True)
    reparam_ratio = sp.simplify((dmt_primitive / c) / (dmw / c))
    check("same-source coordinate reparameterization cancels", is_zero(reparam_ratio - ratio), reparam_ratio)
    return {
        "predicted_response_ratio": "sqrt(2)/(g_2 sqrt(6))",
        "primitive_readout": "y_33=1/sqrt(6)",
        "scaled_family_readout": "y_33(lambda)=lambda/sqrt(6)",
    }


def part5_observable_contract_boundary(statuses: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 5: observable contract boundary")
    strict_rows_present = STRICT_TOP_W_ROWS.exists()
    physical_premise_accepted = False
    direct_measurement_present = strict_rows_present
    proposal_allowed = physical_premise_accepted or direct_measurement_present
    check("strict coefficient-certified top/W FH rows are absent", not strict_rows_present, STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())
    check("physical-intervention premise is not accepted by this runner", not physical_premise_accepted)
    check("current artifact is support, not closure proposal", not proposal_allowed)
    return {
        "physical_intervention_premise_accepted": physical_premise_accepted,
        "strict_same_source_response_measurement_present": direct_measurement_present,
        "proposal_allowed": proposal_allowed,
        "remaining_paths": [
            "derive/audit physical top deformation as primitive RN/Fisher O_top source",
            "measure strict same-source top/W pole response ratio directly",
        ],
        "upstream_statuses": statuses,
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall/nonclaim phrase present: {phrase}", phrase in flat)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "author-side retention proposal",
        "positive Y_T closure has been obtained",
        "the Y_T lane has achieved retained closure",
        "baseline alone forces",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 92)
    print("Y_T FH TOP MASS-RESPONSE PHYSICAL-INTERVENTION BRIDGE")
    print("=" * 92)

    statuses = part1_anchors()
    part2_transfer_matrix_identity()
    normalized_source = part3_normalized_top_source()
    response_contract = part4_mass_response_contract()
    boundary = part5_observable_contract_boundary(statuses)
    part6_firewalls()

    result = {
        "status": "conditional exact support / open-gate FH observable-response bridge",
        "claim": (
            "If the physical top Yukawa deformation is the primitive RN/Fisher "
            "source intervention for normalized O_top, then the FH top/W pole "
            "response readout returns y_33=1/sqrt(6)."
        ),
        "route_algebra_closed": True,
        "normalized_source": normalized_source,
        "response_contract": response_contract,
        "boundary": boundary,
        "proposal_allowed": boundary["proposal_allowed"],
        "proposal_allowed_reason": (
            "Blocked on physical-intervention acceptance or direct strict same-source "
            "top/W pole-response measurement; this bridge is exact support only."
        ),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FH_TOP_MASS_RESPONSE_PHYSICAL_INTERVENTION_BRIDGE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_fh_top_mass_response_physical_intervention_bridge.py",
            "outputs/yt_fh_top_mass_response_physical_intervention_bridge_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
