#!/usr/bin/env python3
"""Origin/main declared-anchor Y_T subchain firewall for this campaign."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUTS = ROOT / "outputs"
NOTE = DOCS / "YT_ORIGIN_MAIN_DECLARED_ANCHOR_FIREWALL_NO_GO_NOTE_2026-05-28.md"
OUTPUT = OUTPUTS / "yt_origin_main_declared_anchor_firewall_no_go_2026-05-28.json"
REMOTE_REF = "origin/main"

DECLARED_NOTE = "docs/YT_DECLARED_ANCHOR_BOUNDED_SUBCHAIN_NARROW_THEOREM_NOTE_2026-05-26.md"
ZERO_IMPORT_NOTE = "docs/YT_ZERO_IMPORT_CHAIN_NOTE.md"
DECLARED_RUNNER = "scripts/frontier_yt_declared_anchor_bounded_subchain.py"
LEDGER = "docs/audit/data/audit_ledger.json"

FORBIDDEN_PROOF_INPUTS = (
    "<P>",
    "plaquette",
    "u_0",
    "alpha_LM",
    "Ward Clebsch",
    "Ward-boundary",
    "kappa_EW",
    "observed",
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


def run_git(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {completed.stderr.strip()}")
    return completed.stdout


def git_blob(path: str) -> str:
    return run_git(["show", f"{REMOTE_REF}:{path}"])


def git_json(path: str) -> dict[str, Any]:
    return json.loads(git_blob(path))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(ledger: dict[str, Any], claim_id: str) -> dict[str, Any]:
    rows = ledger["rows"]
    row = rows.get(claim_id) if isinstance(rows, dict) else None
    if row is not None:
        return row
    iterable = rows.values() if isinstance(rows, dict) else rows
    for candidate in iterable:
        if candidate.get("claim_id") == claim_id:
            return candidate
    raise KeyError(claim_id)


def part1_note_and_remote() -> dict[str, Any]:
    print("\nPart 1: local note and origin/main artifacts")
    check(f"{NOTE.relative_to(ROOT)} exists", NOTE.exists())
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
        "actual_current_surface_status: no-go / forbidden declared-anchor remote subchain",
        "proposal_allowed: false",
        "declared-anchor bounded subchain cannot be used as a proof input",
        "forbidden campaign inputs",
    ):
        check(f"note contains phrase: {phrase}", phrase in note_one_line)

    remote_hash = run_git(["rev-parse", REMOTE_REF]).strip()
    declared = git_blob(DECLARED_NOTE)
    zero_import = git_blob(ZERO_IMPORT_NOTE)
    runner = git_blob(DECLARED_RUNNER)
    ledger = git_json(LEDGER)
    check("origin/main ref is available", len(remote_hash) == 40, remote_hash)
    check("declared-anchor note loaded", "YT Declared-Anchor Bounded Subchain" in declared)
    check("zero-import note loaded", "Zero-Import y_t Derivation" in zero_import)
    check("declared-anchor runner loaded", "Bounded declared-anchor y_t algebraic subchain" in runner)
    return {
        "origin_main_commit": remote_hash,
        "declared_note": declared,
        "zero_import_note": zero_import,
        "declared_runner": runner,
        "ledger": ledger,
    }


def part2_forbidden_inputs(artifacts: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 2: forbidden-input firewall")
    combined = "\n".join(
        (
            artifacts["declared_note"],
            artifacts["zero_import_note"],
            artifacts["declared_runner"],
        )
    )
    present = {token: token in combined for token in FORBIDDEN_PROOF_INPUTS}
    for token, found in present.items():
        check(f"origin/main declared-anchor surface mentions {token}", found)
    check("plaquette/u0 appears as declared anchor", present["plaquette"] and present["u_0"])
    check("alpha_LM appears as declared anchor", present["alpha_LM"])
    check("Ward boundary/Clebsch appears as declared anchor", present["Ward Clebsch"] or present["Ward-boundary"])
    check("kappa_EW appears as declared anchor", present["kappa_EW"])
    return present


def part3_audit_scope(artifacts: dict[str, Any]) -> dict[str, Any]:
    print("\nPart 3: origin/main audit scope")
    ledger = artifacts["ledger"]
    declared = ledger_row(ledger, "yt_declared_anchor_bounded_subchain_narrow_theorem_note_2026-05-26")
    zero_import = ledger_row(ledger, "yt_zero_import_chain_note")
    check("declared-anchor row is retained_bounded", declared.get("effective_status") == "retained_bounded", declared.get("effective_status"))
    check("declared-anchor row is over declared anchors", "declared" in declared.get("claim_scope", "").lower())
    declared_scope = declared.get("claim_scope", "").lower()
    declared_rationale = declared.get("verdict_rationale", "").lower()
    check(
        "declared-anchor row does not derive anchors",
        "no anchor derivation" in declared_scope
        or "do not claim to derive" in declared_rationale,
        declared.get("claim_scope"),
    )
    check("zero-import row is decoration", str(zero_import.get("effective_status", "")).startswith("decoration"), zero_import.get("effective_status"))
    open_deps = zero_import.get("open_dependency_paths", [])
    check("zero-import row keeps plaquette dependency open", any("PLAQUETTE" in dep or "plaquette" in dep for dep in open_deps), open_deps)
    check("zero-import row keeps kappa_EW/selector dependency open", "kappa" in zero_import.get("notes_for_re_audit_if_any", ""), zero_import.get("notes_for_re_audit_if_any"))
    return {
        "declared_effective_status": declared.get("effective_status"),
        "zero_import_effective_status": zero_import.get("effective_status"),
        "zero_import_open_dependency_paths": open_deps,
    }


def part4_scope_and_firewalls() -> None:
    print("\nPart 4: scope and overclaim firewalls")
    note = read(NOTE)
    one_line = " ".join(note.split()).lower()
    for phrase in (
        "prunes only the shortcut",
        "does not challenge the retained-bounded audit status",
        "does not use plaquette, alpha_LM, Ward, kappa_EW, or observed values as proof inputs",
        "strict top/W pole rows remain live",
    ):
        check(f"scope phrase present: {phrase}", phrase.lower() in one_line)
    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "positive Y_T closure is obtained",
        "full Y_T closure",
        "declared anchors are admissible proof inputs",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T ORIGIN/MAIN DECLARED-ANCHOR FIREWALL NO-GO")
    print("=" * 78)
    artifacts = part1_note_and_remote()
    forbidden_inputs = part2_forbidden_inputs(artifacts)
    audit_scope = part3_audit_scope(artifacts)
    part4_scope_and_firewalls()

    result = {
        "actual_current_surface_status": "no-go / forbidden declared-anchor remote subchain",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "prunes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The origin/main declared-anchor Y_T bounded subchain is explicitly "
            "retained-bounded only over declared plaquette/u0/alpha_LM, kappa_EW, "
            "and Ward-boundary/Clebsch inputs. Those are forbidden or open inputs "
            "for this campaign, so the remote packet cannot be imported as a "
            "positive-closure proof input."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": "use origin/main declared-anchor Y_T bounded subchain as current campaign closure proof",
        "route_still_live": (
            "derive allowed same-surface radial/readout/backend laws without forbidden anchors, "
            "or produce accepted strict top/W pole rows"
        ),
        "origin_main_commit": artifacts["origin_main_commit"],
        "forbidden_inputs_present": forbidden_inputs,
        "origin_main_audit_scope": audit_scope,
        "review_surface": [
            NOTE.relative_to(ROOT).as_posix(),
            Path(__file__).relative_to(ROOT).as_posix(),
            OUTPUT.relative_to(ROOT).as_posix(),
            f"{REMOTE_REF}:{DECLARED_NOTE}",
            f"{REMOTE_REF}:{ZERO_IMPORT_NOTE}",
        ],
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
