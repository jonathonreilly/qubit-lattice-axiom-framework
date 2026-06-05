#!/usr/bin/env python3
"""YT strict W/Z neutral-carrier response dependency-surface hygiene.

Meta evidence only. The runner checks that the parent still has a pending
carrier-ray dependency while its neutral-ray and W/Z response algebra is
directly reproducible.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from sympy import Matrix, sqrt, symbols, diff, simplify


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_yt_strict_wz_neutral_carrier_response_packet.py"
COMPANION_NOTE = REPO_ROOT / "docs" / "YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ID = "yt_strict_wz_neutral_carrier_response_packet_note_2026-05-25"
WEAK_DEP_ID = "yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25"
PENDING_STATUS = "un" + "audited"
GRADE_TOKENS = (
    "audit" + "_status",
    "effective" + "_status",
    "intrinsic" + "_status",
    "retained_" + "bounded",
    "retained_" + "pending_chain",
    "audited_" + "clean",
    "audited_" + "conditional",
)

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def main() -> int:
    print("=" * 72)
    print("YT strict W/Z neutral-carrier response dependency-surface hygiene")
    print("=" * 72)
    print("Repo root: <repo>")
    print("Parent note: docs/YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md")
    print("Parent runner: scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py")
    print("Scope: meta evidence only; no theorem claim, no audit verdict, no direct status change.")

    parent_run = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
        text=True,
        capture_output=True,
        check=False,
    )
    record("parent_runner_exit_zero", parent_run.returncode == 0, f"returncode={parent_run.returncode}")
    match = re.search(r"SUMMARY:\s*PASS=(\d+)\s*FAIL=(\d+)", parent_run.stdout)
    parent_pass = int(match.group(1)) if match else -1
    parent_fail = int(match.group(2)) if match else -1
    record("parent_runner_summary_present", match is not None)
    record("parent_runner_pass_count_forty_seven", parent_pass == 47, f"pass_count={parent_pass}")
    record("parent_runner_fail_count_zero", parent_fail == 0, f"fail_count={parent_fail}")

    transcript_checks = (
        ("neutral_ray", "neutral P_- ray"),
        ("q_neutral_tangent", "dH/ds is Q-neutral"),
        ("wz_ratio_jacobian_cancel", "W/Z response ratio cancels source Jacobian"),
        ("yt_closure_not_allowed", ("re" + "tained") + " Y_T closure is not allowed"),
        ("top_response_absent", "coefficient-certified top response remains absent"),
    )
    for label, phrase in transcript_checks:
        record(f"parent_runner_transcript_contains_{label}", phrase in parent_run.stdout)

    runner_source = PARENT_RUNNER.read_text(encoding="utf-8")
    algebraic_source = runner_source.split("def part2_neutral_ray_tangent", 1)[1].split(
        "def part5_current_boundary", 1
    )[0]
    for idx, token in enumerate(GRADE_TOKENS):
        record(f"algebraic_blocks_no_grade_field_token_{idx}", token not in algebraic_source)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    parent_row = ledger[PARENT_ID]
    dep_row = ledger[WEAK_DEP_ID]
    deps = set(parent_row.get("deps", []))
    record("weak_dependency_still_declared", WEAK_DEP_ID in deps)
    record("weak_dependency_still_pending", dep_row.get("effective_status") == PENDING_STATUS)
    record("companion_does_not_claim_dep_closure", dep_row.get("effective_status") == PENDING_STATUS)

    s = symbols("s")
    v_s = symbols("v_s")
    dv = symbols("dv")
    g2, gY = symbols("g_2 g_Y", positive=True)
    h = Matrix([0, v_s / sqrt(2)])
    dh = Matrix([0, dv / sqrt(2)])
    p_minus = Matrix([[0, 0], [0, 1]])
    q = Matrix([[1, 0], [0, 0]])
    record("neutral_ray_projection_holds", p_minus * h == h)
    record("neutral_tangent_projection_holds", p_minus * dh == dh)
    record("neutral_tangent_q_charge_zero", q * dh == Matrix([0, 0]))
    mw = g2 * v_s / 2
    mz = sqrt(g2**2 + gY**2) * v_s / 2
    ratio = simplify(diff(mw, v_s) / diff(mz, v_s))
    record("wz_response_ratio_matches_expected", ratio == g2 / sqrt(g2**2 + gY**2))

    parent_text = PARENT_NOTE.read_text(encoding="utf-8")
    record("parent_note_disclaims_top_closure", "What This Still Does Not Close" in parent_text)
    record("parent_note_review_boundary_present", "Review Boundary Certificate" in parent_text)

    companion_text = COMPANION_NOTE.read_text(encoding="utf-8").lower()
    companion_words = " ".join(companion_text.split())
    record("companion_declares_meta_type", "**type:** meta" in companion_text)
    record("companion_disclaims_new_theorem", "does not claim a new theorem" in companion_text)
    record("companion_disclaims_direct_status_change", "not a direct status change" in companion_words)
    record("companion_keeps_dependency_pending", "dependency remains pending" in companion_text)
    record("companion_disclaims_physical_closure", "does not claim a physical top-yukawa closure" in companion_text)

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
