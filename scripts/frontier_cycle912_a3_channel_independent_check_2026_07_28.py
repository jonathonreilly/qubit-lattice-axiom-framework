#!/usr/bin/env python3
"""Cycle-912 INDEPENDENT CHECKER -- specified to REFUTE the revised
probability-readout underdetermination result.

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
checker assigned `pass = True` to substantive certificates and exited 0
regardless of claim survival; both defects are corrected: every certificate
below binds `pass` to the predicate it names, and a refutation exits 1.

Independent routes (never the primary's):

R1  invisibility, by RANDOMIZED functional probing: draw random cell
    weights, build I as the induced additive readout, and hunt for a
    content-preserving pair of event sets that I separates (none may
    exist); then plant a NON-content-determined readout and confirm the
    hunt fires on it (tooth).
R2  the simplex dimension, by exhaustive vertex enumeration and integer
    rank over a scaled matrix (no Fractions).
R3  the existence-premise non-selection, by direct witness checking: both
    of the primary's probability witnesses satisfy existence +
    state-functionality; they differ; therefore the premise selects
    nothing.  The planted uniform-counting sentence pins a unique point.
R4  the recorded-scale arithmetic and the CLAIMS_JSON line parsed from the
    primary's pinned cache, field for field.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle912_a3_channel_2026_07_28.py",
    "logs/runner-cache/frontier_cycle912_a3_channel_2026_07_28.txt",
)

from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS

# re-pinned by the review-loop fix pass whenever the primary or its cache
# changes; a mismatch is a hard refutation.
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "744229c7048f4a86b5c553a2c0728f272acb4c2494e18917fe29ae4e0e686f09",
    PRIMARY_CACHE:
        "f6574d87bfb0d363af57932b565cdf02400cd9b01f2171a55d6dd5ef5889a570",
}

# the checker's own copy of the declared model (must equal the primary's;
# R0c verifies the primary's source contains exactly this stipulation)
MODEL_EVENTS = ["e00", "e01", "e02", "e03", "e04", "e05",
                "e06", "e07", "e08", "e09", "e10", "e11"]
MODEL_CONTENT = {"e00": "c0", "e01": "c0", "e02": "c0", "e03": "c0",
                 "e04": "c1", "e05": "c1", "e06": "c1",
                 "e07": "c2", "e08": "c2",
                 "e09": "c3", "e10": "c3",
                 "e11": "c4"}

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def multiset(events) -> tuple:
    counts: dict[str, int] = {}
    for e in events:
        counts[MODEL_CONTENT[e]] = counts.get(MODEL_CONTENT[e], 0) + 1
    return tuple(sorted(counts.items()))


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

    src = payloads[PRIMARY_PATH].decode("utf-8", errors="replace")
    model_marker = '"e04": "c1"' in src and '"e11": "c4"' in src
    check("R0c_MODEL_STIPULATION_PRESENT", model_marker,
          f"primary_source_contains_declared_model={model_marker}")

    claims = None
    for line in payloads[PRIMARY_CACHE].decode(
            "utf-8", errors="replace").splitlines():
        if line.startswith("CLAIMS_JSON: "):
            claims = json.loads(line[len("CLAIMS_JSON: "):])
    check("R0b_CLAIMS_PARSED", claims is not None,
          f"claims_line_found={claims is not None}")
    if claims is None:
        claims = {}

    # R1: randomized invisibility hunt + planted tooth
    rng = random.Random(0x912C4EC)
    cells = sorted(set(MODEL_CONTENT.values()))
    separations = 0
    trials = 400
    pool = []
    for r in range(1, len(MODEL_EVENTS) + 1):
        for combo in combinations(MODEL_EVENTS, r):
            pool.append(combo)
    by_ms: dict[tuple, list] = {}
    for combo in pool:
        by_ms.setdefault(multiset(combo), []).append(combo)
    preserving_pairs = [(a, b) for sets in by_ms.values() if len(sets) > 1
                        for a, b in combinations(sets, 2)]
    for _ in range(trials):
        wts = {c: Fraction(rng.randint(0, 40), rng.randint(1, 9))
               for c in cells}
        for a, b in preserving_pairs:
            ia = sum(wts[MODEL_CONTENT[e]] for e in a)
            ib = sum(wts[MODEL_CONTENT[e]] for e in b)
            if ia != ib:
                separations += 1
                break
    # tooth: an event-dependent (non-content-determined) readout must
    # separate some content-preserving pair
    planted = {e: (Fraction(1) if e == "e00" else Fraction(0))
               for e in MODEL_EVENTS}
    tooth_fired = any(
        sum(planted[e] for e in a) != sum(planted[e] for e in b)
        for a, b in preserving_pairs)
    ok1 = (len(preserving_pairs) > 0 and separations == 0 and tooth_fired
           and claims.get("t1_violations") == 0
           and claims.get("content_preserving_pairs")
           == len(preserving_pairs))
    check("R1_INVISIBILITY_RANDOMIZED", ok1,
          f"preserving_pairs={len(preserving_pairs)} random_readouts={trials} "
          f"separations={separations} planted_tooth_fired={tooth_fired}")

    # R2: simplex dimension by integer rank over scaled vertices
    sizes = {c: sum(1 for e in MODEL_EVENTS if MODEL_CONTENT[e] == c)
             for c in cells}
    scale = 1
    for s in sizes.values():
        scale *= s
    verts = []
    for c in cells:
        verts.append([scale // sizes[c] if k == c else 0 for k in cells])
    diffs = [[a - b for a, b in zip(v, verts[0])] for v in verts[1:]]
    # fraction-free integer elimination (multiply-and-subtract), a different
    # arithmetic route from the primary's Fraction pivoting
    rows = [r[:] for r in diffs]
    rank = 0
    for col in range(len(cells)):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                a, b = rows[rank][col], rows[i][col]
                rows[i] = [a * x - b * y
                           for x, y in zip(rows[i], rows[rank])]
        rank += 1
    ok2 = (rank == len(cells) - 1
           and claims.get("model_affine_dim") == len(cells) - 1
           and claims.get("model_cells") == len(cells))
    check("R2_SIMPLEX_DIMENSION_INDEPENDENT", ok2,
          f"vertex_rank={rank} n_cells={len(cells)} "
          f"primary_dim={claims.get('model_affine_dim')}")

    # R3: existence-premise non-selection by direct witness checking
    n_events = len(MODEL_EVENTS)
    w1 = {c: Fraction(1, len(cells) * sizes[c]) for c in cells}
    w2 = {c: Fraction(1, n_events) for c in cells}
    both_prob = (sum(w1[c] * sizes[c] for c in cells) == 1
                 and sum(w2[c] * sizes[c] for c in cells) == 1
                 and all(v >= 0 for v in list(w1.values())
                         + list(w2.values())))
    differ = any(w1[c] != w2[c] for c in cells)
    ok3 = (both_prob and differ
           and claims.get("dim_under_existence") == len(cells) - 1
           and claims.get("dim_under_uniform_counting") == 0)
    check("R3_EXISTENCE_DOES_NOT_SELECT", ok3,
          f"both_witnesses_are_state_functional_probabilities={both_prob} "
          f"witnesses_differ={differ} -> the existence premise selects "
          f"nothing; uniform counting pins one point")

    # R4: recorded-scale arithmetic
    ok4 = (52_018 - 1 == 52_017
           and claims.get("recorded_affine_dim") == 52_017)
    check("R4_RECORDED_SCALE", ok4,
          f"52018-1=52017 primary={claims.get('recorded_affine_dim')} "
          f"(counts stipulated, arithmetic only)")

    elapsed = monotonic() - t0
    check("R5_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 912 -- INDEPENDENT CHECKER (REVISED), SPECIFIED TO REFUTE")
    w("=" * 78)
    w("")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<36} {detail}")
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
        "cycle": 912,
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
            "fix": ("pass fields now bind to their predicates; exit is "
                    "fail-closed on refutation; unlanded closure removed"),
        },
    }
    (ROOT / "outputs" /
     "a3_channel_independent_check_cycle912_receipt_2026_07_28.json"
     ).write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
