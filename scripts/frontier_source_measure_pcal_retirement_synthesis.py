#!/usr/bin/env python3
"""Synthesis gate for the source/measure P-cal retirement campaign block."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUTS = ROOT / "outputs"
OUT = OUTPUTS / "source_measure_pcal_retirement_synthesis_2026-05-30.json"

SYNTHESIS = DOCS / "SOURCE_MEASURE_PCAL_RETIREMENT_SYNTHESIS_NOTE_2026-05-30.md"
RN = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
CUMULANT = DOCS / "SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"
TANGENT = DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
YT_TIER_A = DOCS / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"

RN_OUT = OUTPUTS / "source_measure_pcal_rn_cocycle_2026-05-30.json"
CUMULANT_OUT = OUTPUTS / "source_measure_pcal_cumulant_mobius_2026-05-30.json"
TANGENT_OUT = OUTPUTS / "source_measure_sharp_record_tangent_space_2026-05-30.json"

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


def load(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def part1_artifacts() -> dict[str, Any]:
    print("\nPart 1: artifact presence")
    for path in (SYNTHESIS, RN, CUMULANT, TANGENT, YT_TIER_A, RN_OUT, CUMULANT_OUT, TANGENT_OUT):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    return {}


def part2_runner_outputs() -> dict[str, Any]:
    print("\nPart 2: runner outputs")
    outputs = {
        "rn": load(RN_OUT),
        "cumulant": load(CUMULANT_OUT),
        "tangent": load(TANGENT_OUT),
    }
    for name, data in outputs.items():
        summary = data.get("summary", {})
        check(f"{name} runner has zero failures", summary.get("fail") == 0, summary)
        check(f"{name} runner is exact-support", summary.get("actual_current_surface_status") == "exact-support", summary)
        check(f"{name} runner does not allow proposal yet", summary.get("proposal_allowed") is False, summary)
    return {name: data["summary"] for name, data in outputs.items()}


def part3_synthesis_status() -> dict[str, Any]:
    print("\nPart 3: synthesis status boundary")
    text = read(SYNTHESIS)
    for phrase in (
        "What is now closed",
        "What remains",
        "Impact on Y_T",
        "Status boundary",
        "Non-claims",
    ):
        check(f"synthesis contains section/phrase: {phrase}", phrase in text)
    check("synthesis states exact-support", "actual_current_surface_status: exact-support" in text)
    check("synthesis exposes single semantic residual", "physical source is a smooth sharp-record probability intervention" in text)
    check("synthesis forbids bare retained", "bare_retained_allowed: false" in text)
    check("synthesis says not unbounded Y_T closure", "not unbounded retained Y_T closure" in text)
    return {"actual_status": "exact-support", "single_residual": "physical source is a smooth sharp-record probability intervention"}


def part4_firewall() -> None:
    print("\nPart 4: firewall")
    text = read(SYNTHESIS)
    flat = " ".join(text.split())
    for phrase in ("H_unit", "yt_ward_identity", "y_t_bare", "PDG", "alpha_LM", "plaquette", "fitted selector"):
        check(f"forbidden import named: {phrase}", phrase in flat)
    for phrase in ("Status: retained", "audit-clean retained", "unbounded retained Y_T closure is claimed"):
        check(f"forbidden overclaim absent: {phrase}", phrase not in text)


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE P-CAL RETIREMENT SYNTHESIS")
    print("=" * 88)
    result = {
        "artifacts": part1_artifacts(),
        "runner_outputs": part2_runner_outputs(),
        "synthesis": part3_synthesis_status(),
    }
    part4_firewall()
    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "actual_current_surface_status": "exact-support",
        "trace_class": "direct_blocker_closure_candidate",
        "yt_lambda_closed_if_single_residual_accepted": True,
        "remaining_residual": "physical source is a smooth sharp-record probability intervention",
        "proposal_allowed": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
