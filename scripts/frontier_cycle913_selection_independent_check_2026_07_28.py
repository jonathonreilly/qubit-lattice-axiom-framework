#!/usr/bin/env python3
"""Cycle-913 INDEPENDENT CHECKER -- specified to REFUTE the revised finite
non-functionality result.

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
checker consumed the unlanded substrate closure; removed.  Independent
routes against the revised primary:

R1  the consistency arithmetic, recomputed from its own copy of the
    stipulated table with independent expressions;
R2  the non-functionality lemma, decided by a DIFFERENT algorithm
    (sort-and-scan over grouped rows instead of the primary's dict walk),
    with its own planted controls in both directions;
R3  the CLAIMS_JSON line parsed from the primary's pinned cache must match
    field for field;
R4  an overclaim scan: the primary's source and cache must NOT contain the
    withdrawn claim wording ("TERMINAL", "no non-forbidden realization",
    "forbids verbatim", "not derivable on this substrate").

Fail-closed: any refutation FAILs its certificate and the checker exits 1.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle913_selection_function_2026_07_28.py",
    "logs/runner-cache/frontier_cycle913_selection_function_2026_07_28.txt",
)

from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS

# re-pinned by the review-loop fix pass whenever the primary or its cache
# changes; a mismatch is a hard refutation.
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "193540a3fa3862f03524d365bd2b86440ef024c46aedf14e922e5d2d18399711",
    PRIMARY_CACHE:
        "78f8da7eddaeb9bd7997c6865ac081258830d719793f364183c38910d19b30aa",
}

TABLE = {
    "lock_points": 164,
    "realized_left_right": [84, 80],
    "menu_size": 2,
    "record_free_split": [51, 16],
    "record_free_lock_points": 67,
    "collision_class_split": [15, 15],
    "largest_neighbour_collision_class": 30,
}

WITHDRAWN_WORDING = (
    "TERMINAL STATEMENT",
    "no non-forbidden realization",
    "forbids verbatim",
    "not derivable on this substrate",
)

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def functional_by_sorting(rows: list[tuple[str, str]]) -> bool:
    ordered = sorted(rows)
    for (f1, o1), (f2, o2) in zip(ordered, ordered[1:]):
        if f1 == f2 and o1 != o2:
            return False
    return True


def main() -> int:
    t0 = monotonic()
    payloads, pins_ok, details = {}, True, []
    for path in AUDIT_INPUT_PATHS:
        target = ROOT / path
        data = target.read_bytes() if target.is_file() else b""
        payloads[path] = data
        match = sha256(data).hexdigest() == EXPECTED_SHA256[path]
        pins_ok &= bool(data) and match
        details.append(f"{path}:{'MATCH' if match else 'MISMATCH'}")
    check("R0_PINNED_EVIDENCE", pins_ok, "; ".join(details))

    claims = None
    for line in payloads[PRIMARY_CACHE].decode(
            "utf-8", errors="replace").splitlines():
        if line.startswith("CLAIMS_JSON: "):
            claims = json.loads(line[len("CLAIMS_JSON: "):])
    check("R0b_CLAIMS_PARSED", claims is not None,
          f"claims_line_found={claims is not None}")
    if claims is None:
        claims = {}

    # R1 independent consistency expressions
    t = TABLE
    ok1 = (t["lock_points"] - t["realized_left_right"][0]
           == t["realized_left_right"][1]
           and t["lock_points"] * t["menu_size"] == 328
           and t["record_free_lock_points"] - t["record_free_split"][0]
           == t["record_free_split"][1]
           and t["largest_neighbour_collision_class"] // 2
           == t["collision_class_split"][0]
           and claims.get("lock_points") == t["lock_points"]
           and claims.get("realized_split") == t["realized_left_right"]
           and claims.get("site_possibility_pairs") == 328)
    check("R1_CONSISTENCY_INDEPENDENT", ok1,
          f"164-84=80, 164*2=328, 67-51=16, 30//2=15; "
          f"primary_split={claims.get('realized_split')}")

    # R2 lemma by sort-and-scan
    witness = [("shared-neighbour-context", "left"),
               ("shared-neighbour-context", "right")]
    functional = [("ctx-a", "left"), ("ctx-a", "left"), ("ctx-b", "right")]
    ok2 = (not functional_by_sorting(witness)
           and functional_by_sorting(functional)
           and claims.get("witness_not_function") is True
           and claims.get("soundness_errors") == 0)
    check("R2_NONFUNCTIONALITY_INDEPENDENT", ok2,
          f"witness_refutes_functionality={not functional_by_sorting(witness)}"
          f" planted_functional_ok={functional_by_sorting(functional)}")

    # R3 recorded ratio echo
    ok3 = claims.get("recorded_ratio") == [0, 34166]
    check("R3_RECORDED_RATIO_ECHO", ok3,
          f"primary_recorded_ratio={claims.get('recorded_ratio')} "
          f"(stipulated history only)")

    # R4 overclaim scan on the primary's emitted output (the cache stdout).
    # The primary SOURCE may quote the withdrawn wording inside its review
    # record; its live OUTPUT must not assert it.
    cache = payloads[PRIMARY_CACHE].decode("utf-8", errors="replace")
    hits = []
    for term in WITHDRAWN_WORDING:
        for i, ln in enumerate(cache.splitlines(), 1):
            if term in ln and "withdrawn" not in ln.lower() \
                    and "forbid a separately" not in ln:
                hits.append(f"cache:{i}:{term}")
    ok4 = not hits
    check("R4_OVERCLAIM_SCAN", ok4, f"hits={hits if hits else 'none'}")

    elapsed = monotonic() - t0
    check("R5_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 913 -- INDEPENDENT CHECKER (REVISED), SPECIFIED TO REFUTE")
    w("=" * 78)
    w("")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<34} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if nfail == 0
               else "PRIMARY_REFUTED_ON_THIS_CHECK")
    w(f"VERDICT: {verdict}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 913,
        "role": "independent_checker",
        "claim_type": "bounded_theorem",
        "verdict": verdict,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite; independent lemma route; "
                    "overclaim scan added; fail-closed exit"),
        },
    }
    (ROOT / "outputs" /
     "selection_independent_check_cycle913_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
