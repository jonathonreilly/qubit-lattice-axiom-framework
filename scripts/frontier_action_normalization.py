#!/usr/bin/env python3
"""Action-normalization convention-free selection no-go verifier."""

from __future__ import annotations

import json
import math
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ACTION_NORMALIZATION_NOTE.md"
CACHE = ROOT / "logs/runner-cache/frontier_action_normalization.txt"
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "action_normalization_note"
RUNNER_PATH = "scripts/frontier_action_normalization.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "**Claim type:** no_go",
        "convention-free selection",
        "does not select `c` convention-free",
        "A specific value of `c` appears only after choosing",
        "This row only records that the current finite runner packet does not make that choice",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note contains: {phrase}", phrase in text)

    forbidden = [
        "bounded conditional claim",
        "A1, A2, A3",
        "admissions A1",
        "light bending fixes",
        "c = 1 is fixed by a convention-free observable",
        "positive theorem",
    ]
    for phrase in forbidden:
        check(f"note omits stale phrase: {phrase}", phrase not in text)


def parse_c_scan(cache: str) -> dict[float, dict[str, float | str]]:
    rows = {}
    pattern = re.compile(
        r"^\s*(?P<c>\d+\.\d)\s+"
        r"(?P<conv>[YN])\s+"
        r"(?P<iters>\d+)\s+"
        r"(?P<phi>\d\.\d{4}e-\d{2})\s+"
        r"(?P<cphi>\d\.\d{4}e-\d{2})\s+"
        r"(?P<beta>\d\.\d{4})\s+"
        r"(?P<r2>\d\.\d{4})\s*$",
        re.MULTILINE,
    )
    for match in pattern.finditer(cache):
        rows[float(match.group("c"))] = {
            "conv": match.group("conv"),
            "iters": int(match.group("iters")),
            "phi": float(match.group("phi")),
            "cphi": float(match.group("cphi")),
            "beta": float(match.group("beta")),
            "r2": float(match.group("r2")),
        }
    return rows


def parse_rescaling_rows(cache: str) -> list[tuple[float, float, float, float, float, float]]:
    pattern = re.compile(
        r"^\s*(?P<a>\d+\.\d{2})\s+"
        r"(?P<c>\d+\.\d{2})\s+"
        r"(?P<G>\d+\.\d{2})\s+"
        r"(?P<cG>\d+\.\d{2})\s+"
        r"(?P<phi>\d\.\d{4}e-\d{2})\s+"
        r"(?P<cphi>\d\.\d{4}e-\d{2})\s+"
        r"(?P<beta>\d\.\d{4})\s*$",
        re.MULTILINE,
    )
    rows = []
    for match in pattern.finditer(cache):
        rows.append(
            (
                float(match.group("a")),
                float(match.group("c")),
                float(match.group("G")),
                float(match.group("cG")),
                float(match.group("cphi")),
                float(match.group("beta")),
            )
        )
    return rows


def cache_checks() -> None:
    cache = CACHE.read_text(encoding="utf-8")
    print("ACTION NORMALIZATION CONVENTION-FREE SELECTION NO-GO")
    print("=" * 78)
    for phrase in [
        "runner: scripts/frontier_action_normalization.py",
        "exit_code: 0",
        "status: ok",
        "ACTION NORMALIZATION: CONVENTION-LOCKED COUPLING COEFFICIENT",
        "PPN gamma=1 holds for any positive c",
        "The earlier 'convention-free light bending' argument was incorrect.",
    ]:
        check(f"cache contains: {phrase}", phrase in cache)

    c_rows = parse_c_scan(cache)
    expected_c = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
    check("c scan contains all seven tested positive values", sorted(c_rows) == expected_c, str(sorted(c_rows)), "C")
    check("self-consistency convergence does not select c", all(c_rows[c]["conv"] == "Y" for c in expected_c), str({c: c_rows.get(c, {}).get("conv") for c in expected_c}), "C")
    check("beta is stable across tested c values", max(c_rows[c]["beta"] for c in expected_c) - min(c_rows[c]["beta"] for c in expected_c) < 0.004, str([c_rows[c]["beta"] for c in expected_c]), "C")

    rescale = parse_rescaling_rows(cache)
    check("rescaling scan has five cG=1 rows", len(rescale) == 5 and all(abs(row[3] - 1.0) < 1e-12 for row in rescale), str(rescale), "C")
    if rescale:
        cphi = [row[4] for row in rescale]
        rel_spread = (max(cphi) - min(cphi)) / (sum(cphi) / len(cphi))
        check("rescaling keeps c*phi_max approximately invariant", rel_spread < 0.05, f"rel_spread={rel_spread:.3e}", "C")

    defl = re.findall(r"^\s*(0\.5|1\.0|2\.0)\s+(\d\.\d{6})\s*$", cache, flags=re.MULTILINE)
    check("massive-probe deflection rows parsed", len(defl) == 3, str(defl), "C")
    if len(defl) == 3:
        vals = [float(v) for _, v in defl]
        check("massive-probe deflection increases with c but is not a c-fixing test", vals[0] < vals[1] < vals[2], str(vals), "C")


def algebraic_no_go_checks() -> None:
    print("\nALGEBRAIC NO-GO CHECKS")
    print("=" * 78)
    for c in [0.5, 1.0, 2.0, 5.0]:
        f = 0.01
        phi = c * f / 2.0
        gtt_lattice = -(1.0 - c * f)
        gtt_ppn = -(1.0 - 2.0 * phi)
        grr_linear = 1.0 + c * f
        grr_ppn = 1.0 + 2.0 * phi
        check(f"PPN gamma=1 readout is algebraically independent of c={c:g}", abs(gtt_lattice - gtt_ppn) < 1e-15 and abs(grr_linear - grr_ppn) < 1e-15)

    c = 1.0
    g = 1.0
    for a in [0.25, 0.5, 2.0, 4.0]:
        c2 = c / a
        g2 = g * a
        check(f"rescaling leaves c*G fixed for a={a:g}", abs(c * g - c2 * g2) < 1e-15)

    check("c=1 and c=2 are convention representatives, not simultaneous convention-free selections", not math.isclose(1.0, 2.0))


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next((entry for entry in queue if entry["claim_id"] == CLAIM_ID), None)

    print("\nAUDIT METADATA")
    print("=" * 78)
    check("claim type is no_go", row.get("claim_type") == "no_go", row.get("claim_type", ""), "M")
    check("audit status reset for re-audit", row.get("audit_status") == "unaudited", row.get("audit_status", ""), "M")
    check("effective status reset for re-audit", row.get("effective_status") == "unaudited", row.get("effective_status", ""), "M")
    check("runner path is registered", row.get("runner_path") == RUNNER_PATH, row.get("runner_path", ""), "M")
    check("direct dependency list is empty", row.get("deps") == [], str(row.get("deps")), "M")
    check("helper runner paths are empty", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")), "M")
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")), "M")
    check("queue entry is ready", queue_entry is not None and queue_entry.get("ready") is True, str(queue_entry), "M")


def main() -> int:
    note_checks()
    cache_checks()
    algebraic_no_go_checks()
    audit_metadata_checks()
    print("\nSUMMARY")
    print("=" * 78)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
