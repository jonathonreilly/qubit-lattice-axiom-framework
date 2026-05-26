#!/usr/bin/env python3
"""Complex-action free-gamma no-go verifier.

The row no longer tries to promote the imposed complex kernel to a retained
gravity/horizon theorem. It verifies the committed finite gamma sweep while
checking the exact obstruction: gamma is a free parameter in the current packet.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/COMPLEX_ACTION_NOTE.md"
CACHE = ROOT / "logs/runner-cache/complex_action_harness.txt"
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "complex_action_note"
RUNNER_PATH = "scripts/complex_action_harness.py"

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


def kernel_factor(k: float, length: float, field: float, gamma: float) -> complex:
    return cmath.exp(1j * k * length * (1.0 - field)) * math.exp(-k * gamma * length * field)


def note_boundary_checks() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").split())
    required = [
        "**Claim type:** no_go",
        "exact negative boundary",
        "free real `gamma`",
        "cannot derive a gravity-horizon unification theorem",
        "Those are valid finite-model facts about the imposed kernel",
        "any new axiom or audit verdict",
    ]
    for phrase in required:
        check(f"note contains: {phrase}", phrase in text)

    forbidden = [
        "bounded conditional one-parameter",
        "retained scope",
        "gravity and horizons coexist",
        "horizon-like",
        "superradiance-like",
        "tier-ratifiable gravity-horizon unification theorem",
    ]
    for phrase in forbidden:
        check(f"note omits stale phrase: {phrase}", phrase not in text)


def parse_gamma_table(cache: str) -> dict[float, tuple[float, str, float]]:
    rows: dict[float, tuple[float, str, float]] = {}
    pattern = re.compile(
        r"^\s*(?P<gamma>-?\d+\.\d{2})\s+"
        r"(?P<delta>[+-]\d\.\d{6}e[+-]\d{2})\s+"
        r"(?P<direction>TOWARD|AWAY)\s+"
        r"(?P<escape>\d+\.\d{4})\s*$",
        re.MULTILINE,
    )
    for match in pattern.finditer(cache):
        rows[float(match.group("gamma"))] = (
            float(match.group("delta")),
            match.group("direction"),
            float(match.group("escape")),
        )
    return rows


def cache_checks() -> None:
    cache = CACHE.read_text(encoding="utf-8")
    print("COMPLEX ACTION FREE-GAMMA NO-GO")
    print("=" * 72)

    for phrase in [
        "runner: scripts/complex_action_harness.py",
        "exit_code: 0",
        "status: ok",
        "h=0.5, W=6, L=30, s=0.1, z_src=3.0",
        "match: True",
    ]:
        check(f"cache contains: {phrase}", phrase in cache)

    rows = parse_gamma_table(cache)
    check("gamma sweep has 10 rows", len(rows) == 10, str(len(rows)), "C")
    check("gamma=-0.50 is TOWARD with amplification", rows.get(-0.50, (0, "", 0))[1:] == ("TOWARD", 43.5943), str(rows.get(-0.50)), "C")
    check("gamma=0.00 is real-action TOWARD baseline", rows.get(0.00, (0, "", 0))[1] == "TOWARD", str(rows.get(0.00)), "C")
    check("gamma=0.10 crosses to AWAY", rows.get(0.10, (0, "", 0))[1] == "AWAY", str(rows.get(0.10)), "C")
    check("gamma=2.00 is deep absorption", rows.get(2.00, (0, "", 1))[2] < 1e-3, str(rows.get(2.00)), "C")
    if rows:
        escapes = [rows[g][2] for g in sorted(rows)]
        check("escape is monotonically decreasing across gamma sweep", all(a > b for a, b in zip(escapes, escapes[1:])), str(escapes), "C")

    born = [float(v) for v in re.findall(r"gamma=\d\.\d: \|I3\|/P = ([\d.]+e-\d+)", cache)]
    check("three Born proxy samples parsed", len(born) == 3, str(born), "C")
    check("Born proxy samples are machine small", bool(born) and max(born) < 1e-12, str(born), "C")

    standard = re.search(r"standard propagator delta:\s+([+-]\d\.\d{6}e[+-]\d{2})", cache)
    complex0 = re.search(r"complex\(gamma=0\) delta:\s+([+-]\d\.\d{6}e[+-]\d{2})", cache)
    if standard and complex0:
        delta = abs(float(standard.group(1)) - float(complex0.group(1)))
        check("gamma=0 reduction is exact in cache", delta < 1e-12, f"delta={delta:.3e}", "C")
    else:
        check("gamma=0 reduction lines parsed", False, "missing", "C")


def no_go_algebra_checks() -> None:
    print("\nFREE-GAMMA ALGEBRA")
    print("=" * 72)
    k = 5.0
    length = 1.0
    field = 0.2
    g0 = kernel_factor(k, length, field, 0.0)
    g1 = kernel_factor(k, length, field, 1.0)
    g2 = kernel_factor(k, length, field, 2.0)
    phase_only = cmath.exp(1j * k * length * (1.0 - field))

    check("gamma=0 equals the real-action phase factor", abs(g0 - phase_only) < 1e-15)
    check("positive gamma suppresses amplitude by definition", abs(g1) < abs(g0) and abs(g2) < abs(g1), f"|g0|={abs(g0):.3e}, |g1|={abs(g1):.3e}, |g2|={abs(g2):.3e}")
    expected_ratio = math.exp(-k * (2.0 - 1.0) * length * field)
    observed_ratio = abs(g2) / abs(g1)
    check("gamma ratio is exactly the imposed exponential weight", abs(observed_ratio - expected_ratio) < 1e-15, f"{observed_ratio:.6e}")
    check("zero field makes gamma unobservable in the kernel", abs(kernel_factor(k, length, 0.0, 0.0) - kernel_factor(k, length, 0.0, 2.0)) < 1e-15)


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next((entry for entry in queue if entry["claim_id"] == CLAIM_ID), None)

    print("\nAUDIT METADATA")
    print("=" * 72)
    check("claim type is no_go", row.get("claim_type") == "no_go", row.get("claim_type", ""), "M")
    check("audit status reset for re-audit", row.get("audit_status") == "unaudited", row.get("audit_status", ""), "M")
    check("effective status reset for re-audit", row.get("effective_status") == "unaudited", row.get("effective_status", ""), "M")
    check("runner path is registered", row.get("runner_path") == RUNNER_PATH, row.get("runner_path", ""), "M")
    check("direct dependency list is empty", row.get("deps") == [], str(row.get("deps")), "M")
    check("helper runner paths are empty", row.get("helper_runner_paths") == [], str(row.get("helper_runner_paths")), "M")
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")), "M")
    check("queue entry is ready", queue_entry is not None and queue_entry.get("ready") is True, str(queue_entry), "M")


def main() -> int:
    note_boundary_checks()
    cache_checks()
    no_go_algebra_checks()
    audit_metadata_checks()

    print("\nSUMMARY")
    print("=" * 72)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
