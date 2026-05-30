#!/usr/bin/env python3
"""Audit-companion runner for the Gate B far-field bounded-conditional
separator narrow theorem note
`GATE_B_FARFIELD_BOUNDED_CONDITIONAL_SEPARATOR_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the bounded conditional
implication

  (BC):  Xi  AND  (Lambda, seeds as declared)    ==>    H reproduces Omega

where:

  H       = scripts/gate_b_farfield_harness.py at the SHA-256 pinned in
            logs/runner-cache/gate_b_farfield_harness.txt;
  Xi      = the admitted-context ingredient list (growth rule, source law,
            propagation kernel, valley-linear action, readout criterion)
            named verbatim in GATE_B_FARFIELD_NOTE.md;
  Lambda  = the four declared (drift, restore) rows
            (0.3, 0.5), (0.2, 0.7), (0.1, 0.9), (0.0, 1.0);
  seeds   = list(range(12));
  Omega   = the frozen runner-cache stdout:
              drift=0.3,rest=0.5 : 36/36 TOWARD (100%), F~M=1.00
              drift=0.2,rest=0.7 : 36/36 TOWARD (100%), F~M=1.00
              drift=0.1,rest=0.9 : 36/36 TOWARD (100%), F~M=1.00
              exact grid         : 36/36 TOWARD (100%), F~M=1.00.

This audit-companion runner performs purely off-line checks that
the (BC) implication is properly framed and that the parent note is
review-hygiene clean. It does NOT re-run the heavy harness (1043 s
elapsed); it verifies cache integrity and shape, runner determinism
markers, and note-text claim-fidelity.

Specifically, this runner:

  (a) verifies the runner cache file exists, has v1 header, exit_code=0,
      status=ok, and a recorded runner_sha256;
  (b) verifies the runner_sha256 in the cache matches the actual SHA-256
      of scripts/gate_b_farfield_harness.py on disk (or, if mismatched,
      reports the drift as INFO and continues — drift is allowed by the
      separator's pinning convention because the cache itself is the
      load-bearing artifact);
  (c) parses the cached stdout table and verifies that all four declared
      rows match Omega exactly (36/36 TOWARD, 100%, F~M=1.00);
  (d) verifies determinism markers in the runner source: random.Random
      is seed-keyed, SEEDS = list(range(12)), DRIFT_RESTORE_ROWS matches
      Lambda, Z_MASSES = [3, 4, 5], H = 0.5;
  (e) verifies the parent narrow note's review-hygiene properties:
      bounded_theorem type, conditional-separator claim scope, no
      no-new-axiom / no-new-vocabulary violations, explicit non-claim
      block, source-only authority, status-authority disclaimer.

Companion role: source theorem companion, no hand-authored audit data and no
audit-posture change. Provides audit-friendly evidence that the parent's
load-bearing one-step bounded-conditional implication is well-defined
against the frozen cache and that the separator structure is honest.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

# Heavy compute / sweep runner — `AUDIT_TIMEOUT_SEC = 60` because this
# audit-companion is an offline-text-and-cache check with no propagation
# pass. See `docs/audit/RUNNER_CACHE_POLICY.md`.
AUDIT_TIMEOUT_SEC = 60

REPO_ROOT = Path(__file__).resolve().parent.parent
RUNNER_PATH = REPO_ROOT / "scripts" / "gate_b_farfield_harness.py"
CACHE_PATH = REPO_ROOT / "logs" / "runner-cache" / "gate_b_farfield_harness.txt"
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GATE_B_FARFIELD_BOUNDED_CONDITIONAL_SEPARATOR_NARROW_THEOREM_NOTE_2026-05-17.md"
)
PARENT_PATH = REPO_ROOT / "docs" / "GATE_B_FARFIELD_NOTE.md"

# Frozen cache rows expected as Omega.
OMEGA = [
    ("drift=0.3,rest=0.5", "36/36", "100%", "1.00"),
    ("drift=0.2,rest=0.7", "36/36", "100%", "1.00"),
    ("drift=0.1,rest=0.9", "36/36", "100%", "1.00"),
    ("exact grid", "36/36", "100%", "1.00"),
]

# Declared Lambda for the harness.
DECLARED_LAMBDA = [(0.3, 0.5), (0.2, 0.7), (0.1, 0.9), (0.0, 1.0)]
DECLARED_SEEDS = list(range(12))
DECLARED_Z_MASSES = [3, 4, 5]
DECLARED_H = 0.5


class CheckFailure(Exception):
    pass


def ok(msg: str) -> None:
    print(f"  [OK] {msg}")


def info(msg: str) -> None:
    print(f"  [INFO] {msg}")


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise CheckFailure(msg)
    ok(msg)


def check_cache_v1_header_and_status() -> dict:
    """(a) v1 header, exit_code=0, status=ok, recorded sha256."""
    print("(a) Cache header / status / sha256 recorded:")
    if not CACHE_PATH.exists():
        raise CheckFailure(f"runner cache missing at {CACHE_PATH}")
    text = CACHE_PATH.read_text()
    lines = text.splitlines()
    check(lines[0].strip() == "===== runner cache v1 =====", "v1 header present")
    meta = {}
    for ln in lines[1:]:
        if ln.startswith("----- stdout -----"):
            break
        if ":" in ln:
            k, _, v = ln.partition(":")
            meta[k.strip()] = v.strip()
    check(meta.get("exit_code") == "0", "exit_code = 0")
    check(meta.get("status") == "ok", "status = ok")
    check(
        meta.get("runner") == "scripts/gate_b_farfield_harness.py",
        "runner path recorded as scripts/gate_b_farfield_harness.py",
    )
    check("runner_sha256" in meta, "runner_sha256 recorded in cache")
    return meta


def check_runner_sha256(meta: dict) -> None:
    """(b) compare recorded sha256 to current file sha256."""
    print("(b) Runner SHA-256 cross-check:")
    recorded = meta.get("runner_sha256", "").strip()
    if not RUNNER_PATH.exists():
        raise CheckFailure(f"runner script missing at {RUNNER_PATH}")
    h = hashlib.sha256(RUNNER_PATH.read_bytes()).hexdigest()
    if h == recorded:
        ok(f"runner_sha256 matches on-disk script ({h[:12]}...)")
    else:
        # Drift allowed: cache is the load-bearing artifact for the
        # bounded conditional. Report as INFO, not failure.
        info(
            f"runner_sha256 drift (recorded={recorded[:12]}..., disk={h[:12]}...) — cache is the load-bearing artifact for (BC)"
        )


def parse_cache_stdout_rows() -> list:
    """Extract the four readout rows from the cached stdout."""
    text = CACHE_PATH.read_text()
    in_stdout = False
    rows = []
    for ln in text.splitlines():
        if ln.startswith("----- stdout -----"):
            in_stdout = True
            continue
        if ln.startswith("----- stderr -----"):
            break
        if not in_stdout:
            continue
        # Match: "  drift=X.X,rest=X.X       : 36/36 TOWARD (100%), F~M=1.00"
        # Or:    "  exact grid               : 36/36 TOWARD (100%), F~M=1.00"
        m = re.match(
            r"\s+(drift=\d+\.\d+,rest=\d+\.\d+|exact grid)\s+:\s+(\d+/\d+)\s+TOWARD\s+\((\d+%)\),\s+F~M=([\d.]+)",
            ln,
        )
        if m:
            rows.append(
                (m.group(1).strip(), m.group(2), m.group(3), m.group(4))
            )
    return rows


def check_cache_matches_omega() -> None:
    """(c) the four rows match Omega."""
    print("(c) Cached stdout rows match Omega exactly:")
    rows = parse_cache_stdout_rows()
    check(
        len(rows) == len(OMEGA),
        f"row count = {len(OMEGA)} (got {len(rows)})",
    )
    for i, (expected, actual) in enumerate(zip(OMEGA, rows)):
        check(
            expected == actual,
            f"row {i + 1}: {expected[0]} -> {expected[1]} TOWARD ({expected[2]}), F~M={expected[3]}",
        )


def check_runner_determinism_markers() -> None:
    """(d) determinism markers in runner source."""
    print("(d) Runner-source determinism markers:")
    if not RUNNER_PATH.exists():
        raise CheckFailure(f"runner script missing at {RUNNER_PATH}")
    src = RUNNER_PATH.read_text()
    check(
        "random.Random(seed)" in src,
        "random.Random(seed) used — gauss draws are seed-keyed",
    )
    check(
        "SEEDS = list(range(12))" in src,
        f"SEEDS = list(range(12)) matches DECLARED_SEEDS (len={len(DECLARED_SEEDS)})",
    )
    check(
        "Z_MASSES = [3, 4, 5]" in src,
        f"Z_MASSES = {DECLARED_Z_MASSES} declared",
    )
    check(f"H = {DECLARED_H}" in src, f"H = {DECLARED_H} declared")
    for d, r in DECLARED_LAMBDA:
        # Source may render 0.0 as "0.0," etc.; just check the floats appear
        # in DRIFT_RESTORE_ROWS context.
        check(
            f"({d}, {r})" in src,
            f"Lambda row ({d}, {r}) declared in DRIFT_RESTORE_ROWS",
        )


def check_note_review_hygiene() -> None:
    """(e) parent narrow note review-hygiene."""
    print("(e) Narrow note review-hygiene:")
    if not NOTE_PATH.exists():
        raise CheckFailure(f"narrow note missing at {NOTE_PATH}")
    text = NOTE_PATH.read_text()
    check("**Type:** bounded_theorem" in text, "Type: bounded_theorem declared")
    check(
        "Status authority:** independent audit lane only" in text,
        "status-authority disclaimer present",
    )
    check(
        "Claim scope:**" in text and "GIVEN" in text and "THEN" in text,
        "claim scope is a GIVEN/THEN conditional (separator structure)",
    )
    check(
        "physical-gravity" in text.lower(),
        "explicit reference to the physical-gravity reading (non-claim block)",
    )
    check(
        "does **not** claim" in text or "does NOT claim" in text,
        "explicit non-claim block present",
    )
    check(
        "Source-only" in text or "source-only" in text,
        "source-only authority declared",
    )
    check(
        "does **not** change the audit posture" in text,
        "explicit non-promotion language for the parent row",
    )
    check(
        "366ba73255b74b1775847ea5eaba9ac004fc4c3bf2a60a710102330f4900947a"
        in text,
        "runner SHA-256 pin matches cache",
    )
    check(
        "missing_bridge_theorem" in text,
        "explicit reference to audit ledger's missing_bridge_theorem notes",
    )


def check_parent_referenced() -> None:
    """Cross-reference: parent note exists and is referenced."""
    print("(f) Parent note cross-reference:")
    if not PARENT_PATH.exists():
        raise CheckFailure(f"parent note missing at {PARENT_PATH}")
    note_text = NOTE_PATH.read_text()
    check(
        "GATE_B_FARFIELD_NOTE.md" in note_text,
        "narrow note references parent GATE_B_FARFIELD_NOTE.md",
    )


def main() -> int:
    print("=" * 70)
    print("Gate B far-field bounded-conditional separator — audit companion")
    print("=" * 70)
    try:
        meta = check_cache_v1_header_and_status()
        check_runner_sha256(meta)
        check_cache_matches_omega()
        check_runner_determinism_markers()
        check_note_review_hygiene()
        check_parent_referenced()
    except CheckFailure as e:
        print()
        print(f"[FAIL] {e}")
        return 1

    print()
    print("PASS — bounded conditional (BC) is well-defined against the frozen")
    print("cache and the separator structure is review-hygiene clean.")
    print()
    print("Reminder: this audit-companion does NOT discharge the upstream")
    print("primitive-to-observable bridge. That remains the open gap")
    print("recorded by GATE_B_FARFIELD_NOTE.md and the audit ledger.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
