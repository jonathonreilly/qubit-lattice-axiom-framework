#!/usr/bin/env python3
"""Current-branch discovery audit for accepted strict Y_T top/W pole rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUTS = ROOT / "outputs"
OUTPUT = OUTPUTS / "yt_strict_top_w_pole_row_repository_discovery_no_go_2026-05-27.json"

NOTE = DOCS / "YT_STRICT_TOP_W_POLE_ROW_REPOSITORY_DISCOVERY_NO_GO_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
STRICT_AVAILABILITY = DOCS / "YT_STRICT_SPARSE_TOP_W_POLE_RESPONSE_AVAILABILITY_AUDIT_NOTE_2026-05-27.md"
DIRECT_SPARSE = DOCS / "YT_DIRECT_SAME_SURFACE_SPARSE_TRANSFER_RESPONSE_CERTIFICATE_NOTE_2026-05-27.md"
STRICT_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
NATIVE_BACKEND = DOCS / "YT_NATIVE_SAME_SURFACE_TOP_W_TRANSFER_ACTION_BACKEND_CANDIDATE_NOTE_2026-05-27.md"
BACKEND_PROJECTOR_OBSTRUCTION = DOCS / "YT_NATIVE_BACKEND_AUTHORITY_PROJECTOR_OBSTRUCTION_NOTE_2026-05-27.md"
TOP_PROJECTOR_OBSTRUCTION = DOCS / "YT_TOP_SECTOR_PROJECTOR_GENERATION_LABEL_OBSTRUCTION_NOTE_2026-05-27.md"
MICROSCOPIC_BOUNDARY = DOCS / "YT_MICROSCOPIC_BACKEND_PROJECTOR_MATRIX_ELEMENT_BOUNDARY_NOTE_2026-05-27.md"
MATRIX_ELEMENT = DOCS / "YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md"
C3_DIHEDRAL_BASEPOINT = DOCS / "YT_C3_DIHEDRAL_BASEPOINT_ANCHOR_OBSTRUCTION_NOTE_2026-05-27.md"

FULL_STACK_OUT = OUTPUTS / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"
STRICT_AVAILABILITY_OUT = OUTPUTS / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
DIRECT_SPARSE_OUT = OUTPUTS / "yt_direct_same_surface_sparse_transfer_response_certificate_2026-05-27.json"
STRICT_OBSTRUCTION_OUT = OUTPUTS / "yt_strict_same_source_top_w_response_coefficient_obstruction_2026-05-27.json"
NATIVE_BACKEND_OUT = OUTPUTS / "yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json"
BACKEND_PROJECTOR_OBSTRUCTION_OUT = OUTPUTS / "yt_native_backend_authority_projector_obstruction_2026-05-27.json"
TOP_PROJECTOR_OBSTRUCTION_OUT = OUTPUTS / "yt_top_sector_projector_generation_label_obstruction_2026-05-27.json"
MICROSCOPIC_BOUNDARY_OUT = OUTPUTS / "yt_microscopic_backend_projector_matrix_element_boundary_2026-05-27.json"
MATRIX_ELEMENT_OUT = OUTPUTS / "yt_same_surface_top_matrix_element_factorization_boundary_2026-05-27.json"
C3_DIHEDRAL_BASEPOINT_OUT = OUTPUTS / "yt_c3_dihedral_basepoint_anchor_obstruction_2026-05-27.json"

STRICT_TOP_W_ROWS = OUTPUTS / "yt_fh_top_w_strict_response_rows_2026-05-25.json"
STRICT_SOURCE_HIGGS_ROWS = OUTPUTS / "yt_source_action_block508_id_source_higgs_strict_rows_2026-05-22.json"

DISCOVERY_NAME_KEYWORDS = (
    "strict",
    "sparse",
    "pole",
    "response",
    "top_w",
    "same_surface",
    "backend",
    "projector",
    "matrix_element",
)
DOC_NAME_KEYWORDS = (
    "strict",
    "response",
    "top_w",
    "same_surface",
    "backend",
    "projector",
    "matrix_element",
)
POSITIVE_FLAG_KEYS = (
    "strict_top_w_response_certificate_present",
    "strict_positive_certificate_present",
    "strict_positive_certificate_passes",
    "strict_certificate_passes",
)
BACKEND_KEYS = (
    "accepted_same_surface_backend_present",
    "accepted_same_surface_transfer_backend_present",
)
TOP_POLE_KEYS = ("accepted_top_pole_isolated", "top_pole_isolated")
W_POLE_KEYS = ("accepted_w_pole_isolated", "w_pole_isolated")
TOP_ROW_KEYS = (
    "coefficient_certified_dM_t_row_present",
    "coefficient_certified_dM_t_dh",
    "coefficient_certified_dM_t_dell",
)
W_ROW_KEYS = (
    "coefficient_certified_dM_W_row_present",
    "coefficient_certified_dM_W_dh",
    "coefficient_certified_dM_W_dell",
)
CONTACT_KEYS = ("contact_subtraction_done", "vacuum_contact_subtraction_done")
FV_KEYS = ("finite_volume_ir_controls_pass", "fv_ir_controls_pass", "FV_IR_model_class_checks_pass")
MODEL_KEYS = ("same_model_class",)
FREE_COEFF_KEYS = ("contains_free_top_coefficient_input", "readout_contains_kappa")

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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def iter_key_values(obj: Any, prefix: str = "") -> list[tuple[str, Any]]:
    rows: list[tuple[str, Any]] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            next_prefix = f"{prefix}.{key}" if prefix else key
            rows.append((next_prefix, value))
            rows.extend(iter_key_values(value, next_prefix))
    elif isinstance(obj, list):
        for idx, value in enumerate(obj):
            rows.extend(iter_key_values(value, f"{prefix}[{idx}]"))
    return rows


def truthy_paths(data: dict[str, Any], keys: tuple[str, ...]) -> list[str]:
    return [
        path
        for path, value in iter_key_values(data)
        if path.split(".")[-1] in keys and value is True
    ]


def false_paths(data: dict[str, Any], keys: tuple[str, ...]) -> list[str]:
    return [
        path
        for path, value in iter_key_values(data)
        if path.split(".")[-1] in keys and value is False
    ]


def any_truthy(data: dict[str, Any], keys: tuple[str, ...]) -> bool:
    return bool(truthy_paths(data, keys))


def all_required_positive(data: dict[str, Any]) -> bool:
    has_flag = any_truthy(data, POSITIVE_FLAG_KEYS)
    has_backend = any_truthy(data, BACKEND_KEYS)
    has_top = any_truthy(data, TOP_POLE_KEYS)
    has_w = any_truthy(data, W_POLE_KEYS)
    has_top_row = any_truthy(data, TOP_ROW_KEYS)
    has_w_row = any_truthy(data, W_ROW_KEYS)
    has_contact = any_truthy(data, CONTACT_KEYS)
    has_fv = any_truthy(data, FV_KEYS)
    has_model = any_truthy(data, MODEL_KEYS)
    has_free_coeff = any_truthy(data, FREE_COEFF_KEYS)
    top_level_proposal = data.get("proposal_allowed") is True
    return (
        has_flag
        and has_backend
        and has_top
        and has_w
        and has_top_row
        and has_w_row
        and has_contact
        and has_fv
        and has_model
        and not has_free_coeff
        and top_level_proposal
    )


def discovery_outputs() -> list[Path]:
    paths = []
    for path in sorted(OUTPUTS.glob("yt_*.json")):
        name = path.name.lower()
        if any(keyword in name for keyword in DISCOVERY_NAME_KEYWORDS):
            paths.append(path)
    return paths


def candidate_summary(path: Path) -> dict[str, Any]:
    data = load_json(path)
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "claim_id": data.get("claim_id"),
        "status": data.get("actual_current_surface_status"),
        "trace_class": data.get("trace_class"),
        "proposal_allowed": data.get("proposal_allowed"),
        "fail_count": data.get("fail_count"),
        "positive_flag_true_paths": truthy_paths(data, POSITIVE_FLAG_KEYS),
        "accepted_backend_true_paths": truthy_paths(data, BACKEND_KEYS),
        "top_pole_true_paths": truthy_paths(data, TOP_POLE_KEYS),
        "w_pole_true_paths": truthy_paths(data, W_POLE_KEYS),
        "top_row_true_paths": truthy_paths(data, TOP_ROW_KEYS),
        "w_row_true_paths": truthy_paths(data, W_ROW_KEYS),
        "contact_true_paths": truthy_paths(data, CONTACT_KEYS),
        "fv_true_paths": truthy_paths(data, FV_KEYS),
        "model_true_paths": truthy_paths(data, MODEL_KEYS),
        "free_coefficient_true_paths": truthy_paths(data, FREE_COEFF_KEYS),
        "accepted_backend_false_paths": false_paths(data, BACKEND_KEYS),
        "complete_strict_packet": all_required_positive(data),
    }


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and dependency statuses")
    paths = (
        NOTE,
        FULL_STACK,
        STRICT_AVAILABILITY,
        DIRECT_SPARSE,
        STRICT_OBSTRUCTION,
        NATIVE_BACKEND,
        BACKEND_PROJECTOR_OBSTRUCTION,
        TOP_PROJECTOR_OBSTRUCTION,
        MICROSCOPIC_BOUNDARY,
        MATRIX_ELEMENT,
        C3_DIHEDRAL_BASEPOINT,
        FULL_STACK_OUT,
        STRICT_AVAILABILITY_OUT,
        DIRECT_SPARSE_OUT,
        STRICT_OBSTRUCTION_OUT,
        NATIVE_BACKEND_OUT,
        BACKEND_PROJECTOR_OBSTRUCTION_OUT,
        TOP_PROJECTOR_OBSTRUCTION_OUT,
        MICROSCOPIC_BOUNDARY_OUT,
        MATRIX_ELEMENT_OUT,
        C3_DIHEDRAL_BASEPOINT_OUT,
    )
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Certificate Fields",
        "Assumptions / Imports Exercise",
        "First-Principles / Elon Exercise",
        "No-Go Audit",
        "Literature / Math Search",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: no-go / current-branch strict-row discovery",
        "proposal_allowed: false",
        "no accepted strict top/W pole-row packet is present",
        "accepted_same_surface_backend_present: true",
        "contains_free_top_coefficient_input: false",
    ):
        check(f"note contains discovery phrase: {phrase}", phrase in note)

    deps = {
        "full_stack": load_json(FULL_STACK_OUT),
        "strict_availability": load_json(STRICT_AVAILABILITY_OUT),
        "direct_sparse": load_json(DIRECT_SPARSE_OUT),
        "strict_obstruction": load_json(STRICT_OBSTRUCTION_OUT),
        "native_backend": load_json(NATIVE_BACKEND_OUT),
        "backend_projector_obstruction": load_json(BACKEND_PROJECTOR_OBSTRUCTION_OUT),
        "top_projector_obstruction": load_json(TOP_PROJECTOR_OBSTRUCTION_OUT),
        "microscopic_boundary": load_json(MICROSCOPIC_BOUNDARY_OUT),
        "matrix_element": load_json(MATRIX_ELEMENT_OUT),
        "dihedral_basepoint": load_json(C3_DIHEDRAL_BASEPOINT_OUT),
    }
    for name, data in deps.items():
        check(f"{name} dependency passed", data.get("fail_count") == 0, data.get("fail_count"))
    check(
        "strict availability already marks certificate absent",
        deps["strict_availability"].get("certificate_boundary", {}).get("strict_positive_certificate_present") is False,
    )
    check(
        "direct sparse harness marks strict certificate absent",
        deps["direct_sparse"].get("strict_top_w_response_certificate_present") is False,
    )
    check(
        "native backend candidate is not accepted backend",
        deps["native_backend"].get("candidate_backend", {}).get("accepted_same_surface_transfer_backend_present")
        is False,
    )
    return deps


def part2_named_artifacts() -> dict[str, bool]:
    print("\nPart 2: named strict-row artifacts")
    strict_rows_present = STRICT_TOP_W_ROWS.exists()
    source_rows_present = STRICT_SOURCE_HIGGS_ROWS.exists()
    check("named strict top/W rows artifact absent", not strict_rows_present, STRICT_TOP_W_ROWS.relative_to(ROOT).as_posix())
    check("named strict source/Higgs rows artifact absent", not source_rows_present, STRICT_SOURCE_HIGGS_ROWS.relative_to(ROOT).as_posix())
    return {
        "strict_top_w_rows_artifact_present": strict_rows_present,
        "strict_source_higgs_rows_artifact_present": source_rows_present,
    }


def part3_repository_discovery() -> dict[str, Any]:
    print("\nPart 3: repository discovery scan")
    paths = discovery_outputs()
    summaries = [candidate_summary(path) for path in paths]
    complete = [summary for summary in summaries if summary["complete_strict_packet"]]
    positive_flags = [
        summary
        for summary in summaries
        if summary["positive_flag_true_paths"]
    ]
    top_level_proposals = [
        summary
        for summary in summaries
        if summary["proposal_allowed"] is True
    ]
    accepted_backends = [
        summary
        for summary in summaries
        if summary["accepted_backend_true_paths"]
    ]

    check("discovery scan found Y_T response/backend/projector outputs", len(paths) >= 10, len(paths))
    check("no complete strict positive packet discovered", len(complete) == 0, [item["path"] for item in complete])
    check("no strict positive certificate flag is true", len(positive_flags) == 0, positive_flags)
    check("no relevant top-level proposal_allowed true packet", len(top_level_proposals) == 0, top_level_proposals)
    check(
        "accepted backend true paths are absent in discovery outputs",
        len(accepted_backends) == 0,
        accepted_backends,
    )

    partial_rows = [
        summary
        for summary in summaries
        if summary["top_row_true_paths"] or summary["w_row_true_paths"]
    ]
    check("partial row support/candidates are visible", len(partial_rows) > 0, [item["path"] for item in partial_rows])
    check(
        "partial row packets are not complete strict packets",
        all(not item["complete_strict_packet"] for item in partial_rows),
        [item["path"] for item in partial_rows],
    )
    check(
        "native candidate has coefficient rows but lacks accepted backend",
        any(
            item["path"].endswith("yt_native_same_surface_top_w_transfer_action_backend_candidate_2026-05-27.json")
            and item["top_row_true_paths"]
            and item["w_row_true_paths"]
            and item["accepted_backend_false_paths"]
            for item in summaries
        ),
    )
    check(
        "tainted counterfamily evidence is not a positive packet",
        any(item["free_coefficient_true_paths"] for item in summaries),
    )
    return {
        "candidate_count": len(paths),
        "candidate_paths": [path.relative_to(ROOT).as_posix() for path in paths],
        "complete_strict_packets": complete,
        "positive_flag_packets": positive_flags,
        "accepted_backend_packets": accepted_backends,
        "top_level_proposal_allowed_packets": top_level_proposals,
        "partial_row_packets": partial_rows,
    }


def part4_doc_status_scan() -> dict[str, Any]:
    print("\nPart 4: note wording scan")
    paths = [
        path
        for path in sorted(DOCS.glob("YT*.md"))
        if any(keyword in path.name.lower() for keyword in DOC_NAME_KEYWORDS)
        and "msbar_to_pole" not in path.name.lower()
    ]
    retained_hits = []
    proposal_true_hits = []
    for path in paths:
        text = read(path)
        if "Status:** retained" in text or "Status:** proposed_retained" in text:
            retained_hits.append(path.relative_to(ROOT).as_posix())
        for line in text.splitlines():
            if line.strip() == "proposal_allowed: true":
                proposal_true_hits.append(path.relative_to(ROOT).as_posix())
                break
    check("strict/response/backend/projector docs were scanned", len(paths) >= 10, len(paths))
    check("no scanned doc declares retained/proposed-retained status", len(retained_hits) == 0, retained_hits)
    check("no scanned doc declares proposal_allowed true", len(proposal_true_hits) == 0, proposal_true_hits)
    return {
        "doc_count": len(paths),
        "retained_status_hits": retained_hits,
        "proposal_allowed_true_hits": proposal_true_hits,
    }


def part5_firewalls() -> None:
    print("\nPart 5: firewalls and scope")
    text = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed top/W/Z masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in text)

    for forbidden in (
        "This note derives `Y_T`",
        "positive closure is achieved",
        "actual_current_surface_status: retained",
        "actual_current_surface_status: proposed_retained",
        "proposal_allowed: true",
        "the strict top/W pole-row packet is present on this branch",
    ):
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in text)


def main() -> int:
    print("=" * 78)
    print("Y_T STRICT TOP/W POLE-ROW REPOSITORY DISCOVERY NO-GO")
    print("=" * 78)

    deps = part1_anchors()
    named_artifacts = part2_named_artifacts()
    discovery = part3_repository_discovery()
    doc_scan = part4_doc_status_scan()
    part5_firewalls()

    result = {
        "claim_id": "yt_strict_top_w_pole_row_repository_discovery_no_go_note_2026-05-27",
        "generated_by": "scripts/frontier_yt_strict_top_w_pole_row_repository_discovery_no_go.py",
        "actual_current_surface_status": "no-go / current-branch strict-row discovery",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes hidden-existing-certificate shortcut",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The current branch contains strict-response harnesses, candidate "
            "rows, and no-go packets, but no accepted same-surface strict "
            "top/W pole-row certificate with backend authority, isolated W/top "
            "poles, coefficient-certified rows, contact/FV/IR/model-class "
            "controls, and no free top coefficient input."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": (
            "current branch already contains hidden accepted strict top/W "
            "pole-row evidence under another artifact name"
        ),
        "route_still_live": (
            "produce accepted strict pole-row data, or derive the accepted "
            "same-surface backend/projectors/matrix elements"
        ),
        "named_artifacts": named_artifacts,
        "repository_discovery": discovery,
        "doc_status_scan": doc_scan,
        "dependency_status": {
            name: {
                "status": data.get("actual_current_surface_status"),
                "trace_class": data.get("trace_class"),
                "proposal_allowed": data.get("proposal_allowed"),
                "fail_count": data.get("fail_count"),
            }
            for name, data in deps.items()
        },
        "strict_positive_certificate_present": False,
        "complete_strict_packet_count": len(discovery["complete_strict_packets"]),
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
