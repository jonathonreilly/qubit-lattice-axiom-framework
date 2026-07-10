#!/usr/bin/env python3
"""Class-A certificate over retained inputs for the seed-0 synthesis.

The two family control computations are retained-grade inputs. This runner
performs class-B dependency/provenance verification, parses the frozen source
outputs, and then checks the class-A finite sign/order implication. It
deliberately has no expected direct-dM magnitudes or expected R_hist values.
"""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from statistics import mean


AUDIT_TIMEOUT_SEC = 60
ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "docs/audit/data/audit_ledger.json"
SELECTED_STRENGTH = 0.004
EXPECTED_STRENGTHS = {0.0, 0.002, 0.004, 0.008}
RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}


HEADER_RE = re.compile(
    r"family=(?P<family>Fam[0-9]+)\s+.*\bseed=(?P<seed>[0-9]+)\s+H=(?P<h>[0-9.]+)"
)
STRENGTH_RE = re.compile(r"^\[strength=(?P<strength>[0-9.]+)\]")
VALUE_RE = re.compile(
    r"^\s+(?P<key>dM\(early\)|dM\(late\)|delta_hist|R_hist|delta_hist/s)"
    r"\s*=\s*(?P<value>[-+0-9.eE]+%?)"
)
NULL_RE = re.compile(r"null max \|delta_hist\| = (?P<value>[-+0-9.eE]+)")
SIGN_RE = re.compile(
    r"(?:sign pattern\(nonzero strengths\)|delta_hist sign pattern)\s*=\s*(?P<value>[+\- ]+)"
)
SPREAD_RE = re.compile(r"\|delta_hist/s\| spread\s*=\s*(?P<value>[-+0-9.]+)%")


@dataclass(frozen=True)
class SourceSpec:
    family: str
    claim_id: str
    note_path: str
    runner_path: str
    log_path: str


