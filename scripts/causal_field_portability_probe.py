#!/usr/bin/env python3
"""Fast certificate for the cached causal-field portability probe."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/CAUSAL_FIELD_PORTABILITY_NOTE.md"
CACHE = REPO_ROOT / "logs/runner-cache/causal_field_portability_probe.txt"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "causal_field_portability_note"
RUNNER_PATH = "scripts/causal_field_portability_probe.py"

PASS_COUNT = 0
FAIL_COUNT = 0

EXPECTED_ROWS = {
    "center grown family": {
        "inst": 2.921e-07,
        "forward": 1.951e-07,
        "fwd_ratio": 0.668,
        "dyn1_ratio": 1.456,
        "dyn05_ratio": 0.938,
        "dyn1_delta": 4.253e-07,
        "dyn05_delta": 2.741e-07,
    },
    "portable family 2": {
        "inst": 4.802e-07,
        "forward": 1.758e-07,
        "fwd_ratio": 0.366,
        "dyn1_ratio": 0.732,
        "dyn05_ratio": 0.728,
        "dyn1_delta": 3.517e-07,
        "dyn05_delta": 3.496e-07,
    },
    "portable family 3": {
        "inst": 1.927e-07,
        "forward": 1.522e-07,
        "fwd_ratio": 0.790,
        "dyn1_ratio": 1.623,
        "dyn05_ratio": 1.080,
        "dyn1_delta": 3.128e-07,
        "dyn05_delta": 2.081e-07,
    },
}


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def close(actual: float, expected: float, tol: float = 5e-11) -> bool:
    return abs(actual - expected) <= tol


def note_boundary_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "Claim type:** bounded_theorem",
        "Status:** bounded cached-output certificate",
        "not a cross-family portability theorem",
        "diagnosed family boundary",
        "does not claim",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in text)

    forbidden = [
        "retained framework-operator carrier",
        "audited_conditional",
        "Admitted-context inputs",
        "EVOLVING_NETWORK_PROTOTYPE_V6_NOTE",
        "retained forward-only ratio",
    ]
    for phrase in forbidden:
        check(f"note omits stale carrier phrase: {phrase}", phrase not in text)


def cache_header_checks(cache: str) -> None:
    print("\n=== causal-field portability cache ===")
    required = [
        "runner: scripts/causal_field_portability_probe.py",
        "exit_code: 0",
        "status: ok",
        "families=3, seeds=6, source_layer=8, K=5.0",
        "source anchor target: (y, z)=(0.0, 3.0)",
        "field strength = 5.0e-05, field eps = 0.1",
        "dynamic cone values = [1.0, 0.5]",
    ]
    for phrase in required:
        check(f"cache contains: {phrase}", phrase in cache)


def cache_zero_control_checks(cache: str) -> None:
    delta = re.search(r"max \|delta_y\| across families = (?P<value>[0-9.]+e[+-]\d+)", cache)
    field = re.search(r"max \|field\| across families = (?P<value>[0-9.]+e[+-]\d+)", cache)
    check("zero-control delta row parsed", delta is not None)
    check("zero-control field row parsed", field is not None)
    if delta is not None:
        check("zero-control detector delta is exact zero", float(delta.group("value")) == 0.0, delta.group("value"), kind="C")
    if field is not None:
        check("zero-control field is exact zero", float(field.group("value")) == 0.0, field.group("value"), kind="C")


def cache_family_row_checks(cache: str) -> None:
    row_re = re.compile(
        r"^\s*(?P<label>center grown family|portable family 2|portable family 3)\s+"
        r"(?P<inst>[+-]\d\.\d{3}e[+-]\d+)\u00b1(?P<inst_se>\d\.\d+e[+-]\d+)\s+"
        r"(?P<forward>[+-]\d\.\d{3}e[+-]\d+)\u00b1(?P<forward_se>\d\.\d+e[+-]\d+)\s+"
        r"(?P<fwd_ratio>\d\.\d{3})\s+"
        r"(?P<dyn1_ratio>\d\.\d{3})\s+"
        r"(?P<dyn05_ratio>\d\.\d{3})\s*\n"
        r"\s*\(c=1 delta (?P<dyn1_delta>[+-]\d\.\d{3}e[+-]\d+)\u00b1(?P<dyn1_se>\d\.\d+e[+-]\d+), "
        r"c=0\.5 delta (?P<dyn05_delta>[+-]\d\.\d{3}e[+-]\d+)\u00b1(?P<dyn05_se>\d\.\d+e[+-]\d+)\)",
        re.MULTILINE,
    )
    rows = {m.group("label"): m.groupdict() for m in row_re.finditer(cache)}
    check("all three family rows parsed", set(rows) == set(EXPECTED_ROWS), str(sorted(rows)))
    for label, expected in EXPECTED_ROWS.items():
        row = rows.get(label)
        if row is None:
            continue
        for key, expected_value in expected.items():
            actual = float(row[key])
            check(f"{label} {key} matches cache certificate", close(actual, expected_value), f"{actual:.3e}", kind="C")

    if set(rows) == set(EXPECTED_ROWS):
        fwd_values = [float(rows[label]["fwd_ratio"]) for label in EXPECTED_ROWS]
        dyn05_values = [float(rows[label]["dyn05_ratio"]) for label in EXPECTED_ROWS]
        check("rounded forward-ratio spread agrees with cache row", close(max(fwd_values) - min(fwd_values), 0.423, 2e-3), str(fwd_values), kind="B")
        check("dynamic c=0.5 family spread recomputes to 0.352", close(max(dyn05_values) - min(dyn05_values), 0.352, 5e-4), str(dyn05_values), kind="B")


def cache_spread_checks(cache: str) -> None:
    fwd = re.search(r"forward-only ratio spread across the three families = (?P<value>\d\.\d{3})", cache)
    dyn = re.search(r"dynamic\(c=0\.5\)/instantaneous ratio spread = (?P<value>\d\.\d{3})", cache)
    check("forward-ratio spread row parsed", fwd is not None)
    check("dynamic-ratio spread row parsed", dyn is not None)
    if fwd is not None:
        check("forward-ratio spread is 0.423", math.isclose(float(fwd.group("value")), 0.423, abs_tol=1e-12), fwd.group("value"), kind="C")
    if dyn is not None:
        check("dynamic c=0.5 spread is 0.352", math.isclose(float(dyn.group("value")), 0.352, abs_tol=1e-12), dyn.group("value"), kind="C")


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type remains bounded_theorem", row.get("claim_type") == "bounded_theorem")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("no helper runner paths remain", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")))
    check("no open dependency paths remain", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 80, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    cache = CACHE.read_text(encoding="utf-8")
    cache_header_checks(cache)
    cache_zero_control_checks(cache)
    cache_family_row_checks(cache)
    cache_spread_checks(cache)
    audit_metadata_checks()
    print("\nCausal field portability cached boundary certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
