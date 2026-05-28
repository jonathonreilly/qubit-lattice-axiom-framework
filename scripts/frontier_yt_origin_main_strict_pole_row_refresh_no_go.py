#!/usr/bin/env python3
"""Origin/main refresh audit for strict Y_T top/W pole rows."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUTS = ROOT / "outputs"
NOTE = DOCS / "YT_ORIGIN_MAIN_STRICT_POLE_ROW_REFRESH_NO_GO_NOTE_2026-05-28.md"
OUTPUT = OUTPUTS / "yt_origin_main_strict_pole_row_refresh_no_go_2026-05-28.json"
REMOTE_REF = "origin/main"

CURRENT_REPOSITORY_DISCOVERY = (
    OUTPUTS / "yt_strict_top_w_pole_row_repository_discovery_no_go_2026-05-27.json"
)
CURRENT_STRICT_AVAILABILITY = (
    OUTPUTS / "yt_strict_sparse_top_w_pole_response_availability_audit_2026-05-27.json"
)
FULL_STACK = OUTPUTS / "yt_full_closure_stack_and_strict_pole_response_contract_2026-05-26.json"

NAMED_STRICT_ROW_OUTPUTS = (
    "outputs/yt_fh_top_w_strict_response_rows_2026-05-25.json",
    "outputs/yt_source_action_block508_id_source_higgs_strict_rows_2026-05-22.json",
)
ORIGIN_KNOWN_BLOCKER_OUTPUTS = (
    "outputs/yt_fh_top_w_response_ratio_gate_2026-05-25.json",
    "outputs/yt_fh_top_mass_response_physical_intervention_bridge_2026-05-25.json",
)
DISCOVERY_KEYWORDS = (
    "strict",
    "response",
    "top",
    "top_w",
    "pole",
    "source",
    "higgs",
    "wz",
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
FV_KEYS = (
    "finite_volume_ir_controls_pass",
    "fv_ir_controls_pass",
    "FV_IR_model_class_checks_pass",
)
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


def run_git(args: list[str], *, allow_fail: bool = False) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0 and not allow_fail:
        raise RuntimeError(
            f"git {' '.join(args)} failed: {completed.stderr.strip()}"
        )
    return completed


def git_blob(ref: str, path: str) -> str:
    return run_git(["show", f"{ref}:{path}"]).stdout


def git_json(ref: str, path: str) -> dict[str, Any]:
    return json.loads(git_blob(ref, path))


def git_path_exists(ref: str, path: str) -> bool:
    return run_git(["cat-file", "-e", f"{ref}:{path}"], allow_fail=True).returncode == 0


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
        for index, value in enumerate(obj):
            rows.extend(iter_key_values(value, f"{prefix}[{index}]"))
    return rows


def truthy_paths(data: dict[str, Any], keys: tuple[str, ...]) -> list[str]:
    return [
        path
        for path, value in iter_key_values(data)
        if path.split(".")[-1] in keys and value is True
    ]


def any_truthy(data: dict[str, Any], keys: tuple[str, ...]) -> bool:
    return bool(truthy_paths(data, keys))


def complete_strict_packet(data: dict[str, Any]) -> bool:
    return (
        any_truthy(data, POSITIVE_FLAG_KEYS)
        and any_truthy(data, BACKEND_KEYS)
        and any_truthy(data, TOP_POLE_KEYS)
        and any_truthy(data, W_POLE_KEYS)
        and any_truthy(data, TOP_ROW_KEYS)
        and any_truthy(data, W_ROW_KEYS)
        and any_truthy(data, CONTACT_KEYS)
        and any_truthy(data, FV_KEYS)
        and any_truthy(data, MODEL_KEYS)
        and not any_truthy(data, FREE_COEFF_KEYS)
        and data.get("proposal_allowed") is True
    )


def origin_candidate_paths() -> list[str]:
    listing = run_git(["ls-tree", "-r", "--name-only", REMOTE_REF, "outputs"]).stdout
    paths: list[str] = []
    for raw in listing.splitlines():
        path = raw.strip()
        name = Path(path).name.lower()
        if path.startswith("outputs/yt_") and name.endswith(".json"):
            if any(keyword in name for keyword in DISCOVERY_KEYWORDS):
                paths.append(path)
    return sorted(paths)


def summarize_candidate(path: str) -> dict[str, Any]:
    data = git_json(REMOTE_REF, path)
    return {
        "path": path,
        "fail_count": data.get("fail_count"),
        "status": data.get("status") or data.get("actual_current_surface_status"),
        "proposal_allowed": data.get("proposal_allowed"),
        "positive_flag_true_paths": truthy_paths(data, POSITIVE_FLAG_KEYS),
        "backend_true_paths": truthy_paths(data, BACKEND_KEYS),
        "top_pole_true_paths": truthy_paths(data, TOP_POLE_KEYS),
        "w_pole_true_paths": truthy_paths(data, W_POLE_KEYS),
        "top_row_true_paths": truthy_paths(data, TOP_ROW_KEYS),
        "w_row_true_paths": truthy_paths(data, W_ROW_KEYS),
        "contact_true_paths": truthy_paths(data, CONTACT_KEYS),
        "fv_true_paths": truthy_paths(data, FV_KEYS),
        "model_true_paths": truthy_paths(data, MODEL_KEYS),
        "free_coefficient_true_paths": truthy_paths(data, FREE_COEFF_KEYS),
        "complete_strict_packet": complete_strict_packet(data),
    }


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: note, local anchors, and remote ref")
    for path in (NOTE, CURRENT_REPOSITORY_DISCOVERY, CURRENT_STRICT_AVAILABILITY, FULL_STACK):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_one_line = " ".join(note.split())
    for section in (
        "Question",
        "Answer",
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
        "actual_current_surface_status: no-go / origin-main strict-row refresh",
        "proposal_allowed: false",
        "origin/main does not supply an accepted strict top/W pole-row packet",
        "current-branch discovery no-go remains consistent",
    ):
        check(f"note contains phrase: {phrase}", phrase in note_one_line)

    remote_hash = run_git(["rev-parse", REMOTE_REF]).stdout.strip()
    current_discovery = load_json(CURRENT_REPOSITORY_DISCOVERY)
    current_availability = load_json(CURRENT_STRICT_AVAILABILITY)
    full_stack = load_json(FULL_STACK)
    check("origin/main ref is available", len(remote_hash) == 40, remote_hash)
    check("current branch strict discovery passed", current_discovery.get("fail_count") == 0)
    check("current branch strict availability passed", current_availability.get("fail_count") == 0)
    check("full stack runner was clean before refresh", full_stack.get("fail_count") == 0)
    check("current discovery proposal is false", current_discovery.get("proposal_allowed") is False)
    return {
        "origin_main_commit": remote_hash,
        "current_discovery": current_discovery,
        "current_availability": current_availability,
        "full_stack": full_stack,
    }


def part2_named_strict_rows() -> dict[str, Any]:
    print("\nPart 2: named strict row outputs")
    remote_absence: dict[str, bool] = {}
    current_absence: dict[str, bool] = {}
    for rel in NAMED_STRICT_ROW_OUTPUTS:
        remote_absence[rel] = not git_path_exists(REMOTE_REF, rel)
        current_absence[rel] = not (ROOT / rel).exists()
        check(f"{rel} absent on origin/main", remote_absence[rel])
        check(f"{rel} absent on current branch", current_absence[rel])
    return {
        "remote_absence": remote_absence,
        "current_absence": current_absence,
    }


def part3_origin_main_candidate_scan() -> dict[str, Any]:
    print("\nPart 3: origin/main Y_T candidate scan")
    paths = origin_candidate_paths()
    summaries = [summarize_candidate(path) for path in paths]
    complete = [row for row in summaries if row["complete_strict_packet"]]
    positive_flags = [row for row in summaries if row["positive_flag_true_paths"]]
    free_coeff = [row for row in summaries if row["free_coefficient_true_paths"]]
    check("origin/main Y_T candidate outputs were scanned", len(summaries) >= 10, len(summaries))
    check("no complete strict top/W packet on origin/main", len(complete) == 0, complete)
    check("positive strict flags do not complete certificate", len(complete) == 0 and len(positive_flags) == 0, positive_flags)
    check("free-coefficient taint is not hidden by complete packet", len(complete) == 0 or not free_coeff, free_coeff)
    return {
        "candidate_count": len(summaries),
        "complete_packet_count": len(complete),
        "positive_flag_candidate_count": len(positive_flags),
        "free_coefficient_candidate_count": len(free_coeff),
        "candidate_summaries": summaries,
    }


def part4_origin_main_known_blockers() -> dict[str, Any]:
    print("\nPart 4: known origin/main blocker outputs")
    fh_gate = git_json(REMOTE_REF, ORIGIN_KNOWN_BLOCKER_OUTPUTS[0])
    top_bridge = git_json(REMOTE_REF, ORIGIN_KNOWN_BLOCKER_OUTPUTS[1])
    check("origin/main FH response-ratio gate passed", fh_gate.get("fail_count") == 0)
    check(
        "origin/main FH gate marks strict top/W rows absent",
        fh_gate.get("current_blockers", {}).get("strict_top_w_rows_present") is False,
    )
    check("origin/main FH gate proposal is false", fh_gate.get("proposal_allowed") is False)
    check(
        "origin/main FH gate names coefficient-certified top rows absent",
        "coefficient-certified top FH rows are absent"
        in fh_gate.get("proposal_allowed_reason", ""),
    )
    check("origin/main top-mass bridge passed", top_bridge.get("fail_count") == 0)
    check(
        "origin/main top-mass bridge lacks strict measurement",
        top_bridge.get("boundary", {}).get("strict_same_source_response_measurement_present")
        is False,
    )
    check("origin/main top-mass bridge proposal is false", top_bridge.get("proposal_allowed") is False)
    return {
        "fh_gate": fh_gate,
        "top_mass_bridge": top_bridge,
    }


def part5_scope_and_firewalls() -> None:
    print("\nPart 5: scope and firewalls")
    note = read(NOTE)
    one_line = " ".join(note.split())
    for phrase in (
        "prunes only the remote-refresh shortcut",
        "does not prove no future strict top/W pole-row computation can succeed",
        "strict route remains live",
        "same-source backend authority",
        "contact, FV/IR, and model-class controls",
    ):
        check(f"scope phrase present: {phrase}", phrase in one_line)

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
        "fitted selectors",
        "target value insertion",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "positive Y_T closure is obtained",
        "full Y_T closure",
        "strict top/W pole-row packet is present",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T ORIGIN/MAIN STRICT POLE-ROW REFRESH NO-GO")
    print("=" * 78)

    anchors = part1_anchors()
    named_rows = part2_named_strict_rows()
    candidate_scan = part3_origin_main_candidate_scan()
    known_blockers = part4_origin_main_known_blockers()
    part5_scope_and_firewalls()

    result = {
        "actual_current_surface_status": "no-go / origin-main strict-row refresh",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "A post-fetch origin/main scan finds no accepted same-surface "
            "strict top/W pole-row packet. The named strict row outputs are "
            "absent, current origin/main Y_T outputs keep strict rows blocked, "
            "and no scanned origin/main candidate output satisfies backend, "
            "W/top pole isolation, coefficient-row, contact/FV/IR, model-class, "
            "no-free-coefficient, and proposal gates."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": "origin/main already supplies accepted strict top/W pole-row evidence",
        "route_still_live": (
            "produce new accepted strict top/W pole rows with contact/FV/IR/model-class "
            "controls, or derive accepted same-surface backend/projectors/matrix elements"
        ),
        "origin_main_commit": anchors["origin_main_commit"],
        "named_strict_rows": named_rows,
        "origin_main_candidate_scan": candidate_scan,
        "origin_main_known_blockers": {
            "fh_gate_strict_top_w_rows_present": known_blockers["fh_gate"]
            .get("current_blockers", {})
            .get("strict_top_w_rows_present"),
            "top_mass_bridge_strict_measurement_present": known_blockers[
                "top_mass_bridge"
            ]
            .get("boundary", {})
            .get("strict_same_source_response_measurement_present"),
        },
        "review_surface": [
            NOTE.relative_to(ROOT).as_posix(),
            Path(__file__).relative_to(ROOT).as_posix(),
            OUTPUT.relative_to(ROOT).as_posix(),
            "origin/main:outputs/yt_fh_top_w_response_ratio_gate_2026-05-25.json",
            "origin/main:outputs/yt_fh_top_mass_response_physical_intervention_bridge_2026-05-25.json",
        ],
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
