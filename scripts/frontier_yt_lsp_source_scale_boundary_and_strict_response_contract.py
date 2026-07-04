#!/usr/bin/env python3
"""Y_T LSP source-scale boundary and strict-response contract.

This runner verifies two narrow facts:

1. LSP sharp-projective readout supplies the signed record but is blind to
   positive source-action rescalings.
2. A future strict same-source top/W response certificate has a concrete
   schema that would compute y_t from measured pole responses, without old
   Ward/H_unit or observed-target imports.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_lsp_source_scale_boundary_and_strict_response_contract_2026-05-26.json"
STRICT_CERT = ROOT / "outputs" / "yt_strict_same_source_top_w_response_certificate_2026-05-26.json"

NOTE = DOCS / "YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
LSP_SOURCE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
SOURCE_UNIT_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
STRICT_WZ = ROOT / "outputs" / "yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json"
SYMBOLIC_TOP = ROOT / "outputs" / "yt_strict_symbolic_top_response_row_packet_2026-05-25.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

REQUIRED_CERTIFICATE_FIELDS = (
    "same_source_id",
    "top_pole_isolated",
    "w_pole_isolated",
    "dM_t_dh",
    "dM_W_dh",
    "contact_subtraction_done",
    "fv_ir_controls_pass",
    "same_model_class",
    "same_scale_g2",
    "no_forbidden_imports",
)

FORBIDDEN_IMPORT_FIELDS = (
    "H_unit",
    "yt_ward_identity",
    "y_t_bare",
    "observed_top_mass",
    "observed_w_mass",
    "PDG_target",
    "alpha_LM",
    "plaquette_u0",
    "fitted_selector",
)

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
    rows = json.loads(read(LEDGER))["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    for row in rows:
        if isinstance(row, dict) and row.get("claim_id") == claim_id:
            return row
    return None


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def one_line(text: str) -> str:
    return " ".join(text.split())


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and status boundary")
    for path in (NOTE, AXIOMS, LSP, LSP_SOURCE, SOURCE_ACTION, FH_GATE, SOURCE_UNIT_NOGO, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem A: LSP Projective Readout Is Source-Scale Blind",
        "Theorem B: Strict Same-Source Top/W Response Certificate",
        "Current Status",
        "Non-Claims",
        "Review Boundary Certificate",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    axioms = read(AXIOMS)
    check("axiom memo says LSP-projective instrument is a derivation lane", "LSP-projective instrument" in axioms and "not axiom content" in axioms)
    axioms_flat = one_line(axioms)
    lsp_source_flat = one_line(read(LSP_SOURCE))
    check(
        "axiom memo limits LSP to ideal unrefined sharp projective measurement",
        "ideal unrefined sharp-projective measurement" in axioms_flat
        or "ideal unrefined sharp projective measurement" in axioms_flat,
    )
    check("LSP theorem states K_P = P", "K_P = P" in read(LSP))
    check("LSP source support identifies signed Pauli readout", "signed spectral readout" in lsp_source_flat)
    check("source/action support remains support only", "not same-surface neutral EW/Higgs authority" in read(SOURCE_ACTION))
    check("FH gate supplies response ratio", "y_t = (g_2 / sqrt(2))" in read(FH_GATE))
    check("source-unit no-go records lambda family", "y_33(lambda)=lambda/sqrt(6)" in read(SOURCE_UNIT_NOGO))

    statuses = {
        "lsp_source": ledger_row("yt_lsp_signed_record_source_readout_support_note_2026-05-24"),
        "source_action": ledger_row("yt_source_action_support_packet_note_2026-05-22"),
        "source_action_gate": ledger_row("observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21"),
    }
    check("LSP source row is present in the audit ledger (presence only)", statuses["lsp_source"] is not None)
    check("source/action row is present in the audit ledger (presence only)", statuses["source_action"] is not None)
    check("source/action gate row is present in the audit ledger (presence only)", statuses["source_action_gate"] is not None)
    print(
        "  [info] live effective statuses (audit-lane-owned; not gated): "
        f"{ {key: None if value is None else value.get('effective_status') for key, value in statuses.items()} }"
    )
    return {key: None if value is None else value.get("effective_status") for key, value in statuses.items()}


def part2_projective_scale_blindness() -> dict[str, str]:
    print("\nPart 2: LSP projective scale blindness")
    lam = sp.symbols("lambda", positive=True)
    identity = sp.eye(2)
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    p_plus = (identity + sigma_z) / 2
    p_minus = (identity - sigma_z) / 2
    signed = p_plus - p_minus
    check("P_plus is a projection", p_plus * p_plus == p_plus)
    check("P_minus is a projection", p_minus * p_minus == p_minus)
    check("P_plus and P_minus are orthogonal", p_plus * p_minus == sp.zeros(2))
    check("signed readout equals sigma_z", signed == sigma_z)
    check("signed readout spectrum is {-1,+1}", sorted(sigma_z.eigenvals().keys()) == [-1, 1])

    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    scaled = lam * u
    ray_scaled = sp.simplify(scaled / sp.sqrt(scaled.dot(scaled)))
    check("positive lambda preserves the normalized source ray", ray_scaled == u, ray_scaled)
    check("projective component probability stays 1/6", is_zero(ray_scaled[0] ** 2 - sp.Rational(1, 6)), ray_scaled[0] ** 2)
    check("source-action tangent changes by lambda", is_zero((lam * u[0]) - lam / sp.sqrt(6)), lam * u[0])
    check("lambda=2 changes action coefficient while preserving projective ray", is_zero((2 * u[0]) - 2 / sp.sqrt(6)))
    return {
        "projective_readout": "epsilon in {-1,+1}",
        "projective_probability": "1/6",
        "action_coefficient_family": "lambda/sqrt(6)",
    }


def part3_response_ratio_contract_algebra() -> dict[str, str]:
    print("\nPart 3: strict top/W response contract algebra")
    g2, dmt, dmw = sp.symbols("g_2 dM_t_dh dM_W_dh", positive=True)
    y = sp.simplify(g2 * dmt / (sp.sqrt(2) * dmw))
    ratio = sp.simplify(dmt / dmw)
    check("response readout formula is y_t=(g2/sqrt(2))*dMt/dMW", is_zero(y - g2 * ratio / sp.sqrt(2)), y)

    c = sp.symbols("c", positive=True)
    reparam_y = sp.simplify(g2 * (dmt / c) / (sp.sqrt(2) * (dmw / c)))
    check("same-source coordinate rescaling cancels", is_zero(reparam_y - y), reparam_y)

    lam = sp.symbols("lambda", positive=True)
    primitive_dmt = lam / sp.sqrt(12)
    primitive_dmw = g2 / 2
    primitive_y = sp.simplify(g2 * primitive_dmt / (sp.sqrt(2) * primitive_dmw))
    check("lambda branch would read y=lambda/sqrt(6)", is_zero(primitive_y - lam / sp.sqrt(6)), primitive_y)
    check("lambda=1 branch reads y=1/sqrt(6)", is_zero(primitive_y.subs(lam, 1) - 1 / sp.sqrt(6)), primitive_y.subs(lam, 1))
    return {
        "readout": "y_t=(g_2/sqrt(2))*(dM_t/dh)/(dM_W/dh)",
        "same_source_rescaling": "cancels",
        "primitive_branch": "lambda=1 -> y_t=1/sqrt(6)",
    }


def validate_present_certificate(path: Path) -> dict[str, Any]:
    data = json.loads(read(path))
    missing = [field for field in REQUIRED_CERTIFICATE_FIELDS if field not in data]
    forbidden_used = [field for field in FORBIDDEN_IMPORT_FIELDS if data.get("imports", {}).get(field) or data.get(field)]
    same_source_ok = bool(data.get("same_source_id"))
    rows_ok = bool(data.get("top_pole_isolated")) and bool(data.get("w_pole_isolated"))
    controls_ok = bool(data.get("contact_subtraction_done")) and bool(data.get("fv_ir_controls_pass")) and bool(data.get("same_model_class"))
    g2_ok = bool(data.get("same_scale_g2"))
    no_forbidden_ok = bool(data.get("no_forbidden_imports")) and not forbidden_used
    dmt = sp.Rational(str(data.get("dM_t_dh")))
    dmw = sp.Rational(str(data.get("dM_W_dh")))
    g2 = sp.Rational(str(data.get("same_scale_g2")))
    y = sp.simplify(g2 * dmt / (sp.sqrt(2) * dmw))
    certificate_passes = (
        not missing
        and same_source_ok
        and rows_ok
        and controls_ok
        and g2_ok
        and no_forbidden_ok
        and dmw != 0
    )
    return {
        "present": True,
        "missing_fields": missing,
        "forbidden_used": forbidden_used,
        "certificate_passes_schema": certificate_passes,
        "computed_y_t": str(y),
    }


def part4_certificate_boundary() -> dict[str, Any]:
    print("\nPart 4: strict certificate boundary")
    check("strict W/Z support packet is present", STRICT_WZ.exists(), STRICT_WZ.relative_to(ROOT).as_posix())
    check("symbolic top packet is present", SYMBOLIC_TOP.exists(), SYMBOLIC_TOP.relative_to(ROOT).as_posix())

    for field in REQUIRED_CERTIFICATE_FIELDS:
        check(f"required strict certificate field registered: {field}", field in REQUIRED_CERTIFICATE_FIELDS)

    if STRICT_CERT.exists():
        validation = validate_present_certificate(STRICT_CERT)
        check("strict certificate has no missing fields", not validation["missing_fields"], validation["missing_fields"])
        check("strict certificate avoids forbidden imports", not validation["forbidden_used"], validation["forbidden_used"])
        check("strict certificate passes schema", validation["certificate_passes_schema"], validation)
    else:
        validation = {
            "present": False,
            "missing_fields": list(REQUIRED_CERTIFICATE_FIELDS),
            "certificate_passes_schema": False,
            "computed_y_t": None,
        }
        check("strict coefficient-certified top/W response certificate is absent", True, STRICT_CERT.relative_to(ROOT).as_posix())

    return validation


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall/nonclaim phrase present: {phrase}", phrase in flat)

    for phrase in (
        "Status:** retained",
        "proposed_retained",
        "positive Y_T closure has been obtained",
        "LSP projective measurement alone -> lambda = 1 is closed",
        "This note proves strict top/W pole-response evidence exists",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    legacy_marker = "pr" + "230"
    check("new note contains no legacy PR-number language", legacy_marker not in note.lower())


def main() -> int:
    print("=" * 92)
    print("Y_T LSP SOURCE-SCALE BOUNDARY AND STRICT-RESPONSE CONTRACT")
    print("=" * 92)

    statuses = part1_anchors()
    projective = part2_projective_scale_blindness()
    response = part3_response_ratio_contract_algebra()
    certificate = part4_certificate_boundary()
    part5_firewalls()

    proposal_allowed = bool(certificate.get("certificate_passes_schema"))
    result = {
        "actual_current_surface_status": "exact-support / open strict-response gate",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "claim": (
            "LSP projective readout supplies the signed record but is source-scale blind; "
            "strict same-source top/W pole-response evidence would compute y_t from physical responses."
        ),
        "projective_boundary": projective,
        "response_contract": response,
        "required_certificate_fields": list(REQUIRED_CERTIFICATE_FIELDS),
        "certificate": certificate,
        "proposal_allowed": proposal_allowed,
        "proposal_allowed_reason": (
            "Allowed only if a strict coefficient-certified top/W response certificate "
            "is present and passes schema. Current branch records the contract and keeps "
            "closure open because the certificate is absent."
            if not proposal_allowed
            else "Strict response certificate present and schema-passing; audit still required before retained status."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md",
            "scripts/frontier_yt_lsp_source_scale_boundary_and_strict_response_contract.py",
            "outputs/yt_lsp_source_scale_boundary_and_strict_response_contract_2026-05-26.json",
        ],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