SOURCES = (
    SourceSpec(
        family="Fam1",
        claim_id="wave_direct_dm_h025_fam1_seed0_control_note",
        note_path="docs/WAVE_DIRECT_DM_H025_FAM1_SEED0_CONTROL_NOTE.md",
        runner_path="scripts/wave_direct_dm_h025_fam1_seed0_control_batch.py",
        log_path="logs/2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt",
    ),
    SourceSpec(
        family="Fam2",
        claim_id="wave_direct_dm_h025_fam2_seed0_control_note",
        note_path="docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md",
        runner_path="scripts/wave_direct_dm_h025_fam2_seed0_control_batch.py",
        log_path="logs/2026-04-08-wave-direct-dm-h025-control-fam2-seed0.txt",
    ),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_number(text: str) -> float:
    return float(text.rstrip("%"))


def ledger_rows() -> dict[str, dict[str, object]]:
    data = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = data["rows"]
    require(isinstance(rows, dict), "audit ledger rows must be keyed by claim_id")
    return rows


def check_dependency(spec: SourceSpec, rows: dict[str, dict[str, object]]) -> None:
    require(spec.claim_id in rows, f"missing audit-ledger dependency {spec.claim_id}")
    row = rows[spec.claim_id]
    require(
        row.get("effective_status") in RETAINED_GRADE,
        f"{spec.claim_id}: dependency is not retained-grade",
    )
    require(row.get("chain_closes") is True, f"{spec.claim_id}: dependency chain does not close")

    note = (ROOT / spec.note_path).read_text(encoding="utf-8")
    require(spec.runner_path in note, f"{spec.claim_id}: source runner not registered in source note")
    require(spec.log_path in note, f"{spec.claim_id}: frozen log not registered in source note")
    require((ROOT / spec.runner_path).is_file(), f"{spec.claim_id}: source runner is missing")
    require((ROOT / spec.log_path).is_file(), f"{spec.claim_id}: frozen log is missing")


def parse_log(spec: SourceSpec) -> dict[str, object]:
    path = ROOT / spec.log_path
    parsed: dict[str, object] = {"rows": {}}
    rows = parsed["rows"]
    assert isinstance(rows, dict)
    current_strength: float | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if match := HEADER_RE.search(line):
            parsed["family"] = match.group("family")
            parsed["seed"] = int(match.group("seed"))
            parsed["h"] = float(match.group("h"))
            continue
        if match := STRENGTH_RE.match(line):
            current_strength = float(match.group("strength"))
            rows[current_strength] = {}
            continue
        if match := VALUE_RE.match(line):
            require(current_strength is not None, f"{spec.family}: value before strength block")
            rows[current_strength][match.group("key")] = parse_number(match.group("value"))
            continue
        if match := NULL_RE.search(line):
            parsed["null_max"] = float(match.group("value"))
            continue
        if match := SIGN_RE.search(line):
            parsed["sign_pattern"] = " ".join(match.group("value").split())
            continue
        if match := SPREAD_RE.search(line):
            parsed["reported_spread_percent"] = float(match.group("value"))

    required = {
        "family",
        "seed",
        "h",
        "null_max",
        "sign_pattern",
        "reported_spread_percent",
    }
    require(required.issubset(parsed), f"{spec.family}: incomplete source transcript")
    require(parsed["family"] == spec.family, f"{spec.family}: family label mismatch")
    require(parsed["seed"] == 0, f"{spec.family}: source is not seed 0")
    require(
        math.isclose(float(parsed["h"]), 0.25, rel_tol=0.0, abs_tol=5e-13),
        f"{spec.family}: source is not H=0.25",
    )
    require(set(rows) == EXPECTED_STRENGTHS, f"{spec.family}: incomplete strength ladder")

    for strength, row in rows.items():
        needed = {"dM(early)", "dM(late)", "delta_hist", "R_hist"}
        if strength > 0:
            needed.add("delta_hist/s")
        require(needed.issubset(row), f"{spec.family}: incomplete row at S={strength}")

    null_delta = rows[0.0]["delta_hist"]
    require(
        math.isclose(null_delta, 0.0, rel_tol=0.0, abs_tol=0.0),
        f"{spec.family}: nonzero S=0 delta_hist",
    )
    require(
        math.isclose(float(parsed["null_max"]), 0.0, rel_tol=0.0, abs_tol=0.0),
        f"{spec.family}: nonzero null summary",
    )

    nonzero = [rows[s] for s in sorted(EXPECTED_STRENGTHS) if s > 0]
    require(all(row["delta_hist"] < 0 for row in nonzero), f"{spec.family}: sign control failed")
    require(parsed["sign_pattern"] == "- - -", f"{spec.family}: sign summary failed")

    scaled = [abs(row["delta_hist/s"]) for row in nonzero]
    computed_spread = (max(scaled) - min(scaled)) / mean(scaled) * 100.0
    reported_spread = float(parsed["reported_spread_percent"])
    require(
        math.isclose(computed_spread, reported_spread, rel_tol=0.0, abs_tol=0.005),
        f"{spec.family}: spread summary does not follow from parsed ladder",
    )
    parsed["computed_spread_percent"] = computed_spread
    return parsed


def main() -> int:
    audit_rows = ledger_rows()
    for spec in SOURCES:
        check_dependency(spec, audit_rows)

    parsed = {spec.family: parse_log(spec) for spec in SOURCES}
    fam1 = parsed["Fam1"]["rows"][SELECTED_STRENGTH]  # type: ignore[index]
    fam2 = parsed["Fam2"]["rows"][SELECTED_STRENGTH]  # type: ignore[index]

    require(fam1["delta_hist"] < 0 and fam2["delta_hist"] < 0, "shared sign failed")
    require(
        abs(fam2["delta_hist"]) > abs(fam1["delta_hist"]),
        "Fam2 is not deeper in |delta_hist|",
    )
    require(fam2["R_hist"] < fam1["R_hist"] < 0, "Fam2 is not deeper in R_hist")

    print("WAVE_DIRECT_DM_H025_SEED0_CROSSFAMILY_ASSERTIONS=TRUE")
    print("WAVE_DIRECT_DM_H025_SEED0_DEPENDENCIES_RETAINED_GRADE=TRUE")
    print("WAVE_DIRECT_DM_H025_SEED0_DEPENDENCY_CLASS=B_CROSS_NOTE_INPUT_VERIFICATION")
    print("WAVE_DIRECT_DM_H025_SEED0_LOAD_BEARING_CLASS=A_ALGEBRAIC_INEQUALITY_CLOSURE")
    for family in ("Fam1", "Fam2"):
        row = parsed[family]["rows"][SELECTED_STRENGTH]  # type: ignore[index]
        spread = parsed[family]["computed_spread_percent"]
        dependency_status = audit_rows[
            next(spec.claim_id for spec in SOURCES if spec.family == family)
        ]["effective_status"]
        print(
            f"{family}: dependency_status={dependency_status} "
            f"delta_hist={row['delta_hist']:+.6f} "
            f"R_hist={row['R_hist']:+.2f}% spread={spread:.2f}%"
        )
    print("WAVE_DIRECT_DM_H025_SEED0_SHARED_SIGN=negative")
    print("WAVE_DIRECT_DM_H025_SEED0_COMMON_ORDERING=Fam2_deeper_than_Fam1_at_strength_0.004")
    print("WAVE_DIRECT_DM_H025_SEED0_WEAK_FIELD_CONTROL=TRUE")
    print("WAVE_DIRECT_DM_H025_SEED0_PORTABILITY_LAW=FALSE")
    print("WAVE_DIRECT_DM_H025_STABLE_AMPLITUDE_LAW=FALSE")
    print("RESIDUAL_SCOPE=fam3_family_wide_portability_and_structural_magnitude_law_not_claimed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
