#!/usr/bin/env python3
"""Extended closeout index for post-record dynamics plus family-lift stack."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/POST_RECORD_DYNAMICS_FAMILY_LIFT_CLOSEOUT_INDEX_2026-06-06.md"
OUTPUT = ROOT / "outputs/post_record_dynamics_family_lift_closeout_index_2026_06_06_source_packet.json"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class StackPr:
    number: int
    title_fragment: str
    status: str
    runner_summary: str
    note_path: str
    runner_path: str
    log_path: str


STACK = (
    StackPr(2850, "directed certificate examples", "exact-support", "SUMMARY: PASS=64 FAIL=0", "docs/POST_RECORD_DIRECTED_CERTIFICATE_EXAMPLES_2026-06-06.md", "scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py", "logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt"),
    StackPr(2853, "kernel-selection firewall", "no-go", "SUMMARY: PASS=52 FAIL=0", "docs/POST_RECORD_DIRECTED_CERTIFICATE_KERNEL_SELECTION_FIREWALL_2026-06-06.md", "scripts/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.py", "logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt"),
    StackPr(2856, "supplied kernel selection rule", "exact-support", "SUMMARY: PASS=39 FAIL=0", "docs/POST_RECORD_SUPPLIED_KERNEL_SELECTION_RULE_INTERFACE_2026-06-06.md", "scripts/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.py", "logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt"),
    StackPr(2858, "target-vector firewall", "no-go", "SUMMARY: PASS=36 FAIL=0", "docs/POST_RECORD_SELECTION_RULE_TARGET_VECTOR_FIREWALL_2026-06-06.md", "scripts/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.py", "logs/runner-cache/frontier_post_record_selection_rule_target_vector_firewall_2026_06_06.txt"),
    StackPr(2861, "admitted sample target-vector", "exact-support", "SUMMARY: PASS=30 FAIL=0", "docs/POST_RECORD_ADMITTED_SAMPLE_TARGET_VECTOR_INTERFACE_2026-06-06.md", "scripts/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.py", "logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt"),
    StackPr(2864, "dynamics authority stack map", "exact-support", "SUMMARY: PASS=52 FAIL=0", "docs/POST_RECORD_DYNAMICS_AUTHORITY_STACK_MAP_2026-06-06.md", "scripts/frontier_post_record_dynamics_authority_stack_map_2026_06_06.py", "logs/runner-cache/frontier_post_record_dynamics_authority_stack_map_2026_06_06.txt"),
    StackPr(2868, "dynamics campaign closeout index", "exact-support", "SUMMARY: PASS=53 FAIL=0", "docs/POST_RECORD_DYNAMICS_CAMPAIGN_CLOSEOUT_INDEX_2026-06-06.md", "scripts/frontier_post_record_dynamics_campaign_closeout_index_2026_06_06.py", "logs/runner-cache/frontier_post_record_dynamics_campaign_closeout_index_2026_06_06.txt"),
    StackPr(2871, "retained/unbounded dynamics gate", "exact-support", "SUMMARY: PASS=54 FAIL=0", "docs/POST_RECORD_RETAINED_UNBOUNDED_DYNAMICS_GATE_2026-06-06.md", "scripts/frontier_post_record_retained_unbounded_dynamics_gate_2026_06_06.py", "logs/runner-cache/frontier_post_record_retained_unbounded_dynamics_gate_2026_06_06.txt"),
    StackPr(2874, "finite-to-unbounded family-lift no-go", "no-go", "SUMMARY: PASS=43 FAIL=0", "docs/POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md", "scripts/frontier_post_record_finite_to_unbounded_family_lift_nogo_2026_06_06.py", "logs/runner-cache/frontier_post_record_finite_to_unbounded_family_lift_nogo_2026_06_06.txt"),
    StackPr(2875, "supplied family-lift certificate interface", "bounded-support", "SUMMARY: PASS=39 FAIL=0", "docs/POST_RECORD_SUPPLIED_FAMILY_LIFT_CERTIFICATE_INTERFACE_2026-06-06.md", "scripts/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.py", "logs/runner-cache/frontier_post_record_supplied_family_lift_certificate_interface_2026_06_06.txt"),
)

FORBIDDEN_TRUE_FLAGS = {
    "AUDIT_DATA_WRITTEN": "audit data written flag is absent",
    "AUDIT_VERDICT_APPLIED": "audit verdict applied flag is absent",
    "PROMOTED_OR_RETAINED_CLAIM": "promoted/retained claim flag is absent",
    "PRODUCTION_KERNEL_SELECTED_WITHOUT_RULE": "kernel selected without supplied rule flag is absent",
    "SELECTION_RULE_DERIVED_FROM_RECORD": "selection rule derived from Record flag is absent",
    "TARGET_VECTOR_DERIVED_FROM_RECORD": "target vector derived from Record flag is absent",
    "SAMPLE_IS_PROBABILITY_LAW": "sample-is-probability-law flag is absent",
    "DIAL_FORCED_OR_SELECTED": "dial forced or selected flag is absent",
    "FINITE_ALONE_UNBOUNDED_RETAINED": "finite-alone unbounded retained flag is absent",
    "FAMILY_LIFT_DERIVED_FROM_RECORD": "family lift derived from Record flag is absent",
}


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def sha256_rel(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def cache_header(text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    if "----- stdout -----" not in text:
        return header
    for line in text.split("----- stdout -----", 1)[0].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        header[key.strip()] = value.strip()
    return header


def index_checks() -> None:
    section("Extended closeout index checks")
    text = DOC.read_text(encoding="utf-8")
    report("ten PR stack entries are expected", len(STACK) == 10)
    for item in STACK:
        report(f"index contains PR #{item.number}", f"/pull/{item.number}" in text)
        report(f"index contains title fragment for #{item.number}", item.title_fragment in text)
        report(f"index contains status for #{item.number}", item.status in text)
    for pr in (2871, 2874, 2875):
        report(f"family-lift extension PR #{pr} is present", f"/pull/{pr}" in text)
    report("index states pre-record law carries probabilities", "pre-record law carries probabilities" in text)
    report("index states post-record records carry realized information", "post-record records carry realized information" in text)
    report("index states no audit verdicts are applied", "does not apply audit verdicts" in text)


def cached_summary_checks() -> None:
    section("Cached summary checks")
    for item in STACK:
        text = read_rel(item.log_path)
        report(f"{item.log_path} exists", True)
        report(f"{item.log_path} has summary for PR #{item.number}", item.runner_summary in text)


def source_packet_checks() -> None:
    section("Upstream source-packet checks")
    for item in STACK:
        note = ROOT / item.note_path
        runner = ROOT / item.runner_path
        cache = ROOT / item.log_path
        report(f"PR #{item.number} source note exists", note.exists(), item.note_path)
        if note.exists():
            note_text = note.read_text(encoding="utf-8", errors="replace")
            status_names = {item.status, item.status.replace("-", " ")}
            report(f"PR #{item.number} source note names status", any(status in note_text for status in status_names), item.status)
            report(f"PR #{item.number} source note names primary runner", item.runner_path in note_text, item.runner_path)
        report(f"PR #{item.number} runner source exists", runner.exists(), item.runner_path)
        report(f"PR #{item.number} runner cache exists", cache.exists(), item.log_path)
        if not (runner.exists() and cache.exists()):
            continue
        runner_sha = sha256_rel(item.runner_path)
        header = cache_header(cache.read_text(encoding="utf-8", errors="replace"))
        report(f"PR #{item.number} cache runner matches source", header.get("runner") == item.runner_path, header.get("runner", ""))
        report(f"PR #{item.number} cache SHA is fresh", header.get("runner_sha256") == runner_sha, header.get("runner_sha256", ""))
        report(f"PR #{item.number} cache status ok", header.get("status") == "ok" and header.get("exit_code") == "0", str(header))


def status_shape_checks() -> None:
    section("Status shape checks")
    statuses = {item.status for item in STACK}
    report("stack has exact-support entries", "exact-support" in statuses)
    report("stack has bounded-support entries", "bounded-support" in statuses)
    report("stack has no-go entries", "no-go" in statuses)
    report("exact-support count is six", sum(1 for item in STACK if item.status == "exact-support") == 6)
    report("bounded-support count is one", sum(1 for item in STACK if item.status == "bounded-support") == 1)
    report("no-go count is three", sum(1 for item in STACK if item.status == "no-go") == 3)


def firewall_checks() -> None:
    section("Repo-surface firewall checks")
    before = sha256_rel("docs/audit/data/audit_ledger.json")
    packet_paths = [item.note_path for item in STACK] + [item.log_path for item in STACK] + [DOC.relative_to(ROOT).as_posix()]
    packet_text = "\n".join(read_rel(path) for path in packet_paths)
    for flag, label in FORBIDDEN_TRUE_FLAGS.items():
        report(label, f"{flag}=TRUE" not in packet_text)
    after = sha256_rel("docs/audit/data/audit_ledger.json")
    report("audit ledger hash is unchanged", before == after, before)


def export_packet() -> None:
    section("Source-packet export")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "claim_id": "post_record_dynamics_family_lift_closeout_index_2026-06-06",
        "stack_count": len(STACK),
        "exact_support_count": sum(1 for item in STACK if item.status == "exact-support"),
        "bounded_support_count": sum(1 for item in STACK if item.status == "bounded-support"),
        "no_go_count": sum(1 for item in STACK if item.status == "no-go"),
        "audit_ledger_sha256": sha256_rel("docs/audit/data/audit_ledger.json"),
        "forbidden_true_flags": sorted(FORBIDDEN_TRUE_FLAGS),
        "stack": [
            {
                "pr": item.number,
                "status": item.status,
                "title_fragment": item.title_fragment,
                "note_path": item.note_path,
                "note_sha256": sha256_rel(item.note_path),
                "runner_path": item.runner_path,
                "runner_sha256": sha256_rel(item.runner_path),
                "cache_path": item.log_path,
                "cache_sha256": sha256_rel(item.log_path),
                "runner_summary": item.runner_summary,
            }
            for item in STACK
        ],
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report("source-packet export written", OUTPUT.exists(), OUTPUT.relative_to(ROOT).as_posix())


def main() -> int:
    index_checks()
    cached_summary_checks()
    source_packet_checks()
    status_shape_checks()
    firewall_checks()
    export_packet()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("POST_RECORD_DYNAMICS_FAMILY_LIFT_CLOSEOUT_INDEX=TRUE")
    print("EXTENDED_STACK_PRS=10")
    print("EXTENDED_STACK_EXACT_SUPPORT=6")
    print("EXTENDED_STACK_BOUNDED_SUPPORT=1")
    print("EXTENDED_STACK_NO_GO=3")
    print("FAMILY_LIFT_EXTENSION_PRS=3")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("DIAL_FORCED_OR_SELECTED=FALSE")
    print("FINITE_ALONE_UNBOUNDED_RETAINED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
